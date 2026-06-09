def solve():
    """Minimum path sum from any cell in the left column to any cell in the right
    column, moving up, down, or right (same matrix as Problem 81)."""
    with open("assets/0081_matrix.txt") as f:
        grid = [[int(x) for x in line.split(",")] for line in f]
    n = len(grid)

    cost = [grid[i][0] for i in range(n)]      # costs to be in the left column
    for j in range(1, n):
        # Enter column j by stepping right from the same row...
        nxt = [cost[i] + grid[i][j] for i in range(n)]
        # ...then relax vertical moves within the column: once downward, once up.
        for i in range(1, n):
            nxt[i] = min(nxt[i], nxt[i - 1] + grid[i][j])
        for i in range(n - 2, -1, -1):
            nxt[i] = min(nxt[i], nxt[i + 1] + grid[i][j])
        cost = nxt
    return min(cost)

if __name__ == "__main__":
    print(solve())  # 260324
