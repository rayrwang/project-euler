"""Project Euler 849: The Tournament.

Each pair of teams plays twice and the four points of a pairing can
split as (4,0), (3,1), (2,2), (1,3) or (0,4) — every integer split is
realisable (win+win, win+draw, win+loss or draw+draw, ...).  So the
possible final outcomes are exactly the score multisets of a 4-fold
generalised tournament, and by Landau/Moon's theorem an ascending
vector s_1 <= ... <= s_n is achievable iff every prefix satisfies
sum_{i<=k} s_i >= 4 binom(k, 2) with equality at k = n.  (A brute
force over all 5^binom(n,2) split assignments confirms this
characterisation for n <= 4.)

Counting the Landau sequences is a dynamic program over (last value
s, slack), where slack_k = sum_{i<=k} s_i - 4 binom(k, 2) must stay
non-negative and return to zero at the end.  Adding team k+1 with
value s' >= s shifts the slack by s' - 4k, so with a cumulative sum
over the value axis each transition is a single slice copy and the
whole table updates in O(v_max) vectorised operations per team.  The
slack never needs to exceed about n^2 (early values cannot outrun the
fixed total under monotonicity); the result is unchanged when the cap
is raised by half.  The code reproduces F(2) = 3 and F(7) = 32923 and
computes F(100) modulo 10^9 + 7 in a few seconds.
"""

from __future__ import annotations

from itertools import combinations, product

import numpy as np

MOD = 10**9 + 7


def outcomes(n: int, slack_cap: int | None = None) -> int:
    vmax = 4 * (n - 1)
    if slack_cap is None:
        slack_cap = n * n + 10
    dp = np.zeros((vmax + 1, slack_cap + 1), dtype=np.int64)
    for v in range(min(vmax, slack_cap) + 1):
        dp[v][v] = 1
    for k in range(1, n):
        cum = np.cumsum(dp, axis=0) % MOD
        ndp = np.zeros_like(dp)
        for sp in range(vmax + 1):
            shift = sp - 4 * k
            if shift >= 0:
                ndp[sp, shift:] = cum[sp, : slack_cap + 1 - shift]
            else:
                ndp[sp, : slack_cap + 1 + shift] = cum[sp, -shift:]
        dp = ndp
    return int(dp[:, 0].sum() % MOD)


def outcomes_brute(n: int) -> int:
    pairs = list(combinations(range(n), 2))
    seen = set()
    for splits in product(range(5), repeat=len(pairs)):
        score = [0] * n
        for (a, b), k in zip(pairs, splits):
            score[a] += k
            score[b] += 4 - k
        seen.add(tuple(sorted(score)))
    return len(seen)


def main() -> None:
    for n in (2, 3, 4):
        assert outcomes(n) == outcomes_brute(n)
    assert outcomes(7) == 32923
    print(outcomes(100))  # 936203459


if __name__ == "__main__":
    main()
