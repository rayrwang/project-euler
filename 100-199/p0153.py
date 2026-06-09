import math

import numba


@numba.njit(cache=True)
def _dsum(k: int) -> int:
    # sum_{n<=k} sigma(n) = sum_d d*floor(k/d), via hyperbola blocking.
    s = 0
    d = 1
    while d <= k:
        q = k // d
        hi = k // q
        s += q * (d + hi) * (hi - d + 1) // 2
        d = hi + 1
    return s


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _total(n: int, r: int) -> int:
    # T(N) = sum over primitive (a',b'), a'>=1, of a' * D(N // (a'^2+b'^2)),
    # where D(K) = sum_{m<=K} sigma(m). b'=0 only for a'=1; both signs of b'>0.
    total = 0
    for a in range(1, r + 1):
        a2 = a * a
        if a2 > n:
            break
        if a == 1:
            total += _dsum(n)        # (1, 0): real divisors
        b = 1
        while a2 + b * b <= n:
            if _gcd(a, b) == 1:
                total += 2 * a * _dsum(n // (a2 + b * b))
            b += 1
    return total


def solve(n: int = 100_000_000) -> int:
    return int(_total(n, math.isqrt(n)))


if __name__ == "__main__":
    print(solve())  # 17971254122360635
