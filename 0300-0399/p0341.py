import numba
import numpy as np


@numba.jit(cache=True)
def golomb_table(base: int) -> np.ndarray:
    """Golomb's sequence G(1..base) via G(n) = 1 + G(n - G(G(n - 1)))."""
    g = np.zeros(base + 1, dtype=np.int64)
    g[1] = 1
    for n in range(2, base + 1):
        g[n] = 1 + g[n - g[g[n - 1]]]
    return g


def golomb_sum_of_cubes(limit: int) -> int:
    """sum of G(n^3) for 1 <= n < limit.

    Value c occupies positions (A(c-1), A(c)] where A(c) = sum_{j<=c} G(j),
    so G(N) is the c with A(c-1) < N <= A(c).  Across the run of value w
    (the c with G(c) = w), A(c) sweeps W(w-1) + w, ..., W(w) in steps of w,
    where W(w) = sum_{j<=w} j G(j).  So locate w with W(w-1) < N <= W(w) by
    binary search over W, then c = A(w-1) + ceil((N - W(w-1)) / w).
    """
    base = 11_000_000  # W(base) must exceed the largest query (~10^18)
    g = golomb_table(base)
    a = np.cumsum(g)  # a[c] = A(c); a[0] = 0
    w_tab = np.cumsum(g * np.arange(base + 1, dtype=np.int64))  # W
    queries = np.arange(1, limit, dtype=np.int64) ** 3
    assert w_tab[-1] >= queries[-1]
    w = np.searchsorted(w_tab, queries)  # W(w-1) < N <= W(w)
    c = a[w - 1] + (queries - w_tab[w - 1] + w - 1) // w
    return int(c.sum())


if __name__ == "__main__":
    g = golomb_table(1_000_000)
    assert g[1000] == 86 and g[1_000_000] == 6137
    assert golomb_sum_of_cubes(1000) == 153506976
    print(golomb_sum_of_cubes(1_000_000))  # 56098610614277014
