from functools import cache
from math import isqrt

PHI_NUM = (1 + 5**0.5) / 2  # only used in the brute-force check


@cache
def is_losing(x: int, y: int) -> bool:
    """Game-tree evaluation of the position (x, y), x <= y."""
    if x == y or y % x == 0:
        return False  # a pile can be emptied immediately
    return all(
        not is_losing(*sorted((x, y - k * x)))
        for k in range(1, y // x + 1)
        if y - k * x > 0
    )


def floor_div_phi(n: int) -> int:
    """floor(n / phi) = floor(n (sqrt(5) - 1) / 2), exactly."""
    return (isqrt(5 * n * n) - n) // 2


def beatty(n: int) -> tuple[int, int, int]:
    """(sum of f, sum of x f, sum of f^2) for f = floor(phi x), x = 1..n.

    Counting lattice points under y = phi x turns each sum into one over
    the reflected region: with m = floor(n / phi) and g(y) = floor(y / phi),
        sum f       = n m       - sum g
        sum x f     = m n(n+1)/2 - (sum g^2 + sum g) / 2
        sum f^2     = n m^2 + m n(n+1) + Sq - sum g^2 - 2 sum y g(y)
    (the last after also splitting phi = 1 + 1/phi), where Sq is the sum
    of squares. Since 1/phi = phi - 1, the inner sums are the same triple
    at m = floor(n / phi) < 0.62 n, so the recursion terminates in
    O(log n) exact-integer steps.
    """
    if n <= 0:
        return 0, 0, 0
    m = floor_div_phi(n)
    t0m, t1m, t2m = beatty(m)
    sq = n * (n + 1) * (2 * n + 1) // 6
    tri = n * (n + 1) // 2
    t0 = tri + n * m - t0m
    t1 = sq + m * tri - (t2m + t0m) // 2  # t2m + t0m = sum g(g+1), even
    t2 = sq + m * n * (n + 1) + n * m * m - t2m - 2 * t1m
    return t0, t1, t2


def s_total(n: int) -> int:
    """Sum of x + y over losing positions 0 < x < y <= n.

    The game is the Euclid game: (x, y) with x < y is losing exactly when
    y < phi x (verified below against full game-tree search). Splitting at
    x1 = floor(n / phi) + 1, the y-range cap is floor(phi x) below x1 and
    n at or above it; both pieces reduce to the Beatty power sums and
    Faulhaber formulas.
    """
    x1 = floor_div_phi(n) + 1
    m = x1 - 1
    t0, t1, t2 = beatty(m)
    sx = m * (m + 1) // 2
    sx2 = m * (m + 1) * (2 * m + 1) // 6
    region1 = t1 - sx2 + (t2 + t0 - sx2 - sx) // 2
    lo, hi = x1, n - 1
    region2 = 0
    if lo <= hi:
        s1 = hi * (hi + 1) // 2 - (lo - 1) * lo // 2
        s2 = (
            hi * (hi + 1) * (2 * hi + 1) // 6
            - (lo - 1) * lo * (2 * lo - 1) // 6
        )
        cnt = hi - lo + 1
        region2 = n * s1 - s2 + (cnt * n * (n + 1) - s2 - s1) // 2
    return region1 + region2


if __name__ == "__main__":
    # The losing positions are exactly x < y < phi x (Euclid game).
    for x in range(1, 40):
        for y in range(x + 1, 41):
            assert is_losing(x, y) == (y < PHI_NUM * x), (x, y)
    assert s_total(10) == 211
    assert s_total(10**4) == 230312207313
    print(s_total(10**16) % 7**10)  # 54672965
