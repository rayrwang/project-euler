"""Project Euler 991: Fruit Salad.

With (a, b, c) = (apple, banana, pineapple) the equation is

    a/(b+c) + b/(c+a) + c/(a+c) = 4.

The second and third fractions share the denominator a + c, so it collapses
to a/s + s/(a+c) = 4 with s = b + c. Hence a + c = s^2/(4s - a): writing
d = 4s - a we need d | s^2, and then a = 4s - d, c = s^2/d - a, b = s - c.

Pairs (s, d) with d | s^2 are exactly d = e^2 m, s = e m k with gcd(e, k) = 1
(take g = gcd(d, s), e = d/g, m = g/e, k = s/g; then d | s^2 iff e | g).
In these coordinates everything is linear in m:

    a = e m (4k - e),  b = m (5ek - k^2 - e^2),  c = m (k^2 - 4ek + e^2),
    a + b + c = 5s - d = e m (5k - e).

Positivity of a, b, c restricts k/e to two bands, (1/4, 2 - sqrt(3)) and
(2 + sqrt(3), (5 + sqrt(21))/2), and the bound T = e m (5k - e) <= 10^7
caps e at a few thousand. For each coprime (e, k) in the bands all
m <= M = floor(10^7 / (e(5k - e))) are solutions, contributing
e (5k - e) M (M + 1) / 2 to the answer.

Verified against brute force over all triples (limit 200) and over (s, d)
pairs (limits up to 5000): identical solution sets.
"""

from math import gcd, isqrt


def solve(limit: int) -> int:
    tot = 0
    e1 = isqrt(4 * limit) + 2  # band 1: base ~ e^2 / 4
    e2 = isqrt(limit // 17) + 2  # band 2: base = e(5k - e) > 17.6 e^2
    for e in range(1, e1 + 1):
        ks = set(range(max(1, e // 4), e * 27 // 100 + 3))
        if e <= e2:
            ks |= set(range(max(1, e * 373 // 100), e * 48 // 10 + 3))
        for k in ks:
            if gcd(e, k) != 1:
                continue
            if (
                4 * k - e < 1
                or k * k - 4 * e * k + e * e < 1
                or 5 * e * k - k * k - e * e < 1
            ):
                continue
            base = e * (5 * k - e)
            m = limit // base
            if m:
                tot += base * m * (m + 1) // 2
    return tot


if __name__ == "__main__":
    print(solve(10**7))  # 23871972654940
