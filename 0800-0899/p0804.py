import math

import numba

N = 10**16


@numba.jit(cache=True)
def isqrt_i64(d: int) -> int:
    """Exact integer floor square root of d (0 <= d < 2^63)."""
    s = int(math.sqrt(d))
    while s * s > d:
        s -= 1
    while (s + 1) * (s + 1) <= d:
        s += 1
    return s


@numba.jit(cache=True)
def count_x(y: int, n: int) -> int:
    """Number of integers x with x^2 + x y + 41 y^2 <= n.

    Multiplying by 4 and completing the square gives the equivalent integer
    condition (2x + y)^2 <= 4n - 163 y^2 (note 163 = 4*41 - 1 is the negative
    discriminant of the form). With s = floor(sqrt(4n - 163 y^2)) this is
    -s <= 2x + y <= s, a contiguous range of x whose size is counted exactly.
    """
    d = 4 * n - 163 * y * y
    if d < 0:
        return 0
    s = isqrt_i64(d)
    hi = (s - y) // 2  # floor((s - y)/2)
    lo = (-s - y + 1) // 2  # ceil((-s - y)/2)
    return hi - lo + 1 if hi >= lo else 0


@numba.jit(cache=True)
def solve(n: int) -> int:
    """T(n) = #{(x, y) in Z^2 : 1 <= x^2 + x y + 41 y^2 <= n}.

    Summing g over 1..n counts every lattice point whose form value lands in
    [1, n]. The count of x is even in y, so sum y >= 1 and double, add the
    y = 0 row, and subtract the single origin (where the form is 0).
    """
    y_max = isqrt_i64(4 * n // 163) + 2
    total = count_x(0, n)
    for y in range(1, y_max + 1):
        total += 2 * count_x(y, n)
    return total - 1


if __name__ == "__main__":
    print(solve(N))  # 4921370551019052
