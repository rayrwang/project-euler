"""
Project Euler Problem 799: Pentagonal Puzzle
https://projecteuler.net/problem=799

Find the smallest pentagonal number expressible as the sum of two pentagonal
numbers in over 100 different ways.

With P_n = n(3n-1)/2 and X = 6m-1, A = 6a-1, B = 6b-1, multiplying
P_m = P_a + P_b by 24 gives

    X^2 + 1 = A^2 + B^2,

so the number of ways equals the number of unordered pairs {A, B} of positive
integers with A = B = 5 (mod 6) and A^2 + B^2 = N := X^2 + 1.  Every odd
prime factor of N is = 1 (mod 4), so representations come from the Gaussian
factorization N = -i (1+i)^2 prod (pi_p conj(pi_p))^e_p.

Plan (X = 6k-1 ascending, so pentagonal numbers ascending):
 1. For every prime p = 1 (mod 4) up to XMAX, compute a square root s of -1
    (mod p); then p | X^2 + 1 exactly on two progressions X = +-s (mod p).
    Sweeping those progressions over the array indexed by k, dividing out p
    and accumulating d(k) = prod (e_p + 1), costs about 1e8 cheap operations.
    Any cofactor left after the sweep is 1 or a single prime > XMAX (two such
    factors would exceed N), doubling d.
 2. A pair count > 100 requires d >= 201, since the number of unordered
    representations is at most (d+1)/2.  Such X are rare; for them only, a
    second sweep records the actual prime factorization.
 3. For each candidate in ascending order, Cornacchia's algorithm splits each
    prime as p = u^2 + v^2, all divisor combinations pi^j conj(pi)^(e-j) are
    multiplied out exactly, and the distinct unordered pairs {|A|, |B|} with
    A = B = 5 (mod 6) are counted; the first X reaching over 100 ways gives
    the answer (X^2 - 1)/24.

The Gaussian counting is validated against a direct quadratic brute force
over all pentagonal numbers below P_300 before the main run.
"""

from math import isqrt

import numpy as np
from numba import njit

KMAX = 30_000_000  # X = 6k - 1 up to ~1.8e8; answer X = 162252407
XMAX = 6 * KMAX


def sieve_primes(n):
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, isqrt(n) + 1):
        if is_p[i]:
            is_p[i * i :: i] = False
    return np.flatnonzero(is_p).astype(np.int64)


@njit(cache=True)
def powmod(a, e, m):
    r = 1
    a %= m
    while e > 0:
        if e & 1:
            r = r * a % m
        a = a * a % m
        e >>= 1
    return r


