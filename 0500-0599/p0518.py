"""Project Euler Problem 518: Prime Triples and Geometric Sequences.

S(n) = sum of a+b+c over prime triples a<b<c<n with a+1, b+1, c+1 in geometric
progression.  A positive-integer geometric progression with squarefree ratio is
exactly (k y^2, k x y, k x^2) for integers x > y >= 1 with gcd(x, y) = 1 and k >= 1
(then b^2 = a c automatically).  So set

    a = k y^2 - 1,   b = k x y - 1,   c = k x^2 - 1,

require all three prime and c < n = 10^8, and sum a + b + c.  Since y < x the
ordering a < b < c is automatic.  We sieve primes to n and iterate over x, then k
(pruning on c = k x^2 - 1 being prime), then coprime y < x.
"""

import numpy as np
import numba

from funcs import prime_sieve_bool


@numba.jit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.jit(cache=True)
def _S(n: int, sieve: np.ndarray) -> int:
    total = 0
    x = 2
    while x * x <= n:
        xx = x * x
        k = 1
        while k * xx <= n:
            c = k * xx - 1
            if sieve[c]:
                kx = k * x
                for y in range(1, x):
                    a = k * y * y - 1
                    if a >= 2 and sieve[a]:
                        b = kx * y - 1
                        if sieve[b] and _gcd(x, y) == 1:
                            total += a + b + c
            k += 1
        x += 1
    return total


def S(n: int) -> int:
    sieve = prime_sieve_bool(n)  # sieve[i] True iff i prime, indices 0..n-1
    return int(_S(n, sieve))


if __name__ == "__main__":
    assert S(100) == 1035, S(100)
    print(S(10**8))  # 100315739184392
