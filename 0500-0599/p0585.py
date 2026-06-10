"""
https://projecteuler.net/problem=585

F(n) counts distinct values sqrt(x + sqrt(y) + sqrt(z)) (x <= n; y, z
positive non-squares) that denest into a finite +-combination of
square roots of integers. Find F(5 * 10^6).

Structure of denestings. If kappa = sum s_i sqrt(a_i) then kappa^2
has even coefficients on every surd class, so the value
V = x + sqrt(y) + sqrt(z) determines kappa = sqrt(V) > 0 uniquely
and distinct values correspond to distinct kappa. A Galois argument
pins down kappa: every automorphism of the multiquadratic closure
fixing Q(sqrt(D1), sqrt(D2)) (the field of V) sends kappa to
+-kappa, so kappa = sqrt(rho) * mu with mu in the quadruple field -
kappa has at most four surd components whose cores form a coset of a
Klein group. Three components force three surd classes in kappa^2,
so kappa is either

  family 1:  kappa = sqrt(A) + sqrt(B), giving V = (A+B) + 2 sqrt(AB)
             (one surd class; requires AB non-square), or
  family 2:  kappa = +-sqrt(p1) +- sqrt(q1) +- sqrt(p2) +- sqrt(q2)
             with four pairwise distinct cores and p1 q1 = p2 q2
             (this kills exactly one of the three surd classes of
             kappa^2 - two cannot vanish, by applying the
             automorphism negating the surviving class - and the
             sign pattern is forced up to the global sign).

F1(n) counts unordered {A, B} with A + B <= n minus the square
products A = kappa a^2, B = kappa b^2 (kappa squarefree), i.e.
sum_x floor(x/2) - sum_(kappa squarefree) Q(floor(n/kappa)) with
Q(M) = #{a >= b >= 1 : a^2 + b^2 <= M}.

F2(n) counts the family-2 configurations: all orbits of the ordered
tuples (p1, q1, p2, q2) under the 8 relabelings are free (fixed
points need equal cores), so F2 = (ordered count)/8. The classical
bijection p1 = ef, q1 = gh, p2 = eh, q2 = gf with gcd(f, h) = 1
turns p1 q1 = p2 q2 into sum = (e+g)(f+h), so the unconstrained
ordered count is sum_t phi(t) * B(floor(n/t)) with B(M) = M(M-1)/2.
Core collisions come in three patterns, each equivalent to a single
group relation: (I) core(p1) = core(q1) <=> efgh square,
(II) core(p1) = core(p2) <=> f, h both squares,
(III) core(p1) = core(q2) (same count as II by swapping p2 and q2),
and any two patterns force all four cores equal (E); so
bad = I + II + III - 2E. II = sum over coprime (F, H) of
B(floor(n/(F^2+H^2))); E = sum over coprime (F, H) of
R(floor(n/(F^2+H^2))) with R(M) = sum_(x^2+y^2 <= M)
SF(floor(M/(x^2+y^2))) (SF = squarefree counts); and I is summed per
m over the decompositions p1 = kappa a^2, q1 = kappa b^2 with
kappa a b = m, weight kappa(a^2+b^2), counting weight pairs
s1 + s2 <= n by sort + two-pointer (m <= n/4 since s >= 2m).

Verified against a literal brute force over ordered tuples with core
tests for n <= 30 and all the given values F(10) = 17, F(15) = 46,
F(20) = 86, F(30) = 213, F(100) = 2918, F(5000) = 11134074.
"""

from math import isqrt

import numba
import numpy as np


@numba.njit(cache=True, inline="always")
def _isq(x: np.int64) -> np.int64:
    if x < 0:
        return np.int64(-1)
    r = np.int64(np.sqrt(x))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


@numba.njit(cache=True)
def _phi_sieve(n: int) -> np.ndarray:
    phi = np.arange(n + 1, dtype=np.int64)
    for p in range(2, n + 1):
        if phi[p] == p:
            for j in range(p, n + 1, p):
                phi[j] -= phi[j] // p
    return phi


@numba.njit(cache=True)
def _sqfree_sieve(n: int) -> tuple[np.ndarray, np.ndarray]:
    sf = np.ones(n + 1, dtype=np.int8)
    d = 2
    while d * d <= n:
        for j in range(d * d, n + 1, d * d):
            sf[j] = 0
        d += 1
    cum = np.zeros(n + 1, dtype=np.int64)
    s = np.int64(0)
    for i in range(1, n + 1):
        s += sf[i]
        cum[i] = s
    return sf, cum


