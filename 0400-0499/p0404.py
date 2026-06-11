"""Project Euler 404: Crisscross Ellipses.

E_a: x^2 + 4y^2 = 4a^2 and its rotation by theta intersect at four points with
distances b < c from the origin; count triplets of positive integers (a, b, c)
with a <= N = 10^17.

In polar form a point of E_a satisfies r^2 (1 + 3 sin^2 phi) = 4a^2, so the
intersections lie at phi = theta/2 + k pi/2, giving c^2 = 4a^2/(1+3sin^2) and
b^2 = 4a^2/(1+3cos^2). Adding the two reciprocals yields the Diophantine
condition 4a^2 (b^2 + c^2) = 5 b^2 c^2. Writing b : c = m : n in lowest terms
forces m^2 + n^2 = 5 w^2 with gcd(m, n) = 1, and then (a, b, c) =
(m n j / 2, m w j, n w j): exactly one of m, n is even and w is odd, so the
solutions for fixed (m, n, w) are j = 1, 2, ..., floor(2N / (m n)). A real
rotation angle 0 < theta < 90 requires 1/2 < m/n < 1, i.e. m < n < 2m.

Primitive solutions of m^2 + n^2 = 5 w^2 are parametrized in Gaussian
integers: m + n i = unit * (2+i) * (x+yi)^2 with gcd(x, y) = 1, x + y odd, and
(2-i) not dividing x+yi (equivalently 2x != y mod 5). Taking x, y >= 1 selects
one representative per unit orbit, and the conjugate family corresponds to
swapping x and y, so every unordered primitive pair appears exactly once.
Since mn > 2w^2 = 2(x^2+y^2)^2, only x^2 + y^2 <= sqrt(N) matters - about
6 * 10^7 lattice pairs, a couple of seconds in a parallel numba loop. The
parametrized count is asserted against brute force and the given values
C(10^3) = 7, C(10^4) = 106, C(10^6) = 11845.
"""

from math import isqrt

import numpy as np
from numba import njit, prange

N = 10**17


def brute_count(amax):
    cnt = 0
    for a in range(1, amax + 1):
        for b in range(a + 1, 2 * a):
            den = 5 * b * b - 4 * a * a
            num = 4 * a * a * b * b
            if den <= 0 or num % den:
                continue
            c2 = num // den
            c = isqrt(c2)
            if c * c == c2 and c > b:
                cnt += 1
    return cnt


@njit(cache=True)
def gcd64(a, b):
    while b:
        a, b = b, a % b
    return a


@njit(parallel=True, cache=True)
def fast_count(n):
    lim = 2 * n
    wmax = np.int64(np.sqrt(np.float64(n))) + 2
    xmax = np.int64(np.sqrt(np.float64(wmax))) + 1
    total = np.int64(0)
    for x in prange(1, xmax + 1):  # ty: ignore[not-iterable]
        sub = np.int64(0)
        y = np.int64(1)
        while x * x + y * y <= wmax:
            if (x + y) & 1 and (2 * x - y) % 5 != 0 and gcd64(x, y) == 1:
                u = x * x - y * y
                v = x * y
                m = abs(2 * u - 2 * v)
                k = abs(u + 4 * v)
                if m > k:
                    m, k = k, m
                if k < 2 * m and m * k <= lim and gcd64(m, k) == 1:
                    sub += lim // (m * k)
            y += 1
        total += sub
    return total


if __name__ == "__main__":
    assert fast_count(10**3) == brute_count(10**3) == 7
    assert fast_count(10**4) == 106
    assert fast_count(10**6) == 11845
    print(fast_count(N))  # 1199215615081353
