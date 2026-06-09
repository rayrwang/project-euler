"""Project Euler Problem 668: Square Root Smooth Numbers.

A number is square-root smooth if all its prime factors are strictly less than its
square root.  Count them up to N = 10^10 (1 counts).

A number n is NOT square-root smooth iff it has a prime factor p >= sqrt(n).  Such a
p is unique (two primes >= sqrt(n) would multiply to > n) and equals the largest
prime factor, with n = p*m where m = n/p <= sqrt(n) <= p.  Conversely every pair
(p prime, 1 <= m <= p, p*m <= N) gives a distinct non-smooth number, so

    #not-smooth = sum_{p <= N} min(p, floor(N/p)),
    S(N) = N - sum_{p <= N} min(p, floor(N/p)).

Split at R = floor(sqrt N):  primes p <= R contribute p (sum of primes <= R), and
primes p > R contribute floor(N/p), grouped as sum_{q=1}^{R-1} q*(pi(N//q) -
pi(N//(q+1))) using a Lucy_Hedgehog prime count.  Check: S(100) = 29.
"""

import numpy as np
import numba

from funcs import prime_sieve_int


@numba.jit(cache=True)
def _isqrt(n: int) -> int:
    x = int(n**0.5)
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@numba.jit(cache=True)
def _lucy_large(N: int):
    r = _isqrt(N)
    small = np.empty(r + 1, dtype=np.int64)
    large = np.empty(r + 1, dtype=np.int64)
    for v in range(1, r + 1):
        small[v] = v - 1
    for i in range(1, r + 1):
        large[i] = N // i - 1
    for p in range(2, r + 1):
        if small[p] == small[p - 1]:
            continue
        sp = small[p - 1]
        p2 = p * p
        i = 1
        while i <= r and N // i >= p2:
            ip = i * p
            if ip <= r:
                sub = large[ip]
            else:
                sub = small[N // ip]
            large[i] -= sub - sp
            i += 1
        v = r
        while v >= p2:
            small[v] -= small[v // p] - sp
            v -= 1
    return large, r


@numba.jit(cache=True)
def _tail(N: int, large: np.ndarray, r: int) -> int:
    # sum_{R < p <= N} floor(N/p) = sum_{q=1}^{r-1} q*(pi(N//q) - pi(N//(q+1)))
    total = 0
    for q in range(1, r):
        total += q * (large[q] - large[q + 1])
    return total


def S(N: int) -> int:
    large, r = _lucy_large(N)
    primes = prime_sieve_int(r + 1)
    sum_primes_le_r = int(primes.sum())
    nonsmooth = sum_primes_le_r + int(_tail(N, large, r))
    return N - nonsmooth


if __name__ == "__main__":
    assert S(100) == 29, S(100)
    print(S(10**10))  # 2811077773
