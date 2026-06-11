"""Project Euler problem 596: Number of Lattice Points in a Hyperball.

T(r) counts integer quadruples with x^2 + y^2 + z^2 + t^2 <= r^2.
Find T(10^8) mod 1000000007.

By Jacobi's four-square theorem, r4(n) = 8 sigma(n) - 32 sigma(n/4)
(the second term only when 4 | n), i.e. 8 times the sum of divisors of n
not divisible by 4.  Summing over n <= N = r^2 and swapping the order,

  T(r) = 1 + 8 sum_{d <= N, 4 nmid d} d floor(N / d)
       = 1 + 8 (S(N) - 4 S(N / 4)),    S(N) = sum_d d floor(N / d),

since the d divisible by 4 contribute 4 S(N/4) after substituting
d = 4e.  S is evaluated with the standard divisor-block decomposition in
O(sqrt(N)) = 10^8 block steps; triangular sums of d up to 10^16 are
taken mod p by reducing each factor before the product and multiplying
by the inverse of 2.

Verified: brute-force counts for r = 2, 5, 100 against the given values,
and the given exact T(10^4) = 49348022079085897 both exactly (via a
block-decomposed exact S in Python integers) and mod p.
"""

import numpy as np
from numba import njit

P = 1000000007
INV2 = (P + 1) // 2


@njit(cache=True, inline="always")
def tri_mod(x):
    """x (x + 1) / 2 mod P for x up to about 1e16."""
    return x % P * ((x + 1) % P) % P * INV2 % P


@njit(cache=True)
def s_mod(n):
    """sum_{d=1..n} d * floor(n / d) mod P."""
    tot = np.int64(0)
    d = np.int64(1)
    while d <= n:
        q = n // d
        d2 = n // q
        tot = (tot + q % P * ((tri_mod(d2) - tri_mod(d - 1)) % P)) % P
        d = d2 + 1
    return tot % P


@njit(cache=True)
def t_mod(r):
    n = r * r
    return (1 + 8 * ((s_mod(n) - 4 * s_mod(n // 4)) % P)) % P


def s_exact(n: int) -> int:
    tot, d = 0, 1
    while d <= n:
        q = n // d
        d2 = n // q
        tot += q * (d2 * (d2 + 1) - (d - 1) * d) // 2
        d = d2 + 1
    return tot


def t_exact(r: int) -> int:
    n = r * r
    return 1 + 8 * (s_exact(n) - 4 * s_exact(n // 4))


def brute(r: int) -> int:
    cnt = 0
    r2 = r * r
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if x * x + y * y > r2:
                continue
            for z in range(-r, r + 1):
                s3 = x * x + y * y + z * z
                if s3 > r2:
                    continue
                tmax = int((r2 - s3) ** 0.5)
                while (tmax + 1) ** 2 <= r2 - s3:
                    tmax += 1
                while tmax**2 > r2 - s3:
                    tmax -= 1
                cnt += 2 * tmax + 1
    return cnt


def main() -> None:
    for r, want in [(2, 89), (5, 3121), (100, 493490641)]:  # given
        assert brute(r) == want and t_exact(r) == want and t_mod(r) == want, r
    assert t_exact(10**4) == 49348022079085897  # given
    assert t_mod(10**4) == 49348022079085897 % P

    print(t_mod(10**8))  # 734582049


if __name__ == "__main__":
    main()
