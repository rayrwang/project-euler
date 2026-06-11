"""
Project Euler Problem 785: Symmetric Diophantine Equation
https://projecteuler.net/problem=785

Sum x + y + z over all solutions of 15(x^2 + y^2 + z^2) = 34(xy + yz + zx)
with 1 <= x <= y <= z <= N = 10^9 and gcd(x, y, z) = 1.

A conic.  The equation is a projective conic with rational point
P0 = (1, 7, 16).  Intersecting lines through P0 with the line z = 0
parametrises every rational point: with R = (m, n, 0), the second
intersection of the line P0 R with the conic is Q(R) P0 - B(P0, R) R where
B is the polar bilinear form, giving

    x = 767 m^2 + 334 mn +  15 n^2
    y = 105 m^2 + 514 mn + 473 n^2
    z = 240 m^2 - 544 mn + 240 n^2.

Every primitive solution equals this triple divided by its content g at a
unique primitive parameter +-(m, n) (the inverse map is the linear
(m : n) = (z - 16x : 7z - 16y)).  Since x <= y <= z forces x, y, z
pairwise distinct here (x = y has no rational solution), each unordered
solution corresponds to exactly one parameter, so no deduplication is
needed.

Content.  g is supported on the primes 2 and 19: an odd prime q divides
all three values only if q divides both B(P0, R) = -16(47m + 23n) and
Q(R) = 15m^2 - 34mn + 15n^2, whose resultant is 77824 = 2^12 * 19.  The
parameters of content divisible by q lie in O(1) projective residue
classes mod q (the "bad" residues where all three forms vanish).  Each bad
class is an index-q sublattice; rewriting the forms in a basis of that
sublattice makes all coefficients divisible by q, and dividing by q yields
a new parametrisation of the same conic covering exactly those solutions.
Recursing (2-classes may refine by 2 or 19; 19-classes only by 19, so each
parameter's content is peeled off in canonical order and counted once)
builds a finite tree: the three forms have no common root over any field,
so the q-adic valuation of the content at primitive parameters is bounded
and chains die out.  Sublattices whose basis matrix entries share a common
factor contain no primitive parameters at all and are pruned; without that
pruning a vacuous period-two 2-adic chain recurs forever.  The tree has
764 nodes and does not depend on N.

Enumeration.  x + y + z = 8(139 m^2 + 38 mn + 91 n^2) is positive
definite, and valid triples have x + y + z <= 3N, so each node only needs
the lattice points of an ellipse containing about 0.01 N points (the
discriminant of the sum form is invariant, so the ellipse has the same
area at every node).  For each point, evaluate x, y, z incrementally,
keep it if 0 < x <= y <= z <= N, the original (m, n) is primitive and the
value gcd is 1.  Verified against a brute-force search for N = 3000.
"""

import numpy as np
from numba import njit, prange

N = 10**9

# x, y, z forms and the parameters-to-original transform of the root node
ROOT = ((767, 334, 15), (105, 514, 473), (240, -544, 240))


def evf(f, m, n):
    return f[0] * m * m + f[1] * m * n + f[2] * n * n


def transform(f, p, r, s, t):
    """Coefficients of f after (m, n) = (p u + r v, s u + t v)."""
    a, b, c = f
    return (
        a * p * p + b * p * s + c * s * s,
        2 * a * p * r + b * (p * t + r * s) + 2 * c * s * t,
        a * r * r + b * r * t + c * t * t,
    )


def reduce_basis(forms, mat):
    """Gauss-reduce the basis with respect to the (definite) sum form."""
    while True:
        a, b, c = (sum(f[i] for f in forms) for i in range(3))
        if a > c:
            forms = [(f[2], -f[1], f[0]) for f in forms]
            mat = (mat[0][1], -mat[0][0]), (mat[1][1], -mat[1][0])
            continue
        if abs(b) > a:
            k = -round(b / (2 * a))
            if k:  # (u, v) = (u' + k v', v') sends b to b + 2ak
                forms = [transform(f, 1, k, 0, 1) for f in forms]
                mat = (
                    (mat[0][0], mat[0][0] * k + mat[0][1]),
                    (mat[1][0], mat[1][0] * k + mat[1][1]),
                )
                continue
        return forms, mat


