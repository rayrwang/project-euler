"""Project Euler 931: Totient Graph.

Edges go from b to a = pb with weight phi(pb) - phi(b), which equals
(p-1)phi(b) when p | b and (p-2)phi(b) otherwise.  Fixing the prime
p with p^e || n, the b with pb | n are b = p^j m, m | n/p^e, and

  sum_j [weight factor] = (p-2) + (p-1) sum_{j=1}^{e-1} phi(p^j) * (p-1)
                        = (p-1)p^(e-1) - 1 = phi(p^e) - 1,

while sum_{m | k} phi(m) = k turns the m-sum into n/p^e.  Hence

    t(n) = sum_{p^e || n} (phi(p^e) - 1) * n / p^e

(t(45) = 5*5 + 3*9 = 52 as given).  Summing over n <= N with q = p^e
and m coprime to p, q m <= N:

    T(N) = sum_q (phi(q) - 1) * (S(N/q) - p * S(N/(qp))),

S(x) = x(x+1)/2.  The e >= 2 prime powers and the p*S(N/p^2) correction
involve only p <= sqrt(N); the bulk sum_{p <= N} (p-2) S(N/p) is grouped
by the value w = N/p, using prime counts and prime sums at all division
points N/d from a Lucy_Hedgehog sieve in O(N^(3/4)) (counts exact in
int64, sums modulo 715827883).

Verified: the t(n) identity against direct divisor-graph computation for
n < 300, the given T(10) = 26 and T(100) = 5282, and T(10^6) against a
smallest-prime-factor sieve brute force.
"""

import numpy as np
from numba import njit

M = 715827883


@njit(cache=True, inline="always")
def s_tri(x):
    return x % M * ((x + 1) % M) % M * ((M + 1) // 2) % M


@njit(cache=True)
def solve(n: int) -> int:
    r = int(np.sqrt(n))
    while (r + 1) * (r + 1) <= n:
        r += 1
    while r * r > n:
        r -= 1
    small_c = np.zeros(r + 1, dtype=np.int64)
    large_c = np.zeros(r + 1, dtype=np.int64)
    small_s = np.zeros(r + 1, dtype=np.int64)
    large_s = np.zeros(r + 1, dtype=np.int64)
    for v in range(1, r + 1):
        small_c[v] = v - 1
        small_s[v] = (s_tri(v) - 1) % M
    for d in range(1, r + 1):
        w = n // d
        large_c[d] = w - 1
        large_s[d] = (s_tri(w) - 1) % M
    for p in range(2, r + 1):
        if small_c[p] == small_c[p - 1]:
            continue
        pc = small_c[p - 1]
        ps = small_s[p - 1]
        p2 = p * p
        pm = p % M
        dmax = min(n // p2, r)
        for d in range(1, dmax + 1):
            wd = d * p
            if wd <= r:
                cc, ss = large_c[wd], large_s[wd]
            else:
                v = n // wd
                cc, ss = small_c[v], small_s[v]
            large_c[d] -= cc - pc
            large_s[d] = (large_s[d] - pm * ((ss - ps) % M)) % M
        for v in range(r, p2 - 1, -1):
            vv = v // p
            small_c[v] -= small_c[vv] - pc
            small_s[v] = (small_s[v] - pm * ((small_s[vv] - ps) % M)) % M

    total = 0
    # bulk: sum_{p <= n} (p - 2) S(n // p), grouped by w = n // p
    d = 1
    while d <= n:
        w = n // d
        d2 = n // w
        lo = n // (w + 1)
        if lo <= r:
            cs_lo, cc_lo = small_s[lo] if lo >= 1 else 0, \
                small_c[lo] if lo >= 1 else 0
        else:
            cs_lo, cc_lo = large_s[n // lo], large_c[n // lo]
        if d2 <= r:
            cs_hi, cc_hi = small_s[d2], small_c[d2]
        else:
            cs_hi, cc_hi = large_s[n // d2], large_c[n // d2]
        cs = (cs_hi - cs_lo) % M
        cc = (cc_hi - cc_lo) % M
        total = (total + s_tri(w) * ((cs - 2 * cc) % M)) % M
        d = d2 + 1

    # corrections: p^2 term of e = 1, and prime powers e >= 2 (p <= r)
    for p in range(2, r + 1):
        if small_c[p] == small_c[p - 1]:
            continue
        q = p * p
        total = (total - p % M * ((p - 2) % M) % M * s_tri(n // q)) % M
        phi = p - 1
        while q <= n:
            phi = phi * p  # phi(p^e) for q = p^e
            inner = (s_tri(n // q) - p % M * s_tri(n // q // p)) % M
            total = (total + (phi - 1) % M * inner) % M
            if q > n // p:
                break
            q *= p
    return total % M


def _brute(n_max: int) -> int:
    spf = np.zeros(n_max + 1, dtype=np.int64)
    for i in range(2, n_max + 1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i] == 0, i, spf[i::i])
    tot = 0
    for n in range(2, n_max + 1):
        x = n
        while x > 1:
            p = int(spf[x])
            pe = 1
            while x % p == 0:
                x //= p
                pe *= p
            tot += (pe - pe // p - 1) * (n // pe)
    return tot % M


if __name__ == "__main__":
    assert solve(10) == 26  # given
    assert solve(100) == 5282  # given
    assert solve(10**5) == _brute(10**5)
    assert solve(10**6) == _brute(10**6)
    print(solve(10**12))  # 128856311
