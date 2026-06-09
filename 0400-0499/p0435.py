MOD = 1307674368000  # 15!

def fib_pair(n: int, mod: int) -> tuple[int, int]:
    """(f_n, f_{n+1}) mod `mod` via fast doubling, with f_0=0, f_1=1."""
    if n == 0:
        return (0 % mod, 1 % mod)
    a, b = fib_pair(n >> 1, mod)
    c = a * ((2 * b - a) % mod) % mod
    d = (a * a + b * b) % mod
    if n & 1:
        return (d, (c + d) % mod)
    return (c, d)

def f_n_at(n: int, x: int, m: int) -> int:
    """F_n(x) = sum_{i=0}^n f_i x^i, reduced mod m.

    Since sum_i f_i x^i = x/(1-x-x^2), the partial sum telescopes to
        F_n(x) = (f_{n+1} x^{n+1} + f_n x^{n+2} - x) / (x^2 + x - 1),
    an exact integer. The denominator D = x^2+x-1 may not be invertible mod m,
    so compute the numerator mod m*D (where it equals D*(F_n(x) mod m)) and
    divide by D.
    """
    if x == 0:
        return 0
    d = x * x + x - 1
    md = m * d
    fn, fn1 = fib_pair(n, md)
    numerator = (fn1 * pow(x, n + 1, md) + fn * pow(x, n + 2, md) - x) % md
    return (numerator // d) % m

if __name__ == "__main__":
    assert f_n_at(7, 11, 10**18) == 268357683
    n = 10**15
    print(sum(f_n_at(n, x, MOD) for x in range(101)) % MOD)  # 252541322550
