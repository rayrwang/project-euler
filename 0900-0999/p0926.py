"""Project Euler 926: Total Roundness.

The roundness of n in base b is v_b(n) = max{k : b^k | n}, so the total
roundness counts pairs (b, k) with b >= 2, k >= 1 and b^k | n:

    R(n) = sum_{k>=1} #{b >= 2 : b^k | n}
         = sum_{k>=1} ( prod_p (floor(e_p / k) + 1) - 1 ),

since the b with b^k | n correspond to choosing each prime exponent of b
at most floor(e_p / k), and b = 1 is excluded.  For n = N! the
exponents are Legendre's e_p = sum_i floor(N / p^i).  Sorting the
exponents in decreasing order, the k-th term is a product over the
prefix with e_p >= k, so the total work is sum_p e_p = sum over prime
powers q <= N of floor(N/q), about N log log N (~3 * 10^7 for N = 10^7).

Verified against direct base-by-base roundness counting for n = 20,
n = 10! = 3628800 (given R = 6 and 312) and random n.
"""

import numpy as np
from numba import njit

P = 10**9 + 7


@njit(cache=True)
def _exponents(n: int) -> np.ndarray:
    """Legendre exponents of all primes <= n in n!, sorted decreasing."""
    sieve = np.ones(n + 1, dtype=np.bool_)
    sieve[:2] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = False
        i += 1
    primes = np.flatnonzero(sieve)
    es = np.zeros(len(primes), dtype=np.int64)
    for idx in range(len(primes)):
        p = primes[idx]
        e = 0
        q = p
        while q <= n:
            e += n // q
            if q > n // p:
                break
            q *= p
        es[idx] = e
    return -np.sort(-es)


@njit(cache=True)
def _total(es: np.ndarray) -> int:
    tot = 0
    kmax = es[0]
    for k in range(1, kmax + 1):
        pr = 1
        for e in es:
            if e < k:
                break
            pr = pr * (e // k + 1) % P
        tot = (tot + pr - 1) % P
    return tot % P


def solve(n: int) -> int:
    return _total(_exponents(n))


def _brute_r(n: int) -> int:
    tot = 0
    for b in range(2, n + 1):
        x = n
        while x % b == 0:
            x //= b
            tot += 1
    return tot % P


if __name__ == "__main__":
    assert _brute_r(20) == 6  # given
    assert _brute_r(3628800) == 312  # given R(10!)
    assert solve(10) == 312
    import math
    for m in (6, 7, 8, 9):
        assert solve(m) == _brute_r(math.factorial(m)), m
    print(solve(10_000_000))  # 40410219
