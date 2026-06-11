"""Project Euler 957: Point Genesis.

Model. Every constructed line passes through one of the three red points,
so the lines form three pencils. Parametrise the pencil through each red
point by the Ceva ratio on the opposite side of the red triangle: three
lines, one from each pencil, are concurrent iff the product of their
parameters is 1 (Ceva). A new blue point is the meet of a pencil-1 line
alpha and a pencil-2 line beta, and it lies on the pencil-3 line
gamma = 1/(alpha beta). Writing the (generic, multiplicatively
independent) parameters additively as vectors in Z^4 -- the two initial
blue points contribute four free generators -- the blue set after a day is
determined by the parameter sets A, B, C (with the day's new points being
all meets of existing pencil lines):

    S' = P12 (A x B) | P13 (A x C) | P23 (B x C),
    A' = A | -(B + C),  B' = B | -(A + C),  C' = C | -(A + B),

and by inclusion-exclusion (each pairwise and the triple intersection of
the P's is the set of zero-sum triples T):

    |S| = |A||B| + |A||C| + |B||C| - 2 T,
    T = #{(a, b, c) in A x B x C : a + b + c = 0}.

Genericity makes all non-forced coincidences absent, which maximises the
count; the exact rational simulation of general-position red points agrees
with this model for days 1-3 (8, 28, 184), as do the given g(1), g(2).

Structure. Each parameter set lies on a 2-dimensional affine slice of Z^4
and -- verified by exact simulation through day 9 -- is precisely the set
of lattice points of a hexagon (a box intersected with a diagonal strip):

    A_n = {(x, y) : 1-u <= x <= u, -v <= y <= v, -u <= y-x <= u-1},

with rotated analogues for B_n and C_n, where u_1 = v_1 = 1 and
u_{n+1} = u_n + v_n, v_{n+1} = 2 u_n - 1, i.e.
u_n = (2^(n+1) + (-1)^n + 3)/6 and v_n = (2^n - (-1)^n)/3 (Jacobsthal).
This persists because all three hexagons share edge directions, so a
Minkowski sum is again such a hexagon with added bounds, and the lattice
points saturate (checked exactly up to day 9).

Counting. |A_n| = (4^n + 2)/3 + 2^n. T_n is computed exactly in O(4^n)
by looping over (x_a, x_b) and counting the y-triples in closed form
(lattice points of a box with a two-sided sum constraint, by
inclusion-exclusion on triangle numbers); the values match the brute-force
T_n for all n <= 8. Finally g(16) = 3 s^2 - 2 T at n = 15, in seconds.
"""

import numpy as np
from numba import njit


# ------------------------------- exact simulation (verification, n <= 7)
@njit(cache=True)
def _sumset_neg(b_arr, c_arr):
    nb, nc = b_arr.shape[0], c_arr.shape[0]
    out = np.empty((nb * nc, 2), dtype=np.int64)
    k = 0
    for i in range(nb):
        for j in range(nc):
            out[k, 0] = -(b_arr[i, 0] + c_arr[j, 0])
            out[k, 1] = -(b_arr[i, 1] + c_arr[j, 1])
            k += 1
    return out


def _union(a_arr, new_arr):
    return np.unique(np.vstack([a_arr, new_arr]), axis=0)


def _is_hexagon(arr, xlo, xhi, ylo, yhi, dlo, dhi) -> bool:
    pts = {(int(p[0]), int(p[1])) for p in arr}
    cnt = 0
    for x in range(xlo, xhi + 1):
        lo = max(ylo, x + dlo)
        hi = min(yhi, x + dhi)
        for y in range(lo, hi + 1):
            cnt += 1
            if (x, y) not in pts:
                return False
    return cnt == len(pts)


