"""
https://projecteuler.net/problem=564

A segment of length 2n-3 is split uniformly at random into one of
the C(2n-4, n-1) ordered sequences of n positive integer parts,
which become consecutive sides of the maximal-area convex n-gon.
E(n) is the expected area; find S(50) = sum_(n=3..50) E(n) to 6
decimals.

The maximal-area polygon with given sides is the cyclic one, and its
area does not depend on the side order, so E(n) collapses to a sum
over partitions of 2n-3 into n parts (at most p(47) = 124754 of
them for n = 50), each weighted by its number of arrangements
n! / prod(multiplicities!) over the binomial total.

For each side multiset the circumradius R solves
sum_i 2 arcsin(s_i / 2R) = 2 pi when the centre is inside the
polygon (the expression is decreasing in R and at R = s_max / 2 its
sign decides the case); otherwise the centre lies beyond the longest
side and R solves arcsin(s_max / 2R) = sum_(i != max)
arcsin(s_i / 2R), with the longest side's triangle counted
negatively in the area sum A = sum +- (R^2 / 2) sin(2 arcsin(s_i /
2R)). A root always exists since s_max < sum of the rest (the
largest part of 2n-3 among n parts is at most n-2 < n-1). Bisection
to ~1e-15 relative accuracy over all 320k partitions gives S(50)
far beyond the required precision.

The given E(3) = 0.433013, E(4) = 1.299038, S(5) = 4.604767 and
S(10) = 66.955511 are asserted.
"""

from collections import Counter
from math import comb, factorial

import numba
import numpy as np


@numba.njit(cache=True)
def _cyclic_area(s: np.ndarray) -> float:
    smax = s[0]
    n = len(s)
    r0 = smax / 2.0
    h0 = -2 * np.pi
    for i in range(n):
        h0 += 2 * np.arcsin(min(s[i] / (2 * r0), 1.0))
    if h0 >= 0.0:  # circumcentre inside
        lo, hi = r0, r0
        while True:
            hi *= 2
            hh = -2 * np.pi
            for i in range(n):
                hh += 2 * np.arcsin(s[i] / (2 * hi))
            if hh < 0:
                break
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            hh = -2 * np.pi
            for i in range(n):
                hh += 2 * np.arcsin(s[i] / (2 * mid))
            if hh >= 0:
                lo = mid
            else:
                hi = mid
        r = 0.5 * (lo + hi)
        a = 0.0
        for i in range(n):
            a += 0.5 * r * r * np.sin(2 * np.arcsin(s[i] / (2 * r)))
        return a
    # centre beyond the longest side
    lo, hi = r0, r0
    while True:
        hi *= 2
        gg = -np.arcsin(min(smax / (2 * hi), 1.0))
        for i in range(1, n):
            gg += np.arcsin(s[i] / (2 * hi))
        if gg > 0:
            break
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        gg = -np.arcsin(min(smax / (2 * mid), 1.0))
        for i in range(1, n):
            gg += np.arcsin(s[i] / (2 * mid))
        if gg > 0:
            hi = mid
        else:
            lo = mid
    r = 0.5 * (lo + hi)
    a = -0.5 * r * r * np.sin(2 * np.arcsin(min(smax / (2 * r), 1.0)))
    for i in range(1, n):
        a += 0.5 * r * r * np.sin(2 * np.arcsin(s[i] / (2 * r)))
    return a


def _partitions(t: int) -> list[list[int]]:
    out: list[list[int]] = []

    def rec(rem: int, mx: int, cur: list[int]) -> None:
        if rem == 0:
            out.append(cur[:])
            return
        for p in range(min(rem, mx), 0, -1):
            cur.append(p)
            rec(rem - p, p, cur)
            cur.pop()

    rec(t, max(t, 1), [])
    return out if t > 0 else [[]]


def e_of(n: int) -> float:
    total_w = comb(2 * n - 4, n - 1)
    acc = 0.0
    for part in _partitions(n - 3):
        if len(part) > n:
            continue
        sides = sorted((p + 1 for p in part), reverse=True) + [1] * (n - len(part))
        w = factorial(n)
        for c in Counter(sides).values():
            w //= factorial(c)
        acc += (w / total_w) * _cyclic_area(np.array(sides, dtype=np.float64))
    return acc


if __name__ == "__main__":
    assert round(e_of(3), 6) == 0.433013  # given
    assert round(e_of(4), 6) == 1.299038  # given
    assert round(sum(e_of(n) for n in range(3, 6)), 6) == 4.604767  # given
    assert round(sum(e_of(n) for n in range(3, 11)), 6) == 66.955511  # given

    print(f"{sum(e_of(n) for n in range(3, 51)):.6f}")  # 12363.698850
