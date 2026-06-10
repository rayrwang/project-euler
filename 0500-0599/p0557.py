"""
https://projecteuler.net/problem=557

A triangle is cut by two cevians, one from each of two vertices to
the opposite side, into four integer-area pieces: a (the triangle
between the two cut vertices), b and c (the other two triangles,
b <= c) and d (the quadrilateral). S(n) sums the total area
a + b + c + d over all valid quadruples with total at most n; find
S(10^4).

With cevian feet at fractions e, f along the sides, barycentric
coordinates of the intersection give a/T = (1-e)(1-f)/(1-ef),
b/T = e(1-f)^2/(1-ef), c/T = f(1-e)^2/(1-ef) for total T. From
a + b = (1-f)T and a + c = (1-e)T, i.e. e = (b+d)/T, f = (c+d)/T,
substituting back collapses the whole geometry into one relation:

    1/(a+b) + 1/(a+c) = 1/a + 1/T,

equivalently T (a^2 - bc) = a (a+b)(a+c), with d =
bc(2a + b + c)/(a^2 - bc) automatically a positive integer whenever
T is integral. Conversely any quadruple satisfying the relation has
e, f in (0, 1) reconstructing exactly those areas (checked with
exact rationals for every quadruple with T <= 60), so the relation
is the full characterisation.

Enumeration: for each a and b <= c with bc < a^2, T is monotone
increasing in c, so c is bounded by c <= a^2 (n-a-b)/(a^2+ab+nb)
from T <= n; the triple loop with a divisibility test then runs
about 2 * 10^10 iterations, parallelised over a. Verified against a
literal quadruple-loop brute force at n = 100, the given S(20) =
259, and the two given quadruples (22,8,11,14), (20,2,24,9) being
exactly the solutions with total 55.
"""

from fractions import Fraction

import numba
import numpy as np


@numba.njit(cache=True, parallel=True)
def _s_arr(n: int) -> np.ndarray:
    totals = np.zeros(n, dtype=np.int64)
    for a in numba.prange(1, n):  # ty: ignore[not-iterable]
        sub = np.int64(0)
        for b in range(1, n):
            num = a * a * (n - a - b)
            den = a * a + a * b + n * b
            cmax = num // den
            if cmax < b:
                break
            for c in range(b, cmax + 1):
                m = a * a - b * c
                if m <= 0:
                    break
                rhs = a * (a + b) * (a + c)
                if rhs % m == 0 and rhs // m <= n:
                    sub += rhs // m
        totals[a] = sub
    return totals


def s_of(n: int) -> int:
    return int(_s_arr(n).sum())


@numba.njit(cache=True)
def _brute_s(n: int) -> int:
    tot = 0
    for t in range(4, n + 1):
        for a in range(1, t - 2):
            for b in range(1, t - a - 1):
                for c in range(b, t - a - b):
                    d = t - a - b - c
                    if d < 1:
                        break
                    if t * (a * a - b * c) == a * (a + b) * (a + c):
                        tot += t
    return tot


def _areas_from_ef(e: Fraction, f: Fraction, t: Fraction):
    den = 1 - e * f
    a = (1 - e) * (1 - f) / den * t
    b = e * (1 - f) ** 2 / den * t
    c = f * (1 - e) ** 2 / den * t
    return a, b, c, t - a - b - c


if __name__ == "__main__":
    sols = []
    for t in range(4, 61):
        for a in range(1, t - 2):
            for b in range(1, t - a - 1):
                for c in range(b, t - a - b):
                    d = t - a - b - c
                    if d < 1:
                        break
                    if t * (a * a - b * c) == a * (a + b) * (a + c):
                        sols.append((a, b, c, d))
                        e, f = Fraction(b + d, t), Fraction(c + d, t)
                        assert 0 < e < 1 and 0 < f < 1
                        assert _areas_from_ef(e, f, Fraction(t)) == (a, b, c, d)
    assert sorted(s for s in sols if sum(s) == 55) == [
        (20, 2, 24, 9),
        (22, 8, 11, 14),
    ]  # given
    assert sum(sum(s) for s in sols if sum(s) <= 20) == 259 == s_of(20)  # given
    assert s_of(100) == _brute_s(100)

    print(s_of(10**4))  # 2699929328
