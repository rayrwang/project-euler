"""Project Euler problem 579: Lattice Points in Lattice Cubes.

S(n) sums the lattice points contained in every lattice cube whose
vertices lie in [0, n]^3.  Find S(5000) mod 10^9.

Counting points in one cube: the three edge vectors e_i (mutually
orthogonal, length L) span a sublattice of determinant L^3, so the
half-open cube contains exactly L^3 points.  Adding the far faces, edges
and vertex, the closed cube holds points on a half-open k-face spanned by
a subset of edges; a half-open edge holds g_i = gcd(e_i) points and a
half-open face spanned by e_i, e_j holds gcd(e_i x e_j) = L g_k points
(the cross product is +-L e_k).  Altogether

    N = L^3 + (L + 1)(g_1 + g_2 + g_3) + 1,

which reproduces both worked examples (64 for the axis cube of side 3,
40 for the tilted one).

Enumerating cubes: an ordered right-handed edge triple is L/m times the
quaternion rotation matrix R(q) of a primitive quaternion q with norm
m = a^2+b^2+c^2+d^2, and content arguments show every cube is uniquely an
integer multiple g of a primitive cube (gcd of all nine entries 1), whose
side is necessarily odd: mod 2, an even side would force every row even.
A primitive cube of side l has exactly 24 right-handed matrices (8
corners x 3 cyclic orders); multiplying q on the right by the 48 binary
octahedral units shows precisely 8 of the corresponding 48 quaternions
have odd norm, all equal to l (Lipschitz units keep norm l; the
(1+-i)-type give norm 2l; Hurwitz units give all-odd quadruples of norm
4l).  So summing over all primitive quaternions with odd norm <= n and
dividing by 8 visits each primitive cube exactly once.

For each cube the bounding-box widths are the column abs-sums of the edge
matrix, the number of translates inside [0, n]^3 is the product of
(n - g w_c + 1), and an inner loop scales by g while g * max(w) <= n.
Everything is accumulated mod 8 * 10^9 (32-bit-split mulmod keeps int64
exact), and the final division by 8 is exact.

Verified: S(1), S(2), S(4), S(5), S(10) and S(50) against the given
values, plus a fully independent brute force for n = 2, 4, 5 that
enumerates orthogonal triples directly, deduplicates cubes by their
vertex sets, and counts interior points by testing every bounding-box
lattice point against the cube inequalities.
"""

import numpy as np
from numba import njit


def brute_s(n: int) -> int:
    """Independent check: enumerate all lattice cubes in [0, n]^3 directly."""
    from itertools import product

    rng = range(-n, n + 1)
    vecs = [np.array(v) for v in product(rng, rng, rng) if v != (0, 0, 0)]
    by_norm: dict[int, list[np.ndarray]] = {}
    for v in vecs:
        by_norm.setdefault(int(v @ v), []).append(v)
    cubes = set()
    for l2, vs in by_norm.items():
        side = int(round(l2**0.5))
        if side * side != l2:
            continue
        for e1 in vs:
            for e2 in vs:
                if int(e1 @ e2) != 0:
                    continue
                e3 = np.cross(e1, e2)
                if any(x % side for x in e3):
                    continue
                e3 = e3 // side
                vts = [
                    s1 * e1 + s2 * e2 + s3 * e3
                    for s1 in (0, 1)
                    for s2 in (0, 1)
                    for s3 in (0, 1)
                ]
                arr = np.array(vts)
                arr = arr - arr.min(axis=0)
                cubes.add(tuple(sorted(map(tuple, arr))))
    total = 0
    for key in cubes:
        arr = np.array(key)
        w = arr.max(axis=0)
        if any(int(wi) > n for wi in w):
            continue
        d2 = ((arr - arr[0]) ** 2).sum(axis=1)
        order = np.argsort(d2)
        edges = [arr[order[t]] - arr[0] for t in (1, 2, 3)]
        l2 = int(d2[order[1]])
        assert int(d2[order[2]]) == l2 and int(d2[order[3]]) == l2
        cnt = 0
        for x in product(range(w[0] + 1), range(w[1] + 1), range(w[2] + 1)):
            p = np.array(x) - arr[0]
            if all(0 <= int(p @ ei) <= l2 for ei in edges):
                cnt += 1
        tr = 1
        for wi in w:
            tr *= n - int(wi) + 1
        total += tr * cnt
    return total


@njit(cache=True, inline="always")
def gcd3(a, b, c):
    a, b, c = abs(a), abs(b), abs(c)
    while b:
        a, b = b, a % b
    while c:
        a, c = c, a % c
    return a


@njit(cache=True, inline="always")
def gcd4(a, b, c, d):
    g = gcd3(a, b, c)
    d = abs(d)
    while d:
        g, d = d, g % d
    return g


@njit(cache=True, inline="always")
def mulmod(a, b, m):
    """a * b mod m, exact for a, b < 2^33."""
    b1, b0 = b >> 16, b & 0xFFFF
    return ((a * b1 % m) << 16) % m + a * b0 % m


@njit(cache=True)
def solve(n):
    mod8 = 8 * 10**9
    total = np.int64(0)
    amax = int(n**0.5) + 1
    for a in range(-amax, amax + 1):
        na = a * a
        if na > n:
            continue
        for b in range(-amax, amax + 1):
            nb = na + b * b
            if nb > n:
                continue
            for c in range(-amax, amax + 1):
                nc = nb + c * c
                if nc > n:
                    continue
                for d in range(-amax, amax + 1):
                    m = nc + d * d
                    if m > n or m % 2 == 0:
                        continue
                    if gcd4(a, b, c, d) != 1:
                        continue
                    r11 = a * a + b * b - c * c - d * d
                    r12 = 2 * (b * c - a * d)
                    r13 = 2 * (b * d + a * c)
                    r21 = 2 * (b * c + a * d)
                    r22 = a * a - b * b + c * c - d * d
                    r23 = 2 * (c * d - a * b)
                    r31 = 2 * (b * d - a * c)
                    r32 = 2 * (c * d + a * b)
                    r33 = a * a - b * b - c * c + d * d
                    w0 = abs(r11) + abs(r21) + abs(r31)
                    w1 = abs(r12) + abs(r22) + abs(r32)
                    w2 = abs(r13) + abs(r23) + abs(r33)
                    wm = max(w0, w1, w2)
                    if wm > n:
                        continue
                    gg = gcd3(r11, r12, r13) + gcd3(r21, r22, r23) + gcd3(r31, r32, r33)
                    for g in range(1, n // wm + 1):
                        side = g * m
                        t = np.int64(n - g * w0 + 1) * (n - g * w1 + 1) % mod8
                        t = mulmod(t, np.int64(n - g * w2 + 1), mod8)
                        npts = (
                            mulmod(np.int64(side) * side % mod8, np.int64(side), mod8)
                            + np.int64(side + 1) * (g * gg)
                            + 1
                        ) % mod8
                        total = (total + mulmod(t, npts, mod8)) % mod8
    assert total % 8 == 0
    return (total // 8) % 10**9


def main() -> None:
    for nn, want in [(1, 8), (2, 91), (4, 1878), (5, 5832), (10, 387003)]:
        assert solve(nn) == want, nn  # given
    assert solve(50) == 29948928129 % 10**9  # given
    for nn in (2, 4, 5):
        assert brute_s(nn) == solve(nn), nn  # independent enumeration

    print(solve(5000))  # 3805524


if __name__ == "__main__":
    main()
