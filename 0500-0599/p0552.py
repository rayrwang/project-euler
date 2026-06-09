"""
https://projecteuler.net/problem=552

A_n is the smallest positive integer with A_n mod p_i = i for all
1 <= i <= n (p_i the i-th prime). S(n) sums the primes up to n that
divide at least one A_k. Find S(300000).

Incremental CRT: with M_n = p_1 ... p_n, the solution grows as
A_n = A_(n-1) + t M_(n-1) where t = (n - A_(n-1)) / M_(n-1) mod p_n,
0 <= t < p_n; inductively 1 <= A_n <= M_n, so this is the minimal
positive solution.

The crucial observation: once p_j enters the system (n >= j),
A_n = j (mod p_j) with 0 < j < p_j, so p_j never divides any later
A_n. Hence each prime q = p_j <= 300000 only needs A_n mod q for
n < j. We track a[j] = A_n mod p_j and m[j] = M_n mod p_j for every
prime index j > n, updating both in O(1) per pair: a step costs
O(K - n) with K = pi(300000) = 25997, about K^2 / 2 = 3.4 * 10^8
operations in total. Whenever a[j] hits 0, prime p_j divides that A_n
and is marked.

The recurrence is cross-checked against exact big-integer CRT for the
given A_2 = 5, A_3 = 23, A_4 = 53, A_5 = 1523 and
A_10 = 5765999453, and S(50) = 69 is asserted.
"""

import sys
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402


@numba.njit(cache=True)
def _solve(primes: np.ndarray) -> np.ndarray:
    """For each prime p_j (0-based j), mark whether p_j divides some
    A_n with n < j + 1."""
    k = len(primes)
    a = np.ones(k, dtype=np.int64)  # A_1 = 1 mod p_j
    m = np.empty(k, dtype=np.int64)  # M_1 = 2 mod p_j
    for j in range(k):
        m[j] = 2 % primes[j]
    marked = np.zeros(k, dtype=np.bool_)
    for n in range(2, k + 1):
        p = primes[n - 1]
        # t = (n - A_(n-1)) * M_(n-1)^(-1) mod p, via Fermat inverse
        diff = (n - a[n - 1]) % p
        inv = 1
        base = m[n - 1] % p
        e = p - 2
        while e:
            if e & 1:
                inv = inv * base % p
            base = base * base % p
            e >>= 1
        t = diff * inv % p
        # update residues for all primes not yet in the system
        for j in range(n, k):
            q = primes[j]
            a[j] = (a[j] + t * m[j]) % q
            if a[j] == 0:
                marked[j] = True
            m[j] = m[j] * p % q
    return marked


def s_of(n: int) -> int:
    primes = prime_sieve_int(n)
    marked = _solve(primes)
    return int(primes[marked].sum())


def a_exact(n: int, primes: np.ndarray) -> int:
    """A_n by exact big-integer incremental CRT."""
    a, m = 1, 2
    for i in range(2, n + 1):
        p = int(primes[i - 1])
        t = (i - a) * pow(m, -1, p) % p
        a += t * m
        m *= p
    return a


if __name__ == "__main__":
    ps = prime_sieve_int(100)
    assert [a_exact(i, ps) for i in (2, 3, 4, 5)] == [5, 23, 53, 1523]
    assert a_exact(10, ps) == 5765999453
    assert s_of(50) == 69  # 5 | A_2, 23 | A_3, 41 | A_10

    print(s_of(300000))  # 326227335
