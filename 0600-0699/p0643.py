"""Project Euler Problem 643: 2-Friendly.

gcd(p, q) = 2^t with t > 0 means p = 2^t p', q = 2^t q' with gcd(p', q') = 1,
so summing over t and writing Phi(m) = sum_{k <= m} phi(k),

    f(n) = sum_{t >= 1} #{ p' < q' <= floor(n / 2^t) : gcd(p', q') = 1 }
         = sum_{t >= 1} ( Phi(floor(n / 2^t)) - 1 ),

since the coprime pairs with q' >= 2 number sum_{q'=2}^m phi(q') = Phi(m)-1.

Phi is computed modulo 10^9 + 7 with the standard sublinear recursion

    Phi(n) = n (n + 1) / 2 - sum_{d=2}^{n} Phi(floor(n / d)),

grouping equal quotients, memoising, and reading values below 2 * 10^7 from
a sieved prefix table.  All arguments ever needed are quotients of 10^11,
so the cache is shared across the powers of two.

Checks: f(10^2) = 1031 and f(10^6) = 321418433 mod 10^9 + 7.
"""

import sys
from functools import cache

import numpy as np

MOD = 10**9 + 7
SIEVE_LIMIT = 2 * 10**7
INV2 = pow(2, MOD - 2, MOD)


def phi_prefix_sums(limit: int) -> np.ndarray:
    phi = np.arange(limit + 1, dtype=np.int64)
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            phi[i::i] -= phi[i::i] // i
    return np.cumsum(phi) % MOD


PHI_SMALL = phi_prefix_sums(SIEVE_LIMIT)


@cache
def Phi(n: int) -> int:
    """sum of phi(k) for k <= n, modulo MOD."""
    if n <= SIEVE_LIMIT:
        return int(PHI_SMALL[n])
    total = n % MOD * ((n + 1) % MOD) % MOD * INV2 % MOD
    d = 2
    while d <= n:
        q = n // d
        d_hi = n // q  # largest d with the same quotient
        total -= (d_hi - d + 1) % MOD * Phi(q) % MOD
        d = d_hi + 1
    return total % MOD


def f(n: int) -> int:
    total = 0
    t = 1
    while 2**t <= n:
        total += Phi(n // 2**t) - 1
        t += 1
    return total % MOD


if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    assert f(10**2) == 1031, f(10**2)
    assert f(10**6) == 321418433, f(10**6)
    print(f(10**11))  # 968274154
