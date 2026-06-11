"""Project Euler 489: Common Factors Between Two Sequences.

G(a, b) is the smallest n >= 0 maximizing gcd(n^3 + b, (n + a)^3 + b);
find H(18, 1900) = sum of G(a, b) over 1 <= a <= 18, 1 <= b <= 1900.

Any common divisor of the two values divides their resultant
Res(x^3 + b, (x + a)^3 + b) = a^3 ((a^3)^2 + 27 b^2), so only the primes of
a^3 (a^6 + 27 b^2) matter (a^6 + 27 b^2 <= 1.3 * 10^8 here, factorable by
trial division). For a prime p > a not dividing 3: both n and n + a are cube
roots of -b mod p, so their quotient is a primitive cube root of unity omega
(forcing p = 1 mod 3) and n = a / (omega - 1) mod p - just two candidates to
check against n^3 = -b. Small primes (p <= 1200, covering p | 3a and shared
factors with b) are scanned directly. Each base solution is Hensel-lifted:
writing n = s + t p^k, the pair of congruences becomes two linear conditions
on t, solved or declared inconsistent per the usual derivative cases; the
maximal liftable exponent e_p gives the p-part of the maximum gcd.

The maximum gcd is the product of the p^(e_p) (the per-prime maxima are
simultaneously achievable by CRT and cannot be exceeded prime by prime), and
G(a, b) is the smallest CRT representative over all combinations of the
per-prime solution sets. Verified against direct brute-force scanning for
all a, b <= 5 and against H(5, 5) = 128878 and H(10, 10) = 32936544.
"""

import random
from itertools import product

import numpy as np
from numba import njit


@njit(cache=True)
def brute_g(a, b, scan):
    best = np.int64(0)
    arg = np.int64(0)
    for n in range(scan):
        x = np.int64(n**3 + b)
        y = np.int64((n + a) ** 3 + b)
        while y:
            x, y = y, x % y
        if x > best:
            best = x
            arg = n
    return arg


def solve_prime(p, max_e, a, b):
    """Maximal e and solution set of n^3=-b, (n+a)^3=-b mod p^e."""
    sols = []
    if p <= 1200:
        for n in range(p):
            if (n**3 + b) % p == 0 and ((n + a) ** 3 + b) % p == 0:
                sols.append(n)
    elif p % 3 == 1:
        w = 1
        while w == 1:
            w = pow(random.randrange(2, p), (p - 1) // 3, p)
        for om in (w, w * w % p):
            n = a * pow(om - 1, -1, p) % p
            if (n**3 + b) % p == 0 and ((n + a) ** 3 + b) % p == 0:
                sols.append(n)
        sols = sorted(set(sols))
    if not sols:
        return 0, []
    e, mod = 1, p
    while e < max_e:
        newsols = []
        for s in sols:
            c1 = ((s**3 + b) // mod) % p
            d1 = 3 * s * s % p
            c2 = (((s + a) ** 3 + b) // mod) % p
            d2 = 3 * (s + a) * (s + a) % p
            if d1 != 0:
                t1 = (-c1) * pow(d1, -1, p) % p
                ts = [t1] if (c2 + t1 * d2) % p == 0 else []
            elif c1 != 0:
                ts = []
            elif d2 != 0:
                ts = [(-c2) * pow(d2, -1, p) % p]
            elif c2 != 0:
                ts = []
            else:
                ts = list(range(p))
            for t in ts:
                newsols.append(s + t * mod)
        if not newsols:
            break
        sols = sorted(set(newsols))
        mod *= p
        e += 1
    return e, sols


def g_fast(a, b):
    r0 = a**6 + 27 * b * b
    fac = {}
    for base, mult in ((a, 3), (r0, 1)):
        m = base
        d = 2
        while d * d <= m:
            while m % d == 0:
                fac[d] = fac.get(d, 0) + mult
                m //= d
            d += 1
        if m > 1:
            fac[m] = fac.get(m, 0) + mult
    crt_mods, crt_sets = [], []
    for p, max_e in sorted(fac.items()):
        e, sols = solve_prime(p, max_e, a, b)
        if e > 0 and sols:
            crt_mods.append(p**e)
            crt_sets.append(sols)
    if not crt_mods:
        return 0
    best = None
    for combo in product(*crt_sets):
        x, mod = 0, 1
        for r, m in zip(combo, crt_mods):
            x += mod * ((r - x) % m * pow(mod % m, -1, m) % m)
            mod *= m
        if best is None or x < best:
            best = x
    return best


def total_h(m, n):
    return sum(g_fast(a, b) for a in range(1, m + 1) for b in range(1, n + 1))


if __name__ == "__main__":
    for a in range(1, 6):
        for b in range(1, 6):
            scan = min(a**3 * (a**6 + 27 * b * b), 3_000_000)
            assert g_fast(a, b) == int(brute_g(a, b, scan))
    assert total_h(5, 5) == 128878
    assert total_h(10, 10) == 32936544
    print(total_h(18, 1900))  # 1791954757162
