import numba


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _count(limit: int) -> int:
    # Euclid: primitive triple a=m^2-n^2, b=2mn, c=m^2+n^2, perimeter 2m(m+n).
    # Inner-square tiling works iff (b-a) | c; this is scale-invariant, so each
    # qualifying primitive contributes floor((limit-1)/P) multiples.
    total = 0
    m = 2
    while 2 * m * (m + 1) < limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and _gcd(m, n) == 1:
                p = 2 * m * (m + n)
                if p >= limit:
                    break
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                d = a - b if a > b else b - a
                if c % d == 0:
                    total += (limit - 1) // p
        m += 1
    return total


def solve(limit: int = 100_000_000) -> int:
    return int(_count(limit))


if __name__ == "__main__":
    print(solve())  # 10057761
