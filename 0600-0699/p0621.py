"""Project Euler Problem 621: Expressing an Integer as the Sum of Triangular Numbers.

n = T_a + T_b + T_c  <=>  8n + 3 = (2a+1)^2 + (2b+1)^2 + (2c+1)^2, so with
m = 8n + 3, G(n) counts ordered triples of positive odd squares summing to
m (every representation of m == 3 mod 8 as three squares is automatically
all-odd, and signs give G(n) = r_3(m) / 8).

Fix the first square: G(n) = sum over odd x with x^2 <= m - 2 of P(m - x^2),
where P(r) counts ordered pairs of positive odd y, z with y^2 + z^2 = r.
Each r == 2 mod 4 forces both coordinates odd and nonzero, so by Jacobi's
two-square theorem P(r) = r_2(r) / 4 = d_1(r) - d_3(r), the multiplicative
function with factor (e + 1) at p == 1 mod 4, factor [e even] at
p == 3 mod 4, and factor 1 at p = 2.  Check: G(9) = 7 by hand.

Factoring all 3.4 million values r(x) = m - x^2 at once is a quadratic
polynomial sieve: for each odd prime p <= sqrt(max r), solve x^2 == m
(mod p) (Tonelli-Shanks; skip non-residues), convert the two roots to
index progressions over the odd-x grid, and at each hit divide out the
full power of p.  Whatever remains after sieving is 1 or a single prime
> sqrt(max r) with exponent 1.

Checks: G(1000) = 78 and G(10^6) = 2106.
"""

from math import isqrt

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
def sqrt_mod(a: int, p: int) -> int:
    """Tonelli-Shanks square root of residue a modulo odd prime p."""
    if p % 4 == 3:
        return mod_pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while mod_pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, mod_pow(z, q, p), mod_pow(a, q, p), mod_pow(a, (q + 1) // 2, p)
    while t != 1:
        t2, i = t, 0
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = mod_pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


@numba.jit(cache=True)
def G_sieve(m: int, length: int, sieve_limit: int, primes: np.ndarray) -> int:
    residual = np.empty(length, dtype=np.int64)
    pairs = np.ones(length, dtype=np.int64)  # d_1 - d_3 accumulator
    for i in range(length):
        x = 2 * i + 1
        residual[i] = (m - x * x) // 2  # exponent of 2 is exactly 1
    for p in primes:
        if p == 2 or p > sieve_limit:
            continue
        mm = m % p
        if mm == 0:
            roots = (0, 0)
        else:
            if mod_pow(mm, (p - 1) // 2, p) != 1:
                continue  # m is not a QR: p never divides m - x^2
            s = sqrt_mod(mm, p)
            roots = (s, p - s)
        inv2 = (p + 1) // 2
        for j in range(2):
            if j == 1 and roots[1] == roots[0]:
                break
            s = roots[j]
            i0 = (s - 1) % p * inv2 % p  # x = 2i + 1 == s (mod p)
            for i in range(i0, length, p):
                e = 0
                while residual[i] % p == 0:
                    residual[i] //= p
                    e += 1
                if p % 4 == 1:
                    pairs[i] *= e + 1
                elif e % 2 == 1:
                    pairs[i] = 0
    total = 0
    for i in range(length):
        r = residual[i]
        if r > 1:  # a single leftover prime, exponent 1
            if r % 4 == 1:
                pairs[i] *= 2
            else:
                pairs[i] = 0
        total += pairs[i]
    return total


def G(n: int, primes: np.ndarray) -> int:
    m = 8 * n + 3
    length = (isqrt(m - 2) + 1) // 2  # x = 2i + 1 for i = 0 .. length-1
    return int(G_sieve(m, length, isqrt(m - 3), primes))


if __name__ == "__main__":
    target = 17526 * 10**9
    primes = sieve_primes(isqrt(8 * target + 3) + 1)
    assert G(9, primes) == 7
    assert G(1000, primes) == 78
    assert G(10**6, primes) == 2106
    print(G(target, primes))  # 11429712
