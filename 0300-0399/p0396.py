from math import gcd

MOD = 10**9
EXACT_BITS = 200_000  # keep exact integers up to this size


def carmichael(m: int) -> int:
    lam = 1
    mm = m
    p = 2
    while p * p <= mm:
        if mm % p == 0:
            k = 0
            while mm % p == 0:
                mm //= p
                k += 1
            if p == 2:
                lpk = 1 if k == 1 else (2 if k == 2 else 1 << (k - 2))
            else:
                lpk = p ** (k - 1) * (p - 1)
            lam = lam * lpk // gcd(lam, lpk)
        p += 1
    if mm > 1:
        lam = lam * (mm - 1) // gcd(lam, mm - 1)
    return lam


CHAIN: list[int] = [MOD]
while CHAIN[-1] > 1:
    CHAIN.append(carmichael(CHAIN[-1]))


class Num:
    """Integer known exactly while small, and modulo the Carmichael chain.

    chain[i + 1] = lambda(chain[i]), so 2^x mod chain[i] is recoverable from
    x mod chain[i + 1] once x is astronomically large (universal exponent
    lifting, valid even though gcd(2, 10^9) > 1 because x far exceeds the
    2-adic valuation of every modulus).
    """

    __slots__ = ("exact", "mods")

    def __init__(self, exact: int | None, mods: list[int] | None = None):
        self.exact = exact
        if mods is None:
            assert exact is not None
            mods = [exact % m for m in CHAIN]
        self.mods = mods

    def shift(self, c: int) -> "Num":  # self + c for small int c
        exact = None if self.exact is None else self.exact + c
        return Num(exact, [(v + c) % m for v, m in zip(self.mods, CHAIN)])

    def __add__(self, other: "Num") -> "Num":
        exact = None
        if self.exact is not None and other.exact is not None:
            exact = self.exact + other.exact
        return Num(exact, [(a + b) % m for a, b, m in zip(self.mods, other.mods, CHAIN)])

    def __mul__(self, other: "Num") -> "Num":
        exact = None
        if (
            self.exact is not None
            and other.exact is not None
            and self.exact.bit_length() + other.exact.bit_length() < EXACT_BITS
        ):
            exact = self.exact * other.exact
        return Num(exact, [a * b % m for a, b, m in zip(self.mods, other.mods, CHAIN)])


def pow2(x: Num) -> Num:
    if x.exact is not None:
        exact = (1 << x.exact) if x.exact < EXACT_BITS else None
        return Num(exact, [pow(2, x.exact, m) for m in CHAIN])
    # x is gigantic: lift the exponent through the chain.
    mods = []
    for i, m in enumerate(CHAIN):
        if i + 1 < len(CHAIN):
            e = x.mods[i + 1] + CHAIN[i + 1]
        else:
            e = 1  # modulus is 1 here anyway
        mods.append(pow(2, e, m))
    return Num(None, mods)


def clear_position(j: int, d: Num | int, base: Num) -> Num:
    """Final base after a digit d at position j (lower digits zero) reaches 0.

    Digits are preserved verbatim by rebasing, so position 0 just counts
    down (base grows by d); a unit decrement at position j >= 1 borrows,
    writing the old base into every lower position, and those are cleared
    in turn.
    """
    if isinstance(d, int):
        d = Num(d)
    if j == 0:
        return base + d
    if j == 1:
        return pow2(d) * base.shift(1) + Num(-1)
    assert d.exact is not None, "iteration count at position >= 2 must be exact"
    for _ in range(d.exact):
        old = base
        base = base.shift(1)
        for k in range(j):
            base = clear_position(k, old, base)
    return base


def g(n: int) -> Num:
    base = Num(2)
    j = 0
    while n:
        if n & 1:
            base = clear_position(j, 1, base)
        n >>= 1
        j += 1
    return base  # G(n) = final base - 2


def g_brute(n: int) -> int:
    v, b, count = n, 2, 0
    while v:
        count += 1
        digits = []
        while v:
            digits.append(v % b)
            v //= b
        for d in reversed(digits):
            v = v * (b + 1) + d
        v -= 1
        b += 1
    return count


if __name__ == "__main__":
    for n in range(1, 8):
        exact = g(n).exact
        assert exact is not None and exact - 2 == g_brute(n)
    assert sum(g_brute(n) for n in range(1, 8)) == 2517
    total = sum(g(n).mods[0] - 2 for n in range(1, 16)) % MOD
    print(total)  # 173214653
