import math


def solve(h0: float, v: float, g: float) -> float:
    """Volume swept by fragments of a firecracker bursting at height h0.

    Each fragment follows a ballistic arc; over all launch directions the
    trajectories fill the region below the envelope ("parabola of safety")
        Y(r) = h0 + v^2/(2g) - g r^2 / (2 v^2),
    revolved about the vertical axis. With A = h0 + v^2/(2g) the apex height
    and B = g/(2 v^2), the region reaches the ground at r_max^2 = A/B, and the
    shell integral collapses:
        V = integral_0^r_max 2 pi r (A - B r^2) dr = pi A^2 / (2 B) = pi A^2 v^2 / g.
    """
    a = h0 + v * v / (2 * g)
    return math.pi * a * a * v * v / g


if __name__ == "__main__":
    print(f"{solve(100.0, 20.0, 9.81):.4f}")  # 1856532.8455
