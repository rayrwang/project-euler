import numba
import numpy as np


def _build_grid(n: int = 2000) -> np.ndarray:
    total = n * n
    s = np.empty(total + 1, dtype=np.int64)  # 1-indexed
    for k in range(1, 56):
        s[k] = (100003 - 200003 * k + 300007 * k * k * k) % 1000000 - 500000
    for k in range(56, total + 1):
        s[k] = (s[k - 24] + s[k - 55] + 1000000) % 1000000 - 500000
    return s[1:].reshape(n, n)


@numba.njit(cache=True)
def _best(grid: np.ndarray) -> int:
    n = grid.shape[0]
    best = grid[0, 0]

    # rows and columns and both diagonals via Kadane
    for i in range(n):
        cur = 0
        for j in range(n):  # row
            cur = grid[i, j] + (cur if cur > 0 else 0)
            if cur > best:
                best = cur
        cur = 0
        for j in range(n):  # column
            cur = grid[j, i] + (cur if cur > 0 else 0)
            if cur > best:
                best = cur
    # diagonals (down-right) starting on top row / left col
    for start in range(n):
        cur = 0
        i, j = 0, start
        while i < n and j < n:
            cur = grid[i, j] + (cur if cur > 0 else 0)
            if cur > best:
                best = cur
            i += 1
            j += 1
        if start != 0:
            cur = 0
            i, j = start, 0
            while i < n and j < n:
                cur = grid[i, j] + (cur if cur > 0 else 0)
                if cur > best:
                    best = cur
                i += 1
                j += 1
    # anti-diagonals (down-left) starting on top row / right col
    for start in range(n):
        cur = 0
        i, j = 0, start
        while i < n and j >= 0:
            cur = grid[i, j] + (cur if cur > 0 else 0)
            if cur > best:
                best = cur
            i += 1
            j -= 1
        if start != n - 1:
            cur = 0
            i, j = start, n - 1
            while i < n and j >= 0:
                cur = grid[i, j] + (cur if cur > 0 else 0)
                if cur > best:
                    best = cur
                i += 1
                j -= 1
    return best


def solve() -> int:
    return int(_best(_build_grid()))


if __name__ == "__main__":
    print(solve())  # 52852124
