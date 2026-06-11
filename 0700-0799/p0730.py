from itertools import combinations
from math import gcd, isqrt

import numba
import numpy as np

# Write d = r - q >= 1 and e = r + q, so a k-shifted triple is exactly
# d*e = p^2 + k with d = e (mod 2), q = (e - d)/2 >= p and perimeter
# p + e <= n.  For a fixed d the divisor condition says p^2 = -k (mod d)
# (plus, exactly, 2d | p^2 + k when d is even, and p^2 + k odd when d is
# odd), so the valid p form arithmetic progressions; the bounds are
# p^2 + d p <= n d - k (perimeter) and p^2 - 2 d p + k - d^2 >= 0 (q >= p,
# a parabola giving [1, d - t] u [d + t, ...] with t = ceil(sqrt(2d^2-k))).
# Counting p in those progressions is O(1) per pair (d, root).
#
# The pairs (d, rho) with rho^2 = -k (mod d), d <= n/8 + 2 are enumerated in
# O(#pairs) through binary quadratic forms: [d, 2 rho, (rho^2+k)/d] has
# discriminant -4k, so the pairs of content g (g^2 | 4k) correspond to
# primitive representations, modulo automorphisms, of d/g by the form
# classes of discriminant -4k/g^2.  Each class's representations are walked
# with Conway's topograph: from the well of the reduced form [a, b, c]
# (superbase values a, c, a - |b| + c, mirror-oriented when b < 0), crossing
# an edge between regions A, B away from third C discovers one new region
# C2 = 2(A + B) - C, whose root is (A - B - C2)/2 modulo C2 by the
# orientation rule; values only grow away from the well, so branches are cut
# at the bound.  Classes of discriminant -3 and -4 carry extra units and
# their region sums are divided by 3 and 2.  This enumeration was verified
# to reproduce the exact multiset {(d, rho)} for many k and bounds.
#
# A triple of gcd h needs h^2 | k and scales to a primitive (k/h^2)-shifted
# triple of perimeter <= n/h, so with T_k the count of all triples,
# P_k(n) = sum_(h^2 | k) mu(h) T_(k/h^2)(n/h), and k = 0 is the classical
# Euclid count of primitive Pythagorean triples.  Everything is checked
# against brute force for all k at n = 10^4 (including the given P_0, P_20
# and S(10, 10^4)) before the final run.

N = 10**8


