"""Project Euler Problem 681: Maximal Area.

For fixed sides the maximal quadrilateral is cyclic, with Brahmagupta's
area sqrt((s-a)(s-b)(s-c)(s-d)), s the semiperimeter.  Substituting
w = s - d <= x = s - c <= y = s - b <= z = s - a gives a bijection
(a <= b <= c <= d are recovered as a = (w + x + y - z) / 2 etc.) under
which M = sqrt(w x y z), the perimeter is w + x + y + z, and the
constraints become: w >= 1, z < w + x + y (positivity of a; with the
parity condition this is equivalent to a >= 1), w + x + y + z even
(integrality), and w x y z a perfect square at most n^2.

So SP(n) sums w + x + y + z over w <= x <= y <= z with z < w + x + y,
even total, and w x y z = m^2 <= n^2.  Since z >= y forces
w x y^2 <= n^2, the triples (w, x, y) are enumerable (about 2.3 * 10^9
for n = 10^6).  For each, w x y z is a square exactly when z = u t^2
where u is the squarefree part of w x y, computed from a sieved
squarefree-part table via sf(ab) = sf(a) sf(b) / gcd(sf(a), sf(b))^2
applied twice; t then runs over the few values with
y <= u t^2 <= min(w + x + y - 1, n^2 / (w x y)).

Verified: SP(10) = 186 and SP(100) = 23238, both also against an
independent brute force over quadruples (which checks squareness
directly), and the example M(2, 2, 3, 3) = 6.
"""

import math

import numba
import numpy as np

N = 1_000_000


def squarefree_table(limit: int) -> np.ndarray:
    sf = np.arange(limit + 1, dtype=np.int64)
    d = 2
    while d * d <= limit:
        d2 = d * d
        for m in range(d2, limit + 1, d2):
            while sf[m] % d2 == 0:
                sf[m] //= d2
        d += 1
    return sf


@numba.jit(nogil=True)
def solve(n2: int, sf: np.ndarray) -> int:
    total = 0
    w = 1
    while w * w * w * w <= n2:
        sfw = sf[w]
        x = w
        while w * x * x * x <= n2:
            g = math.gcd(sfw, sf[x])
            sfwx = sfw * sf[x] // (g * g)
            wx = w * x
            lim = n2 // wx
            ymax = int(np.sqrt(lim))
            while ymax * ymax > lim:
                ymax -= 1
            while (ymax + 1) * (ymax + 1) <= lim:
                ymax += 1
            for y in range(x, ymax + 1):
                g = math.gcd(sfwx, sf[y])
                u = sfwx * sf[y] // (g * g)
                wxy = wx * y
                zmax = w + x + y - 1
                if zmax > n2 // wxy:
                    zmax = n2 // wxy
                if u > zmax:
                    continue
                t = int(np.sqrt(y / u))
                while u * t * t < y:
                    t += 1
                while t > 1 and u * (t - 1) * (t - 1) >= y:
                    t -= 1
                base = w + x + y
                z = u * t * t
                while z <= zmax:
                    if (base + z) % 2 == 0:
                        total += base + z
                    t += 1
                    z = u * t * t
            x += 1
        w += 1
    return total


def sp_brute(n: int) -> int:
    n2 = n * n
    total = 0
    w = 1
    while w**4 <= n2:
        x = w
        while w * x**3 <= n2:
            y = x
            while w * x * y * y <= n2:
                for z in range(y, min(w + x + y - 1, n2 // (w * x * y)) + 1):
                    if (w + x + y + z) % 2 == 0:
                        m = math.isqrt(w * x * y * z)
                        if m * m == w * x * y * z:
                            total += w + x + y + z
                y += 1
            x += 1
        w += 1
    return total


if __name__ == "__main__":
    sf = squarefree_table(N)
    assert sp_brute(6) - sp_brute(5) >= 2 + 2 + 3 + 3  # M(2,2,3,3) = 6
    assert solve(10 * 10, sf) == 186 == sp_brute(10)
    assert solve(100 * 100, sf) == 23238 == sp_brute(100)
    print(solve(N * N, sf))  # 2611227421428
