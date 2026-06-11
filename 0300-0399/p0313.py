from collections import deque

import numba
import numpy as np

from funcs import prime_sieve_bool


def s_bfs(m: int, n: int) -> int:
    """Exact S(m, n) by BFS over (red square, blank square) states.

    All counters except the red one are interchangeable, so the position is
    fully described by where the red counter and the blank are.
    """
    start = ((0, 0), (m - 1, n - 1))
    goal_red = (m - 1, n - 1)
    dist = {start: 0}
    queue = deque([start])
    while queue:
        red, blank = queue.popleft()
        d = dist[(red, blank)]
        if red == goal_red:
            return d
        bx, by = blank
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            cx, cy = bx + dx, by + dy  # counter sliding into the blank
            if not (0 <= cx < m and 0 <= cy < n):
                continue
            new_red = blank if (cx, cy) == red else red
            state = (new_red, (cx, cy))
            if state not in dist:
                dist[state] = d + 1
                queue.append(state)
    raise ValueError("unsolvable grid")


def s_formula(m: int, n: int) -> int:
    """S(m, n) for m >= n >= 2, matching the BFS on small grids."""
    if m < n:
        m, n = n, m
    if m == n:
        return 5 if n == 2 else 8 * n - 11
    return 6 * m + 2 * n - 13


@numba.jit(cache=True)
def count_grids(limit: int, is_pr: np.ndarray) -> int:
    """Number of grids with S(m, n) = p^2 over primes p < limit.

    The diagonal family 8n - 11 = 5 (mod 8) never hits an odd p^2 = 1 (mod 8),
    and 6m + 2n - 13 is odd, ruling out p = 2.  For odd p set
    t = (p^2 + 13) / 2 so the equation becomes 3m + n = t with n >= 2, m > n,
    i.e. t/4 < m <= (t - 2)/3; double for both orientations.
    """
    total = 0
    for p in range(3, limit):
        if not is_pr[p]:
            continue
        t = (p * p + 13) // 2
        hi = (t - 2) // 3
        lo = t // 4  # m > t/4 strictly; t is never divisible by 4 (t is odd)
        if hi > lo:
            total += 2 * (hi - lo)
    return total


if __name__ == "__main__":
    assert s_bfs(2, 2) == 5
    assert s_bfs(5, 4) == 25
    for m in range(2, 7):
        for n in range(2, m + 1):
            assert s_bfs(m, n) == s_formula(m, n)

    is_pr = prime_sieve_bool(1_000_000)
    assert count_grids(100, is_pr) == 5482
    print(count_grids(1_000_000, is_pr))  # 2057774861813004
