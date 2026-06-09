"""
https://projecteuler.net/problem=555

M_{m,k,s}(n) = n - s for n > m, else M(M(n + k)). With F the set of
fixed points, SF their sum, and S(p, m) = sum of SF(m, k, s) over
1 <= s < k <= p, find S(10^6, 10^6).

Structure: let d = k - s > 0. For n in (m - k, m] we have n + k > m,
so M(n) = M(M(n + k)) = M(n + k - s) = M(n + d): M is d-periodic just
below m, and iterating until the argument exceeds m gives values in
(m - s, m - s + d]. Working downward, the same periodicity propagates
to all n <= m exactly when the second application lands back in a
consistent residue, which happens iff d | s. In that case M maps every
n <= m to the unique element of [m - s + 1, m - s + d] congruent to it
modulo d, so the fixed points are precisely the (at most d)
non-negative integers in that interval; if d does not divide s there
are no fixed points at all. This characterization is verified below by
exhaustive comparison with the literal recursive definition for
several m and every 1 <= s < k <= 3m + 2 (covering the clipping at 0
when s > m).

For S(p, m) with p <= m + 1 no clipping occurs (s < k <= p implies
s <= m), so writing s = d t, k = d (t + 1):

    S(p, m) = sum_{d >= 1} sum_{t = 1}^{floor(p / d) - 1}
              [ d (m - d t) + d (d + 1) / 2 ],

and the inner sum collapses to a closed form, leaving a single O(p)
loop over d.
"""

import sys
from functools import lru_cache


def fixed_points_brute(m: int, k: int, s: int) -> list[int]:
    """Fixed points straight from the recursive definition."""

    @lru_cache(maxsize=None)
    def m_rec(n: int) -> int:
        if n > m:
            return n - s
        return m_rec(m_rec(n + k))

    return [n for n in range(m + 1) if m_rec(n) == n]


def fixed_points_formula(m: int, k: int, s: int) -> list[int]:
    d = k - s
    if s % d != 0:
        return []
    lo, hi = max(0, m - s + 1), m - s + d
    return list(range(lo, hi + 1)) if hi >= 0 else []


def s_of(p: int, m: int) -> int:
    assert p <= m + 1  # no clipping below 0 in this regime
    total = 0
    for d in range(1, p // 2 + 1):
        t_max = p // d - 1
        if t_max < 1:
            continue
        total += (
            t_max * d * m - d * d * t_max * (t_max + 1) // 2 + t_max * d * (d + 1) // 2
        )
    return total


if __name__ == "__main__":
    sys.setrecursionlimit(1_000_000)
    # the fixed-point characterization matches the literal definition
    for mm in (1, 2, 7, 23, 30, 41):
        for kk in range(2, 3 * mm + 3):
            for ss in range(1, kk):
                assert fixed_points_brute(mm, kk, ss) == fixed_points_formula(
                    mm, kk, ss
                ), (mm, kk, ss)
    assert fixed_points_formula(100, 11, 10) == [91]  # the McCarthy 91 case
    assert s_of(10, 10) == 225
    assert s_of(1000, 1000) == 208724467

    print(s_of(10**6, 10**6))  # 208517717451208352
