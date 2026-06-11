"""
Project Euler Problem 738: Counting Ordered Factorisations
https://projecteuler.net/problem=738

d(n, k) counts factorisations n = x_1 * ... * x_k with 1 <= x_1 <= ... <= x_k,
and D(N, K) = sum over n <= N, k <= K of d(n, k).  Find D(10^10, 10^10) mod
10^9 + 7.

Reduction.  Dropping padding 1s, a factorisation of n with k factors is a
multiset of factors >= 2 of size j <= k.  A multiset of size j is counted in
d(n, k) for every k >= max(j, 1), i.e. with weight K - j + 1 (the empty
multiset of n = 1 has weight K).  Letting c be the number of multisets of
integers >= 2 with product <= N (empty multiset included) and s the sum of
their sizes,

    D(N, K) = K + (K + 1)(c - 1) - s,

valid because K = 10^10 far exceeds the largest possible multiset size
(log2 N ~ 33).

Smallest-factor recursion.  Conditioning on the smallest element f,

    c(B, m) = 1 + sum_{f >= m, f <= B} c(floor(B / f), f),

with a parallel recursion for the size sum.  Every f > sqrt(B) admits only the
singleton {f}, so that tail is a closed form (count B - max(m, 2) + 1 with size
1 each) and the recursion branches only on f <= sqrt(B).  Counts are taken
modulo 10^9 + 7; the size sum s is bounded by c * 33 so it also fits once
reduced.  Verified against D(10, 10) = 153 and D(100, 100) = 35384.
"""

import numpy as np
from numba import njit

MOD = 1_000_000_007


@njit(cache=True)
def isqrt_nb(x):
    if x < 2:
        return x
    r = np.int64(np.sqrt(np.float64(x)))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


@njit(cache=False)
def rec(b, m):
    """Return (count, sizesum) mod MOD for multisets of integers >= m with
    product <= b (empty multiset included, contributing count 1 size 0)."""
    count = np.int64(1)  # empty multiset
    size = np.int64(0)
    r = isqrt_nb(b)
    f = m
    while f <= r:
        sub_c, sub_s = rec(b // f, f)
        count = (count + sub_c) % MOD
        # each sub-multiset gains one element (the f we prepend): size += sub_c + sub_s
        size = (size + sub_c + sub_s) % MOD
        f += 1
    # f in (sqrt(b), b]: only the singleton {f} fits (f*f > b), size 1 each
    lo = r + 1
    if lo < m:
        lo = m
    if lo <= b:
        cnt = b - lo + 1
        count = (count + cnt) % MOD
        size = (size + cnt) % MOD
    return count, size


def d_of(n, k):
    c, s = rec(n, 2)
    c %= MOD
    s %= MOD
    return (k + (k + 1) * (c - 1) - s) % MOD


def main():
    assert d_of(10, 10) == 153
    assert d_of(100, 100) == 35384
    return d_of(10**10, 10**10)


if __name__ == "__main__":
    print(main())  # 143091030
