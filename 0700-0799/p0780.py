"""
Project Euler Problem 780: Toriangulations
https://projecteuler.net/problem=780

F(n) counts non-equivalent tilings, over all a x b tori (rectangles with
opposite sides identified), by exactly n unit equilateral triangles;
tilings are equivalent when one deforms into the other by continuously
sliding triangles.  G(N) sums F(n) for n <= N; given G(6) = 14,
G(100) = 8090 and G(10^5) = 645124048 (mod 10^9 + 7), find G(10^9)
modulo 10^9 + 7.

Strip structure.  Every tiling of the plane by unit equilateral
triangles consists of parallel strips of height sqrt(3)/2 -- rows of
alternating up/down triangles -- each free to slide along itself, and
the only tilings with strips in more than one direction are the three
strip systems of a perfect triangular lattice.  On a torus the strips
close along a primitive lattice vector w = (pa, qb), gcd(p, q) = 1,
whose length c = |w| must be a whole number of triangle bases, and m
parallel strips fill the torus: ab = c m sqrt(3)/2 and n = 2cm.
Continuous deformation is exactly strip sliding, so on a fixed torus
each system (direction, c, m) is one equivalence class -- and the torus
itself is pinned by the data, since p^2 a^2 and q^2 b^2 are the roots of
Y^2 - c^2 Y + 3 p^2 q^2 c^2 m^2 / 4 = 0, which has positive solutions
exactly when c^2 > 3 p^2 q^2 m^2 (equality is impossible as sqrt(3) is
irrational).  Reading the eight pictured 6-triangle tilings shows the
counting conventions: a x b and b x a count as different tori (the two
quadratic roots give the two orderings), and the windings (p, q) and
(-p, q) are inequivalent mirror tilings.

Counting systems.  Writing k = n/2, the axis-aligned windings (1,0) and
(0,1) give 2 tau(k) tilings (one torus per divisor pair c m = k and its
transpose).  Skew windings give, for each factorisation c m = k, four
tilings (mirror times root choice) per coprime ordered pair p, q >= 1
with pq <= L(c, m), the largest integer with 3 L^2 m^2 < c^2; counting
coprime ordered pairs with product j adds the factor 2^omega(j).

Merging.  When the torus carries a perfect triangular-lattice tiling,
its three strip systems slide into the common lattice configuration and
the three classes collapse into one, saving exactly 2; distinct lattice
tilings of one torus never share a strip direction, so savings add.
Lattice tilings correspond to rectangular sublattices of the triangular
lattice Z[w] together with an ordered orthogonal frame: a primitive
vector u (modulo the six units) with norm N, its primitive perpendicular
u(2w - 1)/gcd, and stretch factors s, t >= 1.  The frame index is
k0 = 2N, or 2N/3 when 3 | N, and primitive vectors of norm N modulo
units number 2^(number of primes = 1 mod 3 dividing N) when
N = 3^e * (product of primes = 1 mod 3), e <= 1, else zero.  Pairing N
and 3N gives one term 2 * 2^omega(M) per 3-free product M of primes
= 1 mod 3, with k0 = 2M, contributing tau-partial-sums Dtau(K/(2M)).

Totals.  G(N) = 2 Dtau(K) + 4 * sum over (c, m, j) with c m <= K and
sqrt(3) j m < c of 2^omega(j), minus 2 * 2 * sum over M of
2^omega(M) Dtau(floor(K / 2M)), all mod 10^9 + 7, where K = N/2.  The
double sum runs in O(K) after noting that for fixed m the inner pairs
number about K/(sqrt(3) m^2); the M-sum enumerates the ~2 * 10^7
qualifying smooth numbers by depth-first search over primes = 1 mod 3.
All three given values check out, and the total takes about twenty
seconds.
"""

import numpy as np
from numba import njit

MOD = 10**9 + 7
N = 10**9


@njit(cache=True)
def isqrt64(x):
    if x <= 0:
        return np.int64(0)
    r = np.int64(np.sqrt(np.float64(x)))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