@numba.njit(cache=True)
def brute_all(n, kmax):
    """P_k(n) for k = 0..kmax by direct enumeration (reference)."""
    res = np.zeros(kmax + 1, dtype=np.int64)
    for p in range(1, n // 3 + 1):
        for q in range(p, n + 1):
            m = p * p + q * q
            r = int(np.sqrt(m))
            while r * r < m:
                r += 1
            if p + q + r > n:
                break
            while True:
                k = r * r - m
                if k > kmax or p + q + r > n:
                    break
                if r >= q and np.gcd(np.gcd(p, q), r) == 1:
                    res[k] += 1
                r += 1
    return res


def euclid_p0(n):
    """Primitive Pythagorean triples with perimeter <= n."""
    cnt = 0
    m = 2
    while 2 * m * (m + 1) <= n:
        lim = min(m - 1, n // (2 * m) - m)
        if lim >= 1:
            mm, f, primes = m, 2, []
            while f * f <= mm:
                if mm % f == 0:
                    primes.append(f)
                    while mm % f == 0:
                        mm //= f
                f += 1
            if mm > 1:
                primes.append(mm)
            par = (m + 1) & 1
            for rr in range(len(primes) + 1):
                for comb in combinations(primes, rr):
                    d = 1
                    for x in comb:
                        d *= x
                    if d % 2 == 0:
                        c = lim // d if par == 0 else 0
                    else:
                        big = lim // d
                        c = (big + 1) // 2 if par == 1 else big // 2
                    cnt += (-1) ** rr * c
        m += 1
    return cnt


def reduced_forms(disc):
    res = []
    for a in range(1, isqrt(-disc // 3) + 2):
        for b in range(-a + 1, a + 1):
            if (b * b - disc) % (4 * a):
                continue
            c = (b * b - disc) // (4 * a)
            if c < a or (a == c and b < 0):
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            res.append((a, b, c))
    return res


@numba.njit(cache=True)
def isqrt_nb(x):
    r = np.int64(np.sqrt(x))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


@numba.njit(cache=True)
def ap_count(lo, hi, r0, step):
    if hi < lo:
        return 0
    a = (hi - r0) // step + 1 if hi >= r0 else 0
    b = (lo - 1 - r0) // step + 1 if lo - 1 >= r0 else 0
    return a - b


@numba.njit(cache=True)
def count_for_pair(d, rho, j, bound):
    """Valid p with p = rho (mod d) giving a triple of perimeter <= bound."""
    md = bound * d - j
    if md < 0:
        return 0
    p2 = (isqrt_nb(d * d + 4 * md) - d) // 2
    while p2 * p2 + d * p2 > md:
        p2 -= 1
    while (p2 + 1) * (p2 + 1) + d * (p2 + 1) <= md:
        p2 += 1
    if 2 * d * d <= j:
        p1 = np.int64(1)
        p0 = np.int64(0)
    else:
        s = isqrt_nb(2 * d * d - j)
        if s * s == 2 * d * d - j:
            p1, t = d + s, s
        else:
            p1, t = d + s + 1, s + 1
        p0 = min(d - t, p2)
    if d % 2 == 0:
        if (rho * rho + j) % (2 * d) != 0:
            return 0
        return ap_count(p1, p2, rho % d, d) + ap_count(1, p0, rho % d, d)
    tpar = (j + 1) & 1
    r0 = (rho if (rho & 1) == tpar else rho + d) % (2 * d)
    return ap_count(p1, p2, r0, 2 * d) + ap_count(1, p0, r0, 2 * d)


@numba.njit(cache=True)
def topo_class_sum(a, b, c, g, big_d, j, bound):
    """Sum of progression counts over the (d, rho) pairs of one form class."""
    dg = big_d // g
    total = np.int64(0)
    bb = b if b >= 0 else -b
    r0v = a - bb + c
    if b >= 0:
        x, y = a, c
    else:
        x, y = c, a
    if g * r0v <= big_d:
        total += count_for_pair(g * r0v, ((y - x - r0v) * g // 2) % (g * r0v), j, bound)
    if g * x <= big_d:
        total += count_for_pair(g * x, ((r0v - y - x) * g // 2) % (g * x), j, bound)
    if g * y <= big_d:
        total += count_for_pair(g * y, ((x - r0v - y) * g // 2) % (g * y), j, bound)
    cap = 9_000_000
    sa = np.empty(cap, dtype=np.int64)
    sb = np.empty(cap, dtype=np.int64)
    sc = np.empty(cap, dtype=np.int64)
    sa[0], sb[0], sc[0] = x, y, r0v
    sa[1], sb[1], sc[1] = y, r0v, x
    sa[2], sb[2], sc[2] = r0v, x, y
    sp = 3
    while sp > 0:
        sp -= 1
        aa, ab, ac = sa[sp], sb[sp], sc[sp]
        while True:
            c2 = 2 * (aa + ab) - ac
            if c2 > dg:
                break
            dd = g * c2
            total += count_for_pair(dd, ((aa - ab - c2) * g // 2) % dd, j, bound)
            sa[sp], sb[sp], sc[sp] = c2, ab, aa
            sp += 1
            if sp >= cap:
                return np.int64(-1)
            ac = ab
            ab = c2
    return total


def t_all(j, bound):
    """All j-shifted triples (j >= 1) with perimeter <= bound."""
    big_d = bound // 8 + 2
    total = 0
    g = 1
    while g * g <= 4 * j:
        if (4 * j) % (g * g) == 0:
            disc = -(4 * j) // (g * g)
            if (-disc) % 4 in (0, 3):
                w2 = 3 if disc == -3 else 2 if disc == -4 else 1
                for (a, b, c) in reduced_forms(disc):
                    sub = topo_class_sum(a, b, c, g, big_d, j, bound)
                    assert sub >= 0 and sub % w2 == 0
                    total += sub // w2
        g += 1
    return total


def p_k(k, n):
    if k == 0:
        return euclid_p0(n)
    total, h = 0, 1
    mu = {1: 1, 2: -1, 3: -1, 5: -1, 6: 1, 7: -1, 10: 1}
    while h * h <= k:
        if k % (h * h) == 0 and h in mu:
            total += mu[h] * t_all(k // (h * h), n // h)
        h += 1
    return total


if __name__ == "__main__":
    ref = brute_all(10**4, 100)
    assert ref[0] == 703 and ref[20] == 1979 and ref[:11].sum() == 10956
    assert all(p_k(k, 10**4) == ref[k] for k in range(101))

    s = euclid_p0(N)
    for h, mu in ((1, 1), (2, -1), (3, -1), (5, -1), (6, 1), (7, -1), (10, 1)):
        for j in range(1, 100 // (h * h) + 1):
            s += mu * t_all(j, N // h)
    print(s)  # 1315965924
