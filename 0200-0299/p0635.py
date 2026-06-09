"""Project Euler Problem 635: Subset Sums.

A_q(n) counts the n-element subsets of {1, ..., qn} with sum divisible by n.
By the roots-of-unity filter, for a primitive d-th root w (d | n) the product
over one period collapses to (1 - (-z)^d)^{qn/d}, whose z^n coefficient is
binom(qn/d, n/d) up to sign, so

    A_q(n) = (1/n) sum_{d | n} phi(d) (-1)^{(n/d) (d + 1)} binom(qn/d, n/d).

For an odd prime p this is just (binom(qp, p) + (p - 1) q) / p, and for
p = 2 it is (binom(2q, 2) - q) / 2.  Verified: A_2(5) = 52, A_3(5) = 603,
S_2(10) = 554.

The work is therefore binom(2p, p) and binom(3p, p) mod 10^9 + 9 for every
prime p <= 10^8: stream the factorial k! once for k up to 3 * 10^8,
recording its value whenever k equals p, 2p or 3p for a prime p (three
pointer walks over the sorted prime multiples), then assemble each binomial
with two Fermat inversions.
"""

import numba
import numpy as np

MOD = 10**9 + 9


def sieve_primes(n: int) -> np.ndarray:
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = False
    return np.flatnonzero(is_p).astype(np.int64)


@numba.jit(cache=True)
def factorials_at_multiples(primes: np.ndarray) -> tuple:
    """k! mod MOD at k = p, 2p, 3p for each prime p, by one streaming pass."""
    n = len(primes)
    f1 = np.zeros(n, dtype=np.int64)
    f2 = np.zeros(n, dtype=np.int64)
    f3 = np.zeros(n, dtype=np.int64)
    i1 = i2 = i3 = 0
    fact = 1
    for k in range(1, 3 * primes[-1] + 1):
        fact = fact * k % MOD
        if i1 < n and k == primes[i1]:
            f1[i1] = fact
            i1 += 1
        if i2 < n and k == 2 * primes[i2]:
            f2[i2] = fact
            i2 += 1
        if i3 < n and k == 3 * primes[i3]:
            f3[i3] = fact
            i3 += 1
    return f1, f2, f3


@numba.jit(cache=True)
def mod_pow(a: int, b: int, mod: int) -> int:
    r = 1
    a %= mod
    while b > 0:
        if b & 1:
            r = r * a % mod
        a = a * a % mod
        b >>= 1
    return r


@numba.jit(cache=True)
def total(primes: np.ndarray, f1: np.ndarray, f2: np.ndarray, f3: np.ndarray) -> int:
    s = (6 - 2) // 2 + (15 - 3) // 2  # p = 2 terms: A_2(2) + A_3(2)
    for i in range(1, len(primes)):  # odd primes
        p = primes[i]
        inv_fp = mod_pow(f1[i], MOD - 2, MOD)
        inv_f2p = mod_pow(f2[i], MOD - 2, MOD)
        c2 = f2[i] * inv_fp % MOD * inv_fp % MOD  # binom(2p, p)
        c3 = f3[i] * inv_fp % MOD * inv_f2p % MOD  # binom(3p, p)
        a2 = (c2 + (p - 1) % MOD * 2) % MOD
        a3 = (c3 + (p - 1) % MOD * 3) % MOD
        s = (s + (a2 + a3) * mod_pow(p, MOD - 2, MOD)) % MOD
    return s % MOD


def S2_plus_S3(limit: int) -> int:
    primes = sieve_primes(limit)
    f1, f2, f3 = factorials_at_multiples(primes)
    return int(total(primes, f1, f2, f3))


def A(q: int, n: int, brute: bool = False) -> int:
    """Direct small-case evaluation for the asserts."""
    from itertools import combinations
    from math import comb

    if brute:
        return sum(
            1 for c in combinations(range(1, q * n + 1), n) if sum(c) % n == 0
        )
    if n == 2:
        return (comb(2 * q, 2) - q) // 2
    return (comb(q * n, n) + (n - 1) * q) // n


if __name__ == "__main__":
    assert A(2, 5) == A(2, 5, brute=True) == 52
    assert A(3, 5) == A(3, 5, brute=True) == 603
    assert A(2, 2) == A(2, 2, brute=True) and A(3, 7) == A(3, 7, brute=True)
    assert sum(A(2, p) for p in (2, 3, 5, 7)) == 554  # S_2(10)
    # given: S_2(100) = 100433628 and S_3(100) = 855618282 modulo 10^9 + 9
    assert S2_plus_S3(100) == (100433628 + 855618282) % MOD
    print(S2_plus_S3(10**8))  # 689294705
