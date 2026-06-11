"""
Project Euler Problem 750: Optimal Card Stacking
https://projecteuler.net/problem=750

Cards 1..N lie at table positions 1..N, with the card at position p equal to
3^p mod (N + 1) (a permutation for the values of N used).  A pile may be
dragged onto another only if the combined pile is "in sequence"; G(N) is the
minimal total horizontal drag distance needed to gather all cards into one
pile.  Find G(976).

Any pile that ever appears holds a consecutive range of cards [i..j], because
being in sequence must hold for the final pile and every merge preserves it.
Dropping [i..k] onto [k+1..j] reads i, ..., k, k+1, ..., j top to bottom (in
sequence) while the reverse does not, so the moving pile always carries the
smaller cards, the merged pile stays where the target was, and by induction
each pile [i..j] sits at the original position of card j.  The merge cost is
|pos[k] - pos[j]|, giving the interval DP

    dp[i][j] = min_{i <= k < j} ( dp[i][k] + dp[k+1][j] + |pos[k] - pos[j]| ),

with G(N) = dp[1][N].  The position convention (pile at the seat of its
largest card) is pinned down by the check values G(6) = 8 and G(16) = 47;
the alternative (smallest card) would give 9 and 54.
"""

import numpy as np
from numba import njit


@njit(cache=True)
def g_of(n):
    # pos[c] = table position of card c, where card at position p is 3^p mod (n+1)
    pos = np.zeros(n + 1, dtype=np.int64)
    val = 1
    for p in range(1, n + 1):
        val = val * 3 % (n + 1)
        pos[val] = p
    # interval DP over card ranges [i..j], 1-indexed
    dp = np.zeros((n + 2, n + 2), dtype=np.int64)
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            best = np.int64(1) << 62
            for k in range(i, j):
                cost = dp[i, k] + dp[k + 1, j] + abs(pos[k] - pos[j])
                if cost < best:
                    best = cost
            dp[i, j] = best
    return dp[1, n]


def main():
    assert g_of(6) == 8
    assert g_of(16) == 47
    return g_of(976)


if __name__ == "__main__":
    print(main())  # 160640
