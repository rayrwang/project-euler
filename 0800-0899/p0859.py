"""Project Euler 859: Cookie Game.

Odd may take a pile of 2k+1 cookies, eat one and leave two piles of k;
Even may take a pile of 2k, eat two and leave two piles of k-1.  The
player without a move loses, Odd moving first.  Count the partitions
of 300 for which Even wins.

This is a partizan game and each pile is independent, so the position
is the disjunctive sum of single-pile games.  With Odd as Left, a pile
of 2k+1 has the single option {2 g(k) | } and a pile of 2k the single
option { | 2 g(k-1)}.  By induction every pile value is an *integer*:
g(1) = 1, g(2) = -1, and the simplicity rule gives
    g(2k+1) = 2 g(k) + 1 if g(k) >= 0 else 0,
    g(2k)   = 2 g(k-1) - 1 if g(k-1) <= 0 else 0.
A sum of numbers is a number, and Right (Even) wins moving second
exactly when the total is <= 0.  Since |g(n)| <= n, the weight of a
partition of N lies in [-N, N], and a standard unbounded-knapsack
partition DP over (cookies used, weight sum) counts the partitions of
300 with non-positive total value in about a second.  The code checks
the given C(5) = 2 and C(16) = 64.
"""

from __future__ import annotations


def pile_values(n: int) -> list[int]:
    g = [0] * (n + 1)
    if n >= 1:
        g[1] = 1
    if n >= 2:
        g[2] = -1
    for m in range(3, n + 1):
        if m % 2 == 1:
            t = 2 * g[m // 2]
            g[m] = t + 1 if t >= 0 else 0
        else:
            t = 2 * g[m // 2 - 1]
            g[m] = t - 1 if t <= 0 else 0
    return g


def even_wins(n: int) -> int:
    """Number of partitions of n whose total game value is <= 0."""
    g = pile_values(n)
    offset = n
    width = 2 * n + 1
    dp = [[0] * width for _ in range(n + 1)]
    dp[0][offset] = 1
    for part in range(1, n + 1):
        w = g[part]
        lo = max(0, w)
        hi = min(width, width + w)
        for c in range(part, n + 1):
            src = dp[c - part]
            dst = dp[c]
            for j in range(lo, hi):
                v = src[j - w]
                if v:
                    dst[j] += v
    return sum(dp[n][: offset + 1])


def main() -> None:
    assert even_wins(5) == 2
    assert even_wins(16) == 64
    print(even_wins(300))  # 1527162658488196


if __name__ == "__main__":
    main()
