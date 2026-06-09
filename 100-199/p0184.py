from collections import Counter
from math import gcd

import numba
import numpy as np


@numba.njit(cache=True)
def _left_counts(xs: np.ndarray, ys: np.ndarray) -> np.ndarray:
    # For each point, how many others lie strictly counter-clockwise within (0, pi).
    n = xs.shape[0]
    out = np.zeros(n, dtype=np.int64)
    for i in range(n):
        xi, yi, c = xs[i], ys[i], 0
        for j in range(n):
            if xi * ys[j] - yi * xs[j] > 0:
                c += 1
        out[i] = c
    return out


def solve(radius: int = 105) -> int:
    # Triangles on lattice points inside the disk that strictly contain the
    # origin. A triangle fails to contain it when its three direction-angles fit
    # in a closed half-plane: max angular gap > pi (open half-plane) or == pi
    # (an antipodal pair, leaving the origin on an edge). Both are subtracted.
    pts = [
        (x, y)
        for x in range(-radius + 1, radius)
        for y in range(-radius + 1, radius)
        if 0 < x * x + y * y < radius * radius
    ]
    n = len(pts)
    xs = np.array([p[0] for p in pts], dtype=np.int64)
    ys = np.array([p[1] for p in pts], dtype=np.int64)
    left = _left_counts(xs, ys)

    # points sharing a direction, counted once per pair via index order
    groups: dict[tuple[int, int], list[int]] = {}
    for i, (x, y) in enumerate(pts):
        g = gcd(abs(x), abs(y))
        groups.setdefault((x // g, y // g), []).append(i)
    same_after = [0] * n
    for idxs in groups.values():
        for rank, i in enumerate(idxs):
            same_after[i] = len(idxs) - rank - 1

    open_half = sum((b := left[i] + same_after[i]) * (b - 1) // 2 for i in range(n))

    # triples containing an opposite-direction pair (angular gap exactly pi)
    dirs = Counter()
    for x, y in pts:
        g = gcd(abs(x), abs(y))
        dirs[(x // g, y // g)] += 1
    opp_pairs = k2 = 0
    seen: set = set()
    for d, s in dirs.items():
        s_opp = dirs.get((-d[0], -d[1]), 0)
        if s_opp:
            key = frozenset((d, (-d[0], -d[1])))
            if key not in seen:
                seen.add(key)
                opp_pairs += s * s_opp
            k2 += (s * (s - 1) // 2) * s_opp
    antipodal = opp_pairs * (n - 2) - k2

    total = n * (n - 1) * (n - 2) // 6
    return total - open_half - antipodal


if __name__ == "__main__":
    print(solve())  # 1725323624056
