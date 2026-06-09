from decimal import Decimal, getcontext

import numba
import numpy as np

MOD = 50515093


@numba.njit(cache=True)
def _min_sq_dist(xs: np.ndarray, ys: np.ndarray, cell: int) -> int:
    """Exact minimal squared distance via grid hashing with 3x3 probing."""
    n = xs.shape[0]
    g = MOD // cell + 1
    counts = np.zeros(g * g + 1, dtype=np.int64)
    cx = xs // cell
    cy = ys // cell
    keys = cx * g + cy
    for i in range(n):
        counts[keys[i] + 1] += 1
    for i in range(g * g):
        counts[i + 1] += counts[i]
    order = np.empty(n, dtype=np.int64)
    fill = counts[:-1].copy()
    for i in range(n):
        k = keys[i]
        order[fill[k]] = i
        fill[k] += 1
    best = np.int64(2**62)
    for i in range(n):
        x, y = xs[i], ys[i]
        for dx in range(-1, 2):
            a = cx[i] + dx
            if a < 0 or a >= g:
                continue
            for dy in range(-1, 2):
                b = cy[i] + dy
                if b < 0 or b >= g:
                    continue
                k = a * g + b
                for t in range(counts[k], counts[k + 1]):
                    j = order[t]
                    if j <= i:
                        continue
                    d = (xs[j] - x) ** 2 + (ys[j] - y) ** 2
                    if d < best:
                        best = d
    return int(best)


def shortest_distance(k: int) -> Decimal:
    """d(k) for the BBS-style point stream, exact integer arithmetic + sqrt."""
    s = np.empty(2 * k, dtype=np.int64)
    v = 290797
    for i in range(2 * k):
        s[i] = v
        v = v * v % MOD
    xs, ys = s[0::2].copy(), s[1::2].copy()
    # Cell size near the expected minimal distance scale keeps buckets tiny;
    # 3x3 probing is exhaustive because the answer is far below the cell size.
    cell = max(1000, MOD // (int(np.sqrt(k)) + 1))
    getcontext().prec = 30
    return Decimal(int(_min_sq_dist(xs, ys, cell))).sqrt()


if __name__ == "__main__":
    assert f"{shortest_distance(14):.9f}" == "546446.466846479"
    print(f"{shortest_distance(2_000_000):.9f}")  # 20.880613018
