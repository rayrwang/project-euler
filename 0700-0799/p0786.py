"""
Project Euler Problem 786: Billiard
https://projecteuler.net/problem=786

A billiard ball leaves corner A of a kite-shaped table (angles 120, 90,
60, 90 degrees at A, B, C, D; AB = AD) and returns to A after at most N
bounces, never touching a corner mid-trace.  B(10) = 6, B(100) = 478,
B(1000) = 45790; find B(10^9).

Unfolding.  The kite is two 30-60-90 triangles glued along the diagonal
AC, and that triangle has angles pi/3, pi/2, pi/6, so its reflections
tile the plane: the (2, 3, 6) tiling, i.e. side-2 hexagons each cut into
12 triangles by the spokes to their vertices and the apothems to their
edge midpoints.  A-images are the hexagon vertices, C-images the
centres, B- and D-images the edge midpoints.  Every hypotenuse (an AC
edge) is interior to exactly one triangle pair, so the plane carries a
canonical kite decomposition and a billiard trace develops into a
straight ray from A.  In integer coordinates (p, q) for the real point
(p/2, q sqrt(3)/2), a direction is a primitive (a, b) with 0 < |b| < a
(the open 120-degree wedge), the trace is valid exactly when the first
lattice vertex on the ray is an A-image, and the bounce count is the
number of crossed edges that are not spokes.

The arithmetic of traces.  The vertex type of k(a, b) depends only on
the point modulo the translation lattice Z(6,2) + Z(0,4), so the class
of (a, b) mod 12 decides everything: an exact rational-arithmetic walker
over the triangle tiling (verified against B(10) and B(100)) shows the
first vertex is an A-image precisely when 3 | a, reached at the k-th
multiple with k = 2 if a, b are both odd, else 4.  The bounce counts fit
exactly piecewise-linear formulas, split by the 30-degree line a = 3b
where one mirror family changes crossing direction: with m = k/2 and
gamma = 4 if (a + b) mod 6 is 4 or 5, else 5,

    3 f(a, b) = m (3a + b) - gamma   if a >= 3b,
    3 f(a, b) = m (2a + 4b) - gamma  if a <= 3b,

verified against the walker for every primitive direction with a <= 130
and reproducing all three given values of B by direct enumeration.

Counting.  By the b <-> -b mirror symmetry, B(N) is twice the number of
primitive pairs with a = 3a', 1 <= b < 3a', 3 not dividing b,
gcd(a', b) = 1 and f <= N.  Moebius inversion over d = gcd removes the
coprimality; for fixed d the inequality reads 9x + y <= V or
6x + 4y <= V with V = floor((3N + gamma) / (m d)), so the inner count is
a sum over eight (parity of a', b mod 6) classes of lattice-point counts
in two triangles with both coordinates in arithmetic progressions --
each an O(log) Euclidean floor-sum.  Grouping d by the constant value
blocks of floor((3N + 4)/d) and floor((3N + 5)/d) needs the Mertens
function restricted to residues 1, 5, 2, 4 mod 6: writing M* and D for
the Moebius partial sums over n coprime to 6, plain and twisted by the
character n mod 6 -> +-1, both satisfy the usual O(N^(2/3))
sieve-plus-recursion (the twisted one with a bounded character sum), and
M_(1,5) = (M* +- D)/2 while even residues reduce by d = 2e to
M_2(x) = -M_1(x/2), M_4(x) = -M_5(x/2).  The whole computation takes
under a second and was cross-checked against brute-force counts up to
N = 10^4.
"""

import numpy as np
from numba import njit

N = 10**9


