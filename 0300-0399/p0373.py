import sys
from math import isqrt

import numpy as np


def _points(R: int) -> tuple[list[int], list[int]]:
    """Gaussian integers e + a*i of norm (2R)^2 with a > 0 (upper half).

    These are exactly the sides: a side `a` of an integer triangle with
    integer circumradius R satisfies a^2 + e^2 = (2R)^2, because
    cos(opposite angle) = sqrt(4R^2 - a^2)/(2R) is rational.
    """
    d = 2 * R
    d2 = d * d
    a = np.arange(1, d + 1, dtype=np.int64)
    e2 = d2 - a * a
    e = np.sqrt(e2.astype(np.float64)).astype(np.int64)
    for _ in range(2):
        e = np.where((e + 1) * (e + 1) <= e2, e + 1, e)
        e = np.where(e * e > e2, e - 1, e)
    mask = e * e == e2
    es = e[mask].tolist()
    as_ = a[mask].tolist()
    re: list[int] = []
    im: list[int] = []
    for ai, ei in zip(as_, es):
        re.append(ei)
        im.append(ai)
        if ei != 0:
            re.append(-ei)
            im.append(ai)
    return re, im


def _triangles_from(R: int) -> int:
    """Count integer triangles with circumradius exactly R, by brute force on
    the lattice points of the radius-2R circle.

    A triangle corresponds to an unordered triple of upper-half points whose
    product equals -(2R)^3 (their arguments A, B, C sum to pi).  Ordered
    triples are counted in O(U^2): the third vertex is forced by the first
    two, z_k = -conj(z_i z_j)/w.  Isoceles triangles are added back so the
    unordered count is (ordered + 3*isoceles)/6 (no equilateral exists).
    """
    re, im = _points(R)
    u = len(re)
    w = 2 * R
    pset = set(zip(re, im))
    ordered = 0
    for i in range(u):
        ei, ai = re[i], im[i]
        for j in range(u):
            ej, aj = re[j], im[j]
            pr, pi = ei * ej - ai * aj, ei * aj + ai * ej
            if (-pr) % w == 0 and pi % w == 0 and ((-pr) // w, pi // w) in pset:
                ordered += 1
    iso = 0
    for i in range(u):
        ei, ai = re[i], im[i]
        pr, pi = ei * ei - ai * ai, 2 * ei * ai
        if (-pr) % w == 0 and pi % w == 0:
            z = ((-pr) // w, pi // w)
            if z in pset and z != (ei, ai):
                iso += 1
    return (ordered + 3 * iso) // 6


def circumradius_sum(n: int) -> int:
    """Sum of circumradii R <= n over all integer-sided triangles whose
    circumradius is an integer.

    The triangle count T(R) depends only on the multiset of exponents of the
    primes p == 1 (mod 4) dividing R (factors of 2 and primes == 3 (mod 4)
    leave the Gaussian-prime arguments unchanged), so write
        S(n) = sum_{m} g(sig(m)) * m * H(n / m),
    where m ranges over integers built only from primes == 1 (mod 4), sig(m)
    is its exponent multiset, and H(x) sums all k <= x having no prime factor
    == 1 (mod 4).  For a single prime power g(p^a) = a(a+1) - ceil(a/2);
    multi-prime values are tabulated once by brute force on the smallest
    representative.
    """
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes1 = np.nonzero(sieve)[0]
    primes1 = primes1[primes1 % 4 == 1]

    has1 = np.zeros(n + 1, dtype=bool)
    for p in primes1:
        has1[p::p] = True
    weighted = np.arange(n + 1, dtype=np.int64)
    weighted[has1] = 0
    h_prefix = np.cumsum(weighted)  # H(x) = h_prefix[x]

    cache: dict[tuple[int, ...], int] = {}
    plist = primes1.tolist()

    def g(sig: list[int]) -> int:
        key = tuple(sorted(sig, reverse=True))
        if not key:
            return 0
        if key in cache:
            return cache[key]
        if len(key) == 1:
            a = key[0]
            val = a * (a + 1) - (a + 1) // 2
        else:
            r = 1
            for pr, a in zip(plist, key):
                r *= pr**a
            val = _triangles_from(r)
        cache[key] = val
        return val

    np1 = len(plist)
    total = 0

    def rec(idx: int, m: int, sig: list[int]) -> None:
        nonlocal total
        if sig:
            total += g(sig) * m * int(h_prefix[n // m])
        for i in range(idx, np1):
            p = plist[i]
            if m * p > n:
                break
            pe = p
            e = 1
            while m * pe <= n:
                rec(i + 1, m * pe, sig + [e])
                pe *= p
                e += 1

    sys.setrecursionlimit(100000)
    rec(0, 1, [])
    return total


if __name__ == "__main__":
    assert circumradius_sum(100) == 4950
    assert circumradius_sum(1200) == 1653605
    print(circumradius_sum(10**7))  # 727227472448913