def build_nodes():
    from math import gcd

    nodes = []
    stack = [(list(ROOT), ((1, 0), (0, 1)), True)]
    while stack:
        forms, mat, allow2 = stack.pop()
        forms, mat = reduce_basis(forms, mat)
        nodes.append((forms, mat))
        for q, child_allow2 in ((2, allow2), (19, False)):
            if q == 2 and not allow2:
                continue
            residues = [(1, j) for j in range(q)] + [(0, 1)]
            for ru, rv in residues:
                if any(evf(f, ru, rv) % q for f in forms):
                    continue  # not a bad residue
                if ru % q:
                    p_, s_, r_, t_ = ru, rv, 0, q
                else:
                    p_, s_, r_, t_ = q, 0, ru, rv
                nf = [transform(f, p_, r_, s_, t_) for f in forms]
                if any(co % q for f in nf for co in f):
                    continue
                nf = [tuple(co // q for co in f) for f in nf]
                nm = (
                    (mat[0][0] * p_ + mat[0][1] * s_, mat[0][0] * r_ + mat[0][1] * t_),
                    (mat[1][0] * p_ + mat[1][1] * s_, mat[1][0] * r_ + mat[1][1] * t_),
                )
                if (
                    gcd(
                        gcd(abs(nm[0][0]), abs(nm[0][1])),
                        gcd(abs(nm[1][0]), abs(nm[1][1])),
                    )
                    != 1
                ):
                    continue  # sublattice holds no primitive (m, n)
                stack.append((nf, nm, child_allow2))
    return nodes


@njit(cache=True)
def gcd64(a, b):
    while b:
        a, b = b, a % b
    return a


@njit(cache=True)
def node_sweep(coefs, mats, k, n_limit):
    """Sum x + y + z and count valid triples found at node k."""
    lim = 3 * n_limit
    ax, bx, cx = coefs[k, 0], coefs[k, 1], coefs[k, 2]
    ay, by, cy = coefs[k, 3], coefs[k, 4], coefs[k, 5]
    az, bz, cz = coefs[k, 6], coefs[k, 7], coefs[k, 8]
    sa, sb, sc = ax + ay + az, bx + by + bz, cx + cy + cz
    m11, m12, m21, m22 = mats[k, 0], mats[k, 1], mats[k, 2], mats[k, 3]
    total = np.int64(0)
    cnt = np.int64(0)
    # largest u with a non-empty row: sa u^2 - sb^2 u^2 / (4 sc) <= lim
    umax = np.int64(np.sqrt(4.0 * sc * lim / (4.0 * sa * sc - np.float64(sb) * sb))) + 2
    for u in range(umax + 1):
        disc = sb * sb * u * u - 4 * sc * (sa * u * u - lim)
        if disc < 0:
            continue
        sq = np.int64(np.sqrt(np.float64(disc)))
        while sq * sq > disc:
            sq -= 1
        while (sq + 1) * (sq + 1) <= disc:
            sq += 1
        vlo = (-sb * u - sq) // (2 * sc)
        vhi = (-sb * u + sq) // (2 * sc) + 1
        if u == 0 and vlo < 1:
            vlo = np.int64(1)
        if vlo > vhi:
            continue
        v = vlo
        x = ax * u * u + bx * u * v + cx * v * v
        y = ay * u * u + by * u * v + cy * v * v
        z = az * u * u + bz * u * v + cz * v * v
        dx = bx * u + cx * (2 * v + 1)
        dy = by * u + cy * (2 * v + 1)
        dz = bz * u + cz * (2 * v + 1)
        m = m11 * u + m12 * v
        n = m21 * u + m22 * v
        while v <= vhi:
            if 0 < x <= y <= z <= n_limit:
                if gcd64(abs(m), abs(n)) == 1:
                    if gcd64(gcd64(x, y), z) == 1:
                        total += x + y + z
                        cnt += 1
            x += dx
            y += dy
            z += dz
            dx += 2 * cx
            dy += 2 * cy
            dz += 2 * cz
            m += m12
            n += m22
            v += 1
    return total, cnt


@njit(cache=True, parallel=True)
def sweep(coefs, mats, n_limit):
    nn = coefs.shape[0]
    totals = np.zeros(nn, dtype=np.int64)
    counts = np.zeros(nn, dtype=np.int64)
    for k in prange(nn):  # ty: ignore[not-iterable]
        t, c = node_sweep(coefs, mats, k, n_limit)
        totals[k] = t
        counts[k] = c
    return totals.sum(), counts.sum()


def solve(n_limit, packed=None):
    if packed is None:
        packed = pack_nodes()
    coefs, mats = packed
    total, _ = sweep(coefs, mats, n_limit)
    return int(total)


def pack_nodes():
    nodes = build_nodes()
    coefs = np.array(
        [[c for f in forms for c in f] for forms, _ in nodes], dtype=np.int64
    )
    mats = np.array(
        [[m[0][0], m[0][1], m[1][0], m[1][1]] for _, m in nodes],
        dtype=np.int64,
    )
    return coefs, mats


def main():
    packed = pack_nodes()
    assert solve(100, packed) == 184  # the three given solutions
    assert solve(3000, packed) == 264368  # brute-force verified
    return solve(N, packed)


if __name__ == "__main__":
    print(main())  # 29526986315080920
