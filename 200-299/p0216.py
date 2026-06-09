import math

import numpy as np
from numba import njit


@njit(cache=True)
def _modpow(b: int, e: int, m: int) -> int:
    r = 1
    b %= m
    while e > 0:
        if e & 1:
            r = r * b % m
        b = b * b % m
        e >>= 1
    return r


@njit(cache=True)
def _tonelli(a: int, p: int) -> int:
    # One square root of a modulo odd prime p (a assumed a quadratic residue).
    a %= p
    if a == 0:
        return 0
    if p % 4 == 3:
        return _modpow(a, (p + 1) // 4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while _modpow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m = s
    c = _modpow(z, q, p)
    t = _modpow(a, q, p)
    r = _modpow(a, (q + 1) // 2, p)
    while True:
        if t == 1:
            return r
        i = 0
        t2 = t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
            if i == m:
                break
        b = _modpow(c, 1 << (m - i - 1), p)
        m = i
        c = b * b % p
        t = t * c % p
        r = r * b % p


@njit(cache=True)
def _count(n_max: int, primes: np.ndarray) -> int:
    # t(n) = 2n^2 - 1 is composite iff some prime p divides it, i.e.
    # n^2 = (p+1)/2 (mod p). This is solvable only when 2 is a QR mod p
    # (p = +-1 mod 8). Mark n = +-root (mod p); survivors are prime.
    is_prime = np.ones(n_max + 1, dtype=np.uint8)
    is_prime[0] = 0
    if n_max >= 1:
        is_prime[1] = 0
    for pi in range(len(primes)):
        p = primes[pi]
        if p == 2 or (p % 8 != 1 and p % 8 != 7):
            continue
        root = _tonelli((p + 1) // 2, p)
        for r0 in (root, p - root):
            n = r0 % p
            if n < 2:
                n += p * ((2 - n + p - 1) // p)
            while n <= n_max:
                if 2 * n * n - 1 != p:
                    is_prime[n] = 0
                n += p
    return int(is_prime[2 : n_max + 1].sum())


def solve(n_max: int = 50_000_000) -> int:
    limit = int(math.isqrt(2 * n_max * n_max - 1)) + 1
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = np.nonzero(sieve)[0].astype(np.int64)
    return _count(n_max, primes)


if __name__ == "__main__":
    print(solve())  # 5437849