@njit(cache=True)
def floor_sum(n, a, b, m):
    """sum_{i=0}^{n-1} floor((a*i + b)/m) for m > 0 and any-sign a, b."""
    ans = 0
    if a < 0:
        a2 = a % m
        ans -= n * (n - 1) // 2 * ((a2 - a) // m)
        a = a2
    if b < 0:
        b2 = b % m
        ans -= n * ((b2 - b) // m)
        b = b2
    while True:
        if a >= m:
            ans += n * (n - 1) // 2 * (a // m)
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y = a * n + b
        if y < m:
            break
        n = y // m
        b = y % m
        m, a = a, m
    return ans


@njit(cache=True)
def sum_count_ap(x1, x2, xi, px, al, be, eta, py):
    """sum over x in [x1, x2] with x = xi mod px of
    #{1 <= y <= al*x + be : y = eta mod py}; needs al*x + be >= 0."""
    if x2 < x1:
        return 0
    xs = x1 + (xi - x1) % px
    if xs > x2:
        return 0
    n = (x2 - xs) // px + 1
    return floor_sum(n, al * px, al * xs + be - eta + py, py)


@njit(cache=True)
def region_counts(V, xi, px, eta, py):
    """Lattice points with x = xi (mod px), y = eta (mod py) in
    {1 <= y <= x, 9x + y <= V}  union  {x < y < 3x, 6x + 4y <= V}."""
    total = 0
    # region 1, split where min(x, V - 9x) switches
    x0 = V // 10
    total += sum_count_ap(1, x0, xi, px, 1, 0, eta, py)
    total += sum_count_ap(x0 + 1, (V - 1) // 9, xi, px, -9, V, eta, py)
    # region 2: count y <= upper minus y <= x, upper = min(3x-1, (V-6x)//4)
    x1 = (V + 4) // 18
    x2 = (V - 4) // 10
    total += sum_count_ap(1, x1, xi, px, 3, -1, eta, py)
    total -= sum_count_ap(1, x1, xi, px, 1, 0, eta, py)
    if x2 >= x1 + 1:
        xs = x1 + 1 + (xi - (x1 + 1)) % px
        if xs <= x2:
            n = (x2 - xs) // px + 1
            # floor((V-6x)/4) composed with the progression count
            total += floor_sum(n, -6 * px, V - 6 * xs + 4 * (py - eta), 4 * py)
            total -= floor_sum(n, px, xs - eta + py, py)
    return total


@njit(cache=True)
def sieve_class_mertens(limit):
    """Partial sums over n <= x coprime to 6 of mu(n) and mu(n)*chi(n),
    chi = +1 / -1 for n = 1 / 5 mod 6."""
    mu = np.zeros(limit + 1, dtype=np.int8)
    mu[1] = 1
    primes = np.empty(limit // 2 + 1, dtype=np.int64)
    npr = 0
    comp = np.zeros(limit + 1, dtype=np.uint8)
    for i in range(2, limit + 1):
        if not comp[i]:
            primes[npr] = i
            npr += 1
            mu[i] = -1
        for j in range(npr):
            p = primes[j]
            if i * p > limit:
                break
            comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    cms = np.zeros(limit + 1, dtype=np.int64)
    cdx = np.zeros(limit + 1, dtype=np.int64)
    for x in range(1, limit + 1):
        a = cms[x - 1]
        b = cdx[x - 1]
        r = x % 6
        if r == 1:
            a += mu[x]
            b += mu[x]
        elif r == 5:
            a += mu[x]
            b -= mu[x]
        cms[x] = a
        cdx[x] = b
    return cms, cdx


@njit(cache=True)
def _q6(y):
    if y <= 0:
        return 0
    r = y % 6
    return (y // 6) * 2 + (1 if r >= 1 else 0) + (1 if r >= 5 else 0)


@njit(cache=True)
def _schi(y):
    if y <= 0:
        return 0
    r = y % 6
    return (1 if r >= 1 else 0) - (1 if r >= 5 else 0)


@njit(cache=True)
def build_big(K, cms, cdx):
    """M*(K//i) and D(K//i) for all i, by the standard recursion."""
    limit = cms.shape[0] - 1
    imax = K // limit
    big_m = np.zeros(imax + 1, dtype=np.int64)
    big_d = np.zeros(imax + 1, dtype=np.int64)
    for i in range(imax, 0, -1):
        x = K // i
        rm = np.int64(1)
        rd = np.int64(1)
        e = np.int64(2)
        while e <= x:
            v = x // e
            e2 = x // v
            if v <= limit:
                mv, dv = cms[v], cdx[v]
            else:
                j = K // v
                mv, dv = big_m[j], big_d[j]
            rm -= (_q6(e2) - _q6(e - 1)) * mv
            rd -= (_schi(e2) - _schi(e - 1)) * dv
            e = e2 + 1
        big_m[i] = rm
        big_d[i] = rd
    return big_m, big_d


@njit(cache=True)
def count_traces(N, cms, cdx, K1, bm1, bd1, K2, bm2, bd2):
    """#{(a', b): 1 <= b < 3a', gcd(a', b) = 1, 3 not| b, f(3a', b) <= N}."""
    limit = cms.shape[0] - 1

    def lookup(x):
        if x <= limit:
            return cms[x], cdx[x]
        i = K1 // x
        if i < bm1.shape[0] and K1 // i == x:
            return bm1[i], bd1[i]
        i = K2 // x
        return bm2[i], bd2[i]

    def class_mertens(x):
        # Moebius partial sums over d = 1, 5, 2, 4 mod 6
        if x <= 0:
            return np.int64(0), np.int64(0), np.int64(0), np.int64(0)
        ms, dx = lookup(x)
        m1 = (ms + dx) // 2
        m5 = (ms - dx) // 2
        h = x // 2
        if h > 0:
            msh, dxh = lookup(h)
            m1h = (msh + dxh) // 2
            m5h = (msh - dxh) // 2
        else:
            m1h = np.int64(0)
            m5h = np.int64(0)
        return m1, m5, -m1h, -m5h

    dmax = K2 // 10
    total = np.int64(0)
    d = np.int64(1)
    p1 = p5 = p2 = p4 = np.int64(0)
    while d <= dmax:
        t4 = K1 // d
        t5 = K2 // d
        d2 = min(K1 // t4, K2 // t5)
        if d2 > dmax:
            d2 = dmax
        m1, m5, m2, m4 = class_mertens(d2)
        w1, w5, w2, w4 = m1 - p1, m5 - p5, m2 - p2, m4 - p4
        p1, p5, p2, p4 = m1, m5, m2, m4
        if w1 != 0 or w5 != 0:
            for xi_par in range(2):  # 1: a' odd, 0: a' even
                for vi in range(4):
                    v = (1, 2, 4, 5)[vi]
                    if xi_par == 1:
                        gp = 4 if v <= 2 else 5
                        m = 1 if v % 2 == 1 else 2
                    else:
                        gp = 4 if v >= 4 else 5
                        m = 2
                    V = (t4 if gp == 4 else t5) // m
                    if V < 10:
                        continue
                    xi = 1 if xi_par == 1 else 2
                    if w1 != 0:
                        total += w1 * region_counts(V, xi, 2, v, 6)
                    if w5 != 0:
                        eta = (5 * v) % 6
                        total += w5 * region_counts(V, xi, 2, eta, 6)
        if w2 != 0 or w4 != 0:
            for vi in range(2):
                v = (2, 4)[vi]
                gp = 4 if v >= 4 else 5
                V = (t4 if gp == 4 else t5) // 2
                if V >= 10:
                    if w2 != 0:
                        total += w2 * region_counts(V, 1, 1, (2 * v) % 3, 3)
                    if w4 != 0:
                        total += w4 * region_counts(V, 1, 1, v % 3, 3)
        d = d2 + 1
    return total


def bounce_total(n, limit=None):
    """B(n): traces from A back to A with at most n bounces."""
    if limit is None:
        limit = max(1000, int((3 * n) ** (2 / 3)) + 10)
    k1, k2 = 3 * n + 4, 3 * n + 5
    cms, cdx = sieve_class_mertens(limit)
    bm1, bd1 = build_big(k1, cms, cdx)
    bm2, bd2 = build_big(k2, cms, cdx)
    return 2 * int(count_traces(n, cms, cdx, k1, bm1, bd1, k2, bm2, bd2))


def main():
    assert bounce_total(10) == 6
    assert bounce_total(100) == 478
    assert bounce_total(1000) == 45790
    return bounce_total(N)


if __name__ == "__main__":
    print(main())  # 45594532839912702
