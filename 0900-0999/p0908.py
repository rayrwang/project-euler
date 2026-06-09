"""Project Euler 908: Clock Sequence II.

A periodic sequence segments into blocks summing to 1, 2, 3, ... iff every
triangular number T(n) = n(n+1)/2 occurs among its prefix sums.  For a
period that is a composition of s into p parts with prefix sums
S(1) < ... < S(p) = s, the achievable prefix sums of the infinite sequence
are {k s + S(r) : k >= 0}, so the condition is exactly

    D(s) := {((T(n) - 1) mod s) + 1 : n >= 1}  is a subset of  {S(r)},

(representatives taken in [1, s]; T(n) mod s is periodic in n with period
dividing 2s, and s itself always lies in D(s) since T(2s) = s(2s + 1)).
This criterion was verified against direct simulation of the segmentation.

Counting.  Compositions of s into p parts are subsets of [1, s-1] of size
p - 1 (the prefix sums without the final s), so with d(s) = |D(s)| - 1 the
number of clock compositions of length p and sum s is
C(s - 1 - d(s), p - 1 - d(s)).  Distinct sequences correspond to primitive
compositions counted by minimal period; Moebius inversion of
g(p) = sum_s C(s - 1 - d(s), p - 1 - d(s)) over the divisor lattice gives

    C(N) = sum_{q <= N} g(q) * Mertens(N // q).

The map m(T(n)) is a bijection onto the distinct residues of T(n) mod s,
and that count is multiplicative: mod 2^k the triangular numbers cover all
residues, while mod an odd p^k they biject (via 8 T(n) + 1 = (2n + 1)^2)
with the squares, of which there are 1 + sum_{e = k, k-2, ...>= 1}
phi(p^e)/2.  Hence d(s) is sieved multiplicatively.  Density bounds (each
odd prime factor keeps at least p/(2(p+1)) >= 3/8 of residues) show
d(s) < 10^4 forces s below ~1.5 * 10^6; in fact only 47228 values of s
qualify, the largest 294525.  All verified against brute force for
C(3) = 3, C(4) = 7, C(10) = 561.
"""

import numba
import numpy as np

MOD = 1111211113  # prime


def sieve_counts(smax: int) -> np.ndarray:
    """count[s] = #distinct triangular residues mod s."""
    spf = np.zeros(smax + 1, dtype=np.int64)
    for i in range(2, smax + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    cnt = np.ones(smax + 1, dtype=np.int64)
    for s in range(2, smax + 1):
        p = int(spf[s])
        m, k = s, 0
        while m % p == 0:
            m //= p
            k += 1
        if p == 2:
            f = 1 << k
        else:
            f, e = 1, k
            while e >= 1:
                f += (p**e - p ** (e - 1)) // 2
                e -= 2
        cnt[s] = cnt[m] * f
    return cnt


@numba.njit(cache=True)
def accumulate_g(rel_s, rel_d, fact, inv_fact, n, mod):
    g = np.zeros(n + 1, dtype=np.int64)
    for idx in range(len(rel_s)):
        s = rel_s[idx]
        d = rel_d[idx]
        a = s - 1 - d
        for p in range(d + 1, n + 1):
            b = p - 1 - d
            if b > a:
                break
            g[p] = (g[p] + fact[a] * inv_fact[b] % mod * inv_fact[a - b]) % mod
    return g


def mertens(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int64)
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, n + 1):
        if is_p[i]:
            is_p[2 * i :: i] = False
            mu[i::i] *= -1
            mu[i * i :: i * i] = 0
    mu[0] = 0
    return np.cumsum(mu)


def solve(n: int) -> int:
    smax = max(200, 250 * n)
    cnt = sieve_counts(smax)
    rel = np.nonzero(cnt[1:] <= n)[0] + 1
    assert rel.max() < smax * 3 // 5, "raise smax"
    rel_d = (cnt[rel] - 1).astype(np.int64)

    fmax = int(rel.max())
    fact = np.ones(fmax + 1, dtype=np.int64)
    for i in range(1, fmax + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = np.ones(fmax + 1, dtype=np.int64)
    inv_fact[fmax] = pow(int(fact[fmax]), MOD - 2, MOD)
    for i in range(fmax, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    g = accumulate_g(rel.astype(np.int64), rel_d, fact, inv_fact, n, MOD)
    big_m = mertens(n)
    ans = 0
    for q in range(1, n + 1):
        ans = (ans + int(g[q]) * int(big_m[n // q])) % MOD
    return ans % MOD


if __name__ == "__main__":
    assert solve(3) == 3
    assert solve(4) == 7
    assert solve(10) == 561
    print(solve(10**4))  # 451822602
