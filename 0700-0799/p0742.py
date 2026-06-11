"""
Project Euler Problem 742: Minimum Area of a Symmetrical Convex Grid Polygon
https://projecteuler.net/problem=742

A(N) is the minimum area of a convex lattice polygon with N vertices that has
both horizontal and vertical mirror symmetry.  Find A(1000).

Structure.  The polygon is fixed by its first-quadrant chain of edge vectors
(-a_i, b_i) with a_i, b_i >= 1; convexity makes every direction appear once and
primitive vectors beat longer ones of the same slope.  For 4 | N there are two
configurations: vertices on both axes (lattice centre, t = N/4 chain vectors,
"VV") or unit edges crossing both axes (half-integer centre, t = N/4 - 1,
"EE").  Expanding 2*Area = sum_{i<j} cross(e_i, e_j) over the full symmetric
edge cycle gives

    Area_VV = 2 sum a_i b_i + 4 sum_{i<j} max(a_i b_j, a_j b_i),
    Area_EE = Area_VV + 2 sum (a_i + b_i) + 1.

The hand cases A(4) = 1 (unit square, EE with t = 0) and A(8) = 7 fix the
constants.

Exact DP.  Sort the candidate primitive vectors steepest first (slope b/a
descending).  Then for i before j, max(a_i b_j, a_j b_i) = a_j b_i, so a newly
chosen flatter vector j interacts with all earlier chosen vectors only through
4 a_j B, where B = sum of earlier chosen b's.  A DP over (count, B) is thus
exact: each vector adds 2 a b + 4 a B (plus 2(a + b) for the EE objective).
Over the pool of primitive vectors with a, b <= 40 and B <= 3000 this is exact
and reproduces A(40) = 1039 and A(100) = 17473; the value is stable under
enlarging the pool and cap.
"""

from math import gcd

import numpy as np
from numba import njit

INF = np.int64(1) << 60


@njit(cache=True)
def run_dp(av, bv, t, bcap, ee):
    """Minimum accumulated cost selecting exactly t vectors, DP over prefix
    sum B of chosen b's.  Vectors (av, bv) are pre-sorted steepest first.
    ee = 1 adds the per-vector 2(a+b) term for the EE objective."""
    dp = np.full((t + 1, bcap + 1), INF, dtype=np.int64)
    dp[0, 0] = 0
    nvec = av.shape[0]
    for v in range(nvec):
        a = av[v]
        b = bv[v]
        extra = 2 * (a + b) if ee == 1 else 0
        # iterate counts downward so each vector is used at most once
        for c in range(t - 1, -1, -1):
            row = dp[c]
            nrow = dp[c + 1]
            for bb in range(bcap - b + 1):
                cur = row[bb]
                if cur >= INF:
                    continue
                add = 2 * a * b + 4 * a * bb + extra
                nb = bb + b
                if cur + add < nrow[nb]:
                    nrow[nb] = cur + add
    best = INF
    for bb in range(bcap + 1):
        if dp[t, bb] < best:
            best = dp[t, bb]
    return best


def a_of(n, cap=40, bcap=3000):
    vecs = [
        (a, b)
        for a in range(1, cap + 1)
        for b in range(1, cap + 1)
        if gcd(a, b) == 1
    ]
    # steepest first: descending slope b/a, i.e. descending b * (1/a)
    vecs.sort(key=lambda v: -v[1] / v[0])
    av = np.array([a for a, _ in vecs], dtype=np.int64)
    bv = np.array([b for _, b in vecs], dtype=np.int64)

    best = INF
    # VV configuration: t = n/4 vectors
    if n % 4 == 0:
        t_vv = n // 4
        t_ee = n // 4 - 1
        if t_vv > 0:
            best = min(best, int(run_dp(av, bv, t_vv, bcap, 0)))
        if t_ee == 0:
            best = min(best, 1)  # EE unit square
        else:
            r = int(run_dp(av, bv, t_ee, bcap, 1))
            if r < INF:
                best = min(best, r + 1)
    return best


def main():
    assert a_of(4, 6, 60) == 1
    assert a_of(8, 8, 120) == 7
    assert a_of(40, 12, 400) == 1039
    assert a_of(100, 20, 800) == 17473
    return a_of(1000, 40, 3000)


if __name__ == "__main__":
    print(main())  # 18397727
