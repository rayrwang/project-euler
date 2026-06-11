"""Project Euler 482: The Incenter of a Triangle.

Sum L = p + |IA| + |IB| + |IC| over integer-sided triangles with perimeter
p <= 10^7 whose incenter-vertex distances are all integers.

With tangent lengths x = s-a, y = s-b, z = s-c and inradius r, each corner is
a right triangle: IA^2 = x^2 + r^2, and the half angles satisfy
alpha + beta + gamma = pi/2, equivalent to r^2 (x + y + z) = x y z. The
cosines of the half angles (x/IA etc.) are rational; writing the sines as
rationals times sqrt(D) (squarefree D), cos(gamma) = sin(alpha + beta) is
sqrt(D) times a positive rational, so D = 1: all sines are rational too. A
parity argument then kills odd perimeters (4r^2 = 4 IA^2 - (2x)^2 would be
congruent to 3 mod 4, impossible for a rational r with integer square), so
x, y, z are integers and r^2 = IA^2 - x^2 is an integer, hence r itself is a
positive integer.

Enumerate r: the legal tangent lengths are x = (e - d)/2 over factorizations
d e = r^2 (d < r, matching parity), since (IA - x)(IA + x) = r^2. Ordering
x >= y >= z makes z = r cot(gamma) <= sqrt(3) r (largest half angle is at
least pi/6) and y < P/4. For each such pair, x = r^2 (y + z) / (y z - r^2) is
decreasing in y; when it is an integer the third corner is automatically
Pythagorean (alpha = pi/2 - beta - gamma has rational sine and cosine, so
IA^2 = x^2 + r^2 is a perfect square). Total work is about sum tau(r^2),
done in a parallel numba loop over r up to P / (6 sqrt(3)).
"""

import numpy as np
from numba import njit, prange

P = 10**7


def spf_sieve(limit):
    spf = np.zeros(limit + 1, dtype=np.int64)
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i] == 0, i, spf[i::i])
    return spf


@njit(cache=True)
def isqrt64(n):
    u = np.int64(np.sqrt(np.float64(n)))
    while u * u > n:
        u -= 1
    while (u + 1) * (u + 1) <= n:
        u += 1
    return u


@njit(parallel=True, cache=True)
def total_sum(perim_limit, spf):
    half = perim_limit // 2
    rmax = np.int64(half / (3.0 * np.sqrt(3.0))) + 2
    partial = np.zeros(rmax + 1, np.int64)
    for r in prange(1, rmax + 1):  # ty: ignore[not-iterable]
        # factor r
        pr = np.empty(16, np.int64)
        ex = np.empty(16, np.int64)
        m = r
        npr = 0
        while m > 1:
            p = spf[m]
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            pr[npr] = p
            ex[npr] = e
            npr += 1
        # divisors d of r^2 with d < r; if r even, 1 <= v2(d) <= 2 v2(r) - 1
        divs = np.empty(4096, np.int64)
        nd = 1
        divs[0] = 1
        for i in range(npr):
            p = pr[i]
            hi = 2 * ex[i]
            if p == 2:
                hi = 2 * ex[i] - 1  # exponent of 2 must be in [1, 2 v2(r) - 1]
                base = nd
                pe = np.int64(1)
                cnt = 0
                for e in range(1, hi + 1):
                    pe *= p
                    for j in range(base):
                        v = divs[j] * pe
                        if v < r:
                            divs[base + cnt] = v
                            cnt += 1
                # powers of two replace (lo > 0): drop the pe^0 copies
                for j in range(cnt):
                    divs[j] = divs[base + j]
                nd = cnt
            else:
                base = nd
                cnt = 0
                pe = np.int64(1)
                for e in range(1, hi + 1):
                    pe *= p
                    for j in range(base):
                        v = divs[j] * pe
                        if v < r:
                            divs[base + cnt] = v
                            cnt += 1
                nd = base + cnt
        # tangent-length candidates, ascending
        xs = np.empty(nd, np.int64)
        nx = 0
        for j in range(nd):
            d = divs[j]
            if d < r:
                xs[nx] = (r * r // d - d) // 2
                nx += 1
        xs = np.sort(xs[:nx])
        nd = nx
        r2 = r * r
        ycap = half // 2
        sub = np.int64(0)
        for zi in range(nd):
            z = xs[zi]
            if z * z > 3 * r2:
                break
            ymin = max(z, r2 // z + 1)
            j = np.searchsorted(xs, ymin)
            while j < nd:
                y = xs[j]
                if y > ycap:
                    break
                den = y * z - r2
                num = r2 * (y + z)
                x = num // den
                if x < y:
                    break
                if num % den == 0:
                    s = x + y + z
                    if s <= half:
                        ia = isqrt64(x * x + r2)
                        ib = isqrt64(y * y + r2)
                        ic = isqrt64(z * z + r2)
                        sub += 2 * s + ia + ib + ic
                j += 1
        partial[r] = sub
    return partial.sum()


if __name__ == "__main__":
    spf = spf_sieve(int(P / 2 / (3 * 3**0.5)) + 2)
    assert total_sum(10**3, spf) == 3619
    print(total_sum(P, spf))  # 1400824879147
