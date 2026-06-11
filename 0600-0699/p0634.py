"""Project Euler Problem 634: Numbers of the Form a^2 b^3.

Count x <= N = 9 * 10^18 with x = a^2 b^3 for integers a, b >= 2.

Split on whether x is a perfect square (every representation x = a^2 b^3 of
a square forces b to be a square, since exponents 2 alpha + 3 gamma must all
be even).

Non-squares: writing b = s t^2 with s squarefree turns a^2 b^3 into
(a t^3)^2 s^3, so every non-square x of the form has a representation with b
squarefree, and that representation is unique - s is the product of the
primes with odd exponent in x, and then a = sqrt(x / s^3).  So the
non-square count is the sum over squarefree s >= 2 of the number of a >= 2
with a^2 s^3 <= N, i.e. isqrt(N / s^3) - 1 (empty for s as 1 would give
squares, and a = 1 would give pure cubes).

Squares: x = c^2 with c <= M = isqrt(N).  Here x = a^2 (beta^2)^3 means
c = a beta^3 with a, beta >= 2, i.e. c is divisible by some cube beta^3 >= 8
with cofactor >= 2.  Any non-cubefree c works (take beta = p prime with
p^3 | c; the cofactor is 1 only when c = p^3 exactly, and a prime cube has
no other cube divisor), so the square count is

    #(non-cubefree c <= M) - #(primes p with p^3 <= M),

with the cubefree count from Moebius: sum_d mu(d) floor(M / d^3).

Verified: F(100) = 2, F(2 * 10^4) = 130, F(3 * 10^6) = 2014, and brute
force for N <= 10^5.
"""

from math import isqrt

import numpy as np


def moebius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for p in range(2, n + 1):
        if is_p[p]:
            if p * p <= n:
                is_p[p * p :: p] = False
            mu[p::p] *= -1
            mu[p * p :: p * p] = 0
    return mu


def icbrt(n: int) -> int:
    """Integer cube root."""
    r = round(n ** (1 / 3))
    while r**3 > n:
        r -= 1
    while (r + 1) ** 3 <= n:
        r += 1
    return r


def f(n: int) -> int:
    # Non-squares: b = s squarefree >= 2, a >= 2.
    s_max = icbrt(n // 4)
    mu = moebius_sieve(max(s_max, isqrt(isqrt(n)) + 2))
    total = sum(
        isqrt(n // (s * s * s)) - 1 for s in range(2, s_max + 1) if mu[s]
    )

    # Squares: c = a beta^3 <= M with a, beta >= 2.
    m = isqrt(n)
    d_max = icbrt(m)
    cubefree = sum(int(mu[d]) * (m // d**3) for d in range(1, d_max + 1))
    prime_cubes = sum(
        1 for p in range(2, d_max + 1) if mu[p] == -1 and all(
            p % q for q in range(2, isqrt(p) + 1)
        )
    )
    return total + (m - cubefree) - prime_cubes


def f_brute(n: int) -> int:
    hits = set()
    b = 2
    while 4 * b**3 <= n:
        a = 2
        while a * a * b**3 <= n:
            hits.add(a * a * b**3)
            a += 1
        b += 1
    return len(hits)


if __name__ == "__main__":
    assert f(100) == f_brute(100) == 2
    assert all(f(n) == f_brute(n) for n in range(3001))
    assert all(f(n) == f_brute(n) for n in range(3001, 10**5, 997))
    assert f(2 * 10**4) == 130
    assert f(3 * 10**6) == 2014
    print(f(9 * 10**18))  # 4019680944
