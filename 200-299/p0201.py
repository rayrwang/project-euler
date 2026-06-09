import numpy as np


def solve(n: int = 100, k: int = 50) -> int:
    # dp[j][s] = number of j-element subsets of {1^2, ..., n^2} summing to s,
    # counts capped at 2 since only sums reachable by exactly one subset matter.
    items = [i * i for i in range(1, n + 1)]
    smax = sum(items)
    dp = np.zeros((k + 1, smax + 1), dtype=np.int8)
    dp[0][0] = 1
    for x in items:
        for j in range(k, 0, -1):
            dp[j][x:] = np.minimum(2, dp[j][x:] + dp[j - 1][: smax + 1 - x])
    row = dp[k]
    return int(np.dot(np.arange(smax + 1)[row == 1], np.ones((row == 1).sum(), dtype=object)))


if __name__ == "__main__":
    print(solve())  # 115039000
