import math

from numba import njit


@njit(cache=True)
def _isqrt(n: int) -> int:
    if n < 1:
        return 0
    x = int(math.sqrt(n))
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@njit(cache=True)
def _disk_lt(r2: int) -> int:
    # Lattice points strictly inside a circle of radius^2 = r2 (Gauss circle).
    if r2 <= 0:
        return 0
    u_max = _isqrt(r2 - 1)
    half = 0
    for u in range(1, u_max + 1):
        m = r2 - u * u
        if m >= 1:
            half += 2 * _isqrt(m - 1) + 1
    return (2 * _isqrt(r2 - 1) + 1) + 2 * half


def solve(r: int = 10**9) -> int:
    # B makes triangle OBC obtuse (C = (r/4, r/4)) in three disjoint ways:
    # angle O obtuse  -> half-plane x + y < 0,
    # angle C obtuse  -> half-plane x + y > r/2,
    # angle B obtuse  -> open disk on diameter OC, centre (r/8, r/8), R^2 = r^2/32.
    # Each region is intersected with the diamond |x| + |y| <= r and stripped of
    # the degenerate collinear points on the line x = y.
    total = 2 * r * r + 2 * r + 1
    even = (r + 1) if r % 2 == 0 else r
    odd = (2 * r + 1) - even

    region_o = (total - even) // 2 - r // 2
    lo, hi = r // 2 + 1, r
    even_c = hi // 2 - (lo - 1) // 2
    odd_c = (hi - lo + 1) - even_c
    region_c = even_c * even + odd_c * odd - (r // 2 - r // 4)
    region_b = _disk_lt(r * r // 32) - (r // 4 - 1)
    return region_o + region_c + region_b


if __name__ == "__main__":
    print(solve())  # 1598174770174689458
