"""Project Euler 864: Square + 1 = Squarefree.

Count x with 1 <= x <= N = 123567101113 such that x^2 + 1 is squarefree.

By Mobius inversion C(N) = sum_d mu(d) S(d) with S(d) = #{x <= N :
d^2 | x^2 + 1}.  Only d whose prime factors are congruent to 1 mod 4
contribute (x^2 + 1 is never divisible by 4 nor by primes 3 mod 4),
and each such prime p has two square roots of -1 modulo p^2 obtained
by a Tonelli exponentiation modulo p followed by a Hensel lift.

The sum splits at Z ~ N^(2/3).  For d <= Z a depth-first search over
products of primes builds the 2^omega(d) roots modulo d^2 by CRT and
adds mu(d) S(d) exactly.  For d > Z we have m = (x^2 + 1) / d^2 <=
(N^2 + 1) / Z^2, so the remaining terms are exactly the solutions of
the negative Pell equations x^2 - m d^2 = -1 with x <= N and d > Z,
one equation per m.  All such solutions are convergents of the
continued fraction of sqrt(m), recognised by the classical identity
p_{k-1}^2 - m q_{k-1}^2 = (-1)^k Q_k without forming the huge squares;
since convergent numerators grow at least like Fibonacci numbers, at
most ~55 steps are needed before exceeding N, and the expansion is run
for every m simultaneously with vectorised numpy.  Two distinct large
primes cannot both have squares dividing x^2 + 1 (their product would
exceed N), so each surviving pair simply contributes mu(d), computed
by trial division over primes 1 mod 4.

The implementation is validated against a direct sieve for small N
and by agreement between different choices of the cutoff Z.
"""

from __future__ import annotations

import sys

import numpy as np

N_TARGET = 123567101113
Z_TARGET = 25_000_000

# Small primes congruent to 3 mod 4 used to pre-filter m: any prime
# 3 mod 4 dividing m would have to divide x^2 + 1, which is impossible.
FILTER_PRIMES = (3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83)


def sieve(limit: int) -> np.ndarray:
    flags = np.ones(limit + 1, dtype=np.uint8)
    flags[:2] = 0
    for i in range(2, int(limit**0.5) + 1):
        if flags[i]:
            flags[i * i :: i] = 0
    return np.nonzero(flags)[0]


def root_minus_one(p: int) -> int:
    """Square root of -1 modulo p^2 for a prime p = 1 mod 4."""
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            r = pow(a, (p - 1) // 4, p)
            break
    else:  # pragma: no cover - unreachable for prime p = 1 mod 4
        raise AssertionError
    t = (-(r * r + 1) // p * pow(2 * r, p - 2, p)) % p
    return (r + t * p) % (p * p)


def small_d_sum(n: int, z: int, plist: list[tuple[int, int, int]]) -> int:
    """sum of mu(d) S(d) over d <= z with all prime factors 1 mod 4."""
    sys.setrecursionlimit(10000)
    total = 0

    def dfs(start: int, d: int, dsq: int, roots: list[int], mu: int) -> None:
        nonlocal total
        s = 0
        for r in roots:
            s += (n - r) // dsq + 1 if r else n // dsq
        total += mu * s
        for j in range(start, len(plist)):
            p, rp, psq = plist[j]
            if d * p > z:
                break
            inv = pow(dsq, -1, psq)
            nroots = []
            for r in roots:
                nroots.append(r + dsq * ((rp - r) * inv % psq))
                nroots.append(r + dsq * ((psq - rp - r) * inv % psq))
            dfs(j + 1, d * p, dsq * psq, nroots, -mu)

    dfs(0, 1, 1, [0], 1)
    return total


def pell_pairs(n: int, z: int) -> np.ndarray:
    """d-values of all pairs (x, d) with d^2 | x^2 + 1, x <= n, d > z."""
    m_max = (n * n + 1) // ((z + 1) * (z + 1))
    m = np.arange(2, m_max + 1, dtype=np.int64)
    keep = ((m & 3) == 1) | ((m & 3) == 2)
    for p in FILTER_PRIMES:
        keep &= (m % p) != 0
    m = m[keep]
    a0 = np.sqrt(m.astype(np.float64)).astype(np.int64)
    a0 -= a0 * a0 > m
    a0 += (a0 + 1) ** 2 <= m
    nonsquare = a0 * a0 != m
    m = m[nonsquare]
    a0 = a0[nonsquare]
    big_p = np.zeros_like(m)
    big_q = np.ones_like(m)
    a = a0.copy()
    num_prev, num = np.ones_like(m), a0.copy()
    den_prev, den = np.zeros_like(m), np.ones_like(m)
    found: list[np.ndarray] = []
    k = 0
    while m.size:
        big_p = a * big_q - big_p
        big_q = (m - big_p * big_p) // big_q
        k += 1
        if k & 1:
            sol = (big_q == 1) & (num <= n) & (den > z)
            if sol.any():
                found.append(den[sol])
        a = (a0 + big_p) // big_q
        num_next = a * num + num_prev
        active = num_next <= n
        if not active.all():
            m, a0, big_p, big_q, a = (
                m[active],
                a0[active],
                big_p[active],
                big_q[active],
                a[active],
            )
            den_next = a * den[active] + den_prev[active]
            num_prev, num = num[active], num_next[active]
            den_prev, den = den[active], den_next
        else:
            den_next = a * den + den_prev
            num_prev, num = num, num_next
            den_prev, den = den, den_next
    if not found:
        return np.zeros(0, dtype=np.int64)
    return np.concatenate(found)


def mobius(value: int, primes: list[int]) -> int:
    omega = 0
    x = value
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            x //= p
            if x % p == 0:
                return 0
            omega += 1
    if x > 1:
        omega += 1
    return -1 if omega & 1 else 1


def squarefree_count(n: int, z: int) -> int:
    primes = sieve(z)
    plist = []
    for p in primes:
        p = int(p)
        if p % 4 == 1:
            plist.append((p, root_minus_one(p), p * p))
    total = small_d_sum(n, z, plist)
    factor_primes = [p for p, _, _ in plist]
    for d in pell_pairs(n, z):
        total += mobius(int(d), factor_primes)
    return total


def main() -> None:
    assert squarefree_count(10, 5) == 9
    assert squarefree_count(1000, 30) == 895
    assert squarefree_count(10**6, 200) == squarefree_count(10**6, 5000)
    print(squarefree_count(N_TARGET, Z_TARGET))  # 110572936177


if __name__ == "__main__":
    main()
