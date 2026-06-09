"""Project Euler Problem 810: XOR-Primes.

The XOR-product is carry-less binary multiplication, i.e. multiplication of
polynomials over GF(2).  An XOR-prime is therefore an irreducible polynomial
over GF(2) (of degree >= 1) read as an integer.  Ordered by integer value the
XOR-primes are 2, 3, 7, 11, 13, ...  We want the 5,000,000th one.

A degree-d polynomial has integer value in [2^d, 2^(d+1)), so ordering by value
is the same as ordering by degree then by value.  Counting irreducibles by
degree shows the 5,000,000th has degree 26, so a carry-less sieve up to 2^27 is
enough: mark every value that is a carry-less product of two factors >= 2; the
unmarked values >= 2, in increasing order, are exactly the XOR-primes.
"""

import numba
import numpy as np


@numba.njit(cache=True)
def _clmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


@numba.njit(cache=True)
def _deg(a):
    d = -1
    while a:
        a >>= 1
        d += 1
    return d


@numba.njit(cache=True)
def _sieve(n):
    comp = np.zeros(n, dtype=np.uint8)
    maxdeg = _deg(n - 1)
    # Every composite of degree <= maxdeg has a factor of degree <= maxdeg // 2.
    plim = 1 << (maxdeg // 2 + 1)
    for p in range(2, plim):
        if comp[p] == 0:  # p is an XOR-prime (irreducible)
            dp = _deg(p)
            qlim = 1 << (maxdeg - dp + 1)  # deg(p) + deg(q) <= maxdeg
            for q in range(2, qlim):
                c = _clmul(p, q)
                if c < n:
                    comp[c] = 1
    return comp


@numba.njit(cache=True)
def _nth(comp, n, k):
    cnt = 0
    for v in range(2, n):
        if comp[v] == 0:
            cnt += 1
            if cnt == k:
                return v
    return -1


def solve(k=5_000_000, n=1 << 27):
    comp = _sieve(n)
    return _nth(comp, n, k)


if __name__ == "__main__":
    print(solve())  # 124136381
