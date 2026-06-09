from math import isqrt

# Expanding both square sums and completing squares turns the pivot
# condition into a Pell-type form: with X = 2k - m, Y = 2n + m + 1,
#     (m + 1) X^2 - m Y^2 = -m (m + 1),
# whose solutions are permuted by the automorphism from the unit
# t^2 - 4 m (m + 1) s^2 = 1, (t, s) = (2m + 1, 2):
#     (X, Y) -> (t X + 2 m Y, 2 (m + 1) X + t Y).
# Fundamental solutions satisfy 0 <= X <= m (X = m, Y = m + 1 is the obvious
# degenerate pivot k = m, n = 0); moreover m | X^2 since
# m Y^2 = (m + 1)(X^2 + m), so candidate X are the multiples of
# r(m) = prod p^ceil(e/2). A second class with X = 0 exists exactly when
# m + 1 is a perfect square - missing it loses pivots such as k = 820
# (m = 8, n = 861). Each fundamental (X, Y) is expanded forward from both
# (X, Y) and (-X, Y); n >= k requires leaving the degenerate seeds. The
# smallest non-trivial pivot per m is 2 m (m + 1), bounding m. Verified
# against brute force for k <= 3000 (exact set) and k <= 10^6 (sum).


def _square_root_radical(m: int, spf: list[int]) -> int:
    r = 1
    while m > 1:
        p = spf[m]
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        r *= p ** ((e + 1) // 2)
    return r


def solve(limit: int = 10**10) -> int:
    m_max = isqrt(limit // 2) + 2
    spf = list(range(m_max + 2))
    for i in range(2, isqrt(m_max + 2) + 1):
        if spf[i] == i:
            for j in range(i * i, m_max + 2, i):
                if spf[j] == j:
                    spf[j] = i

    pivots: set[int] = set()
    m = 1
    while 2 * m * (m + 1) <= limit:
        t = 2 * m + 1
        r = _square_root_radical(m, spf)
        x0 = 0
        while x0 <= m:
            num = (m + 1) * (x0 * x0 + m)
            if num % m == 0:
                y2 = num // m
                y0 = isqrt(y2)
                if y0 * y0 == y2 and (x0 - m) % 2 == 0 and (y0 - m - 1) % 2 == 0:
                    for sx in (1,) if x0 == 0 else (1, -1):
                        x, y = sx * x0, y0
                        while True:
                            k = (x + m) // 2
                            if k > limit:
                                break
                            if x > 0:
                                n = (y - m - 1) // 2
                                if n >= k:
                                    pivots.add(k)
                            x, y = t * x + 2 * m * y, 2 * (m + 1) * x + t * y
            x0 += r
        m += 1
    return sum(pivots)


if __name__ == "__main__":
    print(solve())  # 238890850232021
