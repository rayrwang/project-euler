"""
https://projecteuler.net/problem=567

Each of n turns picks k uniformly from 1..n with prize 1/k. In game
A the generator (each of n lights on with probability 1/2) fires
once and Jerry wins 1/k if exactly k lights are on; in game B Tom
and Jerry each generate a uniformly random k-subset and Jerry wins
1/k on a match. Over the n turns,

    J_A(n) = 2^-n sum_k C(n,k)/k,    J_B(n) = sum_k 1/(k C(n,k)).

Find S(m) = sum_(n<=m) (J_A(n) + J_B(n)) for m = 123456789, to 8 dp.

For A, the identity sum_k C(n,k)/k = sum_j (2^j - 1)/j (verified
exactly for n < 200) lets the double sum telescope over n:

    sum_(n<=m) J_A(n) = 2 H_m - 2 sum_(j<=m) 2^-j / j - E(m),

with E(m) = sum_j (2^(j-m) - 2^-m)/j carrying only the ~200 top
terms. For B, the terms of J_B decay super-polynomially away from
the edges k = 1, 2, ... and k = n, n-1, ...; summing windows of 60
from each edge (Kahan-compensated) is exact to double precision for
n up to N0 = 10^6, and beyond N0 the expansion
J_B(n) = 2/n + 2/(n(n-1)) + 4/(n(n-1)(n-2)) + O(1/n^4) telescopes in
closed form, the neglected tail being below 4/N0^3 * O(1) ~ 1e-17.
H_m uses the Euler-Maclaurin form ln m + gamma + 1/2m - ... with
error far below 1e-9 (checked against exact partial sums).

Asserted: the given J_A(6) = 0.39505208, J_B(6) = 0.43333333 and
S(6) = 7.58932292 (computed exactly with fractions), exact-vs-fast
agreement of S(100) to 1e-9, and stability of the answer under
N0 -> 2 * 10^6.
"""

from fractions import Fraction
from math import comb, log

import numba

GAMMA = 0.5772156649015328606065120900824024


def _ja_exact(n: int) -> Fraction:
    return Fraction(sum(Fraction(comb(n, k), k) for k in range(1, n + 1)), 2**n)


def _jb_exact(n: int) -> Fraction:
    return sum((Fraction(1, k * comb(n, k)) for k in range(1, n + 1)), Fraction(0))


def _h(m: int) -> float:
    if m < 100:
        return sum(1.0 / i for i in range(1, m + 1))
    return log(m) + GAMMA + 1 / (2 * m) - 1 / (12 * m**2) + 1 / (120 * m**4)


@numba.njit(cache=True)
def _sum_jb_upto(n0: int) -> float:
    """Kahan-compensated sum of J_B(n) for n = 1..n0."""
    total = 0.0
    comp = 0.0
    for n in range(1, n0 + 1):
        s = 0.0
        if n <= 120:
            c = 1.0
            for k in range(1, n + 1):
                c = c * (n - k + 1) / k
                s += 1.0 / (k * c)
        else:
            c = 1.0
            for k in range(1, 61):  # small-k edge
                c = c * (n - k + 1) / k
                s += 1.0 / (k * c)
            c = 1.0
            for j in range(60):  # k = n - j edge, C(n, n-j) = C(n, j)
                if j > 0:
                    c = c * (n - j + 1) / j
                s += 1.0 / ((n - j) * c)
        y = s - comp
        t = total + y
        comp = (t - total) - y
        total = t
    return total


def s_of(m: int, n0: int = 10**6) -> float:
    el = sum(2.0 ** (-j) / j for j in range(1, min(80, m + 1)))
    e = sum(2.0 ** (-i) / (m - i) for i in range(min(200, m)))
    if m <= 60:
        e -= 2.0 ** (-m) * _h(m)
    sum_ja = 2 * _h(m) - 2 * el - e
    n0 = min(n0, m)
    sum_jb = _sum_jb_upto(n0)
    sum_jb += 2 * (_h(m) - _h(n0))
    sum_jb += 2 * (1.0 / n0 - 1.0 / m)
    sum_jb += 2 * (1.0 / ((n0 - 1) * n0) - 1.0 / ((m - 1) * m))
    return sum_ja + sum_jb


if __name__ == "__main__":
    for n in range(1, 200):  # identity behind the J_A telescope
        lhs = sum(Fraction(comb(n, k), k) for k in range(1, n + 1))
        assert lhs == sum(Fraction(2**j - 1, j) for j in range(1, n + 1))

    assert f"{float(_ja_exact(6)):.8f}" == "0.39505208"  # given
    assert f"{float(_jb_exact(6)):.8f}" == "0.43333333"  # given
    s6 = float(sum(_ja_exact(n) + _jb_exact(n) for n in range(1, 7)))
    assert f"{s6:.8f}" == "7.58932292" == f"{s_of(6):.8f}"  # given

    s100 = float(sum(_ja_exact(n) + _jb_exact(n) for n in range(1, 101)))
    assert abs(s_of(100) - s100) < 1e-9

    ans = s_of(123456789)
    assert abs(s_of(123456789, n0=2 * 10**6) - ans) < 1e-9

    print(f"{ans:.8f}")  # 75.44817535
