from itertools import product
from math import comb

import numba
import numpy as np

# Ordered 4-tuples of lines per set of exactly k distinct lines: k! * StirlingS2(4, k).
SURJ = {1: 1, 2: 14, 3: 36, 4: 24}


def _line_masks() -> np.ndarray:
    """81-bit point masks (two uint64 each) of the 1080 SETs in AG(4, 3)."""
    points = list(product(range(3), repeat=4))
    index = {p: i for i, p in enumerate(points)}
    seen = set()
    for a in points:
        for b in points:
            if a == b:
                continue
            c = tuple((-(x + y)) % 3 for x, y in zip(a, b))  # a + b + c = 0
            if c in (a, b):
                continue
            seen.add(frozenset((index[a], index[b], index[c])))
    masks = np.zeros((len(seen), 2), dtype=np.uint64)
    for i, line in enumerate(seen):
        for p in line:
            masks[i, p // 64] |= np.uint64(1) << np.uint64(p % 64)
    return masks


@numba.njit(cache=True, inline="always")
def _popcount(x: np.uint64) -> int:
    x = x - ((x >> np.uint64(1)) & np.uint64(0x5555555555555555))
    x = (x & np.uint64(0x3333333333333333)) \
        + ((x >> np.uint64(2)) & np.uint64(0x3333333333333333))
    x = (x + (x >> np.uint64(4))) & np.uint64(0x0F0F0F0F0F0F0F0F)
    return int((x * np.uint64(0x0101010101010101)) >> np.uint64(56))


@numba.njit(cache=True)
def _dist_123(m0: np.ndarray, m1: np.ndarray, n_lines: int) -> np.ndarray:
    """Union-size histograms for distinct-line sets of size 1, 2 and 3."""
    d = np.zeros((4, 13), dtype=np.int64)
    for i in range(n_lines):
        a0, a1 = m0[i], m1[i]
        d[1, _popcount(a0) + _popcount(a1)] += 1
        for j in range(i + 1, n_lines):
            b0, b1 = a0 | m0[j], a1 | m1[j]
            d[2, _popcount(b0) + _popcount(b1)] += 1
            for k in range(j + 1, n_lines):
                d[3, _popcount(b0 | m0[k]) + _popcount(b1 | m1[k])] += 1
    return d


@numba.njit(cache=True)
def _dist_4(m0: np.ndarray, m1: np.ndarray, n_lines: int) -> np.ndarray:
    """Union-size histogram for the C(1080, 4) sets of four distinct lines."""
    cnt = np.zeros(13, dtype=np.int64)
    for i in range(n_lines):
        a0, a1 = m0[i], m1[i]
        for j in range(i + 1, n_lines):
            b0, b1 = a0 | m0[j], a1 | m1[j]
            for k in range(j + 1, n_lines):
                c0, c1 = b0 | m0[k], b1 | m1[k]
                for ell in range(k + 1, n_lines):
                    u = _popcount(c0 | m0[ell]) + _popcount(c1 | m1[ell])
                    cnt[u] += 1
    return cnt


_HISTOGRAM_CACHE: dict[int, np.ndarray] | None = None


def _histogram() -> dict[int, np.ndarray]:
    """Union-size histograms for distinct-line sets of sizes 1..4 (computed once)."""
    global _HISTOGRAM_CACHE
    if _HISTOGRAM_CACHE is None:
        masks = _line_masks()
        n_lines = masks.shape[0]
        m0 = np.ascontiguousarray(masks[:, 0])
        m1 = np.ascontiguousarray(masks[:, 1])
        d123 = _dist_123(m0, m1, n_lines)
        _HISTOGRAM_CACHE = {
            1: d123[1], 2: d123[2], 3: d123[3],
            4: _dist_4(m0, m1, n_lines),
        }
    return _HISTOGRAM_CACHE


def sum_of_fourth_powers(n: int) -> int:
    """F(n) = sum over n-card collections C of S(C)^4.

    Expanding S(C)^4 as a sum over ordered 4-tuples of SETs contained in C and
    swapping the order of summation, F(n) counts, over all ordered 4-tuples of
    SETs, the collections containing the union of their points. A tuple whose
    SETs cover u distinct points lies in exactly C(81 - u, n - u) collections,
    so F(n) = sum over ordered 4-tuples C(81 - u, n - u).

    Group the tuples by their set of k distinct SETs (k = 1..4): there are
    SURJ[k] ordered tuples per such set, and u depends only on the geometry.
    Tabulating the union-size histogram of distinct-SET sets of each size (any
    two SETs meet in at most one point, so unions span 3..12 points) gives F(n)
    directly. Checks: F(3) = 1080, F(6) = 159690960.
    """
    total = 0
    for k, counts in _histogram().items():
        for u in range(13):
            if counts[u] and n >= u:
                total += SURJ[k] * int(counts[u]) * comb(81 - u, n - u)
    return total


if __name__ == "__main__":
    assert sum_of_fourth_powers(3) == 1080
    assert sum_of_fourth_powers(6) == 159690960
    print(sum_of_fourth_powers(12))  # 11871909492066000