@njit(cache=True)
def sqrt_minus_one(p):
    """A square root of -1 modulo a prime p = 1 (mod 4)."""
    a = 2
    while True:
        s = powmod(a, (p - 1) // 4, p)
        if s * s % p == p - 1:
            return s
        a += 1


@njit(cache=True)
def sweep(primes, kmax, record_for, max_rec):
    """First pass (record_for empty): divide N(k) = (6k-1)^2 + 1 by every
    sieved prime, returning d(k) = prod (e+1) (leftover prime included) and
    the s-values.  Second pass (record_for[k] >= 0 marks candidate indices):
    additionally record (candidate, p, e) triples."""
    res = np.empty(kmax + 1, dtype=np.uint64)
    d = np.ones(kmax + 1, dtype=np.uint32)
    for k in range(1, kmax + 1):
        x = np.uint64(6 * k - 1)
        res[k] = (x * x + np.uint64(1)) // np.uint64(2)
    rec_c = np.empty(max_rec, dtype=np.int32)
    rec_p = np.empty(max_rec, dtype=np.int64)
    rec_e = np.empty(max_rec, dtype=np.int8)
    nrec = 0
    inv6cache = 0
    for t in range(primes.shape[0]):
        p = primes[t]
        s = sqrt_minus_one(p)
        inv6cache = powmod(6, p - 2, p)
        for sgn in range(2):
            ss = s if sgn == 0 else p - s
            # X = 6k - 1 = ss (mod p)  ->  k = (ss + 1) / 6 (mod p)
            k0 = (ss + 1) % p * inv6cache % p
            if k0 == 0:
                k0 = p
            up = np.uint64(p)
            for k in range(k0, kmax + 1, p):
                e = 0
                while res[k] % up == np.uint64(0):
                    res[k] //= up
                    e += 1
                d[k] *= np.uint32(e + 1)
                if e > 0 and record_for[k] >= 0 and nrec < max_rec:
                    rec_c[nrec] = record_for[k]
                    rec_p[nrec] = p
                    rec_e[nrec] = e
                    nrec += 1
    # leftover prime cofactors
    left = np.empty(kmax + 1, dtype=np.uint64)
    for k in range(1, kmax + 1):
        left[k] = res[k]
        if res[k] > np.uint64(1):
            d[k] *= np.uint32(2)
    return d, left, rec_c[:nrec], rec_p[:nrec], rec_e[:nrec]


def cornacchia(p):
    """u, v with u^2 + v^2 = p for prime p = 1 (mod 4)."""
    a = 2
    while pow(a, (p - 1) // 2, p) != p - 1:
        a += 1
    s = pow(a, (p - 1) // 4, p)
    r0, r1 = p, s
    lim = isqrt(p)
    while r1 > lim:
        r0, r1 = r1, r0 % r1
    u = r1
    v = isqrt(p - u * u)
    assert u * u + v * v == p
    return u, v


def count_ways(x, factors):
    """Unordered pairs {A, B}, A = B = 5 (mod 6), A^2 + B^2 = x^2 + 1, given
    the prime factorization (p, e) of the odd part."""
    z_list = [(1, 1)]  # 1 + i accounts for the single factor of two
    for p, e in factors:
        u, v = cornacchia(p)
        powers = [(1, 0)]
        for _ in range(e):
            a, b = powers[-1]
            powers.append((a * u - b * v, a * v + b * u))
        cpowers = [(a, -b) for a, b in powers]
        new = []
        for a, b in z_list:
            for j in range(e + 1):
                c, dd = powers[j]
                f, g = cpowers[e - j]
                cf, dg = c * f - dd * g, c * g + dd * f
                new.append((a * cf - b * dg, a * dg + b * cf))
        z_list = new
    pairs = set()
    n = x * x + 1
    for a, b in z_list:
        a, b = abs(a), abs(b)
        assert a * a + b * b == n
        pairs.add((min(a, b), max(a, b)))
    return sum(1 for a, b in pairs if a % 6 == 5 and b % 6 == 5)


def factor_small(n):
    f = []
    m = n
    p = 3
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            f.append((p, e))
        p += 2
    if m > 1:
        f.append((m, 1))
    return f


def validate():
    """Brute-force cross-check of the Gaussian counting for all pentagonal
    numbers up to P_300."""
    pent = [n * (3 * n - 1) // 2 for n in range(1, 301)]
    pset = set(pent)
    from collections import Counter

    cnt = Counter()
    for i in range(300):
        for j in range(i, 300):
            s = pent[i] + pent[j]
            if s in pset:
                cnt[s] += 1
    for m in range(1, 301):
        x = 6 * m - 1
        ways = count_ways(x, factor_small((x * x + 1) // 2))
        assert ways == cnt.get(pent[m - 1], 0), (m, ways)


def main():
    validate()
    primes = sieve_primes(XMAX)
    primes = primes[primes % 4 == 1]
    no_rec = np.full(KMAX + 1, -1, dtype=np.int32)
    d, left, _, _, _ = sweep(primes, KMAX, no_rec, 1)
    cand = [k for k in range(1, KMAX + 1) if d[k] >= 201]
    record_for = np.full(KMAX + 1, -1, dtype=np.int32)
    for i, k in enumerate(cand):
        record_for[k] = i
    _, left2, rc, rp, re = sweep(primes, KMAX, record_for, 1 << 22)
    factors = [[] for _ in cand]
    for i in range(rc.shape[0]):
        factors[rc[i]].append((int(rp[i]), int(re[i])))
    for i, k in enumerate(cand):
        if left2[k] > 1:
            factors[i].append((int(left2[k]), 1))
    for i, k in enumerate(cand):
        x = 6 * k - 1
        if count_ways(x, factors[i]) > 100:
            return (x * x - 1) // 24
    raise RuntimeError("no answer below XMAX; increase KMAX")


if __name__ == "__main__":
    print(main())  # 1096910149053902
