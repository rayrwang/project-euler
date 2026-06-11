"""Project Euler 459: Flipping Game.

Two players flip rectangles (square width, triangular height, white disk in
the upper-right corner) on an N x N board, trying to make it all black;
W(N) counts the first player's winning first moves. Find W(10^6).

This is a coin-turning game: the position value is the XOR over white disks
of per-cell Grundy values, and since every move is a product of a horizontal
move (flip a run of square length ending at the chosen column) and a
vertical one (triangular length), the Tartan theorem applies: the cell value
is the NIM-PRODUCT g1(x) (x) g2(y) of the two one-dimensional ruler games.
Each 1D Grundy follows g(x) = mex over allowed lengths L of
P(x) xor P(x - L + 1), with P the prefix XOR of g - O(N sqrt N) with a
stamped mex array (Grundy values stay below the move count, ~1500).

Because nim-multiplication is bilinear over XOR, the XOR of a w x h
rectangle of cell values factorises as A (x) B with A = P1(x+1) xor
P1(x-w+1) and B = P2(y+1) xor P2(y-h+1). The all-white start has total value
T = P1(N) (x) P2(N), and a first move wins iff its rectangle value equals T.
So W(N) = sum over value pairs (v, u) with v (x) u = T of cntA[v] * cntB[u],
where the counts tally A and B over all ~10^9 (position, length) choices -
the values fit in 12 bits, so this is two histogram passes plus a few
thousand nim-products. W(1) = 1, W(2) = 0, W(5) = 8 and W(100) = 31395 are
all asserted.
"""

from functools import lru_cache

import numpy as np
from numba import njit

N = 10**6
VCAP = 4096  # grundy values < #moves+1 < 1500, so all XORs < 2048


@lru_cache(maxsize=None)
def nmul(a, b):
    """Nim multiplication."""
    if a < b:
        a, b = b, a
    if b == 0:
        return 0
    if b == 1:
        return a
    f = 2
    while f * f <= a:
        f = f * f
    a1, a0 = divmod(a, f)
    b1, b0 = divmod(b, f)
    if b1 == 0:
        return nmul(a1, b0) * f ^ nmul(a0, b0)
    aa = nmul(a1, b1)
    cross = nmul(a1, b0) ^ nmul(a0, b1)
    return (cross ^ aa) * f ^ nmul(a0, b0) ^ nmul(aa, f // 2)


@njit(cache=True)
def grundy_ruler(n, lengths):
    g = np.zeros(n, np.int64)
    pre = np.zeros(n + 1, np.int64)
    seen = np.zeros(VCAP, np.int64)
    stamp = 0
    for x in range(n):
        stamp += 1
        for li in range(len(lengths)):
            ell = lengths[li]
            if ell > x + 1:
                break
            seen[pre[x] ^ pre[x - ell + 1]] = stamp
        m = 0
        while seen[m] == stamp:
            m += 1
        g[x] = m
        pre[x + 1] = pre[x] ^ m
    return g, pre


@njit(cache=True)
def collect_counts(n, lengths, pre):
    cnt = np.zeros(VCAP, np.int64)
    for x in range(n):
        for li in range(len(lengths)):
            ell = lengths[li]
            if ell > x + 1:
                break
            cnt[pre[x + 1] ^ pre[x - ell + 1]] += 1
    return cnt


def winning_moves(n):
    sq = np.array([k * k for k in range(1, int(n**0.5) + 2) if k * k <= n], np.int64)
    tr = np.array(
        [k * (k + 1) // 2 for k in range(1, n + 2) if k * (k + 1) // 2 <= n], np.int64
    )
    g1, p1 = grundy_ruler(n, sq)
    g2, p2 = grundy_ruler(n, tr)
    assert g1.max() < 2048 and g2.max() < 2048
    target = nmul(int(p1[n]), int(p2[n]))
    cnt_a = collect_counts(n, sq, p1)
    cnt_b = collect_counts(n, tr, p2)
    total = 0
    for v in np.flatnonzero(cnt_a):
        for u in np.flatnonzero(cnt_b):
            if nmul(int(v), int(u)) == target:
                total += int(cnt_a[v]) * int(cnt_b[u])
    return total


if __name__ == "__main__":
    for a, b, expect in ((2, 2, 3), (2, 3, 1), (3, 3, 2), (4, 4, 6), (2, 4, 8), (3, 4, 12)):
        assert nmul(a, b) == expect
    assert winning_moves(1) == 1
    assert winning_moves(2) == 0
    assert winning_moves(5) == 8
    assert winning_moves(100) == 31395
    print(winning_moves(N))  # 3996390106631
