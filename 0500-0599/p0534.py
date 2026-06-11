"""Project Euler problem 534: Weak Queens.

A weak queen with weakness factor w on an n x n board attacks its whole
row, but only up to n - 1 - w squares vertically or diagonally.  Q(n, w)
counts placements of n mutually non-attacking weak queens, and
S(n) = sum of Q(n, w) over 0 <= w < n.  Find S(14).

Since each queen attacks its full row, valid placements have exactly one
queen per row: a column sequence c_1..c_n.  With reach D = n - 1 - w, rows
i < j conflict iff j - i <= D and c_i = c_j or |c_i - c_j| = j - i, i.e.
the classical queen constraints restricted to a sliding window of D rows.

Counting per D:
- D = 0: no constraints at all, n^n.
- 1 <= D <= 7: dynamic programming whose state is the window of the last D
  columns.  The full state space (n+1)^D is far too large at D = 7, but
  only windows that are themselves conflict-free can ever be reached
  (about 4.4 million at n = 14, D = 7, versus 15^7 = 171 million), so the
  solution enumerates exactly the reachable states by frontier expansion
  (sentinel-padded so short prefixes use the same encoding), builds the
  transition table once with binary search, and pushes counts with
  bincount-style scatter-adds.  Counts stay below 2^53, so float64
  accumulation is exact.
- D >= 8: plain backtracking (numba-compiled); the solution counts shrink
  rapidly as constraints strengthen, down to the classical 14-queens count
  365596 at D = 13.

Verified: all three methods (brute force over all n^n sequences, the
sparse DP, and the backtracker) agree for every w at n = 4 and n = 5,
reproducing the given Q(4,0) = 2, Q(4,2) = 16, Q(4,3) = 256, S(4) = 276
and S(5) = 3347; the sparse DP and backtracker also agree on the larger
cross-checks (n, D) = (9,6), (9,7), (10,6), (8,7); at n = 14 both methods
were run at D = 7 and returned identical counts, and Q(14, 0) equals the
known 14-queens number 365596.
"""

from itertools import product

import numpy as np
from numba import njit


def brute_q(n: int, w: int) -> int:
    reach = n - 1 - w
    cnt = 0
    for cols in product(range(n), repeat=n):
        ok = True
        for j in range(n):
            for i in range(max(0, j - reach), j):
                if cols[i] == cols[j] or abs(cols[i] - cols[j]) == j - i:
                    ok = False
                    break
            if not ok:
                break
        cnt += ok
    return cnt


@njit(cache=True)
def backtrack_q(n: int, reach: int) -> int:
    c = np.empty(n, np.int64)
    cand = np.zeros(n + 1, np.int64)
    total = 0
    t = 0
    while t >= 0:
        col = cand[t]
        if col >= n:
            t -= 1
            continue
        cand[t] = col + 1
        ok = True
        dmax = reach if reach < t else t
        for d in range(1, dmax + 1):
            diff = col - c[t - d]
            if diff == 0 or diff == d or diff == -d:
                ok = False
                break
        if not ok:
            continue
        if t == n - 1:
            total += 1
            continue
        c[t] = col
        t += 1
        cand[t] = 0
    return total


def sparse_q(n: int, reach: int) -> int:
    """Window DP over only the reachable (conflict-free) windows."""
    if reach == 0:
        return n**n
    base = n + 1  # digit n = sentinel for not-yet-placed rows
    pows = [base**j for j in range(reach + 1)]
    start = np.array([sum(n * pows[j] for j in range(reach))], dtype=np.int64)

    def expand(ids: np.ndarray) -> tuple[list[np.ndarray], list[np.ndarray]]:
        ts, srcs = [], []
        for col in range(n):
            ok = np.ones(len(ids), dtype=bool)
            for j in range(reach):  # digit j is the row at distance j+1
                cc = (ids // pows[j]) % base
                d = j + 1
                ok &= ~((cc != n) & ((cc == col) | (cc == col - d) | (cc == col + d)))
            ts.append((ids[ok] % pows[reach - 1]) * base + col)
            srcs.append(np.flatnonzero(ok))
        return ts, srcs

    all_states = start.copy()
    frontier = start.copy()
    while len(frontier):
        ts, _ = expand(frontier)
        new = np.unique(np.concatenate(ts))
        frontier = new[~np.isin(new, all_states)]
        if len(frontier):
            all_states = np.unique(np.concatenate([all_states, frontier]))

    ns = len(all_states)
    tgt = np.full((n, ns), -1, dtype=np.int64)
    ts, srcs = expand(all_states)
    for col in range(n):
        tgt[col][srcs[col]] = np.searchsorted(all_states, ts[col])

    x = np.zeros(ns, dtype=np.float64)
    x[np.searchsorted(all_states, start[0])] = 1.0
    for _ in range(n):
        newx = np.zeros(ns, dtype=np.float64)
        for col in range(n):
            m = tgt[col] >= 0
            newx += np.bincount(tgt[col][m], weights=x[m], minlength=ns)
        x = newx
    total = x.sum()
    assert total < 2**53  # float64 exact
    return int(round(total))


def q_value(n: int, reach: int) -> int:
    if reach == 0:
        return n**n
    if reach <= 7:
        return sparse_q(n, reach)
    return backtrack_q(n, reach)


def main() -> None:
    for n in (4, 5):
        for w in range(n):
            reach = n - 1 - w
            b = brute_q(n, w)
            assert sparse_q(n, reach) == b, (n, w)
            assert backtrack_q(n, reach) == b, (n, w)
    assert brute_q(4, 0) == 2 and brute_q(4, 2) == 16 and brute_q(4, 3) == 256
    assert sum(brute_q(4, w) for w in range(4)) == 276
    assert sum(brute_q(5, w) for w in range(5)) == 3347
    for n, reach in [(9, 6), (9, 7), (10, 6), (8, 7)]:
        assert sparse_q(n, reach) == backtrack_q(n, reach), (n, reach)
    assert sparse_q(14, 7) == backtrack_q(14, 7)  # full-size cross-check
    assert backtrack_q(14, 13) == 365596  # classical 14-queens

    ans = sum(q_value(14, 13 - w) for w in range(14))
    print(ans)  # 11726115562784664


if __name__ == "__main__":
    main()
