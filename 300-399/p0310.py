import numba
import numpy as np


@numba.jit(cache=True)
def grundy_square(n_max: int) -> np.ndarray:
    """Grundy value of a single Nim-Square heap of size 0..n_max.

    A move removes a positive square number of stones, so
        g(n) = mex { g(n - s^2) : s >= 1, s^2 <= n }.
    """
    g = np.zeros(n_max + 1, dtype=np.int64)
    for n in range(1, n_max + 1):
        seen = np.zeros(128, dtype=np.bool_)
        s = 1
        while s * s <= n:
            seen[g[n - s * s]] = True
            s += 1
        m = 0
        while seen[m]:
            m += 1
        g[n] = m
    return g


def count_losing(n_max: int) -> int:
    g = grundy_square(n_max)
    size = 1
    while size <= int(g.max()):
        size <<= 1
    # cnt[v] = number of heap sizes in [0, n_max] with Grundy value v.
    cnt = np.zeros(size, dtype=np.int64)
    for v in g:
        cnt[v] += 1

    total_indices = n_max + 1
    z = int(cnt[0])  # heaps that are themselves losing (Grundy 0)

    # pairxor[w] = #{(b, c) ordered : g[b] XOR g[c] = w}; then
    # T = #{(a,b,c) ordered : XOR = 0} = sum_v cnt[v] * pairxor[v].
    pairxor = np.zeros(size, dtype=np.int64)
    for u in range(size):
        cu = int(cnt[u])
        if not cu:
            continue
        for v in range(size):
            pairxor[u ^ v] += cu * int(cnt[v])
    t = int(sum(int(cnt[v]) * int(pairxor[v]) for v in range(size)))

    # Convert ordered count T into sorted (a <= b <= c) count.
    #   all-equal solutions: a=b=c with g=0  -> z
    #   exactly-two-equal multisets {p,p,q}, p!=q, need g[q]=0 -> z*n_max
    #     (q has z choices, p any of the other total_indices-1 indices)
    #   all-distinct multisets: (T - z - 3*(z*n_max)) / 6
    two_equal = z * (total_indices - 1)
    distinct = (t - z - 3 * two_equal) // 6
    return distinct + two_equal + z


if __name__ == "__main__":
    assert count_losing(29) == 1160
    print(count_losing(100_000))  # 2586528661783
