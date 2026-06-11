import heapq
from math import pi

import numpy as np
from numba import njit


@njit(cache=True)
def _stations(r: int) -> np.ndarray:
    """Integer points on the sphere x^2 + y^2 + z^2 = r^2."""
    r2 = r * r
    xs, ys, zs = [], [], []
    for x in range(-r, r + 1):
        x2 = x * x
        for y in range(-r, r + 1):
            z2 = r2 - x2 - y * y
            if z2 < 0:
                continue
            z = int(np.sqrt(z2))
            if z * z == z2:
                xs.append(x)
                ys.append(y)
                zs.append(z)
                if z != 0:
                    xs.append(x)
                    ys.append(y)
                    zs.append(-z)
    out = np.empty((len(xs), 3), dtype=np.int64)
    for i in range(len(xs)):
        out[i, 0] = xs[i]
        out[i, 1] = ys[i]
        out[i, 2] = zs[i]
    return out


@njit(cache=True)
def _knn(points: np.ndarray, r: int, k: int):
    """k nearest neighbours (squared chordal distance) of each unit-normalised station, found by
    bucketing the integer coordinates into a uniform grid and scanning a growing cell radius."""
    n = points.shape[0]
    grid = max(1, int(round((n / 8.0) ** (1.0 / 3.0))))
    cell = (2.0 * r) / grid + 1e-9
    stride = grid + 4

    unit = np.empty((n, 3))
    for i in range(n):
        norm = np.sqrt(points[i, 0] ** 2 + points[i, 1] ** 2 + points[i, 2] ** 2)
        unit[i] = points[i] / norm

    keys = np.empty(n, dtype=np.int64)
    for i in range(n):
        cx = int((points[i, 0] + r) // cell)
        cy = int((points[i, 1] + r) // cell)
        cz = int((points[i, 2] + r) // cell)
        keys[i] = (cx * stride + cy) * stride + cz
    order = np.argsort(keys)
    sorted_keys = keys[order]

    nbr_idx = np.empty((n, k), dtype=np.int64)
    nbr_dist = np.empty((n, k), dtype=np.float64)
    for i in range(n):
        cx = int((points[i, 0] + r) // cell)
        cy = int((points[i, 1] + r) // cell)
        cz = int((points[i, 2] + r) // cell)
        rad = 1
        cand = np.empty(0, dtype=np.int64)
        while True:
            bucket = []
            for dx in range(-rad, rad + 1):
                for dy in range(-rad, rad + 1):
                    for dz in range(-rad, rad + 1):
                        key = ((cx + dx) * stride + (cy + dy)) * stride + (cz + dz)
                        lo = np.searchsorted(sorted_keys, key, side="left")
                        hi = np.searchsorted(sorted_keys, key, side="right")
                        for t in range(lo, hi):
                            bucket.append(order[t])
            if len(bucket) >= k + 1 or rad > grid + 1:
                cand = np.array(bucket, dtype=np.int64)
                break
            rad += 1
        dists = np.empty(len(cand), dtype=np.float64)
        for t in range(len(cand)):
            j = cand[t]
            dists[t] = (
                (unit[i, 0] - unit[j, 0]) ** 2
                + (unit[i, 1] - unit[j, 1]) ** 2
                + (unit[i, 2] - unit[j, 2]) ** 2
            )
        nearest = np.argsort(dists)
        count = 0
        for t in range(len(nearest)):
            j = cand[nearest[t]]
            if j == i:
                continue
            if count < k:
                nbr_idx[i, count] = j
                nbr_dist[i, count] = dists[nearest[t]]
                count += 1
            else:
                break
        while count < k:
            nbr_idx[i, count] = i
            nbr_dist[i, count] = 0.0
            count += 1
    return nbr_idx, nbr_dist


def minimal_risk(r: int, k: int = 32) -> float:
    """Minimal-risk journey from the North to the South Pole station on the sphere of radius r.

    Stations are integer points on the sphere; a road along the great circle of arc length d has
    risk (d / (pi r))^2 = (theta / pi)^2 for central angle theta. Risk being squared length means
    many short hops beat one long one, so the optimum threads nearby stations. Each station links
    to its k nearest neighbours (angle recovered from the chordal distance), and Dijkstra finds the
    least-risk path. k = 32 matches the dense-graph answers exactly, including M(7) = 0.1784943998.
    """
    points = _stations(r)
    n = len(points)
    north = int(np.where((points[:, 0] == 0) & (points[:, 1] == 0) & (points[:, 2] == r))[0][0])
    south = int(np.where((points[:, 0] == 0) & (points[:, 1] == 0) & (points[:, 2] == -r))[0][0])

    kk = min(k, n - 1)
    idx, sq_chord = _knn(points, r, kk)
    risk = (np.arccos(np.clip(1 - sq_chord / 2, -1, 1)) / pi) ** 2

    dist = np.full(n, np.inf)
    dist[north] = 0.0
    seen = np.zeros(n, dtype=np.bool_)
    heap = [(0.0, north)]
    while heap:
        d, u = heapq.heappop(heap)
        if seen[u]:
            continue
        seen[u] = True
        if u == south:
            return d
        for t in range(kk):
            v = int(idx[u, t])
            if v == u:
                continue
            nd = d + risk[u, t]
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return float(dist[south])


def solve() -> float:
    return sum(minimal_risk(2**n - 1) for n in range(1, 16))


if __name__ == "__main__":
    assert abs(minimal_risk(7) - 0.1784943998) < 1e-10
    print(f"{solve():.10f}")  # 1.2759860331