@njit(cache=True)
def dtau(x):
    """sum_{k<=x} tau(k) by the hyperbola method."""
    if x <= 0:
        return np.int64(0)
    s = isqrt64(x)
    t = np.int64(0)
    for i in range(1, s + 1):
        t += x // i
    return 2 * t - s * s


@njit(cache=True)
def omega_sieve(n):
    om = np.zeros(n + 1, dtype=np.int8)
    for p in range(2, n + 1):
        if om[p] == 0:
            for q in range(p, n + 1, p):
                om[q] += 1
    return om


@njit(cache=True)
def skew_sum(K, om):
    """sum of 2^omega(j) over (c, m, j): cm <= K, sqrt(3) j m < c, mod MOD."""
    total = np.int64(0)
    m = np.int64(1)
    while m <= K:
        C = K // m
        j = np.int64(1)
        any_j = False
        while True:
            t = isqrt64(3 * j * j * m * m)
            if t >= C:
                break
            any_j = True
            total = (total + (np.int64(1) << om[j]) * ((C - t) % MOD)) % MOD
            j += 1
        if not any_j:
            break  # larger m is only worse
        m += 1
    return total


@njit(cache=True)
def prime_sieve(n):
    comp = np.zeros(n + 1, dtype=np.uint8)
    for i in range(2, n + 1):
        if not comp[i]:
            for q in range(i * i, n + 1, i):
                comp[q] = 1
    cnt = 0
    for i in range(2, n + 1):
        if not comp[i]:
            cnt += 1
    primes = np.empty(cnt, dtype=np.int64)
    cnt = 0
    for i in range(2, n + 1):
        if not comp[i]:
            primes[cnt] = i
            cnt += 1
    return primes


@njit(cache=True)
def lattice_sum(K, primes1):
    """sum over M (all prime factors = 1 mod 3, 2M <= K) of
    2^omega(M) * Dtau(K // (2M)), mod MOD."""
    K2 = K // 2
    if K2 < 1:
        return np.int64(0)
    v0 = isqrt64(K2)
    tau_small = np.zeros(v0 + 1, dtype=np.int64)
    for i in range(1, v0 + 1):
        for q in range(i, v0 + 1, i):
            tau_small[q] += 1
    dts = np.zeros(v0 + 1, dtype=np.int64)
    for i in range(1, v0 + 1):
        dts[i] = dts[i - 1] + tau_small[i]
    np1 = primes1.shape[0]
    cap = 2 * np1 + 200
    st_m = np.empty(cap, dtype=np.int64)
    st_i = np.empty(cap, dtype=np.int64)
    st_w = np.empty(cap, dtype=np.int64)
    st_m[0] = 1
    st_i[0] = 0
    st_w[0] = 1
    top = 1
    total = np.int64(0)
    while top > 0:
        top -= 1
        m_val = st_m[top]
        i0 = st_i[top]
        w = st_w[top]
        v = K2 // m_val
        dt = dts[v] if v <= v0 else dtau(v)
        total = (total + (w % MOD) * (dt % MOD)) % MOD
        for i in range(i0, np1):
            p = primes1[i]
            if m_val * p > K2:
                break
            mp = m_val * p
            while mp <= K2:
                st_m[top] = mp
                st_i[top] = i + 1
                st_w[top] = 2 * w
                top += 1
                mp *= p
    return total


def torus_tilings(n):
    """G(n) mod MOD."""
    big_k = n // 2
    if big_k < 1:
        return 0
    om = omega_sieve(max(2, int(big_k / np.sqrt(3)) + 2))
    part_axis = 2 * (dtau(big_k) % MOD) % MOD
    part_skew = 4 * skew_sum(big_k, om) % MOD
    primes = prime_sieve(max(3, big_k // 2))
    primes1 = primes[primes % 3 == 1]
    part_reg = 4 * lattice_sum(big_k, primes1) % MOD
    return (part_axis + part_skew - part_reg) % MOD


def main():
    assert torus_tilings(6) == 14
    assert torus_tilings(100) == 8090
    assert torus_tilings(10**5) == 645124048
    return torus_tilings(N)


if __name__ == "__main__":
    print(main())  # 613979935
