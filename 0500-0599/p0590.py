"""
https://projecteuler.net/problem=590

H(n) counts the sets of positive integers whose least common
multiple is exactly n, and L(n) = lcm(1..n). Find
HL(50000) = H(L(50000)) modulo 10^9.

A set with lcm n consists of divisors of n covering each prime's
maximal exponent. Inclusion-exclusion over the primes whose exponent
is capped one below maximal gives, for n = prod p_i^e_i,

    H(n) = sum over T of (-1)^|T| 2^(prod_i (e_i + 1 - [i in T])),

verified against literal subset enumeration for small n and the
given H(12) = 44. For L(50000) the primes group by exponent: one
each of e = 15, 9, 6, 5, two of e = 4, five of e = 3, thirty-seven
of e = 2, and k1 = 5085 primes with e = 1. Choices within a class of
c equal exponents contribute binomially, so the sum collapses to
about 10^4 class-choice combinations times a sum over j (the number
of capped e=1 primes) of C(k1, j) (-1)^j 2^(D 2^(k1-j)).

The towers 2^E mod 10^9 split by CRT: E >= 9 always (D >= 2^37 for
the real computation), so the residue is 0 mod 2^9, while 2 is a
primitive root mod 5^9 with order 4 * 5^8, so only E mod 4*5^8 is
needed. Exact small exponents are handled directly so that the same
code validates the small HL values against exact big-integer
evaluation. Binomials mod 10^9 come from a Pascal row.
"""

from itertools import product
from math import comb, lcm

import numba
import numpy as np

MOD = 10**9
P59 = 5**9
ORD = 4 * 5**8  # multiplicative order of 2 mod 5^9
INV512 = pow(512, -1, P59)


@numba.njit(cache=True)
def _pascal_row(k1: int, mod: int) -> np.ndarray:
    c = np.zeros(k1 + 1, dtype=np.int64)
    c[0] = 1
    for i in range(1, k1 + 1):
        for j in range(i, 0, -1):
            c[j] = (c[j] + c[j - 1]) % mod
    return c


@numba.njit(cache=True)
def _kernel(coefs, ds, dsmall, c, k1):
    total = np.int64(0)
    for t in range(coefs.shape[0]):
        sub = np.int64(0)
        e = ds[t] % ORD
        for j in range(k1, -1, -1):
            e_small = np.int64(-1)
            if dsmall[t] > 0:
                sh = k1 - j
                if sh < 60 and dsmall[t] < (np.int64(1) << np.int64(60 - sh)):
                    ee = dsmall[t] << np.int64(sh)
                    if ee < 64:
                        e_small = ee
            if e_small >= 0:
                v = (np.int64(1) << e_small) % MOD
            else:  # E >= 9 here, so 2^E = 0 mod 2^9; CRT with mod 5^9
                r = np.int64(1)
                b = np.int64(2)
                ee = e
                while ee > 0:
                    if ee & 1:
                        r = r * b % P59
                    b = b * b % P59
                    ee >>= 1
                v = 512 * (r * INV512 % P59) % MOD
            term = c[j] * v % MOD
            sub = (sub + term) % MOD if j % 2 == 0 else (sub - term) % MOD
            e = e * 2 % ORD
        total = (total + coefs[t] * sub) % MOD
    return total % MOD


def hl(n: int) -> int:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    classes: dict[int, int] = {}
    for p in np.nonzero(sieve)[0]:
        e = 1
        while int(p) ** (e + 1) <= n:
            e += 1
        classes[e] = classes.get(e, 0) + 1
    k1 = classes.pop(1, 0)
    es = sorted(classes)
    cs = [classes[e] for e in es]
    row = _pascal_row(k1, MOD)
    combos = list(product(*[range(cc + 1) for cc in cs]))
    coefs = np.zeros(len(combos), dtype=np.int64)
    ds = np.zeros(len(combos), dtype=np.int64)
    dsm = np.zeros(len(combos), dtype=np.int64)
    for t, tt in enumerate(combos):
        coef, d_mod, d_exact, sgn = 1, 1, 1, 0
        for e, cc, ti in zip(es, cs, tt):
            coef = coef * comb(cc, ti) % MOD
            sgn += ti
            d_mod = d_mod * pow(e, ti, ORD) % ORD * pow(e + 1, cc - ti, ORD) % ORD
            if d_exact > 0:
                d_exact *= e**ti * (e + 1) ** (cc - ti)
                if d_exact > 10**15:
                    d_exact = -1
        coefs[t] = coef if sgn % 2 == 0 else (MOD - coef) % MOD
        ds[t] = d_mod
        dsm[t] = d_exact
    return int(_kernel(coefs, ds, dsm, row, k1))


def _h_exact(n: int) -> int:
    fac: dict[int, int] = {}
    m, d = n, 2
    while d * d <= m:
        while m % d == 0:
            fac[d] = fac.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        fac[m] = fac.get(m, 0) + 1
    es = list(fac.values())
    return sum(
        (-1) ** sum(t)
        * 2 ** np.prod([e if ti else e + 1 for e, ti in zip(es, t)], dtype=object)
        for t in product([0, 1], repeat=len(es))
    )


def _brute_h(n: int) -> int:
    divs = [d for d in range(1, n + 1) if n % d == 0]
    cnt = 0
    for mask in range(1, 1 << len(divs)):
        ell = 1
        for i, d in enumerate(divs):
            if mask >> i & 1:
                ell = lcm(ell, d)
        cnt += ell == n
    return cnt


if __name__ == "__main__":
    for n in (6, 12, 30, 36, 60, 96):
        assert _brute_h(n) == _h_exact(n), n
    assert _h_exact(12) == 44  # given HL(4) = H(12) = 44

    for n in (3, 4, 6, 8, 10, 13, 20):
        ell = 1
        for i in range(2, n + 1):
            ell = lcm(ell, i)
        assert _h_exact(ell) % MOD == hl(n), n

    print(hl(50000))  # 834171904
