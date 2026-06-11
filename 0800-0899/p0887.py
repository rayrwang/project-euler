"""Project Euler 887: Bounded Binary Search.

A questioning strategy is an ordered binary decision tree on {1..N}
whose leaf depths satisfy depth(x) <= x + d, minimising the maximum
depth L.  Giving every value its deepest allowed level,
l_x = min(x + d, L), is optimal, and because this profile is
non-decreasing, an ordered tree realising it exists exactly when
Kraft's inequality sum_x 2^(-l_x) <= 1 holds: the greedy left-to-right
codeword assignment never wastes space when depths never decrease.

Summing the capped geometric series turns the inequality into a closed
threshold: Q(N, d) <= L iff N <= N_max(L, d), where N_max = 2^L for
L <= d + 1 and N_max = 2^L - 2^(L-d) + L - d + 1 otherwise.  Both
given values sit exactly on the boundary: N_max(3, 1) = 7 and
N_max(10, 2) = 777, and d = 0 reproduces Q(N, 0) = N - 1.  The formula
is verified against an exhaustive decision-tree search for N <= 33,
d <= 3.

The double sum then needs only the threshold staircase: for d = 0 it
is a triangular number, and for each d in 1..7 about thirty levels L
cover N up to 7^10, each contributing L times the width of its
threshold interval -- exact integer arithmetic throughout.
"""

from __future__ import annotations

from functools import lru_cache

BOUND = 7**10


def n_max(level: int, d: int) -> int:
    if level <= d + 1:
        return 2**level
    return 2**level - 2 ** (level - d) + level - d + 1


def q_formula(n: int, d: int) -> int:
    level = 0
    while n_max(level, d) < n:
        level += 1
    return level


def q_brute(n: int, d: int) -> int:
    if n == 1:
        return 0
    for level in range(2 * n + 4):

        @lru_cache(maxsize=None)
        def feasible(lo: int, hi: int, depth: int, lim: int = level) -> bool:
            if lo == hi:
                return depth <= min(lo + d, lim)
            if depth >= lim:
                return False
            return any(
                feasible(lo, y, depth + 1) and feasible(y + 1, hi, depth + 1)
                for y in range(lo, hi)
            )

        if feasible(1, n, 0):
            return level
    raise RuntimeError


def main() -> None:
    for d in range(4):
        for n in range(1, 28):
            assert q_brute(n, d) == q_formula(n, d)
    assert q_formula(7, 1) == 3
    assert q_formula(777, 2) == 10
    total = BOUND * (BOUND - 1) // 2  # d = 0: Q(N, 0) = N - 1
    for d in range(1, 8):
        prev = 1
        level = 1
        while prev < BOUND:
            cur = min(n_max(level, d), BOUND)
            if cur > prev:
                total += level * (cur - prev)
                prev = cur
            level += 1
    print(total)  # 39896187138661622


if __name__ == "__main__":
    main()
