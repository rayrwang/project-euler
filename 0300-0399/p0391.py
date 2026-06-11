import numba
import numpy as np


@numba.jit(cache=True)
def popcount(x: int) -> int:
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@numba.jit(cache=True)
def m_brute(n: int) -> int:
    """Direct game solution for small n.

    Play lives on indices k of s_k with terminal K = 2^(n+1) - 2: the gap
    popcount(2^(n+1) - 1) = n + 1 > n can never be paid, so K cannot be
    jumped.  P-positions by backward induction; M(n) is the largest cost
    s_j <= n of a first move landing on a P-position.
    """
    big = (1 << (n + 1)) - 2
    p = np.zeros(big + 1, dtype=np.bool_)
    p[big] = True
    for k in range(big - 1, -1, -1):
        cost = 0
        kk = k
        is_p = True
        while kk < big:
            kk += 1
            cost += popcount(kk)
            if cost > n:
                break
            if p[kk]:
                is_p = False
                break
        p[k] = is_p
    best = 0
    cost = 0
    kk = 0
    while True:
        kk += 1
        cost += popcount(kk)
        if cost > n:
            break
        if p[kk]:
            best = cost
    return best


@numba.jit(cache=True, parallel=True)
def m_fast(n: int) -> int:
    """M(n) via the greedy P-chain automaton over scale-recursive tables.

    In this line game a position is P exactly when no P-position lies
    within cost n above it, so the P-set is the greedy chain from the top:
    p_{i+1} = max{k : s_k <= s_{p_i} - (n+1)}.  Scanning indices downward,
    the chain construction is a one-integer automaton: with delta = target
    minus s at the current index, the index is selected iff delta >= 0
    (resetting delta to -(n+1)), and crossing an index adds its popcount.
    M(n) = n + 1 + final delta.

    Indices in an aligned block of size 2^m share their high-part popcount
    h, so the block's effect is a table over the 2n + 2 delta values, and
    T(m, h) = T(m-1, h) o T(m-1, h+1).  Building the (m, h) triangle
    bottom-up costs O(n^3) cheap gathers on L1-resident tables.
    """
    size = 2 * n + 2  # delta in [-(n+1), n] -> index = delta + n + 1
    cur = np.empty((n + 2, size), np.int16)
    for h in numba.prange(n + 2):  # ty: ignore[not-iterable]
        for idx in range(size):
            d = idx - (n + 1)
            cur[h, idx] = (-(n + 1) if d >= 0 else d) + h
    for m in range(1, n + 2):
        hmax = n + 1 - m
        new = np.empty((hmax + 1, size), np.int16)
        for h in numba.prange(hmax + 1):  # ty: ignore[not-iterable]
            up = cur[h + 1]
            low = cur[h]
            for idx in range(size):
                new[h, idx] = low[up[idx] + (n + 1)]
        cur = new
    # Seeding the chain at K gives initial delta = -(n+1) at the very top.
    return n + 1 + cur[0, 0]


def total(n_max: int) -> int:
    for n in range(1, 15):
        assert m_fast(n) == m_brute(n)
    return sum(int(m_fast(n)) ** 3 for n in range(1, n_max + 1))


if __name__ == "__main__":
    print(total(1000))  # 61029882288
