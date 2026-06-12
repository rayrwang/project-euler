"""
Project Euler Problem 791: Average and Variance
https://projecteuler.net/problem=791

S(n) sums a + b + c + d over all integer quadruples 1 <= a <= b <= c <= d <= n
whose average equals exactly twice their variance.  Given S(5) = 48 and
S(10^3) = 37048340, find S(10^8) modulo 433494437.

Reduction.  For four values with sum s and sum of squares Q2, the variance is
Q2/4 - (s/4)^2, so "mean = 2 * variance" is 4 Q2 - s^2 = 2 s, i.e.

    sum_{i<j} (x_i - x_j)^2 = 2 s     (since 4 Q2 - s^2 = sum_{i<j}(x_i-x_j)^2).

Writing the sorted gaps p = b - a, q = c - b, r = d - c >= 0 and expanding,

    8 a = 3 p^2 + 4 p q + 2 p r - 6 p + 4 q^2 + 4 q r + 3 r^2 - 2 r =: Q(p, q, r).

So each gap triple (p, q, r) determines a uniquely, with the quadruple valid
when a = Q/8 is a positive integer and d = a + p + q + r <= n.  A short
check shows Q(p, q, r) is divisible by 8 exactly when r ≡ p (mod 2), and then
Q/8 is automatically an integer; no other divisibility constraint arises.

Summation.  The quadruple sum is s = 4 a + 3 p + 2 q + r = Q/2 + 3 p + 2 q + r.
Fixing (p, q) and letting r run over the values of the correct parity in the
feasible window [r_lo, r_hi] (from a >= 1 and d <= n, both quadratic in r),
the summand is a quadratic in r, so the inner sum over the arithmetic
progression r = r0, r0+2, ... has a closed form.  Both feasible bounds p and
q are O(sqrt(n)) (the form lies in an ellipsoid 3 p^2 + 4 q^2 <~ 8 n), so
looping over the O(n) pairs (p, q) with that O(1) inner sum is an O(n)
algorithm; everything is reduced modulo the prime 433494437, with the
parity-respecting range endpoints found by an exact integer solve of the two
quadratics.  Note the q-feasible set is not always an interval containing
q = 0 (small q can fail a >= 1 while larger q succeeds), so q is swept over
its full range rather than stopped at the first gap.  S(5), S(30) and
S(1000) = 37048340 are asserted before the final run.

Parallelism.  Each prange iteration accumulates its per-p contribution
(already reduced mod MOD) in a local scalar and stores it in acc[p], an
array with exactly one slot per p, so no two threads ever write the same
element; the slots are summed serially afterwards.  (An earlier version
wrote into a 256-slot array at index p % 256, which shares slots across
threads -- a data race under prange that produced nondeterministic results.
A plain scalar reduction `total += local` would also be correct, but it
trips a Numba parfor reduction-analysis bug, "unexpected cycle in lookup()",
when the added value is itself loop-carried, hence the per-p array.)
"""


import numpy as np
from numba import njit, prange

MOD = 433494437
INV2 = (MOD + 1) // 2
INV6 = pow(6, MOD - 2, MOD)


