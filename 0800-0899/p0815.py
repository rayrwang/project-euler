import numba
import numpy as np


@numba.njit(cache=True)
def _prob_max_at_most(n: int, m: int) -> float:
    """Probability the pile count never exceeds m while dealing 4n cards.

    The shuffle only matters through the profile (a1, a2, a3, a4), the number
    of values with that many cards already dealt; the next card belongs to a
    value with j cards seen with probability (4 - j) a_j / R, R cards left.
    Open piles are a1 + a2 + a3, and only the new-pile move a0 -> a1 can
    increase the count, so capping that single transition at m and pushing
    probability forward in t = a1 + 2 a2 + 3 a3 + 4 a4 (each move adds one
    card) gives the survival probability as the mass reaching (0, 0, 0, n).
    """
    width = n + 1
    dp = np.zeros((width, width, width, width), dtype=np.float64)
    dp[0, 0, 0, 0] = 1.0
    total = 4 * n
    for t in range(total):
        r = total - t
        for a4 in range(min(t // 4, n) + 1):
            rem3 = t - 4 * a4
            for a3 in range(min(rem3 // 3, n - a4) + 1):
                rem2 = rem3 - 3 * a3
                for a2 in range(min(rem2 // 2, n - a4 - a3) + 1):
                    a1 = rem2 - 2 * a2
                    if a1 < 0 or a1 + a2 + a3 + a4 > n:
                        continue
                    p = dp[a1, a2, a3, a4]
                    if p == 0.0:
                        continue
                    a0 = n - a1 - a2 - a3 - a4
                    if a0 > 0 and a1 + 1 + a2 + a3 <= m:
                        dp[a1 + 1, a2, a3, a4] += p * 4 * a0 / r
                    if a1 > 0:
                        dp[a1 - 1, a2 + 1, a3, a4] += p * 3 * a1 / r
                    if a2 > 0:
                        dp[a1, a2 - 1, a3 + 1, a4] += p * 2 * a2 / r
                    if a3 > 0:
                        dp[a1, a2, a3 - 1, a4 + 1] += p * a3 / r
    return dp[0, 0, 0, n]


def expected_max_piles(n: int) -> float:
    """E(n) = sum_{m>=1} P(max >= m) = n - sum_{m<n} P(max <= m)."""
    return n - sum(_prob_max_at_most(n, m) for m in range(n))


if __name__ == "__main__":
    assert f"{expected_max_piles(2):.8f}" == "1.97142857"
    print(f"{expected_max_piles(60):.8f}")  # 54.12691621
