"""Project Euler 496: Incenter and Circumcenter of Triangle.

Sum of BC over integer triangles ABC with AC = DI and BC <= 10^9, where I is
the incenter and D the second intersection of line AI with the circumcircle.

D is the arc midpoint of BC, so by the incenter-excenter lemma
DI = DB = 2R sin(A/2). With AC = b = 2R sin B (law of sines), the condition
AC = DI becomes sin B = sin(A/2), i.e. B = A/2 (the supplementary branch
violates A + B < pi). Triangles with A = 2B satisfy the classical relation
a^2 = b (b + c), with a = BC opposite A and b = AC opposite B; conversely
c = (a^2 - b^2)/b is a valid triangle side exactly when b | a^2 and
a/2 < b < a (the lower bound is the triangle inequality c < a + b). All four
example triangles for F(15) = 45 satisfy this.

So F(L) = sum over a <= L of a times the number of divisors of a^2 in
(a/2, a). Every factorization a^2 = d e decomposes uniquely as d = g y^2,
e = g z^2 with gcd(y, z) = 1 and a = g y z, and d in (a/2, a) becomes
y < z < 2y. Hence

    F(L) = sum_{gcd(y,z)=1, y<z<2y} y z * T(floor(L / (y z))),

with T the triangular numbers - about 2 * 10^8 coprime pairs for L = 10^9,
a few seconds in a parallel numba loop. The reduction is asserted against
brute force for small L along with F(15) = 45.
"""

import numpy as np
from numba import njit, prange

L = 10**9


def brute_f(limit):
    tot = 0
    for a in range(1, limit + 1):
        a2 = a * a
        for b in range(a // 2 + 1, a):
            if a2 % b == 0:
                tot += a
    return tot


@njit(cache=True)
def gcd64(a, b):
    while b:
        a, b = b, a % b
    return a


@njit(parallel=True, cache=True)
def fast_f(limit):
    ymax = np.int64(np.sqrt(np.float64(limit))) + 2
    partial = np.zeros(ymax + 1, np.int64)
    for y in prange(1, ymax + 1):  # ty: ignore[not-iterable]
        if y * (y + 1) > limit:
            continue
        sub = np.int64(0)
        zmax = min(2 * y - 1, limit // y)
        for z in range(y + 1, zmax + 1):
            if gcd64(y, z) == 1:
                k = limit // (y * z)
                sub += y * z * (k * (k + 1) // 2)
        partial[y] = sub
    return partial.sum()


if __name__ == "__main__":
    assert fast_f(15) == brute_f(15) == 45
    assert fast_f(1000) == brute_f(1000)
    assert fast_f(5000) == brute_f(5000)
    print(fast_f(L))  # 2042473533769142717
