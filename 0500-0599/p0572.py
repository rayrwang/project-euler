"""
https://projecteuler.net/problem=572

C(n) counts 3x3 integer matrices with M^2 = M and all entries in
[-n, n]; find C(200).

An idempotent matrix is a projection: its rank equals its trace,
which is 0, 1, 2 or 3. Rank 0 and 3 give M = 0 and M = I. A rank-1
integer idempotent factors as M = m p q^T with p, q primitive integer
vectors, and trace m (p . q) = 1 forces m = +-1, so M = p q^T with
p . q = 1 -- and that dot product in turn forces both vectors to be
primitive automatically (a common factor of either would divide 1).
The factorisation is unique up to negating both vectors, so each
matrix corresponds to exactly two pairs (p, q). Rank-2 idempotents
are complements: M^2 = M iff (I - M)^2 = I - M, so they biject with
rank-1 idempotents N = I - M whose off-diagonal entries lie in
[-n, n] and diagonal entries in [1-n, n+1].

Counting pairs: entry (i, j) of p q^T is p_i q_j, so each coordinate
q_j is confined to an interval determined by p (off-diagonal bounds
n/|p_i| and the diagonal product window). Sweep all p with
|p_i| <= n+1 (some q_j is nonzero, so every |p_i| is at most the
largest entry bound); for each p and each q_3 in its interval the
equation p1 q1 + p2 q2 = 1 - p3 q3 is a line in the (q1, q2)
rectangle, counted in O(1) by extended-gcd parametrisation and
interval intersection. The all-zero p is impossible (p . q = 1).
The grand total halves for the (p, q) ~ (-p, -q) symmetry.

C(n) = 2 + R1(box [-n,n]) + R1(box with diagonal [1-n, n+1]) is
verified against literal 9-loop brute force for n = 1, 2, 3,
including the given C(1) = 164 and C(2) = 848.
"""

import numba
import numpy as np


@numba.njit(inline="always")
def _cdiv(a: int, b: int) -> int:
    return -((-a) // b)


@numba.njit(inline="always")
def _interval(p: int, c1: int, c2: int, lo: int, hi: int):
    """Intersect [lo, hi] with {q : c1 <= p*q <= c2}."""
    if p > 0:
        lo = max(lo, _cdiv(c1, p))
        hi = min(hi, c2 // p)
    elif p < 0:
        lo = max(lo, _cdiv(c2, p))
        hi = min(hi, c1 // p)
    elif not (c1 <= 0 <= c2):
        return np.int64(1), np.int64(0)
    return lo, hi


@numba.njit(inline="always")
def _q_iv(p_self: int, p_o1: int, p_o2: int, n: int, dlo: int, dhi: int):
    lo = np.int64(-(1 << 50))
    hi = np.int64(1 << 50)
    lo, hi = _interval(p_self, dlo, dhi, lo, hi)
    if lo > hi:
        return lo, hi
    lo, hi = _interval(p_o1, -n, n, lo, hi)
    if lo > hi:
        return lo, hi
    return _interval(p_o2, -n, n, lo, hi)


@numba.njit(inline="always")
def _ext_gcd(a: int, b: int):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t  # a*old_s + b*old_t = old_r


@numba.njit(inline="always")
def _t_range(qp: int, b: int, lo: int, hi: int):
    """t with lo <= qp + b*t <= hi."""
    if b > 0:
        return _cdiv(lo - qp, b), (hi - qp) // b
    if b < 0:
        return _cdiv(hi - qp, b), (lo - qp) // b
    if lo <= qp <= hi:
        return np.int64(-(1 << 50)), np.int64(1 << 50)
    return np.int64(1), np.int64(0)


@numba.njit(cache=True)
def _count_rank1(n: int, dlo: int, dhi: int) -> np.int64:
    """Rank-1 idempotents p q^T with p.q = 1, off-diagonal entries
    |p_i q_j| <= n and diagonal products in [dlo, dhi]."""
    total = np.int64(0)
    pb = n + 1
    for p1 in range(-pb, pb + 1):
        for p2 in range(-pb, pb + 1):
            gg = np.int64(1)
            s0 = np.int64(0)
            t0 = np.int64(0)
            if p1 != 0 or p2 != 0:
                gg, s0, t0 = _ext_gcd(p1, p2)
            for p3 in range(-pb, pb + 1):
                if p1 == 0 and p2 == 0 and p3 == 0:
                    continue  # p.q = 1 impossible
                lo3, hi3 = _q_iv(p3, p1, p2, n, dlo, dhi)
                if lo3 > hi3:
                    continue
                lo1, hi1 = _q_iv(p1, p2, p3, n, dlo, dhi)
                if lo1 > hi1:
                    continue
                lo2, hi2 = _q_iv(p2, p1, p3, n, dlo, dhi)
                if lo2 > hi2:
                    continue
                for q3 in range(lo3, hi3 + 1):
                    r = 1 - p3 * q3
                    if p1 == 0 and p2 == 0:
                        if r == 0:
                            total += (hi1 - lo1 + 1) * (hi2 - lo2 + 1)
                        continue
                    if r % gg != 0:
                        continue
                    mul = r // gg
                    q1p = s0 * mul
                    q2p = t0 * mul
                    tlo1, thi1 = _t_range(q1p, p2 // gg, lo1, hi1)
                    if tlo1 > thi1:
                        continue
                    tlo2, thi2 = _t_range(q2p, -(p1 // gg), lo2, hi2)
                    tlo = max(tlo1, tlo2)
                    thi = min(thi1, thi2)
                    if thi >= tlo:
                        total += thi - tlo + 1
    return total // 2


@numba.njit(cache=True)
def _brute_c(n: int) -> int:
    cnt = 0
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            for c in range(-n, n + 1):
                for d in range(-n, n + 1):
                    for e in range(-n, n + 1):
                        for f in range(-n, n + 1):
                            for g in range(-n, n + 1):
                                if a * a + b * d + c * g != a:
                                    continue
                                for h in range(-n, n + 1):
                                    if a * b + b * e + c * h != b:
                                        continue
                                    if d * a + e * d + f * g != d:
                                        continue
                                    for i in range(-n, n + 1):
                                        if (
                                            a * c + b * f + c * i == c
                                            and d * b + e * e + f * h == e
                                            and d * c + e * f + f * i == f
                                            and g * a + h * d + i * g == g
                                            and g * b + h * e + i * h == h
                                            and g * c + h * f + i * i == i
                                        ):
                                            cnt += 1
    return cnt


def c_of(n: int) -> int:
    return 2 + int(_count_rank1(n, -n, n)) + int(_count_rank1(n, 1 - n, 1 + n))


if __name__ == "__main__":
    assert c_of(1) == _brute_c(1) == 164  # given
    assert c_of(2) == _brute_c(2) == 848  # given
    assert c_of(3) == _brute_c(3)

    print(c_of(200))  # 19737656
