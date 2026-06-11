"""Project Euler 474: Last Digits of Divisors.

F(n, d) counts divisors of n whose last digits equal d; find F(10^6!, 65432)
modulo P = 10^16 + 61.

Since 65432 = 24 (mod 32), a divisor D = 65432 (mod 10^5) has 2-adic
valuation exactly 3 and is coprime to 5. Writing D = 8m with m coprime to 10,
the condition becomes m = 65432 / 8 = 8179 (mod 12500), where m ranges over
the divisors of 10^6! built from primes other than 2 and 5 (the factor 2^3 is
always available). So we count divisors in a fixed class of the unit group
U(12500), which has 5000 elements.

DP over the group algebra: c[g] = number of partial divisors in class g, and
each prime p with exponent e contributes a geometric series
1 + delta_p + ... + delta_p^e. Multiplication by p^-1 permutes the classes in
cycles (the cosets of <p>), so the convolution is a sliding-window sum of
length (e+1) mod ord(p) around each cycle plus floor((e+1)/ord) copies of the
full cycle sum - O(|U|) per prime, about 5000 * 78498 operations total. The
single coefficient-times-value product per cycle is done with a chunked
mulmod since P^2 overflows 64 bits.

A direct residue-ring DP modulo 10^k verifies the given F(12!, 12) = 11 and
F(50!, 123) = 17888, and cross-checks the group method at F(50!, 65432).
"""

import numpy as np
from numba import njit

P = 10**16 + 61
MOD = 12500  # 10^5 / 2^3
TARGET = 8179  # 65432 / 8


def primes_upto(n):
    flags = np.ones(n + 1, dtype=bool)
    flags[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if flags[i]:
            flags[i * i :: i] = False
    return np.flatnonzero(flags).astype(np.int64)


def legendre(n, p):
    e, q = 0, p
    while q <= n:
        e += n // q
        q *= p
    return e


def count_slow(n, d, k):
    """Reference: full residue-ring DP modulo 10^k over the primes of n!."""
    mod = 10**k
    c = np.zeros(mod, dtype=np.int64)
    c[1 % mod] = 1
    idx_base = np.arange(mod, dtype=np.int64)
    for p in primes_upto(n):
        new = np.zeros(mod, dtype=np.int64)
        pa = 1
        for _ in range(legendre(n, int(p)) + 1):
            np.add.at(new, idx_base * pa % mod, c)
            pa = pa * int(p) % mod
        c = new % P
    return int(c[d % mod])


@njit(cache=True)
def mulmod_small(a, b, p):
    """a * b mod p for a < 2^27, b < p < 2^54, without 64-bit overflow."""
    r = 0
    shift = 18
    while shift >= 0:
        r = ((r << 9) + ((a >> shift) & 511) * b) % p
        shift -= 9
    return r


@njit(cache=True)
def count_units(n, primes, units, pos, target):
    nu = len(units)
    c = np.zeros(nu, np.int64)
    c[pos[1]] = 1
    t = np.zeros(nu, np.int64)
    shift = np.empty(nu, np.int64)
    seq = np.empty(nu, np.int64)
    done = np.empty(nu, np.uint8)
    for pi in range(len(primes)):
        p = primes[pi]
        if p == 2 or p == 5:
            continue
        e = 0
        q = p
        while q <= n:
            e += n // q
            q *= p
        # inverse of p in U(12500) via p^(phi - 1), phi(12500) = 5000
        inv = 1
        base = p % MOD
        exp = 4999
        while exp:
            if exp & 1:
                inv = inv * base % MOD
            base = base * base % MOD
            exp >>= 1
        for g in range(nu):
            shift[g] = pos[units[g] * inv % MOD]
        if e == 1:
            for g in range(nu):
                t[g] = (c[g] + c[shift[g]]) % P
        else:
            done[:] = 0
            for g0 in range(nu):
                if done[g0]:
                    continue
                ln = 0
                g = g0
                while True:
                    seq[ln] = g
                    done[g] = 1
                    ln += 1
                    g = shift[g]
                    if g == g0:
                        break
                cyc = 0
                for i in range(ln):
                    cyc = (cyc + c[seq[i]]) % P
                rem = (e + 1) % ln
                base_val = mulmod_small((e + 1) // ln, cyc, P)
                w = 0
                for j in range(rem):
                    w = (w + c[seq[j]]) % P
                for i in range(ln):
                    t[seq[i]] = (base_val + w) % P
                    w = (w - c[seq[i]] + c[seq[(i + rem) % ln]]) % P
        c, t = t, c
    return c[pos[target]] % P


def count_fast(n):
    units = np.array([r for r in range(MOD) if r % 2 and r % 5], dtype=np.int64)
    pos = np.full(MOD, -1, dtype=np.int64)
    for i, u in enumerate(units):
        pos[u] = i
    return int(count_units(n, primes_upto(n), units, pos, TARGET))


if __name__ == "__main__":
    assert count_slow(12, 12, 2) == 11
    assert count_slow(50, 123, 3) == 17888
    assert count_fast(50) == count_slow(50, 65432, 5)
    print(count_fast(10**6))  # 9690646731515010
