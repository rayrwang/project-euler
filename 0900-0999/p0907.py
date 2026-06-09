"""Project Euler 907: Stacking Cups.

A tower is a bottom-to-top sequence of all n cups, each up (1) or down
(0), where a lower cup (j, o) may support an upper cup (j', o') iff

    nest:         o = o' = 1 and j = j' + 1   (j' sits inside j)
                  o = o' = 0 and j' = j + 1   (j' lowered over j)
    base-to-base: o = 0, o' = 1, |j - j'| = 2
    rim-to-rim:   o = 1, o' = 0, |j - j'| = 2

(the forbidden "two cups rim-to-rim on one cup" never occurs in a single
tower, where each cup supports at most one other).  This model
reproduces all three given values, S(4) = 12, S(8) = 58, S(20) = 5560.

S(n) counts directed Hamiltonian paths in this oriented-cup graph.  For
small n that is a bitmask DP over (used set, last cup, last orientation)
with at most four extensions per state, since all edges join labels at
distance <= 2.  The bounded bandwidth also means the count satisfies a
short linear recurrence; fitting the DP values gives, for n >= 10,

    S(n) = 2 S(n-1) - 3 S(n-2) + 5 S(n-3) - 4 S(n-4)
         + 4 S(n-5) - 3 S(n-6) + S(n-7) - S(n-8)

(a single transient at S(9) = 82, where the fit would give 84).  The
characteristic polynomial factors as (x - 1)(x^2 + 1)^2 (x^3 - x^2 - 1),
so the growth rate is the plastic-like root of x^3 = x^2 + 1.  The
recurrence is verified against the DP for every n in 10..20 (including
the given S(20)) and then iterated mod 10^9 + 7 up to n = 10^7.
"""

import numba
import numpy as np

P = 10**9 + 7


@numba.njit(cache=True)
def s_small(n: int) -> int:
    """Exact S(n) by DP over (mask, last cup, last orientation)."""
    dp = np.zeros((1 << n, n, 2), dtype=np.int64)
    for i in range(n):
        dp[1 << i, i, 0] = 1
        dp[1 << i, i, 1] = 1
    full = (1 << n) - 1
    for mask in range(1, full + 1):
        for last in range(n):
            if not (mask >> last) & 1:
                continue
            for ol in range(2):
                v = dp[mask, last, ol]
                if v == 0:
                    continue
                for up in range(max(0, last - 2), min(n, last + 3)):
                    if (mask >> up) & 1:
                        continue
                    d = up - last
                    for ou in range(2):
                        good = (
                            (ol == 1 and ou == 1 and d == -1)
                            or (ol == 0 and ou == 0 and d == 1)
                            or ((ol + ou == 1) and abs(d) == 2)
                        )
                        if good:
                            dp[mask | (1 << up), up, ou] += v
    tot = 0
    for last in range(n):
        for ol in range(2):
            tot += dp[full, last, ol]
    return tot


@numba.njit(cache=True)
def s_big(n: int, seed: np.ndarray) -> int:
    """S(n) mod P from the order-8 recurrence; seed = S(2..9)."""
    v = seed.copy()
    have = 9
    while have < n:
        nxt = (
            2 * v[7] - 3 * v[6] + 5 * v[5] - 4 * v[4]
            + 4 * v[3] - 3 * v[2] + v[1] - v[0]
        ) % P
        for i in range(7):
            v[i] = v[i + 1]
        v[7] = nxt
        have += 1
    return v[7] % P


def solve(n: int) -> int:
    small = [s_small(k) for k in range(1, 21)]
    assert small[3] == 12 and small[7] == 58 and small[19] == 5560
    seed = np.array(small[1:9], dtype=np.int64)  # S(2)..S(9)
    for k in range(10, 21):  # recurrence agrees with DP on 10..20
        assert s_big(k, seed) == small[k - 1] % P
    return s_big(n, seed)


if __name__ == "__main__":
    print(solve(10**7))  # 196808901
