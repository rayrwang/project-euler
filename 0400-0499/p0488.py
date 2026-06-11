"""Project Euler 488: Unbalanced Nim.

Three-heap Nim where no move may create two equal heaps; F(N) sums a + b + c
over the losing-for-next-player positions with 0 < a < b < c < N. Find the
last nine digits of F(10^18).

A full game DP (states ordered by decreasing total, all heap-lowering moves
that keep the heaps distinct) reproduces F(8) = 42 and F(128) = 496062, and
its P-positions reveal a clean closed structure. With t = floor(lg(a + 1))
and a + 1 = 2^t + u (0 <= u < 2^t), the P-positions with smallest heap a are
exactly

    b = 2^(t+1) m + j - 1,    c = b + g,    g = 2^t + u - 2 (j AND u),

over all m >= 1 and window offsets 0 <= j < 2^t. This characterization
matches the DP exactly for every triple with c < 110.

The sum collapses: a + b + c = 2^(t+1) - 3 + 2(u OR j) + 2 B m with
B = 2^(t+1), and the cutoff c < N depends on (u, j) only through
x = u XOR j, since g + j = 2^t + (u XOR j). Grouping the 4^t pairs (u, j)
by x (each x arises from 2^t pairs, with sum of (u OR j) equal to
2^(t-1) (x + 2^t - 1)) gives

  F(N) = sum_t sum_x [ 2^t M (3 * 2^t - 4 + x) + 2^(2t+1) M (M + 1) ],

with M = floor((N - 2^t - x) / 2^(t+1)). For each t the floor takes at most
two values as x sweeps [0, 2^t), so everything reduces to O(log N) interval
sums in exact integers. The closed form agrees with direct enumeration of
the characterization at many cutoffs and with both given values.
"""

import numpy as np
from numba import njit


@njit(cache=True)
def game_dp(n):
    """is_P[a, b, c] for 0 <= a < b < c < n by exhaustive game search."""
    pos = np.zeros((n, n, n), np.bool_)
    for s in range(0, 3 * n):
        for c in range(2, n):
            for b in range(1, c):
                a = s - b - c
                if a < 0 or a >= b:
                    continue
                win = False
                for idx in range(3):
                    top = a if idx == 0 else (b if idx == 1 else c)
                    for v in range(top):
                        x, y, z = a, b, c
                        if idx == 0:
                            x = v
                        elif idx == 1:
                            y = v
                        else:
                            z = v
                        if x == y or y == z or x == z:
                            continue
                        if x > y:
                            x, y = y, x
                        if y > z:
                            y, z = z, y
                        if x > y:
                            x, y = y, x
                        if pos[x, y, z]:
                            win = True
                            break
                    if win:
                        break
                pos[a, b, c] = not win
    return pos


def p_set_from_formula(n):
    out = set()
    t = 1
    while (1 << t) <= n:
        big_b = 1 << (t + 1)
        for u in range(1 << t):
            a = (1 << t) + u - 1
            for j in range(1 << t):
                g = (1 << t) + u - 2 * (j & u)
                m = 1
                while True:
                    b = big_b * m + j - 1
                    c = b + g
                    if c >= n:
                        break
                    out.add((a, b, c))
                    m += 1
        t += 1
    return out


def f_enum(n):
    return sum(a + b + c for (a, b, c) in p_set_from_formula(n))


def f_fast(n):
    total = 0
    t = 1
    while (1 << t) < n:
        tt = 1 << t
        bb = 1 << (t + 1)
        rr = n - tt  # M(x) = (rr - x) // bb, need >= 1
        xmax = min(tt - 1, rr - bb)
        if xmax >= 0:
            r0 = rr % bb
            for x1, x2, m in (
                (0, min(xmax, r0), rr // bb),
                (r0 + 1, xmax, rr // bb - 1),
            ):
                if x2 < x1 or m < 1:
                    continue
                cnt = x2 - x1 + 1
                sx = (x1 + x2) * cnt // 2
                total += tt * m * ((3 * tt - 4) * cnt + sx)
                total += bb * tt * m * (m + 1) * cnt
        t += 1
    return total


if __name__ == "__main__":
    n_check = 110
    pos = game_dp(n_check)
    actual = {
        (a, b, c)
        for a in range(1, n_check)
        for b in range(a + 1, n_check)
        for c in range(b + 1, n_check)
        if pos[a, b, c]
    }
    assert actual == p_set_from_formula(n_check)
    assert f_fast(8) == f_enum(8) == 42
    assert f_fast(128) == f_enum(128) == 496062
    for small in (13, 50, 257, 1000, 5000):
        assert f_fast(small) == f_enum(small)
    print(f_fast(10**18) % 10**9)  # 216737278
