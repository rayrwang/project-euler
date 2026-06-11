from math import gcd, isqrt, sqrt

import numba
import numpy as np

# Work in the Eisenstein lattice Z[w], w = exp(2 pi i / 3).  Put the 60
# degree vertex at the origin; the two adjacent sides are u and
# v = u (n/m)(1 + w) with n/m in lowest terms, since 1 + w is the unit
# rotation by 60 degrees, and v in Z[w] forces u = m z for some z in Z[w].
# The side lengths are then m|z|, n|z| and k|z| with k^2 = m^2 - mn + n^2,
# so the opposite side is rational relative to the others only when
# m^2 - mn + n^2 is a perfect square, and the incentre works out to
#     I = z (2 + w) (m + n - k) / 3,
# which is a lattice point iff (2 + w) | z or 3 | M, where M = m + n - k
# and (2 + w) is the ramified prime of norm 3.  The inradius is
# r = |z| M sqrt(3) / 6, so r <= R becomes |z|^2 <= 12 R^2 / M^2 (or a
# third of that when z must be divisible by (2 + w)).  Counting lattice
# points of norm <= x is the classical H(x) = 6 sum (floor(x/d) over
# d = 1 mod 3 minus d = 2 mod 3).  Equilateral triangles (m = n = 1) are
# generated three times, once per vertex.
#
# Primitive families are parametrised by coprime (s, t) with t < s - t:
# {m, n} = {s^2 - t^2, t(2s - t)}, divided by 3 when 3 | s + t, giving
# M = 3 t (s - t) (always divisible by 3) or M = t(s - t) = 1 mod 3
# respectively — verified below to be complete and duplicate-free against
# direct enumeration.  Grouping families by M, the answer is a sum of
# O(sqrt(R^2)/M) hyperbola evaluations, about 5 * 10^7 operations in all.

R = 10**6


@numba.njit(cache=True)
def hex_points(x: int) -> int:
    """Nonzero Eisenstein integers with norm <= x."""
    if x <= 0:
        return 0
    s = 0
    d = 1
    while d <= x:
        q = x // d
        d2 = x // q
        s += q * ((1 if d2 % 3 == 1 else 0) - (1 if (d - 1) % 3 == 1 else 0))
        d = d2 + 1
    return 6 * s


@numba.njit(cache=True)
def family_counts(lim_a: int, lim_b: int):
    cnt3 = np.zeros(3 * lim_a + 1, dtype=np.int64)
    cnt1 = np.zeros(lim_b + 1, dtype=np.int64)
    lim = max(lim_a, lim_b)
    for t in range(1, int(np.sqrt(np.float64(lim))) + 2):
        u = t + 1
        while t * u <= lim:
            g, h = np.int64(t), np.int64(u)
            while h:
                g, h = h, g % h
            if g == 1:
                if (2 * t + u) % 3 != 0:  # s + t not divisible by 3
                    if t * u <= lim_a:
                        cnt3[3 * t * u] += 1
                elif t * u <= lim_b:
                    cnt1[t * u] += 1
            u += 1
    return cnt3, cnt1


@numba.njit(cache=True)
def grand_total(r4: int, r12: int, cnt3: np.ndarray, cnt1: np.ndarray) -> int:
    s = hex_points(r4) // 3
    for m in range(1, cnt3.shape[0]):
        if cnt3[m]:
            s += 2 * cnt3[m] * hex_points(r12 // (m * m))
    for m in range(1, cnt1.shape[0]):
        if cnt1[m]:
            s += 2 * cnt1[m] * hex_points(r4 // (m * m))
    return s


def count(r4: int, r12: int) -> int:
    """T(R) given 4R^2 and 12R^2 as integers."""
    cnt3, cnt1 = family_counts(isqrt(r12) // 3 + 1, isqrt(r4) + 1)
    return grand_total(r4, r12, cnt3, cnt1)


def parametrisation_check(limit: int) -> bool:
    """(s, t) families == all primitive solutions with n <= limit."""
    brute = set()
    for n in range(2, limit + 1):
        for m in range(1, n):
            if gcd(m, n) == 1:
                k = isqrt(m * m - m * n + n * n)
                if k * k == m * m - m * n + n * n:
                    brute.add((m, n))
    brute.discard((1, 1))
    par: set = set()
    for s in range(2, 2 * isqrt(limit) + 4):
        for t in range(1, (s + 1) // 2):
            if s - t == t or gcd(s, t) != 1:
                continue
            x, y = s * s - t * t, t * (2 * s - t)
            if (s + t) % 3 == 0:
                x, y = x // 3, y // 3
            if (x, y) != (1, 1) and max(x, y) <= limit:
                if (min(x, y), max(x, y)) in par:
                    return False
                par.add((min(x, y), max(x, y)))
    return par == brute


def geometric_brute(r4: int) -> int:
    """Direct lattice enumeration, independent of the derivation."""
    pts = [(a, b) for a in range(-80, 81) for b in range(-80, 81)]
    vs = [(c, d) for (c, d) in pts if 0 < c * c + d * d - c * d <= 6000]
    seen = set()
    for a, b in pts:
        n1 = a * a + b * b - a * b
        if not 0 < n1 <= 90:
            continue
        for c, d in vs:
            n2 = c * c + d * d - c * d
            dot2 = 2 * a * c + 2 * b * d - a * d - b * c  # 2 Re(u conj(v))
            if dot2 <= 0 or dot2 * dot2 != n1 * n2:
                continue  # angle at origin is 60 deg iff 4 dot^2 = |u|^2|v|^2
            cross = a * d - b * c
            area = abs(cross) * sqrt(3) / 4
            la, lb, lc = (
                sqrt((a - c) ** 2 + (b - d) ** 2 - (a - c) * (b - d)),
                sqrt(n2),
                sqrt(n1),
            )
            s = (la + lb + lc) / 2
            if area * area * 4 > r4 * s * s:  # r = area/s <= R
                continue
            ix = (lb * a + lc * c) / (2 * s)
            iy = (lb * b + lc * d) / (2 * s)
            if abs(ix - round(ix)) > 1e-7 or abs(iy - round(iy)) > 1e-7:
                continue
            tri = ((0, 0), (a, b), (c, d))
            key = min(
                tuple(sorted(((x - px, y - py) for x, y in tri))) for px, py in tri
            )
            seen.add(key)
    return len(seen)


if __name__ == "__main__":
    assert parametrisation_check(3000)
    assert count(1, 3) == 2  # given T(0.5)
    assert count(16, 48) == 44  # given T(2)
    assert count(400, 1200) == 1302  # given T(10)
    assert geometric_brute(1) == 2 and geometric_brute(16) == 44
    print(count(4 * R * R, 12 * R * R))  # 14854003484704
