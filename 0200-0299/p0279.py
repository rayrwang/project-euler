import numba

# Law of cosines makes every angle of an integer triangle have rational
# cosine, and by Niven's theorem the only rational degree angles with
# rational cosine are 60, 90 and 120 (cos = 1/2, 0, -1/2). No triangle has
# two of these except the equilateral (which is simply one 60-degree
# triangle), so the families are disjoint over triangles. Each family is
# counted as sum over primitives of floor(N / p):
#   90:  a, b, c = m^2-n^2, 2mn, m^2+n^2; coprime, opposite parity - each
#        primitive once;
#   60:  a, b, c = m^2-n^2, 2mn-n^2, m^2-mn+n^2 over coprime (m, n); the
#        pairs (m, n) and (m, m-n) give the same triangle, so restrict
#        2n <= m (the self-paired (2, 1) yields the equilateral (1,1,1));
#        the gcd of the triple is 1 or 3 - divide it out;
#   120: a, b, c = m^2-n^2, 2mn+n^2, m^2+mn+n^2 over coprime (m, n); each
#        primitive arises from exactly one generator with triple gcd 1 and
#        one with gcd 3 - keep gcd 1.
# All parametrisations and uniqueness claims were verified exhaustively
# against brute-force enumeration of primitive triangles with perimeter up
# to 3000, and the totals against full brute counts at 3000 and 10000.


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _count(n: int) -> int:
    total = 0
    # 90 degrees
    m = 2
    while 2 * m * (m + 1) <= n:
        for k in range(1, m):
            if (m - k) % 2 == 1 and _gcd(m, k) == 1:
                p = 2 * m * (m + k)
                if p <= n:
                    total += n // p
        m += 1
    # 60 degrees
    m = 2
    while (2 * m - 1) * (m + 1) <= 3 * n:
        for k in range(1, m // 2 + 1):
            if _gcd(m, k) != 1:
                continue
            a = m * m - k * k
            b = 2 * m * k - k * k
            c = m * m - m * k + k * k
            g = _gcd(_gcd(a, b), c)
            p = (a + b + c) // g
            if p <= n:
                total += n // p
        m += 1
    # 120 degrees
    m = 2
    while (2 * m + 1) * (m + 1) <= n:
        for k in range(1, m):
            if _gcd(m, k) != 1:
                continue
            a = m * m - k * k
            b = 2 * m * k + k * k
            c = m * m + m * k + k * k
            if _gcd(_gcd(a, b), c) != 1:
                continue
            p = a + b + c
            if p <= n:
                total += n // p
        m += 1
    return total


def solve(n: int = 10**8) -> int:
    return int(_count(n))


if __name__ == "__main__":
    print(solve())  # 416577688
