import numba
import numpy as np

from funcs import prime_sieve_int


@numba.jit(cache=True)
def _dijkstra_dense(cost: np.ndarray, k: int) -> np.ndarray:
    """Shortest distances from residue 0 in the circulant graph mod k.

    Edges s -> (s + d) mod k of weight cost[d] for d = 1..k-1; the graph
    is dense but tiny, so O(k^2) selection beats a heap.
    """
    inf = np.int64(1) << 60
    dist = np.full(k, inf, dtype=np.int64)
    dist[0] = 0
    done = np.zeros(k, dtype=np.bool_)
    for _ in range(k):
        u, du = -1, inf
        for v in range(k):
            if not done[v] and dist[v] < du:
                u, du = v, dist[v]
        if u < 0:
            break
        done[u] = True
        for d in range(1, k):
            w = (u + d) % k
            nd = du + cost[d]
            if nd < dist[w]:
                dist[w] = nd
    return dist


def m_score(k: int, n: int, primes: np.ndarray) -> int:
    """Maximal prime score of n values in [0, k) summing to a multiple of k.

    Start from the all-(k-1) list, worth n * p(k-1) with sum n(k-1).
    Lowering one entry to k-1-d loses p(k-1) - p(k-1-d) score and shifts
    the sum by -d, so the cheapest valid list costs the shortest path to
    residue n(k-1) mod k in the circulant graph above.  A shortest path
    repeats no residue, so it uses at most k-1 < n single-entry changes.
    """
    cost = np.zeros(k, dtype=np.int64)
    for d in range(1, k):
        cost[d] = primes[k - 1] - primes[k - 1 - d]
    dist = _dijkstra_dense(cost, k)
    return n * int(primes[k - 1]) - int(dist[(n * (k - 1)) % k])


def _m_brute(k: int, n: int, primes: np.ndarray) -> int:
    best = {0: 0}
    for _ in range(n):
        nxt: dict[int, int] = {}
        for r, s in best.items():
            for a in range(k):
                r2 = (r + a) % k
                s2 = s + int(primes[a])
                if nxt.get(r2, -1) < s2:
                    nxt[r2] = s2
        best = nxt
    return best[0]


if __name__ == "__main__":
    primes = prime_sieve_int(80000)
    assert m_score(2, 5, primes) == 14  # given
    # the path argument needs n >= k - 1 (true in the target instance)
    for k in range(2, 8):
        for n in range(k - 1, k + 7):
            assert m_score(k, n, primes) == _m_brute(k, n, primes), (k, n)
    k = 7000
    print(m_score(k, int(primes[k]), primes))  # 4992775389
