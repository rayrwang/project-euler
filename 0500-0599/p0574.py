"""
https://projecteuler.net/problem=574

For a prime q and coprime A >= B > 0 with AB divisible by every
prime below q, any A + B < q^2 and any difference 1 < A - B < q^2 is
prime. V(p) is the smallest A over all such certificates of p, and
S(n) sums V(p) over primes p < n. Find S(3800).

Enlarging q only adds divisibility requirements, so the minimum is
attained at the smallest prime q with q^2 > p. For a sum p = A + B
the gcd condition is automatic and each prime r < q must divide A or
p - A; A is found by scanning [p/2, p). Sums beat differences
whenever they exist since a difference has A = p + B > p. For a
difference, gcd(A, B) = gcd(p, B), so we need the smallest B >= 1
with p not dividing B and B = 0 or -p (mod r) for every odd prime
r < q (r = 2 is automatic for odd p as exactly one of B, B + p is
even).

That is a minimum-CRT problem over 2^17 residue classes for the
largest q = 67. Splitting the odd primes into halves with balanced
products M1, M2 < 2^40, each half's residues are enumerated by
iterative CRT, and for each pair x = x1 + M1 t with
t = (x2 - x1) M1^(-1) mod M2; minimising x is minimising (t, x1)
lexicographically, so everything stays in int64 (an exact 20-bit
split mulmod handles t), with the p | x exclusion checked modularly.

Verified against a direct B-scan up to twice the primorial for all
p < 525, the given V(2) = 1, V(37) = 22, V(151) = 165, and
S(10) = 10, S(200) = 7177.
"""

from math import isqrt

import numba
import numpy as np


def _sieve(n: int) -> list[int]:
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i :: i] = False
    return [int(x) for x in np.nonzero(s)[0]]


PRIMES = _sieve(100)


def _qmin(p: int) -> int:
    for q in PRIMES:
        if q * q > p:
            return q
    raise ValueError


@numba.njit(cache=True, inline="always")
def _mulmod(a: np.int64, b: np.int64, m: np.int64) -> np.int64:
    return (((a >> 20) * b % m << 20) + (a & 0xFFFFF) * b) % m


@numba.njit(cache=True)
def _pair_min(half1, half2, m1, m2, inv, p):
    best_t = np.int64(2**62)
    best_x1 = np.int64(0)
    m1p = m1 % p
    for i2 in range(half2.shape[0]):
        x2 = half2[i2]
        for i1 in range(half1.shape[0]):
            x1 = half1[i1]
            t = _mulmod((x2 - x1) % m2, inv, m2)
            if t > best_t or (t == best_t and x1 >= best_x1):
                continue
            if t == 0 and x1 == 0:
                continue
            if ((x1 % p) + m1p * (t % p)) % p == 0:
                continue
            best_t = t
            best_x1 = x1
    return best_t, best_x1


def _combos(primes_half: list[int], p: int) -> tuple[np.ndarray, int]:
    xs = [0]
    m = 1
    for r in primes_half:
        br = (-p) % r
        inv = pow(m, -1, r)
        xs = [
            x + m * (((v - x) * inv) % r) for x in xs for v in ({0, br} if br else {0})
        ]
        m *= r
    return np.array(sorted(xs), dtype=np.int64), m


def v_of(p: int) -> int:
    q = _qmin(p)
    pr = [r for r in PRIMES if r < q]
    for a in range((p + 1) // 2, p):  # sums first: any sum A < p < any diff A
        if all(a % r == 0 or (p - a) % r == 0 for r in pr):
            return a
    podd = [r for r in pr if r != 2]
    if not podd:
        return p + 1  # B = 1
    h1: list[int] = []
    h2: list[int] = []
    m1 = m2 = 1
    for r in sorted(podd, reverse=True):
        if m1 <= m2:
            h1.append(r)
            m1 *= r
        else:
            h2.append(r)
            m2 *= r
    half1, m1 = _combos(h1, p)
    half2, m2 = _combos(h2, p)
    t, x1 = _pair_min(half1, half2, m1, m2, pow(m1, -1, m2), p)
    b = int(x1) + m1 * int(t)
    assert 1 <= b < 2**62 and b % p
    return p + b


def _v_slow(p: int) -> int:
    q = _qmin(p)
    pr = [r for r in PRIMES if r < q]
    for a in range((p + 1) // 2, p):
        if all(a % r == 0 or (p - a) % r == 0 for r in pr):
            return a
    podd = [r for r in pr if r != 2]
    m = 1
    for r in podd:
        m *= r
    for b in range(1, 2 * m + 1):
        if b % p and all(b % r == 0 or (b + p) % r == 0 for r in podd):
            return p + b
    raise ValueError


if __name__ == "__main__":
    assert v_of(2) == 1 and v_of(37) == 22 and v_of(151) == 165  # given
    for p in _sieve(525):
        assert _v_slow(p) == v_of(p), p
    assert sum(v_of(p) for p in _sieve(9)) == 10  # given S(10)
    assert sum(v_of(p) for p in _sieve(199)) == 7177  # given S(200)

    print(sum(v_of(p) for p in _sieve(3799)))  # 5780447552057000454
