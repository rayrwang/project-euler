"""Project Euler Problem 694: Cube-full Divisors.

s(n) counts the cube-full divisors of n (a number is cube-full if every prime in it
appears to power >= 3; 1 is cube-full).  With S(N) = sum_{i<=N} s(i),

    S(N) = sum_{d cube-full, d<=N} floor(N/d),

since each cube-full d is a divisor of floor(N/d) multiples up to N.

Every cube-full number factors uniquely as d = a^3 b^4 c^5 with b, c squarefree and
gcd(b,c) = 1 (group primes by exponent mod 3: e==0 -> a, e==1 -> uses b, e==2 -> uses
c).  Hence

    S(N) = sum_{b,c sqfree, gcd(b,c)=1} sum_{a>=1, a^3 b^4 c^5 <= N} floor(N / (a^3 b^4 c^5)),

and floor(N/(a^3 b^4 c^5)) = floor(M / a^3) with M = floor(N / (b^4 c^5)).  The total
work is about N^{1/3} * zeta(4/3) * zeta(5/3) ~ 7e6 for N = 10^18.  Checks: S(16)=19,
S(100)=126, S(10000)=13344.
"""

import numpy as np
import numba


@numba.jit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.jit(cache=True)
def _solve(N: int) -> int:
    bmax = int(N ** 0.25) + 2
    sq = np.ones(bmax + 1, dtype=np.bool_)
    sq[0] = False
    i = 2
    while i * i <= bmax:
        i2 = i * i
        for j in range(i2, bmax + 1, i2):
            sq[j] = False
        i += 1

    total = 0
    b = 1
    while True:
        b4 = b * b * b * b
        if b4 > N:
            break
        if sq[b]:
            lim_c5 = N // b4
            c = 1
            while True:
                c5 = c * c * c * c * c
                if c5 > lim_c5:
                    break
                if sq[c] and _gcd(b, c) == 1:
                    M = N // (b4 * c5)
                    a = 1
                    a3 = 1
                    while a3 <= M:
                        total += M // a3
                        a += 1
                        a3 = a * a * a
                c += 1
        b += 1
    return total


def S(N: int) -> int:
    return int(_solve(N))


if __name__ == "__main__":
    assert S(16) == 19, S(16)
    assert S(100) == 126, S(100)
    assert S(10000) == 13344, S(10000)
    print(S(10**18))  # 1339784153569958487
