"""
Project Euler Problem 762: Amoebas in a 2D Grid
https://projecteuler.net/problem=762

A grid has 4 rows (cyclic) and infinitely many columns.  An amoeba at (x, y)
may divide into amoebas at (x+1, y) and (x+1, (y+1) mod 4) provided both
squares are empty.  Starting from one amoeba at (0, 0), C(N) is the number of
distinct arrangements reachable after exactly N divisions.  Given C(2) = 2,
C(10) = 1301, C(20) = 5895236 and C(100) = 125923036 (mod 10^9), find the
last nine digits of C(100000).

Reachability.  Tracing every amoeba's ancestry gives a full binary tree: each
division splits a node into a "stay" child (same row) and an "up" child (row
+ 1), so a node at depth x whose path contains u up-steps sits at cell
(x, u mod 4).  An arrangement is reachable iff it is the leaf-cell set of
such a tree with all leaf cells distinct - internal nodes may revisit cells
(at different times) and a valid division schedule always exists.  This was
verified by exhaustive comparison with a brute-force BFS for N = 0..9.

Counting.  For a fixed arrangement S the per-column node counts are forced:
with n(x, y) nodes at cell (x, y), the leaves are l(x, y) = [(x, y) in S]
(at most one per cell!), the internal count is i = n - l >= 0, and
n(x+1, y) = i(x, y) + i(x, y-1).  Conversely any consistent count profile is
realised by a tree.  Hence C(N) is the number of walks over count vectors
n = (n_0, n_1, n_2, n_3) from (1, 0, 0, 0) to (0, 0, 0, 0) accumulating
exactly N + 1 leaves, where one step chooses l_y <= min(n_y, 1) and moves to
n'_y = i_y + i_{y-1}.

Bounded state space.  The column total satisfies sum(n') = 2(sum(n) - l) with
l <= 4 leaves per column, so from sum(n) >= 8 the total can never decrease
and the absorbing zero state is unreachable: terminating walks stay within
the 330 vectors with sum(n) <= 7.  Leafless steps double sum(n), so within a
fixed leaf count the states are processed in increasing column-total order;
the dynamic programming over (leaf count, state) costs a few thousand
operations per leaf level.
"""

from itertools import product

import numpy as np
from numba import njit

MOD = 10**9
N = 100_000


def build():
    states = []
    index = {}
    for n in product(range(8), repeat=4):
        if sum(n) <= 7:
            index[n] = len(states)
            states.append(n)
    trans = []  # (src, dst, leaves)
    for s in states:
        if sum(s) == 0:
            continue  # absorbing
        si = index[s]
        opts = [range(2 if s[y] >= 1 else 1) for y in range(4)]
        for lv in product(*opts):
            i = tuple(s[y] - lv[y] for y in range(4))
            nxt = tuple(i[y] + i[(y - 1) % 4] for y in range(4))
            if sum(nxt) <= 7:
                trans.append((si, index[nxt], sum(lv)))
    # topological order of leafless edges = increasing column total
    order = np.array(
        sorted(range(len(states)), key=lambda k: sum(states[k])), dtype=np.int64
    )
    e_src = np.array([t[0] for t in trans], dtype=np.int64)
    e_dst = np.array([t[1] for t in trans], dtype=np.int64)
    e_lv = np.array([t[2] for t in trans], dtype=np.int64)
    lf = np.full(len(states), -1, dtype=np.int64)
    for s, t, d in trans:
        if d == 0:
            lf[s] = t
    return states, index, order, e_src, e_dst, e_lv, lf


@njit(cache=True)
def count(n_target, ns, start, zero, order, e_src, e_dst, e_lv, lf):
    """Number of walks with exactly n_target + 1 leaves, mod 10^9."""
    v = np.zeros((5, ns), dtype=np.int64)  # rolling window over leaf counts
    ne = e_src.shape[0]
    ans = np.int64(0)
    for j in range(n_target + 2):
        cur = np.zeros(ns, dtype=np.int64)
        if j == 0:
            cur[start] = 1
        for t in range(ne):
            d = e_lv[t]
            if 1 <= d <= j:
                cur[e_dst[t]] = (cur[e_dst[t]] + v[(j - d) % 5, e_src[t]]) % MOD
        # leafless edges (one per state), in increasing column-total order
        for oi in range(ns):
            k = order[oi]
            if cur[k] != 0 and lf[k] >= 0:
                cur[lf[k]] = (cur[lf[k]] + cur[k]) % MOD
        v[j % 5] = cur
        if j == n_target + 1:
            ans = cur[zero]
    return ans


def main():
    states, index, order, e_src, e_dst, e_lv, lf = build()
    ns = len(states)
    start = index[(1, 0, 0, 0)]
    zero = index[(0, 0, 0, 0)]

    def c(n):
        return int(count(n, ns, start, zero, order, e_src, e_dst, e_lv, lf))

    assert c(2) == 2
    assert c(10) == 1301
    assert c(20) == 5895236
    assert c(100) == 125923036
    return c(N)


if __name__ == "__main__":
    print(main())  # 285528863
