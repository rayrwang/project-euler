"""Project Euler problem 514: Geoboard Shapes.

Each point of the (N+1) x (N+1) lattice [0,N]^2 independently receives a
pin with probability p = 1/(N+1).  E(N) is the expected area of the convex
hull of the pins (zero if fewer than three pins or all collinear).
Compute E(100) rounded to five decimal places.

By the shoelace formula, the hull area is (1/2) sum cross(A, B) over the
directed counter-clockwise hull edges A -> B.  An ordered pair of pinned
points (A, B) is such an edge iff no pin lies strictly to the right of the
directed line AB and no pin lies on that line outside the closed segment
AB (pins on the open segment are allowed; degenerate all-collinear
configurations contribute pairs in both directions which cancel).  Hence

  E = sum over ordered pairs (A,B) of (1/2) cross(A,B) p^2 q^{r(A,B)},

with q = 1 - p and r = #(points strictly right) + #(points on the line
outside the segment).

Group pairs by primitive direction g = (B - A)/gcd and by line.  With the
left normal n = (-g_y, g_x), every point P on a line satisfies n.P = c and
cross(P, g) = -c, so the cross factor is constant per line.  If a line
holds k grid points (spaced by g, since g is primitive), the pairs at gap
m contribute m * (k - m) * q^{k-1-m} after summing cross over positions,
giving a per-line factor T(k) = sum_m m (k-m) q^{k-1-m}, and

  E = sum_g sum_lines -(1/2) c p^2 q^{cum} T(k),

where cum = #(grid points with n.P < c) counts the strictly-right points.
Per direction, the multiset of n.P values over the grid is a histogram
built in O(N^2), then swept in increasing order; with ~2.5e4 primitive
directions the total work is ~7e8 simple operations (under a second with
numba).

Verified against exact enumeration of all 2^((N+1)^2) pin subsets for
N = 1, 2, 3 and the given values E(1) = 0.18750, E(2) = 0.94335,
E(10) = 55.03013.
"""

import math

import numba
import numpy as np


def hull_area2(pts: list[tuple[int, int]]) -> int:
    """Twice the area of the convex hull of a set of lattice points."""
    spts = sorted(set(pts))
    if len(spts) < 3:
        return 0

    def cross(o: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower: list[tuple[int, int]] = []
    for pt in spts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], pt) <= 0:
            lower.pop()
        lower.append(pt)
    upper: list[tuple[int, int]] = []
    for pt in reversed(spts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], pt) <= 0:
            upper.pop()
        upper.append(pt)
    hull = lower[:-1] + upper[:-1]
    a2 = 0
    for i in range(len(hull)):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % len(hull)]
        a2 += x1 * y2 - x2 * y1
    return abs(a2)


def brute_e(n: int) -> float:
    """Exact E(n) by enumerating all pin subsets (tiny n only)."""
    pts = [(x, y) for x in range(n + 1) for y in range(n + 1)]
    m = len(pts)
    p = 1.0 / (n + 1)
    q = 1.0 - p
    total = 0.0
    for mask in range(1 << m):
        chosen = [pts[i] for i in range(m) if mask >> i & 1]
        k = len(chosen)
        if k < 3:
            continue
        a2 = hull_area2(chosen)
        if a2:
            total += 0.5 * a2 * p**k * q ** (m - k)
    return total


@numba.njit(cache=True)
def fast_e(n: int) -> float:
    """E(n) via the per-direction line decomposition."""
    p = 1.0 / (n + 1)
    q = 1.0 - p
    npts = (n + 1) * (n + 1)
    qpow = np.empty(npts + 1)
    qpow[0] = 1.0
    for i in range(1, npts + 1):
        qpow[i] = qpow[i - 1] * q
    tarr = np.zeros(n + 2)
    for k in range(2, n + 2):
        s = 0.0
        for m in range(1, k):
            s += m * (k - m) * qpow[k - 1 - m]
        tarr[k] = s
    hist = np.zeros(4 * n * n + 11, np.int64)
    acc = 0.0
    for gx in range(-n, n + 1):
        for gy in range(-n, n + 1):
            if (gx == 0 and gy == 0) or math.gcd(abs(gx), abs(gy)) != 1:
                continue
            a = -gy
            b = gx
            vmin = min(0, a * n) + min(0, b * n)
            vmax = max(0, a * n) + max(0, b * n)
            for x in range(n + 1):
                base = a * x - vmin
                for y in range(n + 1):
                    hist[base + b * y] += 1
            cum = 0
            dacc = 0.0
            for idx in range(vmax - vmin + 1):
                k = hist[idx]
                if k > 0:
                    if k >= 2:
                        dacc -= 0.5 * (idx + vmin) * qpow[cum] * tarr[k]
                    cum += k
                    hist[idx] = 0
            acc += dacc * p * p
    return acc


def main() -> None:
    for n in (1, 2, 3):
        assert abs(brute_e(n) - fast_e(n)) < 1e-9
    assert f"{fast_e(1):.5f}" == "0.18750"
    assert f"{fast_e(2):.5f}" == "0.94335"
    assert f"{fast_e(10):.5f}" == "55.03013"
    print(f"{fast_e(100):.5f}")  # 8986.86698


if __name__ == "__main__":
    main()
