import numba
import numpy as np


@numba.jit(cache=True)
def black_counts(checkpoints: np.ndarray) -> np.ndarray:
    """Black-square counts after each step count in `checkpoints` (sorted)."""
    size = 1001
    grid = np.zeros((size, size), dtype=np.uint8)
    x, y = size // 2, size // 2
    dx, dy = 0, 1
    black = 0
    out = np.zeros(len(checkpoints), dtype=np.int64)
    idx = 0
    for step in range(1, int(checkpoints[-1]) + 1):
        if grid[x, y] == 0:
            grid[x, y] = 1
            black += 1
            dx, dy = dy, -dx  # turn clockwise
        else:
            grid[x, y] = 0
            black -= 1
            dx, dy = -dy, dx  # turn counterclockwise
        x += dx
        y += dy
        if step == checkpoints[idx]:
            out[idx] = black
            idx += 1
    return out


if __name__ == "__main__":
    target = 10**18
    period = 104  # the highway recurs every 104 steps
    base = 11_000  # safely past the ~10000-step chaotic transient
    start = base + (target - base) % period  # whole periods from here
    checkpoints = np.array([start + k * period for k in range(5)])
    counts = black_counts(checkpoints)
    gains = np.diff(counts)
    assert np.all(gains == gains[0])  # confirm periodicity, don't assume it
    answer = counts[0] + (target - start) // period * gains[0]
    print(answer)  # 115384615384614952
