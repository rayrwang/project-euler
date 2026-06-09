import numba
import numpy as np


def _build(rows: int = 1000) -> np.ndarray:
    total = rows * (rows + 1) // 2
    t = np.empty(total, dtype=np.int64)
    s = 0
    mod = 1 << 20
    for k in range(total):
        s = (615949 * s + 797807) % mod
        t[k] = s - (1 << 19)
    return t


@numba.njit(cache=True)
def _min_triangle(t: np.ndarray, rows: int) -> int:
    # per-row prefix sums (padded) so any row segment is O(1)
    p = np.zeros((rows, rows + 1), dtype=np.int64)
    off = 0
    for r in range(rows):
        acc = 0
        for c in range(r + 1):
            acc += t[off + c]
            p[r, c + 1] = acc
        off += r + 1
    best = t[0]
    for i in range(rows):          # apex row
        for j in range(i + 1):     # apex column
            running = 0
            for d in range(rows - i):
                r = i + d
                running += p[r, j + d + 1] - p[r, j]  # cols j..j+d of row r
                if running < best:
                    best = running
    return best


def solve(rows: int = 1000) -> int:
    return int(_min_triangle(_build(rows), rows))


if __name__ == "__main__":
    print(solve())  # -271248680
