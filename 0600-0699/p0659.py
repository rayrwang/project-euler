"""Project Euler Problem 659: Largest Prime.

If a prime p divides both n^2 + k^2 and (n+1)^2 + k^2 it divides their
difference 2n + 1, and then 4(n^2 + k^2) = (2n+1)^2 - 2(2n+1) + 1 + 4k^2
== 4k^2 + 1 (mod p).  Conversely for any odd p | 4k^2 + 1, choosing n with
2n + 1 == 0 (mod p) makes p divide both successive terms.  Hence P(k) is
simply the largest prime factor of 4k^2 + 1.  (Sanity check: the problem's
n^2 + 3 example has 4*3 + 1 = 13, matching its stated largest prime 13.)

Factor all 10^7 values f(k) = 4k^2 + 1 together with a quadratic polynomial
sieve: for each prime p == 1 (mod 4) up to B = 2*10^7 + 1 the roots of
(2k)^2 == -1 (mod p) come from a Tonelli-Shanks square root of -1, walked
as two index progressions with full power extraction.  Since B^2 exceeds
max f, whatever remains after sieving is 1 or a single prime - the
largest.  Sum modulo 10^18 (terms fit comfortably in int64 alongside the
running remainder).

Check: brute-force largest prime factors of 4k^2 + 1 for k <= 2000.
"""

import numba
import numpy as np


def sieve_primes(n: int) -> np.ndarray:
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = False
    return np.flatnonzero(is_p).astype(np.int64)


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
def sqrt_minus_one(p: int) -> int:
    """A square root of -1 modulo p == 1 (mod 4), via Euler's criterion."""
    z = 2
    while True:
        s = mod_pow(z, (p - 1) // 4, p)
        if s * s % p == p - 1:
            return s
        z += 1


@numba.jit(cache=True)
def sum_largest_primes(K: int, primes: np.ndarray) -> int:
    MOD = 10**18
    residual = np.empty(K + 1, dtype=np.int64)
    largest = np.ones(K + 1, dtype=np.int64)
    for k in range(K + 1):
        residual[k] = 4 * k * k + 1
    for p in primes:
        if p % 4 != 1:
            continue
        s = sqrt_minus_one(p)  # (2k)^2 == -1: 2k == +-s (mod p)
        inv2 = (p + 1) // 2
        for sign in range(2):
            root = s if sign == 0 else p - s
            k0 = root * inv2 % p
            for k in range(k0, K + 1, p):
                if residual[k] % p == 0:
                    while residual[k] % p == 0:
                        residual[k] //= p
                    largest[k] = p  # primes processed in increasing order
    total = 0
    for k in range(1, K + 1):
        lp = residual[k] if residual[k] > 1 else largest[k]
        total = (total + lp) % MOD
    return total


def brute_largest(k: int) -> int:
    n, lp, d = 4 * k * k + 1, 1, 3
    while d * d <= n:
        while n % d == 0:
            n //= d
            lp = d
        d += 2
    return n if n > 1 else lp


if __name__ == "__main__":
    K = 10**7
    primes = sieve_primes(2 * K + 1)
    small = sum_largest_primes(2000, primes)
    assert small == sum(brute_largest(k) for k in range(1, 2001)), small
    print(sum_largest_primes(K, primes))  # 238518915714422000
