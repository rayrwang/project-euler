"""Project Euler 484: Arithmetic Derivative.

The arithmetic derivative has p' = 1 and (ab)' = a'b + ab'; find
sum of gcd(k, k') for 1 < k <= N = 5 * 10^15.

For n = prod p^a, n' = n * sum a/p, and the p-adic valuation of n' is a - 1
when p does not divide a and at least a when p | a. Hence
    g(n) = gcd(n, n') = prod_p p^(a - [p does not divide a])
is multiplicative with g(p) = 1. Writing g = 1 * h (Dirichlet convolution),
h is multiplicative with h(p) = 0 and h(p^a) = g(p^a) - g(p^(a-1)) >= 0, so h
is supported on powerful numbers, of which there are only ~2.17 sqrt(N).
Then sum_{2 <= k <= N} g(k) = -1 + sum_{d powerful} h(d) * floor(N / d),
evaluated by a depth-first search over primes up to sqrt(N) that builds every
powerful number once (skipping subtrees whose h-factor vanishes). The total
~8.9e18 fits (barely) in a signed 64-bit integer.
"""

import math

import numpy as np
from numba import njit

N = 5 * 10**15


def sieve_primes(limit):
    flags = np.ones(limit + 1, dtype=np.bool_)
    flags[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if flags[p]:
            flags[p * p :: p] = False
    return np.flatnonzero(flags).astype(np.int64)


@njit(cache=True)
def g_pp(p, a):
    """g(p^a) = p^a if p | a else p^(a-1)."""
    e = a if a % p == 0 else a - 1
    r = 1
    for _ in range(e):
        r *= p
    return r


@njit(cache=True)
def dfs(i, val, h, n, primes):
    total = h * (n // val)
    for j in range(i, len(primes)):
        p = primes[j]
        if val > n // (p * p):
            break
        v = val * p * p
        e = 2
        while True:
            he = g_pp(p, e) - g_pp(p, e - 1)
            if he > 0:
                total += dfs(j + 1, v, h * he, n, primes)
            if v > n // p:
                break
            v *= p
            e += 1
    return total


def gcd_deriv_sum(n, primes):
    """sum of gcd(k, k') for 1 < k <= n."""
    return dfs(0, 1, 1, n, primes) - 1


def brute(n):
    total = 0
    for k in range(2, n + 1):
        rem, deriv = k, 0
        for p in range(2, k + 1):
            if p * p > rem:
                break
            while rem % p == 0:
                deriv += k // p
                rem //= p
        if rem > 1:
            deriv += k // rem
        total += math.gcd(k, deriv)
    return total


if __name__ == "__main__":
    primes = sieve_primes(math.isqrt(N))
    assert gcd_deriv_sum(10**4, primes) == brute(10**4)
    print(gcd_deriv_sum(N, primes))  # 8907904768686152599
