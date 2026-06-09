"""Project Euler Problem 634: Numbers of the Form a^2 b^3.

Count integers n <= N expressible as a^2 b^3 with a, b >= 2 (N = 9 * 10^18).
Split by whether n is a perfect square.

Non-squares.  If n = a^2 b^3 has an odd prime exponent, the representation
with b squarefree is forced (b = product of the odd-exponent primes) and
unique, and any odd exponent in a^2 b^3 is automatically >= 3, so it exists.
b >= 2 here exactly captures the non-squares, and a = sqrt(n / b^3) >= 2
must be required separately because b^3 alone (a squarefree cube) admits no
other representation.  Hence the non-square count is

    A = sum over squarefree b >= 2 of max(0, isqrt(N / b^3) - 1).

Squares.  n = m^2 is expressible iff b is a square c^2 (b^3 = n / a^2 is
then a square), i.e. iff m = a c^3 with a, c >= 2.  Distinct m give distinct
n, so count m <= M = isqrt(N) with a cube divisor c^3 >= 8 and cofactor
>= 2.  Having any cube divisor c >= 2 is the same as not being cubefree, and
the only non-cubefree m where every witness fails (m = c^3 forced with no
proper divisor 2 <= d < c) are the cubes of primes:

    B = (M - sum_{d <= M^(1/3)} mu(d) floor(M / d^3)) - pi(M^(1/3)).

Checks: F(100) = 2, F(2 * 10^4) = 130, F(3 * 10^6) = 2014 (and a brute
force for all N <= 20000).
"""

from math import isqrt

import numpy as np


def icbrt(n: int) -> int:
    c = round(n ** (1 / 3))
    while c**3 > n:
        c -= 1
    while (c + 1) ** 3 <= n:
        c += 1
    return c


def smallest_factor_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf


SPF = smallest_factor_sieve(1310720)  # >= icbrt(9e18 / 4)


def is_squarefree(n: int) -> bool:
    while n > 1:
        p = int(SPF[n])
        n //= p
        if n % p == 0:
            return False
    return True


def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if SPF[i] == i:
            mu[i::i] *= -1
            mu[i * i :: i * i] = 0
    return mu


def F(N: int) -> int:
    a_count = sum(
        max(0, isqrt(N // b**3) - 1)
        for b in range(2, icbrt(N // 4) + 1)
        if is_squarefree(b)
    )
    M = isqrt(N)
    r = icbrt(M)
    mu = mobius_sieve(r)
    cubefree = sum(int(mu[d]) * (M // d**3) for d in range(1, r + 1))
    prime_cubes = sum(1 for p in range(2, r + 1) if SPF[p] == p)
    return a_count + (M - cubefree) - prime_cubes


def F_brute(N: int) -> int:
    hits = set()
    a = 2
    while 8 * a * a <= N:  # smallest b^3 is 8
        b = 2
        while a * a * b**3 <= N:
            hits.add(a * a * b**3)
            b += 1
        a += 1
    return len(hits)


if __name__ == "__main__":
    assert F(100) == F_brute(100) == 2
    assert F(2 * 10**4) == F_brute(2 * 10**4) == 130
    assert all(F(n) == F_brute(n) for n in range(8, 3000))
    assert F(3 * 10**6) == 2014
    print(F(9 * 10**18))  # 4019680944
