"""
https://projecteuler.net/problem=582

Count integer triangles with one 120-degree angle, sides
a <= b <= c, b - a <= 100 and c <= 10^100.

The 120-degree angle faces c, so c^2 = a^2 + a b + b^2. Substituting
b = a + d with d = b - a in 1..100 (d = 0 forces c = a sqrt(3), never
integral) gives c^2 = 3a^2 + 3ad + d^2, and the quadratic formula
requires 3(4c^2 - d^2) to be a perfect square (3z)^2, i.e.

    x^2 - 3 z^2 = d^2,   x = 2c,   a = (z - d) / 2.

A triangle therefore corresponds to a solution (x, z) of this
Pell-like equation with x even, z = d (mod 2), z >= d + 2 (so a >= 1)
and x <= 2n. The solution set is a union of orbits under
multiplication by the fundamental unit 2 + sqrt(3) of x^2 - 3y^2 = 1,
acting as (x, z) -> (2x + 3z, x + 2z). The inverse map
(x, z) -> (2x - 3z, 2z - x) strictly decreases z whenever z >= 1
(since x > z sqrt(3) > z) and stays non-negative exactly while
z >= d, so every orbit contains a representative with 0 <= z < d.
Enumerating seed solutions with z in [0, 2d] (a comfortable superset)
and expanding each orbit upward with exact integers until x > 2n
collects every solution once (a set deduplicates overlapping seeds);
chains reach 10^100 in about 175 steps.

Verified against brute-force triangle enumeration for n = 1000 and
10^4, plus the given T(1000) = 235 and T(10^8) = 1245.
"""

from math import isqrt


def t_of(n: int) -> int:
    total = 0
    for d in range(1, 101):
        seen = set()
        for z0 in range(2 * d + 1):
            xx = d * d + 3 * z0 * z0
            x0 = isqrt(xx)
            if x0 * x0 != xx:
                continue
            x, z = x0, z0
            while x <= 2 * n:
                seen.add((x, z))
                x, z = 2 * x + 3 * z, x + 2 * z
        for x, z in seen:
            if x % 2 == 0 and (z - d) % 2 == 0 and z >= d + 2:
                total += 1
    return total


def t_brute(n: int) -> int:
    cnt = 0
    for a in range(1, n + 1):
        for b in range(a, a + 101):
            cc = a * a + a * b + b * b
            c = isqrt(cc)
            if c * c == cc and c <= n:
                cnt += 1
    return cnt


if __name__ == "__main__":
    assert t_of(1000) == t_brute(1000) == 235
    assert t_of(10**4) == t_brute(10**4)
    assert t_of(10**8) == 1245  # given

    print(t_of(10**100))  # 19903
