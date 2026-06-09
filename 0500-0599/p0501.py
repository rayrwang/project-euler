import math

import numba
import numpy as np

from funcs import prime_sieve_int

@numba.jit(cache=True)
def lucy_prime_count(n: int):
    """Lucy_Hedgehog prime counting.

    Returns arrays (small, large) and r = isqrt(n) such that
        pi(v)      = small[v]          for 1 <= v <= r,
        pi(n // i) = large[i]          for 1 <= i <= r.
    Runs in O(n**(3/4)).
    """
    r = int(n**0.5)
    while (r + 1) * (r + 1) <= n:
        r += 1
    while r * r > n:
        r -= 1
    small = np.empty(r + 1, dtype=np.int64)
    for v in range(r + 1):
        small[v] = v - 1  # count of {2, ..., v}
    large = np.empty(r + 1, dtype=np.int64)
    for i in range(1, r + 1):
        large[i] = n // i - 1
    for p in range(2, r + 1):
        if small[p] == small[p - 1]:
            continue  # p is composite
        sp = small[p - 1]  # pi(p - 1)
        p2 = p * p
        imax = min(r, n // p2)
        for i in range(1, imax + 1):
            d = i * p
            if d <= r:
                large[i] -= large[d] - sp
            else:
                large[i] -= small[n // d] - sp
        for v in range(r, p2 - 1, -1):
            small[v] -= small[v // p] - sp
    return small, large, r

@numba.jit(cache=True)
def pi_n_over_m(m: int, small, large, r: int, n: int) -> int:
    """pi(n // m) via the Lucy tables."""
    if m <= r:
        return large[m]
    return small[n // m]

@numba.jit(cache=True)
def count_eight_divisors(n: int, primes, small, large, r: int) -> int:
    total = 0

    # Form p^7.
    for p in primes:
        if p**7 <= n:
            total += 1
        else:
            break

    # Form p^3 * q with q prime, q != p.
    for p in primes:
        p3 = p**3
        if p3 > n:
            break
        total += pi_n_over_m(p3, small, large, r, n)
        if p**4 <= n:  # q == p would land in range; remove it
            total -= 1

    # Form p * q * r with p < q < r (squarefree, three distinct primes).
    for ip in range(len(primes)):
        p = int(primes[ip])
        if p * p * p >= n:  # need q, r > p, so p^3 < n
            break
        for iq in range(ip + 1, len(primes)):
            q = int(primes[iq])
            if p * q * q >= n:  # no room for r > q
                break
            # r ranges over primes in (q, n // (p*q)].
            total += pi_n_over_m(p * q, small, large, r, n) - small[q]

    return total

def f(n: int) -> int:
    r = int(math.isqrt(n))
    primes = prime_sieve_int(r + 1)
    small, large, r = lucy_prime_count(n)
    return count_eight_divisors(n, primes, small, large, r)

if __name__ == "__main__":
    assert f(100) == 10
    assert f(1000) == 180
    assert f(10**6) == 224427
    print(f(10**12))  # 197912312715
