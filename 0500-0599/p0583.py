"""
https://projecteuler.net/problem=583

An envelope is a convex pentagon A, B, C, D, E made of a rectangle
ABDE (width w, height h) with an isosceles flap BCD of height t on
top, t < h for validity. A Heron envelope has all five sides and all
five diagonals (AC, AD, BD, BE, CE) integral. S(p) sums the
perimeters of Heron envelopes with perimeter at most p; find S(10^7).

Coordinates A = (0,0), E = (w,0), B = (0,h), D = (w,h),
C = (w/2, h+t) give BD = w, AD = BE = sqrt(w^2 + h^2),
BC = CD = sqrt((w/2)^2 + t^2), AC = CE = sqrt((w/2)^2 + (h+t)^2).
BC integral forces w even, w = 2u, leaving three Pythagorean
conditions sharing legs:

    u^2 + t^2,  u^2 + (h+t)^2  and  (2u)^2 + h^2  all squares,

with perimeter P = 2(h + u + sqrt(u^2 + t^2)) <= p, t >= 1, t < h.

For each u the legs x partnering u come from factorisations
u^2 = d * e with d < e of equal parity, x = (e - d)/2 -- generated
from the divisors of u^2 via an SPF sieve, keeping only 1 <= x <= p
(both t and h + t fit under p; larger x would overflow squares and
can never satisfy the perimeter bound). Each envelope is then a pair
t < y from that list with y > 2t (so h = y - t exceeds t), perimeter
within bound, and 4u^2 + h^2 a perfect square. Sorting the list lets
both loops break early on the monotone perimeter.

The whole pipeline is verified against an independent brute scan
(t and h enumerated directly with square tests) at p = 10^4 -- the
given S(10^4) = 884680 -- and p = 3 * 10^4.
"""

import numba
import numpy as np


@numba.njit(inline="always")
def _is_sq(v: int) -> bool:
    r = np.int64(np.sqrt(v))
    while r * r > v:
        r -= 1
    while (r + 1) * (r + 1) <= v:
        r += 1
    return r * r == v


@numba.njit(cache=True)
def _spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def _solve(p: int, spf: np.ndarray) -> np.int64:
    umax = p // 4
    total = np.int64(0)
    divs = np.empty(20000, dtype=np.int64)
    xs = np.empty(20000, dtype=np.int64)
    for u in range(1, umax + 1):
        m = u
        nd = 1
        divs[0] = 1
        while m > 1:
            q = spf[m]
            e = 0
            while m % q == 0:
                m //= q
                e += 1
            old = nd
            pw = np.int64(1)
            for _ in range(2 * e):
                pw *= q
                for i in range(old):
                    divs[nd] = divs[i] * pw
                    nd += 1
        u2 = np.int64(u) * u
        nx = 0
        for i in range(nd):
            d = divs[i]
            if d < u:  # d < e without overflowing d*d
                e = u2 // d
                if (e - d) % 2 == 0:
                    x = (e - d) // 2
                    if 1 <= x <= p:  # larger x can never fit the perimeter
                        xs[nx] = x
                        nx += 1
        sub = np.sort(xs[:nx])
        for i in range(nx):
            t = sub[i]
            c1sq = u2 + t * t
            c1 = np.int64(np.sqrt(c1sq))
            while c1 * c1 > c1sq:
                c1 -= 1
            while (c1 + 1) * (c1 + 1) <= c1sq:
                c1 += 1
            base = 2 * (u + c1)
            if base + 2 * (t + 1) > p:
                break
            for j in range(i + 1, nx):
                y = sub[j]
                if y <= 2 * t:
                    continue
                h = y - t
                per = base + 2 * h
                if per > p:
                    break
                if _is_sq(4 * u2 + h * h):
                    total += per
    return total


@numba.njit(cache=True)
def _brute(p: int) -> np.int64:
    total = np.int64(0)
    for u in range(1, p // 4 + 1):
        u2 = np.int64(u) * u
        for t in range(1, p // 2):
            c1sq = u2 + t * t
            c1 = np.int64(np.sqrt(c1sq))
            while c1 * c1 > c1sq:
                c1 -= 1
            while (c1 + 1) * (c1 + 1) <= c1sq:
                c1 += 1
            if c1 * c1 != c1sq:
                continue
            if 2 * (u + c1 + t + 1) > p:
                break
            for h in range(t + 1, p):
                per = 2 * (u + c1 + h)
                if per > p:
                    break
                if _is_sq(u2 + (h + t) * (h + t)) and _is_sq(4 * u2 + h * h):
                    total += per
    return total


if __name__ == "__main__":
    spf = _spf_sieve(2_500_001)
    assert int(_solve(10**4, spf)) == int(_brute(10**4)) == 884680  # given
    assert int(_solve(3 * 10**4, spf)) == int(_brute(3 * 10**4))

    print(int(_solve(10**7, spf)))  # 1174137929000
