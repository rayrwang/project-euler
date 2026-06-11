"""Problem 422: Sequence of Points on a Hyperbola.

12x^2 + 7xy - 12y^2 factors as (3x + 4y)(4x - 3y), so on the hyperbola
u v = 625 the substitution u = 25t, v = 25/t gives x = 3t + 4/t,
y = 4t - 3/t, and a chord between parameters t1, t2 has slope
proportional to -1/(t1 t2): chords are parallel iff their parameter
products agree. Since t_X = 1, the construction reads
t_i t_{i-1} = t_{i-2}, i.e. t_i = t_{i-2}/t_{i-1}, and with t_1 = 4,
t_2 = -3/2 the exponents follow c_i = c_{i-2} - c_{i-1}:
    t_n = 4^{a_n} (-3/2)^{b_n},  a_n = (-1)^{n+1} F_{n-2},
                                 b_n = (-1)^n F_{n-1}.
For odd n this is t = s * 2^alpha / 3^m with alpha = F_{n-2} + F_n,
m = F_{n-1}, s = (-1)^m, and the coordinates reduce in closed form:
    x = s (2^{2 alpha - 2} + 3^{2m - 1}) / (2^{alpha - 2} 3^{m - 1}),
    y = s (2^{2 alpha + 2} - 3^{2m + 1}) / (2^{alpha} 3^{m}),
already in lowest terms (numerators are odd-or-v2-exhausted and prime
to 3 by inspection of residues). Everything needed modulo p only
depends on the Fibonacci numbers modulo p - 1 (Fermat) and modulo 2
(the sign).
"""

from fractions import Fraction

P = 10**9 + 7

def exact_point(n: int) -> tuple[Fraction, Fraction]:
    t1, t2 = Fraction(4), Fraction(-3, 2)
    if n == 1:
        t = t1
    elif n == 2:
        t = t2
    else:
        for _ in range(n - 2):
            t1, t2 = t2, t1 / t2
        t = t2
    return 3 * t + 4 / t, 4 * t - 3 / t

def answer_exact(n: int) -> int:
    x, y = exact_point(n)
    return (x.numerator + x.denominator
            + y.numerator + y.denominator) % P

def fib_pair(k: int, mod: int) -> tuple[int, int]:
    if k == 0:
        return 0, 1 % mod
    f, g = fib_pair(k >> 1, mod)
    a = f * (2 * g - f) % mod
    b = (f * f + g * g) % mod
    return (b, (a + b) % mod) if k & 1 else (a, b)

def answer_modular(n: int) -> int:
    """For odd n >= 5 (the case of the target index)."""
    assert n % 2 == 1 and n >= 5
    e = P - 1
    fn2, fn1 = fib_pair(n - 2, e)   # F_{n-2}, F_{n-1} mod p-1
    fn = (fn2 + fn1) % e            # F_n mod p-1
    alpha = (fn2 + fn) % e
    m = fn1
    s = -1 if fib_pair(n - 1, 2)[0] else 1
    xn = s * (pow(2, (2 * alpha - 2) % e, P)
              + pow(3, (2 * m - 1) % e, P)) % P
    xd = pow(2, (alpha - 2) % e, P) * pow(3, (m - 1) % e, P) % P
    yn = s * (pow(2, (2 * alpha + 2) % e, P)
              - pow(3, (2 * m + 1) % e, P)) % P
    yd = pow(2, alpha, P) * pow(3, m, P) % P
    return (xn + xd + yn + yd) % P

if __name__ == "__main__":
    assert exact_point(3) == (Fraction(-19, 2), Fraction(-229, 24))  # given
    assert exact_point(4) == (Fraction(1267, 144), Fraction(-37, 12))  # given
    assert exact_point(7) == (Fraction(17194218091, 143327232),
                              Fraction(274748766781, 1719926784))  # given
    assert answer_exact(7) == 806236837  # given
    for n in range(5, 31, 2):
        assert answer_modular(n) == answer_exact(n), n
    print(answer_modular(11**14))  # 92060460
