import numba

# With a = c, P = (p, a - p) strictly inside AC, brute-force shape
# comparison (sorted squared sides, gcd-normalised) shows the solutions
# split into two disjoint families.
#
# Family 1 (covers all b != d): P is the midpoint of AC, so a = 2m, and
# the similarity condition reduces to (b - a)(d - a) = 2 m^2, verified
# exactly on the brute set. Writing the ordered divisor pair as
# e = 2 g alpha^2, f = g beta^2 (gcd(alpha, beta) = 1, beta odd - the
# unique coprime split of e f = 2 m^2, with m = g alpha beta), the
# perimeter constraint b + d = 4m + e + f < N becomes
# g (2 alpha^2 + 4 alpha beta + beta^2) < N, two ordered pairs per triple.
#
# Family 2 (b = d): the brute table satisfies (b - a)^2 = 2 p q with
# q = a - p on every row, i.e. b = a + 2t with p + q = a, p q = 2 t^2
# (so a^2 - 8 t^2 must be a perfect square); the same coprime split
# {p, q} = {2 g alpha^2, g beta^2} is a bijection onto solutions, with
# b + d = 2(a + 2t) = 2 g (2 alpha^2 + 2 alpha beta + beta^2) < N.
#
# The generated sets match brute force exactly below 100 (74 + 18 = 92)
# and reproduce the given 320471 at 10^5.


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _count(n: int) -> int:
    lim = n - 1
    total = 0
    al = 1
    while 2 * al * al + 4 * al + 1 <= lim:
        be = 1
        while True:
            k1 = 2 * al * al + 4 * al * be + be * be
            if k1 > lim:
                break
            if _gcd(al, be) == 1:
                total += 2 * (lim // k1)
            be += 2
        al += 1
    al = 1
    while 2 * (2 * al * al + 2 * al + 1) <= lim:
        be = 1
        while True:
            k2 = 2 * al * al + 2 * al * be + be * be
            if 2 * k2 > lim:
                break
            if _gcd(al, be) == 1:
                total += lim // (2 * k2)
            be += 2
        al += 1
    return total


def solve(n: int = 10**8) -> int:
    assert _count(100) == 92
    assert _count(10**5) == 320471
    return int(_count(n))


if __name__ == "__main__":
    print(solve())  # 549936643
