"""Project Euler Problem 998: Squaring the Triangle.

The *minimum bounding square* of a triangle is the smallest square (of any
orientation) that fully covers it.  ``T(n)`` is the sum of perimeters of all
non-congruent integer-sided triangles whose minimum bounding square has an
integer side length ``s <= n``.  We must find ``T(10**6)``.

Geometry of the minimum bounding square
---------------------------------------
For an orientation ``theta`` the axis-aligned bounding box of the triangle has
width ``W(theta)`` and height ``H(theta)``; the bounding square at that angle
has side ``max(W, H)``.  The minimum over ``theta`` is attained in one of two
ways:

* **Flush / height dominated.**  One edge lies along a side of the square and
  the opposite vertex touches the far side, so ``s`` equals the *altitude* to
  that edge while the perpendicular extent is no larger.  Taking the shortest
  side ``a`` (whose altitude ``h`` is the largest) this means the triangle is
  two integer right triangles glued along the common leg ``h``: legs ``p, q``
  with ``p^2 + h^2`` and ``q^2 + h^2`` perfect squares, base ``a = p + q`` and
  ``s = h``.  Comparing the flush value ``h`` against the competing tilted
  value of the same edge pair gives the exact regime condition

      ``a <= h``      (height actually dominates) and
      ``h^2 <= h*(p+q) + p*q``   (no tilt beats it),

  the second being ``h^2 (h-a)^2 <= (p q)^2``.

* **Balanced / tilted.**  Here ``W = H = s`` and, the square being tight on all
  four sides while the triangle has only three vertices, one vertex sits at a
  corner of the square and the other two on the opposite two sides.  Placing the
  corner at ``(0, s)`` and the others at ``(u, 0)`` and ``(s, w)`` the three
  squared side lengths are ``u^2 + s^2``, ``s^2 + (s-w)^2`` and
  ``(s-u)^2 + w^2``.  Writing ``l1 = u`` and ``l2 = s - w`` this needs ``l1``
  and ``l2`` to be legs of ``s`` (``l_i^2 + s^2`` a perfect square) and
  ``(s-l1)^2 + (s-l2)^2`` a perfect square.

Both families are therefore enumerated from the *Pythagorean legs of ``s``*:
the values ``p < s`` with ``p^2 + s^2`` a perfect square, obtained from the
divisor pairs ``d * (s^2 / d) = s^2`` of equal parity via ``p = (s^2/d - d)/2``.

A triangle can have integer ``s`` only if its area is rational, and the tilted
candidates are rare, so each tilted hit is confirmed exactly with rational
arithmetic (``min_s2``) that recomputes the true minimum bounding square as the
smallest feasible candidate of the edge-direction "arc" system.

Validated against the given ``T(40)=346``, ``T(400)=76402`` and
``T(2000)=3237036``.
"""

from __future__ import annotations

import math
from fractions import Fraction
from math import isqrt

_HALF_PI = math.pi / 2


