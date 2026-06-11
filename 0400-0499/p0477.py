"""Project Euler 477: Number Sequence Game.

Two players alternately take the first or last element of a sequence, each
maximizing their own total; F(N) is player 1's optimal score on the quadratic
PRNG sequence s_{i+1} = (s_i^2 + 45) mod 1000000007, s_1 = 0. Find F(10^8).

The interval DP is O(N^2), hopeless at N = 10^8. The classical reduction: if
b is an interior element with neighbors a, c and b >= a, b >= c (a local
maximum), then replacing the triple by the single value a - b + c preserves
the optimal score difference - in optimal play one player ends up with b and
the other with both a and c, so the triple acts as one signed unit. Applying
this with a stack while streaming the sequence costs O(N) total and leaves a
sequence with no interior local maxima, i.e. V-shaped (decreasing then
increasing). On a V-shaped sequence optimal play is greedy: every turn the
current player takes the larger end. The first player's score is then
(total + D) / 2, with D the alternating-sign greedy sum of the reduced
stack and total the sum of the original sequence.

The merge lemma plus greedy endgame is verified against the full O(N^2)
interval DP on hundreds of random sequences (including negative values, which
arise inside merges), and reproduces all four given values F(2), F(4),
F(100), F(10^4). The 10^8 run collapses the stack to a handful of elements
and finishes in about a second.
"""

import numpy as np
from numba import njit

MOD = 1000000007
N = 10**8


@njit(cache=True)
def dp_f(s):
    n = len(s)
    if n == 0:
        return np.int64(0)
    diff = s.copy().astype(np.int64)
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            left = s[i] - diff[i + 1]
            right = s[j] - diff[i]
            diff[i] = max(left, right)
    total = np.int64(0)
    for v in s:
        total += v
    return (total + diff[0]) // 2


@njit(cache=True)
def fast_f(s):
    n = len(s)
    st = np.empty(n, np.int64)
    top = -1
    for v in s:
        top += 1
        st[top] = v
        while top >= 2 and st[top - 1] >= st[top - 2] and st[top - 1] >= st[top]:
            merged = st[top - 2] - st[top - 1] + st[top]
            top -= 2
            st[top] = merged
    lo, hi = 0, top
    d = np.int64(0)
    sign = np.int64(1)
    while lo <= hi:
        if st[lo] >= st[hi]:
            d += sign * st[lo]
            lo += 1
        else:
            d += sign * st[hi]
            hi -= 1
        sign = -sign
    total = np.int64(0)
    for v in s:
        total += v
    return (total + d) // 2


@njit(cache=True)
def solve_stream(n):
    st = np.empty(n, np.int64)
    top = -1
    x = np.int64(0)
    total = np.int64(0)
    for _ in range(n):
        v = x
        total += v
        x = x * x % MOD
        x = (x + 45) % MOD
        top += 1
        st[top] = v
        while top >= 2 and st[top - 1] >= st[top - 2] and st[top - 1] >= st[top]:
            merged = st[top - 2] - st[top - 1] + st[top]
            top -= 2
            st[top] = merged
    lo, hi = 0, top
    d = np.int64(0)
    sign = np.int64(1)
    while lo <= hi:
        if st[lo] >= st[hi]:
            d += sign * st[lo]
            lo += 1
        else:
            d += sign * st[hi]
            hi -= 1
        sign = -sign
    return (total + d) // 2


def gen_seq(n):
    s = np.empty(n, np.int64)
    x = 0
    for i in range(n):
        s[i] = x
        x = (x * x + 45) % MOD
    return s


if __name__ == "__main__":
    rng = np.random.default_rng(7)
    for _ in range(400):
        n_small = int(rng.integers(1, 40))
        s = rng.integers(-50, 100, n_small).astype(np.int64)
        assert dp_f(s) == fast_f(s)
    for n_chk, expect in ((2, 45), (4, 4284990), (100, 26365463243), (10**4, 2495838522951)):
        assert fast_f(gen_seq(n_chk)) == expect
    print(solve_stream(N))  # 25044905874565165
