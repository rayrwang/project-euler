"""Project Euler Problem 618: Numbers with a Given Prime Factor Sum.

Every n >= 2 is, uniquely, a multiset of primes, so S(k) is an unbounded
knapsack sum: process the primes p <= 46368 one at a time and let

    f[k] <- f[k] + p * f[k - p]   (for k = p .. K, in increasing k),

starting from f[0] = 1 (the empty product).  Updating k in increasing order
lets each prime be reused, and processing primes one at a time counts each
multiset exactly once, so afterwards f[k] is the sum over all prime
multisets with element sum k of the product of the multiset, i.e. S(k).
Only the last nine digits are needed, so everything is kept modulo 10^9
(intermediate p * f values stay below 4.7 * 10^13, safely inside int64),
and the answer is the sum of S(F_k) for k = 2..24 with F_24 = 46368.
"""

import numba
import numpy as np

MOD = 10**9


def sieve_primes(n: int) -> np.ndarray:
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = False
    return np.flatnonzero(is_p)


@numba.jit(cache=True)
def knapsack(primes: np.ndarray, top: int) -> np.ndarray:
    f = np.zeros(top + 1, dtype=np.int64)
    f[0] = 1
    for p in primes:
        for k in range(p, top + 1):
            f[k] = (f[k] + p * f[k - p]) % MOD
    return f


def solve() -> int:
    fibs = [1, 1]
    while len(fibs) < 24:
        fibs.append(fibs[-1] + fibs[-2])
    top = fibs[-1]

    f = knapsack(sieve_primes(top), top)

    assert f[1] == 0 and f[2] == 2 and f[3] == 3
    assert f[5] == 11 and f[8] == 49
    return int(sum(f[k] for k in fibs[1:]) % MOD)


if __name__ == "__main__":
    print(solve())  # 634212216
