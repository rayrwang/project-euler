import math

LIMIT = 10**9
TARGET = 120


def _fib_pair_mod(t: int, mod: int) -> tuple[int, int]:
    """(F_t mod mod, F_{t+1} mod mod) by fast doubling."""
    if t == 0:
        return 0, 1 % mod
    a, b = _fib_pair_mod(t // 2, mod)
    c = a * (2 * b - a) % mod  # F_{2k}
    d = (a * a + b * b) % mod  # F_{2k+1}
    if t % 2 == 0:
        return c, d
    return d, (c + d) % mod


def _pisano_if_divides(m: int, period: int) -> int:
    """pi(m) if it divides period, else 0.

    pi(m) | t iff F_t = 0 and F_{t+1} = 1 (mod m); the period itself is
    the smallest such divisor of `period`.
    """
    best = 0
    for d in sorted(_divisors(period)):
        f, g = _fib_pair_mod(d, m)
        if f == 0 and g == 1 % m:
            best = d
            break
    return best


def _divisors(n: int) -> list[int]:
    divs = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            divs.append(d)
            if d * d != n:
                divs.append(n // d)
    return divs


def _candidate_primes(period: int) -> list[int]:
    """Primes p with pi(p) | period, i.e. p | gcd(F_period, F_{period+1} - 1).

    The gcd is small enough to factor by trial division.
    """
    a, b = 0, 1
    for _ in range(period):
        a, b = b, a + b
    g = math.gcd(a, b - 1)  # a = F_period, b = F_{period+1}
    primes = []
    d = 2
    while d * d <= g:
        if g % d == 0:
            primes.append(d)
            while g % d == 0:
                g //= d
        d += 1
    if g > 1:
        primes.append(g)
    return primes


def solve() -> int:
    # Prime powers p^e < LIMIT whose Pisano period divides TARGET, with
    # that period; only these may divide an n with pi(n) = TARGET, since
    # pi(p^e) | pi(n) = lcm over prime power factors.
    pps: dict[int, list[tuple[int, int]]] = {}
    for p in _candidate_primes(TARGET):
        if p >= LIMIT:
            continue
        lst = []
        pe = p
        while pe < LIMIT:
            d = _pisano_if_divides(pe, TARGET)
            if d == 0:
                break  # pi(p^e) only grows with e
            lst.append((pe, d))
            pe *= p
        if lst:
            pps[p] = lst
    groups = list(pps.values())

    total = 0

    def dfs(idx: int, n: int, period_lcm: int) -> None:
        nonlocal total
        if period_lcm == TARGET:
            total += n
        for i in range(idx, len(groups)):
            for pe, d in groups[i]:
                if n * pe >= LIMIT:
                    break
                dfs(i + 1, n * pe, math.lcm(period_lcm, d))

    dfs(0, 1, 1)
    return total


def check_small() -> int:
    """Sum of n < 50 with pi(n) = 18, given as 57."""
    global LIMIT, TARGET
    save = LIMIT, TARGET
    LIMIT, TARGET = 50, 18
    res = solve()
    LIMIT, TARGET = save
    return res


if __name__ == "__main__":
    assert check_small() == 57
    print(solve())  # 44511058204
