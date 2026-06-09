"""
https://projecteuler.net/problem=545

Sum_{i=1..n} i^k is a polynomial in n; D(k) is the denominator of the
coefficient a_1 of n^1. Find F(10^5), the 10^5-th k with D(k) = 20010.

By Faulhaber's formula, a_1 = B_k, the k-th Bernoulli number (with
B_1 = +1/2; for k >= 2 even, B_k is the ordinary Bernoulli number, and
for k >= 3 odd, B_k = 0 so D(k) = 1). The von Staudt-Clausen theorem
states that for even k >= 2,

    B_k + sum_{(p-1) | k} 1/p  is an integer  (p prime),

so the denominator of B_k is exactly the product of all primes p with
(p-1) | k. Both facts (a_1 = B_k, and the denominator product) are
verified numerically in the asserts below.

Now 20010 = 2 * 3 * 5 * 23 * 29, so D(k) = 20010 iff
  - (p-1) | k for p in {2, 3, 5, 23, 29}, i.e.
    lcm(1, 2, 4, 22, 28) = 308 divides k, and
  - no other prime p has (p-1) | k.
Writing k = 308 m, the second condition says: no divisor d of 308 m
with d + 1 prime, except d in {1, 2, 4, 22, 28}.

Search: sieve over m. For every prime p <= SMALL (p not in the allowed
set), d = p - 1 divides 308 m iff (d / gcd(d, 308)) | m, so strike out
those m. Survivors are then checked against divisors d >= SMALL of
308 m (rare and few) with a Miller-Rabin test on d + 1.
"""

import sys
from fractions import Fraction
from math import comb, gcd
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import is_prime, prime_sieve_int  # noqa: E402

ALLOWED = (2, 3, 5, 23, 29)  # 2*3*5*23*29 = 20010
BASE = 308  # lcm(p - 1 for p in ALLOWED)
SMALL = 100_000


def bernoulli(kmax: int) -> list[Fraction]:
    """B_0..B_kmax with the B_1 = +1/2 convention, via the standard
    recurrence sum_{j=0..m} C(m+1, j) B_j = 0."""
    b = [Fraction(0)] * (kmax + 1)
    b[0] = Fraction(1)
    for m in range(1, kmax + 1):
        s = sum(comb(m + 1, j) * b[j] for j in range(m) if b[j])
        b[m] = Fraction(-s, m + 1)
    b[1] = Fraction(1, 2)
    return b


def faulhaber_a1(k: int) -> Fraction:
    """Coefficient of n^1 in sum_{i=1..n} i^k, by solving the linear
    system through the first k+1 partial sums (exact arithmetic)."""
    n_pts = k + 1
    mat = []
    s = 0
    for n in range(1, n_pts + 1):
        s += n**k
        mat.append([Fraction(n**i) for i in range(1, n_pts + 1)] + [Fraction(s)])
    for col in range(n_pts):
        piv = next(r for r in range(col, n_pts) if mat[r][col])
        mat[col], mat[piv] = mat[piv], mat[col]
        for r in range(n_pts):
            if r != col and mat[r][col]:
                f = mat[r][col] / mat[col][col]
                for c in range(col, n_pts + 1):
                    mat[r][c] -= f * mat[col][c]
    return mat[0][n_pts] / mat[0][0]


def vsc_denominator(k: int, primes: np.ndarray) -> int:
    prod = 1
    for p in primes:
        if p > k + 1:
            break
        if k % (p - 1) == 0:
            prod *= int(p)
    return prod


@numba.njit(cache=True)
def _spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def _sieve_candidates(m_max: int, small_primes: np.ndarray) -> np.ndarray:
    """valid[m] = False if some prime p (not allowed) has (p-1) | 308*m,
    for p among small_primes."""
    valid = np.ones(m_max + 1, dtype=np.bool_)
    valid[0] = False
    for p in small_primes:
        if p == 2 or p == 3 or p == 5 or p == 23 or p == 29:
            continue
        d = p - 1
        s = d // gcd(d, BASE)
        if s <= m_max:
            valid[s::s] = False
    return valid


@numba.njit(cache=True)
def _check_large_divisors(m: int, spf: np.ndarray) -> bool:
    """k = 308*m. Return True iff no divisor d >= SMALL of k has d+1
    prime. (Divisors < SMALL were already handled by the sieve.)"""
    # factorize k = 2^2 * 7 * 11 * m
    primes = np.empty(20, dtype=np.int64)
    exps = np.empty(20, dtype=np.int64)
    primes[0], exps[0] = 2, 2
    primes[1], exps[1] = 7, 1
    primes[2], exps[2] = 11, 1
    npr = 3
    mm = m
    while mm > 1:
        p = spf[mm]
        found = False
        for i in range(npr):
            if primes[i] == p:
                exps[i] += 1
                found = True
                break
        if not found:
            primes[npr] = p
            exps[npr] = 1
            npr += 1
        mm //= p
    # enumerate divisors
    ndiv = 1
    for i in range(npr):
        ndiv *= exps[i] + 1
    divs = np.empty(ndiv, dtype=np.int64)
    divs[0] = 1
    cnt = 1
    for i in range(npr):
        base_cnt = cnt
        pe = 1
        for _ in range(exps[i]):
            pe *= primes[i]
            for j in range(base_cnt):
                divs[cnt] = divs[j] * pe
                cnt += 1
    for i in range(ndiv):
        d = divs[i]
        if d >= SMALL and is_prime(d + 1):
            return False
    return True


def find_f(target: int) -> int:
    m_max = 4_000_000
    while True:
        small_primes = prime_sieve_int(SMALL)
        valid = _sieve_candidates(m_max, small_primes)
        spf = _spf_sieve(m_max)
        count = 0
        for m in np.flatnonzero(valid):
            if _check_large_divisors(int(m), spf):
                count += 1
                if count == target:
                    return BASE * int(m)
        m_max *= 2


if __name__ == "__main__":
    # verify a_1 = B_k against exact polynomial fits
    bern = bernoulli(60)
    for k in range(1, 13):
        assert faulhaber_a1(k) == bern[k]
    # verify von Staudt-Clausen for even k up to 60
    small_primes = prime_sieve_int(SMALL)
    for k in range(2, 61, 2):
        assert bern[k].denominator == vsc_denominator(k, small_primes)
    assert bern[4].denominator == 30  # D(4) = 30
    assert bernoulli(308)[308].denominator == 20010  # D(308) = 20010
    assert find_f(1) == 308
    assert find_f(10) == 96404

    print(find_f(10**5))  # 921107572
