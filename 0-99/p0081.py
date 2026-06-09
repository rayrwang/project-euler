def solve():
    """Minimum path sum from top-left to bottom-right moving only right or down."""
    with open("assets/0081_matrix.txt") as f:
        grid = [[int(x) for x in line.split(",")] for line in f]
    n = len(grid)
    # dp[i][j]: cheapest cost to reach cell (i, j); you arrive from above or left.
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                best = 0
            elif i == 0:
                best = dp[i][j - 1]
            elif j == 0:
                best = dp[i - 1][j]
            else:
                best = min(dp[i - 1][j], dp[i][j - 1])
            dp[i][j] = grid[i][j] + best
    return dp[n - 1][n - 1]

if __name__ == "__main__":
    print(solve())  # 427337
