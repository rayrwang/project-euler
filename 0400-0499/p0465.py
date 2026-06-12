"""Project Euler 465: Polar Polygons.

P(n) counts polygons with integer vertices, |x|, |y| <= n, whose kernel
strictly contains the origin (counted as edge sets; collinear consecutive
vertices allowed). Find P(7^13) mod 1_000_000_007.

The origin lies strictly inside the kernel iff it is strictly left of
every directed edge line, i.e. cross(v_i, v_(i+1)) > 0 for all cyclically
consecutive vertices. Such a sequence advances in angle by less than pi
each step, winds exactly once (more would force self-intersection), and
hits each ray from the origin at most once. Hence a polar polygon is
exactly: a set of rays whose cyclic angular gaps are all < pi, plus an
independent choice of one lattice point on each chosen ray -- r_d = floor(
n / max(|p|, |q|)) choices for the primitive direction d = (p, q).

So P(n) = sum over gap-feasible ray sets of prod r_d. Complement: sets
with some gap >= pi lie in a closed half-plane; parametrizing by the ray
that starts the cluster gives sum_d r_d * prod over rays in the half-turn
(theta_d, theta_d + pi] of (1 + r_e), double-counting exactly the
antipodal pairs (corrected by (1/2) sum_d r_d^2, using r_(-d) = r_d).

The half-turn product collapses by the dihedral D4 symmetry. Splitting it
into two quarter turns, a 90-degree rotation shows both are equal, and
within a quarter turn the reflection (p, q) <-> (q, p) is mass-preserving
and order-reversing, so the partial octant products multiply back to the
full octant product F regardless of d: every direction sees the same
half-plane product (1+n)^4 F^4, where F = prod_(p>=2) (1 + floor(n/p))^
phi(p) over one open octant. Therefore

    P(n) = (1+n)^8 F^8 - 1 - (1+n)^4 F^4 S1 + S2 / 2,
    S1 = 8n + 8 sum phi(p) floor(n/p),
    S2 = 8n^2 + 8 sum phi(p) floor(n/p)^2,

verified to reproduce P(1), P(2), P(3) exactly by hand. All three
quantities reduce to totient sums Phi(x) at the quotient points of n,
computed with the standard O(n^(2/3)) recursion Phi(v) = v(v+1)/2 -
sum_(d>=2) Phi(v/d) (sieved up to 2.5 * 10^7, memoized above), tracked
mod 10^9+7 for the sums and mod 10^9+6 for the exponents of F (Fermat;
the code asserts no base vanishes mod the prime). A brute force over ray
subsets independently validates n = 1 and n = 2.
"""

from itertools import combinations
from math import atan2, gcd

import numpy as np
from numba import njit

MOD = 1_000_000_007
MODE = MOD - 1  # exponent modulus


@njit(cache=True)
def phi_sieve_prefix(k):
    phi = np.arange(k + 1, dtype=np.int64)
    for i in range(2, k + 1):
        if phi[i] == i:  # prime
            for j in range(i, k + 1, i):
                phi[j] -= phi[j] // i
    for i in range(1, k + 1):
        phi[i] += phi[i - 1]
    return phi  # phi[x] = Phi(x), exact in int64


@njit(cache=True)
def tri_mod(v, m):
    if v % 2 == 0:
        return ((v // 2) % m) * ((v + 1) % m) % m
    return (v % m) * (((v + 1) // 2) % m) % m


@njit(cache=True)
def solve(n, k):
    ps = phi_sieve_prefix(k)
    nq = 0
    i = 1
    while i <= n and n // i > k:
        nq = i
        i += 1
    big_m = np.zeros(nq + 1, np.int64)
    big_e = np.zeros(nq + 1, np.int64)
    for ii in range(nq, 0, -1):  # v ascending
        v = n // ii
        sm = tri_mod(v, MOD)
        se = tri_mod(v, MODE)
        d = np.int64(2)
        while d <= v:
            q = v // d
            d2 = v // q
            if q <= k:
                pm = ps[q] % MOD
                pe = ps[q] % MODE
            else:
                j = n // q
                pm = big_m[j]
                pe = big_e[j]
            sm = (sm - (d2 - d + 1) % MOD * pm) % MOD
            se = (se - (d2 - d + 1) % MODE * pe) % MODE
            d = d2 + 1
        big_m[ii] = sm
        big_e[ii] = se

    big_f = np.int64(1)
    sum_a = np.int64(0)  # sum phi(p) * floor(n/p)   mod MOD
    sum_b = np.int64(0)  # sum phi(p) * floor(n/p)^2 mod MOD
    p = np.int64(2)
    prev_m = ps[1] % MOD
    prev_e = ps[1] % MODE
    while p <= n:
        t = n // p
        p2 = n // t
        if p2 <= k:
            hm = ps[p2] % MOD
            he = ps[p2] % MODE
        else:
            j = n // p2
            hm = big_m[j]
            he = big_e[j]
        cm = (hm - prev_m) % MOD
        ce = (he - prev_e) % MODE
        base = (1 + t) % MOD
        assert base != 0  # Fermat exponent reduction requires nonzero base
        e = ce % MODE
        b = base
        r = np.int64(1)
        while e:
            if e & 1:
                r = r * b % MOD
            b = b * b % MOD
            e >>= 1
        big_f = big_f * r % MOD
        tm = t % MOD
        sum_a = (sum_a + cm * tm) % MOD
        sum_b = (sum_b + cm * (tm * tm % MOD)) % MOD
        prev_m, prev_e = hm, he
        p = p2 + 1

    nm = n % MOD
    s1 = (8 * nm + 8 * sum_a) % MOD
    s2 = (8 * nm * nm + 8 * sum_b) % MOD
    b1 = (1 + nm) % MOD
    b4 = b1 * b1 % MOD * (b1 * b1 % MOD) % MOD
    f4 = big_f * big_f % MOD * (big_f * big_f % MOD) % MOD
    total = b4 * b4 % MOD * (f4 * f4 % MOD) % MOD
    count1 = b4 * f4 % MOD * s1 % MOD
    inv2 = (MOD + 1) // 2
    return (total - 1 - count1 + s2 * inv2) % MOD


def brute(n):
    """Direct count over ray subsets (small n)."""
    dirs = []
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if (x or y) and gcd(abs(x), abs(y)) == 1:
                dirs.append((atan2(y, x), x, y, n // max(abs(x), abs(y))))
    dirs.sort()
    total = 0
    for sz in range(3, len(dirs) + 1):
        for sub in combinations(range(len(dirs)), sz):
            ok = True
            for a in range(sz):
                _, x1, y1, _ = dirs[sub[a]]
                _, x2, y2, _ = dirs[sub[(a + 1) % sz]]
                if x1 * y2 - y1 * x2 <= 0:
                    ok = False
                    break
            if ok:
                prod = 1
                for idx in sub:
                    prod *= dirs[idx][3]
                total += prod
    return total % MOD


if __name__ == "__main__":
    assert solve(1, 2) == brute(1) == 131
    assert solve(2, 2) == brute(2) == 1648531
    assert solve(3, 3) == 1099461296175 % MOD
    assert solve(343, 343) == 937293740
    print(solve(7**13, 25_000_000))  # 585965659
