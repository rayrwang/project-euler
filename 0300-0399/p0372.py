import sys
from math import isqrt


def floor_sum_sqrt(n: int, p: int, q: int, d: int) -> int:
    """sum_{x=1}^n floor( x*(p+sqrt(d))/q ) for a positive value, q>0 and the
    invariant q | (d - p^2).  Walks the continued fraction of sqrt(d): peel the
    integer part, then reflect the fractional slope into its reciprocal (the
    standard PQa transition keeps everything integral), giving O(log n) depth.
    """
    if n <= 0:
        return 0
    a = (p + isqrt(d)) // q
    res = a * n * (n + 1) // 2
    p2 = p - a * q  # remaining slope (p2 + sqrt(d))/q lies in [0, 1)
    m = (n * p2 + isqrt(n * n * d)) // q
    if m > 0:
        qn = (d - p2 * p2) // q
        res += m * n - floor_sum_sqrt(m, -p2, qn, d)
    return res


def floor_root_sum(n: int, k: int) -> int:
    """sum_{x=1}^n floor(x*sqrt(k))."""
    if n <= 0:
        return 0
    s = isqrt(k)
    if s * s == k:
        return s * n * (n + 1) // 2
    return floor_sum_sqrt(n, 0, 1, k)


def lattice_count(m: int, n: int) -> int:
    """Number of lattice points (x, y) with m < x <= n, m < y <= n and
    floor(y^2 / x^2) odd.

    Using floor(y^2/x^2) odd <=> (-1)^floor = -1, the count is
    (n-m)^2/2 - (1/2)(P_N - P_M) where P_Y = sum_{x=m+1..n} sum_{y=1..Y}
    (-1)^floor(y^2/x^2).  For Y=m every term vanishes (y<x), so P_M=(n-m)m.
    Writing the inner sign sum as N + 2*sum_k (-1)^k (N - floor(x*sqrt k)) and
    swapping the order of summation leaves, for each k, the band
    x in (m, floor(n/sqrt k)], whose floor(x*sqrt k) sum is the quadratic-
    irrational floor-sum above.  Perfect-square k carry a +1 boundary term.
    """
    big = n * n
    total = 0
    k = 1
    while True:
        s = isqrt(k)
        square = s * s == k
        if square:
            xk = n // s
        else:
            xk = isqrt(big // k)
            while (xk + 1) ** 2 * k <= big:
                xk += 1
            while xk * xk * k > big:
                xk -= 1
        if xk <= m:
            break
        if square:
            inner = (n + 1) * (xk - m) - s * (xk * (xk + 1) - m * (m + 1)) // 2
        else:
            inner = n * (xk - m) - (floor_root_sum(xk, k) - floor_root_sum(m, k))
        total += inner if k % 2 == 0 else -inner
        k += 1
    sum_pn = (n - m) * n + 2 * total
    sum_pm = (n - m) * m
    val = (n - m) * (n - m) - (sum_pn - sum_pm)
    return val // 2


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    assert lattice_count(0, 100) == 3019
    assert lattice_count(100, 10000) == 29750422
    print(lattice_count(2_000_000, 10**9))  # 301450082318807027
