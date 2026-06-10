import numba

# Minimal quadtree length: a region costs 2 bits if uniform, else
# 1 + the four quadrant costs. Against the disk
# (x - 2^(N-1))^2 + (y - 2^(N-1))^2 <= 2^(2N - 2), a pixel box is all black
# iff its farthest corner is inside and all white iff its closest (clamped)
# point is strictly outside - both O(1) tests, so the recursion only
# descends along the circle boundary (~2 pi 2^N leaf-level cells). Verified
# against explicit pixel-array recursion for N = 1..7.


@numba.njit(cache=False)
def _length(x0: int, y0: int, s: int, c: int, r2: int) -> int:
    x1 = x0 + s - 1
    y1 = y0 + s - 1
    dx = max(abs(x0 - c), abs(x1 - c))
    dy = max(abs(y0 - c), abs(y1 - c))
    if dx * dx + dy * dy <= r2:
        return 2
    cx = min(max(c, x0), x1)
    cy = min(max(c, y0), y1)
    if (cx - c) ** 2 + (cy - c) ** 2 > r2:
        return 2
    h = s // 2
    return (
        1
        + _length(x0, y0 + h, h, c, r2)
        + _length(x0 + h, y0 + h, h, c, r2)
        + _length(x0, y0, h, c, r2)
        + _length(x0 + h, y0, h, c, r2)
    )


def solve(n: int = 24) -> int:
    return int(_length(0, 0, 2**n, 2 ** (n - 1), 4 ** (n - 1)))


if __name__ == "__main__":
    print(solve())  # 313135496
