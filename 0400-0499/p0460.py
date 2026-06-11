"""Problem 460: An Ant on the Move.

A segment from height y0 to y1 is traversed at the logarithmic mean
velocity (y1 - y0)/(ln y1 - ln y0), so its time is exactly the
hyperbolic length integral ds/y along the chord; same-height segments
(v = y0) and vertical ones (time |ln(y1/y0)|) are the limits of the
same formula. F(d) is therefore the shortest hyperbolic length of a
lattice polyline from (0,1) to (d,1), whose continuum geodesic is the
semicircle centred at (d/2, 0) through both endpoints. The optimal
lattice path hugs that circle to within about one unit except near the
two ends, where the geodesic is almost vertical and the path instead
climbs the lattice wall (x = 0 and x = d allow free vertical moves at
cost ln-ratio) before chording onto the circle. The DP therefore uses
a narrow band of candidates around the circle, full-height columns
near both walls, chords spanning up to a few hundred columns, and
vertical sweeps within each column. Validated against a complete
all-lattice-points DP at small d (reproducing all three given values)
and by agreement of two independent parameter settings at d = 10^4.
"""

import numba
import numpy as np

@numba.jit(cache=True, inline="always")
def seg_time(x0: int, y0: int, x1: int, y1: int, lny: np.ndarray) -> float:
    dx = x1 - x0
    dy = y1 - y0
    length = np.sqrt(dx * dx + dy * dy)
    if dy == 0:
        return length / y0
    return length * (lny[y1] - lny[y0]) / dy

@numba.jit(cache=True)
def band_dp(d: int, ymax_per_col: np.ndarray, ymin_per_col: np.ndarray,
            span: int) -> np.ndarray:
    """Shortest hyperbolic-time lattice path (0,1) -> (d,1) using only
    candidate nodes ymin[x]..ymax[x] per column, chords up to `span`
    columns, and vertical moves within a column."""
    ymax_all = 0
    for x in range(d + 1):
        if ymax_per_col[x] > ymax_all:
            ymax_all = ymax_per_col[x]
    lny = np.empty(ymax_all + 2, dtype=np.float64)
    for y in range(1, ymax_all + 2):
        lny[y] = np.log(y)
    inf = 1e30
    dist = np.full((d + 1, ymax_all + 1), inf, dtype=np.float64)
    dist[0, 1] = 0.0
    for x in range(d + 1):
        lo = ymin_per_col[x]
        hi = ymax_per_col[x]
        # vertical relaxation within the column (up then down sweeps)
        for y in range(lo + 1, hi + 1):
            t = dist[x, y - 1] + (lny[y] - lny[y - 1])
            if t < dist[x, y]:
                dist[x, y] = t
        for y in range(hi - 1, lo - 1, -1):
            t = dist[x, y + 1] + (lny[y + 1] - lny[y])
            if t < dist[x, y]:
                dist[x, y] = t
        if x == d:
            break
        # chords to later columns
        xe = x + span
        if xe > d:
            xe = d
        for y in range(lo, hi + 1):
            base = dist[x, y]
            if base >= inf:
                continue
            for x2 in range(x + 1, xe + 1):
                lo2 = ymin_per_col[x2]
                hi2 = ymax_per_col[x2]
                for y2 in range(lo2, hi2 + 1):
                    t = base + seg_time(x, y, x2, y2, lny)
                    if t < dist[x2, y2]:
                        dist[x2, y2] = t
    return dist

def run_band(d: int, center: np.ndarray, width: int, span: int,
             ends: int, wallh: int = 0):
    """One banded DP around `center`; returns (best time, refined center
    from the optimal corridor via forward/backward distances and the
    problem's x-symmetry)."""
    ymin = np.ones(d + 1, dtype=np.int64)
    ymax = np.ones(d + 1, dtype=np.int64)
    for x in range(d + 1):
        c = max(1.0, center[x])
        ymax[x] = int(np.ceil(c)) + width
        ymin[x] = max(1, int(np.floor(c)) - width)
        if min(x, d - x) <= ends:
            ymin[x] = 1  # the geodesic is near-vertical here
            if ymax[x] < wallh:
                ymax[x] = wallh  # allow tall vertical climbs at the walls
    dist = band_dp(d, ymax, ymin, span)
    best = float(dist[d, 1])
    new_center = np.empty(d + 1, dtype=np.float64)
    for x in range(d + 1):
        lo, hi = ymin[x], ymax[x]
        seg = dist[x, lo:hi + 1] + dist[d - x, lo:hi + 1]
        y = lo + int(np.argmin(seg))
        new_center[x] = y
    new_center = 0.5 * (new_center + new_center[::-1])  # symmetrise
    return best, new_center

def geodesic_center(d: int) -> np.ndarray:
    r2 = 1.0 + (d / 2.0) ** 2
    xs = np.arange(d + 1, dtype=np.float64)
    return np.sqrt(np.maximum(1.0, r2 - (xs - d / 2.0) ** 2))

def shortest_time(d: int, width: int, span: int, ends: int,
                  wallh: int) -> float:
    best, _ = run_band(d, geodesic_center(d), width, span, ends, wallh)
    return best

def exact_small(d: int) -> float:
    """Reference: every lattice point with 1 <= y <= d, unlimited span."""
    ymin = np.ones(d + 1, dtype=np.int64)
    ymax = np.full(d + 1, d, dtype=np.int64)
    return float(band_dp(d, ymax, ymin, d)[d, 1])

if __name__ == "__main__":
    assert abs(exact_small(4) - 2.960516287) < 5e-10  # given
    assert abs(exact_small(10) - 4.668187834) < 5e-10  # given
    assert abs(exact_small(100) - 9.217221972) < 5e-10  # given
    # the banded search reproduces the exact reference
    for dd in (10, 100):
        assert abs(shortest_time(dd, 6, dd, 12, dd) - exact_small(dd)) < 1e-12
    # two independent parameter settings must agree
    v1 = shortest_time(10**4, 6, 450, 40, 300)
    v2 = shortest_time(10**4, 10, 600, 80, 600)
    assert abs(v1 - v2) < 1e-10, (v1, v2)
    print(f"{v2:.9f}")  # 18.420738199
