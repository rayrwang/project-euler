def solve(black: int = 60, white: int = 40) -> int:
    # Number of ways to partition (black, white) identical objects into unordered
    # groups: an unbounded 2-D knapsack where each group type (b, w) != (0, 0)
    # is a coin usable any number of times.
    dp = [[0] * (white + 1) for _ in range(black + 1)]
    dp[0][0] = 1
    for b in range(black + 1):
        for w in range(white + 1):
            if b == 0 and w == 0:
                continue
            for i in range(b, black + 1):
                row, prev = dp[i], dp[i - b]
                for j in range(w, white + 1):
                    row[j] += prev[j - w]
    return dp[black][white]


if __name__ == "__main__":
    print(solve())  # 83735848679360680
