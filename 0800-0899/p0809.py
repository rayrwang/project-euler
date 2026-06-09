from fractions import Fraction

from funcs import totient

MOD = 10**15


def chain(r: Fraction) -> list[int]:
    """Whole parts m_i of phi(r_i) along the chain r_{i+1} = frac(phi(r_i)).

    Here phi(c/b) = c/(b - c) = 1/(1 - r) - 1. The chain ends when phi is an
    integer (subtractive Euclid on (b - c, c) terminates).
    """
    ms = []
    while True:
        p = r / (1 - r)
        ms.append(int(p))
        r = p - int(p)
        if r == 0:
            return ms


def f_exact(x: Fraction) -> int:
    """Evaluate f directly; feasible when intermediate values stay moderate.

    Writing x = k + r and phi(r) = 1/(1-r) - 1 = m_i + r_{i+1}, the recursion
    becomes G_i(k) = G_{i+1}(G_i(k-1) + m_i) with base G_i(0) = G_{i+1}(1 + m_i),
    where G_i(k) = f(k + r_i). At the terminal level (phi integral) the
    argument of f is integral, so G_L(k) = (1 + m_L) + k * m_L.
    """
    k, r = divmod(x.numerator, x.denominator)
    if r == 0:
        return k
    ms = chain(Fraction(r, x.denominator))

    def g(i: int, k: int) -> int:
        m = ms[i]
        if i == len(ms) - 1:
            return 1 + m + k * m
        v = g(i + 1, 1 + m)
        for _ in range(k):
            v = g(i + 1, v + m)
        return v

    return g(0, k)


def tower2_mod(height: int, mod: int) -> int:
    """2^2^...^2 (height twos) mod `mod`, assuming height >= 6.

    Uses 2^e mod m = 2^(e mod phi(m) + phi(m)) mod m, valid once
    e >= log2(m), which holds at every level since the remaining tower
    is at least 2^65536.
    """
    if mod == 1:
        return 0
    if height == 1:
        return 2 % mod
    t = totient(mod)
    return pow(2, tower2_mod(height - 1, t) + t, mod)


def f_22_7_mod() -> int:
    """f(22/7) mod 10^15.

    The fraction chain of 22/7 = 3 + 1/7 is 1/7 -> 1/6 -> 1/5 -> 1/4 ->
    1/3 -> 1/2, all m_i = 0 until phi(1/2) = 1. Solving the levels bottom-up:
    G(k, 1/2) = k + 2, G(k, 1/3) = 2k + 3, G(k, 1/4) = 2^(k+3) - 3, and
    G(k, 1/5) = 2^^(k+3) - 3 (tetration). The two outer levels iterate
    x -> 2^^(x+3) - 3, so f(22/7) = 2^^H - 3 with H a tower far exceeding
    65536. Since 2^^h mod 10^15 is constant once h exceeds the length of
    the iterated-totient chain of 10^15 (about 45), any height >= 64 gives
    the stabilized value.
    """
    return (tower2_mod(64, MOD) - 3) % MOD


if __name__ == "__main__":
    assert f_exact(Fraction(3, 2)) == 3
    assert f_exact(Fraction(1, 6)) == 65533
    assert f_exact(Fraction(13, 10)) == 7625597484985
    # Consistency with the closed forms used above: G(2, 1/4) = 2^5 - 3 and
    # G(1, 1/5) = 2^^4 - 3 = 65533 (note f(6/5) = f(1/6), as the chain shows).
    assert f_exact(Fraction(9, 4)) == 2**5 - 3
    assert f_exact(Fraction(6, 5)) == 2**16 - 3
    print(f_22_7_mod())  # 75353432948733
