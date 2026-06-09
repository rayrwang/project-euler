import heapq

def solve():
    """Minimum path sum from top-left to bottom-right moving in any of the four
    directions (same matrix as Problem 81) -- a shortest path, solved by Dijkstra."""
    with open("assets/0081_matrix.txt") as f:
        grid = [[int(x) for x in line.split(",")] for line in f]
    n = len(grid)

    dist = [[None] * n for _ in range(n)]
    pq = [(grid[0][0], 0, 0)]      # (cost so far, row, col); cost includes entry cell
    while pq:
        d, i, j = heapq.heappop(pq)
        if dist[i][j] is not None:
            continue               # already finalized with a cheaper cost
        dist[i][j] = d
        if i == n - 1 and j == n - 1:
            return d
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] is None:
                heapq.heappush(pq, (d + grid[ni][nj], ni, nj))
    return -1

if __name__ == "__main__":
    print(solve())  # 425185