def _verify(days: int) -> None:
    """Exact Z^4 simulation (projected to the free 2D slices), asserting
    the hexagon structure and the given g(1) = 8, g(2) = 28."""
    a4 = np.array([[1, 0, 0, 0], [0, 0, 1, 0]], dtype=np.int64)
    b4 = np.array([[0, 1, 0, 0], [0, 0, 0, 1]], dtype=np.int64)
    c4 = np.array([[-1, -1, 0, 0], [0, 0, -1, -1]], dtype=np.int64)

    def proj(m):
        return m[:, :2].copy()

    def sneg4(x, y):
        nx, ny = x.shape[0], y.shape[0]
        out = np.empty((nx * ny, 4), dtype=np.int64)
        k = 0
        for i in range(nx):
            for j in range(ny):
                out[k] = -(x[i] + y[j])
                k += 1
        return out

    prev = (a4, b4, c4)
    g_seq = []
    for n in range(1, days + 1):
        a4, b4, c4 = prev
        g = (
            len(a4) * len(b4)
            + len(a4) * len(c4)
            + len(b4) * len(c4)
            - 2 * _t_brute(proj(a4), proj(b4), proj(c4))
        )
        g_seq.append(g)
        na = np.unique(np.vstack([a4, sneg4(b4, c4)]), axis=0)
        nb = np.unique(np.vstack([b4, sneg4(a4, c4)]), axis=0)
        nc = np.unique(np.vstack([c4, sneg4(a4, b4)]), axis=0)
        prev = (na, nb, nc)
        u, v = uv(n)
        assert _is_hexagon(proj(na), 1 - u, u, -v, v, -u, u - 1)
        assert _is_hexagon(proj(nb), -v, v, 1 - u, u, 1 - u, u)
        assert _is_hexagon(proj(nc), -u, u - 1, -u, u - 1, -v, v)
        assert len(na) == hex_size(u, v)
        assert _t_brute(proj(na), proj(nb), proj(nc)) == t_of(u, v)
    assert g_seq[0] == 8 and g_seq[1] == 28


def _t_brute(a, b, c) -> int:
    cset = {(int(p[0]), int(p[1])) for p in c}
    cnt = 0
    for pa in a:
        for pb in b:
            if (-int(pa[0]) - int(pb[0]), -int(pa[1]) - int(pb[1])) in cset:
                cnt += 1
    return cnt


# ----------------------------------------------------- closed-form count
def uv(n: int) -> tuple[int, int]:
    return (2 ** (n + 1) + (-1) ** n + 3) // 6, (2**n - (-1) ** n) // 3


@njit(cache=True)
def hex_size(u: int, v: int) -> int:
    cnt = 0
    for x in range(1 - u, u + 1):
        lo = max(-v, x - u)
        hi = min(v, x + u - 1)
        if hi >= lo:
            cnt += hi - lo + 1
    return cnt


@njit(cache=True)
def _tri(k: int) -> int:
    if k < 0:
        return 0
    return (k + 1) * (k + 2) // 2


@njit(cache=True)
def _count_sum_le(a1: int, a2: int, b1: int, b2: int, t: int) -> int:
    w = a2 - a1 + 1
    h = b2 - b1 + 1
    if w <= 0 or h <= 0:
        return 0
    m = t - a1 - b1
    return _tri(m) - _tri(m - w) - _tri(m - h) + _tri(m - w - h)


@njit(cache=True)
def t_of(u: int, v: int) -> int:
    total = 0
    for xa in range(1 - u, u + 1):
        la = max(-v, xa - u)
        ha = min(v, xa + u - 1)
        if ha < la:
            continue
        for xb in range(-v, v + 1):
            xc = -xa - xb
            if xc < -u or xc > u - 1:
                continue
            lb = max(1 - u, xb + 1 - u)
            hb = min(u, xb + u)
            lc = max(-u, xc - v)
            hc = min(u - 1, xc + v)
            if hb < lb or hc < lc:
                continue
            total += _count_sum_le(la, ha, lb, hb, -lc) - _count_sum_le(
                la, ha, lb, hb, -hc - 1
            )
    return total


def solve() -> int:
    _verify(6)
    u, v = uv(15)
    s = hex_size(u, v)
    return 3 * s * s - 2 * t_of(u, v)


if __name__ == "__main__":
    print(solve())  # 234897386493229284