@numba.njit(cache=True)
def _f1(n: int, sf: np.ndarray) -> np.int64:
    tot = np.int64(0)
    for x in range(2, n + 1):
        tot += x // 2
    sub = np.int64(0)
    for g in range(1, n // 2 + 1):
        if not sf[g]:
            continue
        m = n // g
        b = 1
        while 2 * b * b <= m:
            sub += _isq(m - b * b) - b + 1
            b += 1
    return tot - sub


@numba.njit(cache=True)
def _n_ordered(n: int, phi: np.ndarray) -> np.int64:
    tot = np.int64(0)
    for t in range(2, n // 2 + 1):
        m = n // t
        tot += phi[t] * (m * (m - 1) // 2)
    return tot


@numba.njit(cache=True)
def _count_ii(n: int) -> np.int64:
    tot = np.int64(0)
    f = 1
    while f * f + 1 <= n:
        h = 1
        while f * f + h * h <= n:
            a, b = f, h
            while b:
                a, b = b, a % b
            if a == 1:
                m = n // (f * f + h * h)
                tot += m * (m - 1) // 2
            h += 1
        f += 1
    return tot


@numba.njit(cache=True)
def _count_e(n: int, sfcum: np.ndarray) -> np.int64:
    tot = np.int64(0)
    f = 1
    while f * f + 1 <= n:
        h = 1
        while f * f + h * h <= n:
            a, b = f, h
            while b:
                a, b = b, a % b
            if a == 1:
                m = n // (f * f + h * h)
                x = 1
                while x * x + 1 <= m:
                    y = 1
                    while x * x + y * y <= m:
                        tot += sfcum[m // (x * x + y * y)]
                        y += 1
                    x += 1
            h += 1
        f += 1
    return tot


@numba.njit(cache=True)
def _count_i(n: int, sf: np.ndarray) -> np.int64:
    mmax = n // 4
    cnt = np.zeros(mmax + 2, dtype=np.int64)
    for k in range(1, mmax + 1):
        if not sf[k]:
            continue
        a = 1
        while k * a <= mmax and k * (a * a + 1) <= n:
            bh = min(mmax // (k * a), _isq(n // k - a * a))
            for b in range(1, bh + 1):
                cnt[k * a * b] += 1
            a += 1
    off = np.zeros(mmax + 2, dtype=np.int64)
    for m in range(1, mmax + 1):
        off[m + 1] = off[m] + cnt[m]
    sums = np.zeros(off[mmax + 1], dtype=np.int64)
    fill = off.copy()
    for k in range(1, mmax + 1):
        if not sf[k]:
            continue
        a = 1
        while k * a <= mmax and k * (a * a + 1) <= n:
            bh = min(mmax // (k * a), _isq(n // k - a * a))
            for b in range(1, bh + 1):
                m = k * a * b
                sums[fill[m]] = k * (a * a + b * b)
                fill[m] += 1
            a += 1
    tot = np.int64(0)
    for m in range(1, mmax + 1):
        lo, hi = off[m], off[m + 1]
        if hi == lo:
            continue
        seg = np.sort(sums[lo:hi])
        j = hi - lo - 1
        for i in range(hi - lo):
            while j >= 0 and seg[i] + seg[j] > n:
                j -= 1
            if j < 0:
                break
            tot += j + 1
    return tot


def f_of(n: int, phi: np.ndarray, sf: np.ndarray, sfcum: np.ndarray) -> int:
    f2o = (
        _n_ordered(n, phi) - _count_i(n, sf) - 2 * _count_ii(n) + 2 * _count_e(n, sfcum)
    )
    assert f2o % 8 == 0
    return int(_f1(n, sf)) + int(f2o) // 8


def _core(x: int) -> int:
    c, d = 1, 2
    while d * d <= x:
        e = 0
        while x % d == 0:
            x //= d
            e ^= 1
        if e:
            c *= d
        d += 1
    return c * x


def _brute_f(n: int) -> int:
    f1 = sum(
        1
        for a in range(1, n)
        for b in range(1, min(a, n - a) + 1)
        if isqrt(a * b) ** 2 != a * b
    )
    f2o = 0
    for p1 in range(1, n):
        for q1 in range(1, n - p1 + 1):
            m = p1 * q1
            for p2 in range(1, n - p1 - q1 + 1):
                if m % p2:
                    continue
                q2 = m // p2
                if p1 + q1 + p2 + q2 <= n:
                    cs = {_core(p1), _core(q1), _core(p2), _core(q2)}
                    f2o += len(cs) == 4
    assert f2o % 8 == 0
    return f1 + f2o // 8


if __name__ == "__main__":
    n_target = 5_000_000
    phi = _phi_sieve(n_target)
    sf, sfcum = _sqfree_sieve(n_target)
    for n, expect in ((10, 17), (15, 46), (20, 86), (30, 213)):
        assert _brute_f(n) == expect == f_of(n, phi, sf, sfcum), n  # given
    assert f_of(100, phi, sf, sfcum) == 2918  # given
    assert f_of(5000, phi, sf, sfcum) == 11134074  # given

    print(f_of(n_target, phi, sf, sfcum))  # 17714439395932
