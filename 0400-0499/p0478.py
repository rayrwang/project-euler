"""Project Euler 478: Mixtures.

M(n) is the set of mixtures (a : b : c) with 0 <= a, b, c <= n and
gcd(a, b, c) = 1. E(n) counts subsets of M(n) that can produce the mixture
(1 : 1 : 1). Find E(10^7) mod 11^8.

A subset can produce (1 : 1 : 1) iff (1, 1, 1) lies in the conic hull of
its triples. Projecting along the kernel (1, 1, 1) via w = (a - b, b - c),
a subset is *bad* (cannot produce it) iff all its projected directions lie
in an open half-plane, i.e. span less than 180 degrees. Every nonempty bad
subset has a unique first direction theta, giving

    bad = 1 + sum_theta (2^(m_theta) - 1) * 2^(c_theta),

with m_theta the number of triples at direction theta and c_theta the mass
of the open arc (theta, theta + 180).

The direction circle has the dihedral D3 symmetry of permuting (a, b, c):
six cardinal directions (ties like a > b = c), each of mass
Phi = sum_(a<=n) phi(a), and six sectors (strict orderings like
a > b > c). A sector direction with primitive (p, q) = (a - b, b - c) has
mass depending only on s = p + q:

    m_s = sum_(k>=1) #{0 <= c <= n - k s : gcd(c, k) = 1}
        = sum_e mu(e) [T(Q + 1) - s T(T + 1)/2],  Q = floor(n/e),
          T = floor(Q/s),

a closed form costing O(n/s) per s, so O(n log n) overall. There are
phi(s) primitive pairs with p + q = s, hence the sector mass is
F = sum_s phi(s) m_s.

By the 120-degree rotation, c_theta = M'/3 + (mass of the open 60-degree
arc just after theta), where M' = 6 Phi + 6 F is the total mass. For a
cardinal, that arc is one full open sector, mass F. For an interior
direction d the arc is (rest of d's sector) + (next cardinal) + (head of
the next sector); the mirror symmetry (p, q) <-> (q, p) is mass-preserving
and order-reversing, so the head of the next sector weighs exactly the
mass *before* d in its own sector, and the arc collapses to
R(d) + Phi + L(d) = F + Phi - m_s -- a function of s alone. Therefore

    bad = 1 + 6 (2^Phi - 1) 2^(M'/3 + F)
            + 6 * 2^(M'/3 + F + Phi) * sum_s phi(s) (1 - 2^(-m_s)),
    E(n) = 2^(1 + 6 Phi + 6 F) - bad.

Exponents are reduced modulo ord(2 mod 11^8) = 10 * 11^7 (full order,
since 2^10 = 56 != 1 mod 121), and 2^(-m) = (2^(ord - 1))^m. The exact
m_s fit in int64; F (~2 * 10^20) is accumulated mod the order. Asserted
against the four values in the statement and four more verified values.
"""

import numpy as np
from numba import njit

MOD = 11**8  # 214358881
ORD2 = 10 * 11**7  # multiplicative order of 2 mod 11^8


@njit(cache=True)
def sieves(n):
    phi = np.arange(n + 1, dtype=np.int64)
    mu = np.ones(n + 1, np.int8)
    isc = np.zeros(n + 1, np.bool_)
    primes = np.zeros(n // 2 + 10, np.int64)
    np_ = 0
    for i in range(2, n + 1):
        if not isc[i]:
            primes[np_] = i
            np_ += 1
            phi[i] = i - 1
            mu[i] = -1
        for j in range(np_):
            p = primes[j]
            if i * p > n:
                break
            isc[i * p] = True
            if i % p == 0:
                phi[i * p] = phi[i] * p
                mu[i * p] = 0
                break
            else:
                phi[i * p] = phi[i] * (p - 1)
                mu[i * p] = -mu[i]
    return phi, mu


@njit(cache=True)
def powmod(b, e, m):
    r = 1
    b %= m
    while e:
        if e & 1:
            r = r * b % m
        b = b * b % m
        e >>= 1
    return r


@njit(cache=True)
def solve(n):
    phi, mu = sieves(n)
    inv2 = powmod(2, ORD2 - 1, MOD)  # 2^(-1) since 2^ORD2 = 1 mod 11^8
    big_phi = np.int64(0)
    for a in range(1, n + 1):
        big_phi += phi[a]
    phi_e = big_phi % ORD2
    f_e = np.int64(0)  # F mod ORD2 (exponent use only)
    s_sum = np.int64(0)  # sum_s phi(s) (1 - 2^{-m_s}) mod MOD
    for s in range(2, n + 1):
        ms = np.int64(0)
        emax = n // s
        for e in range(1, emax + 1):
            if mu[e] == 0:
                continue
            q = n // e
            t = q // s
            term = t * (q + 1) - s * (t * (t + 1) // 2)
            if mu[e] == 1:
                ms += term
            else:
                ms -= term
        ms_e = ms % ORD2
        f_e = (f_e + phi[s] % ORD2 * ms_e) % ORD2
        s_sum = (s_sum + phi[s] % MOD * ((1 - powmod(inv2, ms_e, MOD)) % MOD)) % MOD
    m_exp = (1 + 6 * phi_e + 6 * f_e) % ORD2
    third = (2 * phi_e + 2 * f_e) % ORD2  # M'/3 = 2 Phi + 2 F
    bad_card = (
        6 * ((powmod(2, phi_e, MOD) - 1) % MOD) % MOD
        * powmod(2, (third + f_e) % ORD2, MOD) % MOD
    )
    bad_int = 6 * powmod(2, (third + f_e + phi_e) % ORD2, MOD) % MOD * s_sum % MOD
    bad = (1 + bad_card + bad_int) % MOD
    return (powmod(2, m_exp, MOD) - bad) % MOD


if __name__ == "__main__":
    assert solve(1) == 103
    assert solve(2) == 520447
    assert solve(10) == 82608406
    assert solve(100) == 158225402
    assert solve(500) == 13801403
    assert solve(1000) == 112631757
    assert solve(10**4) == 131433978
    assert solve(10**5) == 157068696
    assert solve(10**6) == 88238357
    print(solve(10**7))  # 59510340
