"""
https://projecteuler.net/problem=513

ABC has integral sides a <= b <= c, and m_C is the median from C to
the midpoint of AB. F(n) counts triangles with c <= n whose median
m_C is also integral; find F(10^5).

The median length satisfies 4 m^2 = 2a^2 + 2b^2 - c^2. Working mod 8
forces c = 2C even and a = b (mod 2), so with S = (a+b)/2 and
D = (b-a)/2 the condition becomes

    S^2 + D^2 = C^2 + m^2,

with the triangle and ordering constraints C < S <= 2C (degenerate
and c-maximality), 0 <= D <= 2C - S (this is b <= c) and m >= 1.
Grouping as (S-C)(S+C) = (m-D)(m+D) = u w = x y and applying the
standard bijection u = pr, x = ps, w = qs, y = qr with gcd(r,s) = 1
(p = gcd(u,x)), the constraints translate to linear conditions on q:

    qs <= pr + 2C_max,   qs >= 3pr,   qr >= ps,
    q(r - s) <= p(s - 3r)   [forcing s > r],
    and parity: q = p (mod 2) if r, s both odd, else p, q both even.

For each (r, s, p) the admissible q form an arithmetic progression
counted in O(1); the bound q s <= p r + 2 C_max caps s near
sqrt(r^2 + 2 C_max r / p), giving roughly C_max^2 log C_max ~ 10^10
iterations overall, parallelised over r.

Verified against a literal brute force (integer square test of
2a^2 + 2b^2 - c^2 over all triangles) for n in {10, 50, 100, 300,
700}, including the given F(10) = 3 and F(50) = 165.
"""

import numba
import numpy as np


@numba.njit(cache=True)
def _brute(n: int) -> int:
    cnt = 0
    for c in range(2, n + 1):
        for b in range(1, c + 1):
            for a in range(max(1, c - b + 1), b + 1):
                v = 2 * a * a + 2 * b * b - c * c
                if v > 0 and v % 4 == 0:
                    w = v // 4
                    m = np.int64(np.sqrt(w))
                    while m * m > w:
                        m -= 1
                    while (m + 1) * (m + 1) <= w:
                        m += 1
                    if m >= 1 and m * m == w:
                        cnt += 1
    return cnt


@numba.njit(cache=True, parallel=True)
def _fast(n: int) -> np.int64:
    n2 = n // 2
    totals = np.zeros(n2 + 1, dtype=np.int64)
    for r in numba.prange(1, n2 + 1):  # ty: ignore[not-iterable]
        sub = np.int64(0)
        smax = np.int64(np.sqrt(r * r + 2.0 * n2 * r)) + 2
        for s in range(r + 1, smax + 1):
            x, y = r, s
            while y:
                x, y = y, x % y
            if x != 1:
                continue
            both_odd = (r % 2 == 1) and (s % 2 == 1)
            pmax = min(n2 // r, 2 * n2 * r // (s * s - r * r))
            for p in range(1, pmax + 1):
                if not both_odd and p % 2 == 1:
                    continue
                qhi = (p * r + 2 * n2) // s
                qlo = max((3 * p * r + s - 1) // s, (p * s + r - 1) // r)
                if 3 * r > s:  # q(r-s) <= p(s-3r), i.e. D <= 2C - S
                    t2 = (p * (3 * r - s) + (s - r) - 1) // (s - r)
                    if t2 > qlo:
                        qlo = t2
                if qlo < 1:
                    qlo = 1
                if qhi < qlo:
                    continue
                if both_odd:
                    lo = qlo + ((p - qlo) % 2)
                else:
                    lo = qlo + (qlo % 2)
                if lo <= qhi:
                    sub += (qhi - lo) // 2 + 1
        totals[r] = sub
    return totals.sum()


if __name__ == "__main__":
    assert _brute(10) == 3 == _fast(10)  # given
    assert _brute(50) == 165 == _fast(50)  # given
    for n in (100, 300, 700):
        assert _brute(n) == _fast(n), n

    print(_fast(100000))  # 2925619196