@njit(cache=True)
def isqrt_nb(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    r = int(np.sqrt(np.float64(x)))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


@njit(cache=True)
def qval(p, q, r):
    return (
        3 * p * p
        + 4 * p * q
        + 2 * p * r
        - 6 * p
        + 4 * q * q
        + 4 * q * r
        + 3 * r * r
        - 2 * r
    )


@njit(cache=True)
def feasible_r_max(p, q, n):
    """Largest r >= 0 with a = Q/8 >= 1 and d = a + p + q + r <= n, where the
    feasible r form an interval [r_lo, r_hi].  Returns (r_lo, r_hi) or a flag
    r_hi < r_lo for empty.  Conditions:
       a >= 1   :  Q(p,q,r) >= 8
       d <= n   :  Q + 8(p + q + r) <= 8 n
    Both quadratics in r open upward / upward; intersect their solution sets.
    """
    # d <= n  <=>  3 r^2 + (2p + 4q - 2 + 8) r + (3p^2+4pq-6p+4q^2-4q + 8p+8q) <= 8n
    # i.e. 3 r^2 + (2p+4q+6) r + (3p^2+4pq+2p+4q^2+4q) - 8n <= 0
    a2 = 3
    b2 = 2 * p + 4 * q + 6
    c2 = 3 * p * p + 4 * p * q + 2 * p + 4 * q * q + 4 * q - 8 * n
    disc = b2 * b2 - 4 * a2 * c2
    if disc < 0:
        return 1, 0  # empty
    sq = isqrt_nb(disc)
    # upper root r <= (-b2 + sq) / (2 a2)
    r_upper = (-b2 + sq) // (2 * a2)
    while a2 * r_upper * r_upper + b2 * r_upper + c2 > 0:
        r_upper -= 1
    while a2 * (r_upper + 1) * (r_upper + 1) + b2 * (r_upper + 1) + c2 <= 0:
        r_upper += 1
    if r_upper < 0:
        return 1, 0
    # a >= 1 : Q(p,q,r) >= 8.  Q = 3 r^2 + (2p+4q-2) r + (3p^2+4pq-6p+4q^2-4q)
    a1 = 3
    b1 = 2 * p + 4 * q - 2
    c1 = 3 * p * p + 4 * p * q - 6 * p + 4 * q * q - 4 * q - 8
    # smallest r >= 0 with a1 r^2 + b1 r + c1 >= 0
    r_lo = 0
    if a1 * 0 + b1 * 0 + c1 < 0:
        disc1 = b1 * b1 - 4 * a1 * c1
        if disc1 < 0:
            return 1, 0  # never non-negative (shouldn't happen, a1>0)
        sq1 = isqrt_nb(disc1)
        r_lo = (-b1 + sq1) // (2 * a1)
        while a1 * r_lo * r_lo + b1 * r_lo + c1 < 0:
            r_lo += 1
        while r_lo > 0 and a1 * (r_lo - 1) * (r_lo - 1) + b1 * (r_lo - 1) + c1 >= 0:
            r_lo -= 1
        if r_lo < 0:
            r_lo = 0
    return r_lo, r_upper


@njit(cache=True)
def sum_progression(p, q, r0, r1):
    """Sum of (Q(p,q,r)/2 + 3p + 2q + r) over r = r0, r0+2, ..., <= r1,
    modulo MOD.  Q/2 = (3 r^2 + (2p+4q-2) r + C0)/2 with the whole expression
    an integer, so we compute it via modular inverse of 2."""
    if r0 > r1:
        return 0
    cnt = (r1 - r0) // 2 + 1
    # terms in r: f(r) = (Q + 2*(3p+2q+r))/2
    #   Q = 3 r^2 + B r + C,  B = 2p+4q-2, C = 3p^2+4pq-6p+4q^2-4q
    #   f = (3 r^2 + (B+2) r + (C + 6p + 4q)) / 2
    bb = (2 * p + 4 * q - 2 + 2) % MOD
    cc = (3 * p * p + 4 * p * q - 6 * p + 4 * q * q - 4 * q + 6 * p + 4 * q) % MOD
    # sum over arithmetic seq r = r0 + 2k, k=0..cnt-1
    # need S0 = cnt, S1 = sum r, S2 = sum r^2  (mod MOD)
    r0m = r0 % MOD
    cntm = cnt % MOD
    # sum r = cnt*r0 + 2 * (cnt*(cnt-1)/2) = cnt*r0 + cnt*(cnt-1)
    s1 = (cntm * r0m + cntm * ((cnt - 1) % MOD)) % MOD
    # sum r^2 = sum (r0 + 2k)^2 = cnt r0^2 + 4 r0 sum k + 4 sum k^2
    sk = ((cnt - 1) % MOD) * (cnt % MOD) % MOD * INV2 % MOD  # sum_{0}^{cnt-1} k
    sk2 = (
        ((cnt - 1) % MOD)
        * (cnt % MOD)
        % MOD
        * ((2 * (cnt - 1) + 1) % MOD)
        % MOD
        * INV6
        % MOD
    )
    s2 = (cntm * (r0m * r0m % MOD) + 4 * r0m % MOD * sk + 4 * sk2) % MOD
    total = (3 * s2 + bb * s1 + cc * cntm) % MOD * INV2 % MOD
    return total


@njit(parallel=True, cache=True)
def solve(n):
    pmax = isqrt_nb(8 * n // 3) + 2
    qmax = isqrt_nb(8 * n // 4) + 2
    # One slot per p: each prange iteration writes only acc[p], so no two
    # threads ever touch the same element and there is no data race.
    acc = np.zeros(pmax + 1, dtype=np.int64)
    for p in prange(0, pmax + 1):  # ty: ignore[not-iterable]
        local = 0
        for q in range(0, qmax + 1):
            r_lo, r_hi = feasible_r_max(p, q, n)
            if r_lo > r_hi:
                continue
            lo = r_lo
            hi = r_hi
            if (lo % 2) != (p % 2):
                lo += 1
            if (hi % 2) != (p % 2):
                hi -= 1
            if lo <= hi:
                local = (local + sum_progression(p, q, lo, hi)) % MOD
        acc[p] = local
    tot = 0
    for i in range(pmax + 1):
        tot = (tot + acc[i]) % MOD
    return tot


def main():
    assert solve(5) == 48
    assert solve(30) == 5630
    assert solve(1000) == 37048340 % MOD
    return solve(10**8)


if __name__ == "__main__":
    print(main())  # 404890862
