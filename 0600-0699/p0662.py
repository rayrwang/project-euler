"""Project Euler Problem 662: Fibonacci Paths.

Steps go from (a, b) to (a + x, b + y) with x, y >= 0 and sqrt(x^2 + y^2) a
Fibonacci number from {1, 2, 3, 5, ...}.  Useful steps have both components
at most 10^4, so the Fibonacci lengths run up to 10946 (allowed when split
diagonally, e.g. 10946^2 = 4870^2 + 9804^2); for each length F collect the
axis steps (F, 0), (0, F) with F <= W and every Pythagorean decomposition
x^2 + y^2 = F^2 with x, y >= 1 by scanning x and testing F^2 - x^2 for
squareness.

Then a plain path-count DP over the (W+1) x (H+1) grid: each cell sums its
predecessors over all steps, row by row so every source is final before it
is read (steps with x = 0 stay inside the current row but only look left).
About 10^8 cells times 70-odd steps in numba, with int32 storage keeping
the 10001 x 10001 table at 400 MB.

Checks: F(3, 4) = 278 and F(10, 10) = 215846462.
"""

from math import isqrt

import numba
import numpy as np

MOD = 10**9 + 7


def fibonacci_steps(limit: int) -> np.ndarray:
    fibs = [1, 2]
    while fibs[-1] <= limit * 2:  # diagonal steps can use F up to limit*sqrt(2)
        fibs.append(fibs[-1] + fibs[-2])
    steps = []
    for f in fibs:
        if f <= limit:
            steps.append((f, 0))
            steps.append((0, f))
        for x in range(1, min(f, limit) + 1):
            y2 = f * f - x * x
            y = isqrt(y2)
            if 1 <= y <= limit and y * y == y2:
                steps.append((x, y))
    return np.array(sorted(set(steps)), dtype=np.int64)


@numba.jit(cache=True)
def count_paths(W: int, H: int, steps: np.ndarray) -> int:
    grid = np.zeros((H + 1, W + 1), dtype=np.int32)
    grid[0, 0] = 1
    for i in range(H + 1):
        for j in range(W + 1):
            total = np.int64(grid[i, j])
            for s in range(len(steps)):
                x, y = steps[s, 0], steps[s, 1]
                if i >= y and j >= x and (x or y):
                    total += grid[i - y, j - x]
            grid[i, j] = total % MOD
    return int(grid[H, W])


if __name__ == "__main__":
    steps = fibonacci_steps(10**4)
    assert count_paths(3, 4, steps) == 278
    assert count_paths(10, 10, steps) == 215846462
    print(count_paths(10**4, 10**4, steps))  # 860873428