def sieve_spf(n: int) -> list[int]:
    """Smallest-prime-factor sieve up to ``n``."""
    spf = list(range(n + 1))
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def legs_of(s: int, spf: list[int]) -> list[tuple[int, int]]:
    """All ``(p, hyp)`` with ``0 < p < s`` and ``p^2 + s^2 = hyp^2``."""
    if s == 1:
        return []
    m = s
    fac: dict[int, int] = {}
    while m > 1:
        p = spf[m]
        while m % p == 0:
            fac[p] = fac.get(p, 0) + 1
            m //= p
    divs = [1]
    for prime, exp in fac.items():
        powers = [1]
        pe = 1
        for _ in range(2 * exp):
            pe *= prime
            powers.append(pe)
        divs = [d * w for d in divs for w in powers]
    s2 = s * s
    res: list[tuple[int, int]] = []
    for d in divs:
        if d >= s:
            continue
        d2 = s2 // d
        if (d2 - d) & 1:
            continue
        p = (d2 - d) // 2
        if p < s:
            res.append((p, (d + d2) // 2))
    res.sort()
    return res


def min_s2(a: int, b: int, c: int) -> Fraction | None:
    """Exact squared side of the minimum bounding square (None if irrational area)."""
    q = 2 * a * a * b * b + 2 * b * b * c * c + 2 * c * c * a * a - a**4 - b**4 - c**4
    r = isqrt(q)
    if r * r != q:
        return None
    x = Fraction(c * c + b * b - a * a, 2 * c)
    y = Fraction(r, 2 * c)
    vecs = [((Fraction(c), Fraction(0)), c), ((x - c, y), a), ((x, y), b)]
    cands: list[Fraction] = []
    for ii in range(3):
        for jj in range(ii + 1, 3):
            (ux, uy), li = vecs[ii]
            (vx, vy), lj = vecs[jj]
            cc = (ux * vx + uy * vy) / (li * lj)
            ss = (ux * vy - uy * vx) / (li * lj)
            cosd = sind = Fraction(0)
            for cc2, ss2 in ((cc, ss), (ss, -cc), (-cc, -ss), (-ss, cc)):
                if cc2 >= 0 and ss2 >= 0:
                    cosd, sind = cc2, ss2
                    break
            for cd, sd in ((cosd, sind), (sind, cosd)):
                denom = li * li + lj * lj - 2 * li * lj * sd
                if denom > 0:
                    cands.append(Fraction(li * li) * Fraction(lj * lj) * cd * cd / denom)
    for length in (a, b, c):
        cands.append(Fraction(length * length, 2))
    angles = [
        0.0,
        math.atan2(float(y), float(x - c)) % math.pi,
        math.atan2(float(y), float(x)) % math.pi,
    ]
    edges = [(c, angles[0]), (a, angles[1]), (b, angles[2])]
    centres = [(al + _HALF_PI / 2) % _HALF_PI for _, al in edges]

    def feasible(side: float) -> bool:
        pts = []
        for e in range(3):
            length = edges[e][0]
            if side >= length - 1e-9:
                continue
            if side < length / math.sqrt(2) - 1e-7:
                return False
            phi = _HALF_PI / 2 - math.acos(min(1.0, side / length))
            pts.append((centres[e], phi))
        if not pts:
            return True
        for ce, phi in pts:
            for cand_pt in (ce - phi, ce + phi, ce):
                if all(
                    abs(((cand_pt - c2 + _HALF_PI / 2) % _HALF_PI) - _HALF_PI / 2) <= ph2 + 1e-9
                    for c2, ph2 in pts
                ):
                    return True
        return False

    for s2 in sorted(set(cands)):
        if feasible((s2.numerator / s2.denominator) ** 0.5 + 1e-9):
            return s2
    return None


def solve(n: int) -> int:
    spf = sieve_spf(n)
    total = 0
    for s in range(1, n + 1):
        legs = legs_of(s, spf)
        count = len(legs)
        for i in range(count):
            p, hp = legs[i]
            for j in range(i, count):
                qv, hq = legs[j]
                # Family 1: glued right triangles, square side = altitude s.
                base = p + qv
                if base <= s and s * s <= s * base + p * qv:
                    total += base + hp + hq
                # Family 2: triangle inscribed with a vertex in a corner.
                dp = s - p
                dq = s - qv
                aa = dp * dp + dq * dq
                ra = isqrt(aa)
                if ra * ra == aa and ra > 0:
                    tri = tuple(sorted((ra, hp, hq)))
                    s2 = min_s2(*tri)
                    if s2 is not None and s2.denominator == 1:
                        root = isqrt(s2.numerator)
                        if root * root == s2.numerator and root == s:
                            total += ra + hp + hq
    return total


if __name__ == "__main__":
    assert solve(40) == 346, "checkpoint T(40)"
    assert solve(400) == 76402, "checkpoint T(400)"
    assert solve(2000) == 3237036, "checkpoint T(2000)"
    print(solve(10**6))  # 4439835458570
