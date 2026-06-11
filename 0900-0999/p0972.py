"""Project Euler Problem 972: Hyperbolic Lines.

In the open unit disc model of the hyperbolic plane, geodesics are
diameters and circular arcs orthogonal to the unit circle.  ``V(N)`` is
the set of points inside the disc whose coordinates are rationals with
(lowest-terms) denominator at most N, and ``T(N)`` counts ordered triples
of distinct points of ``V(N)`` lying on a common geodesic;
``T(2) = 24``, ``T(3) = 1296``.  Find ``T(12)``.

Any two distinct points of the disc lie on exactly one geodesic, so the
count groups the ~23.4 million unordered pairs of ``V(12)`` by the
geodesic through them: a geodesic containing k points receives
``C(k, 2)`` pairs and contributes ``k(k-1)(k-2)`` ordered triples.

A circle with centre c and radius rho is orthogonal to the unit circle
iff ``|c|^2 = rho^2 + 1``; requiring ``|P - c| = rho`` then gives the
*linear* equation ``2 P . c = |P|^2 + 1``.  For two points the 2x2 system
yields a rational centre by Cramer's rule, and the pair (P, Q) is
diametral exactly when P, Q, O are collinear (vanishing determinant).

Scaling all coordinates by ``L = lcm(1..N)`` makes everything integral:
with ``X = Lx`` the equation reads ``2L (X c_x + Y c_y) = X^2 + Y^2 +
L^2``, so the centre is ``( (s_P Y_Q - s_Q Y_P), (X_P s_Q - X_Q s_P) ) /
(2L (X_P Y_Q - X_Q Y_P))`` with ``s = X^2 + Y^2 + L^2``.  The canonical
key is this triple divided by its gcd with positive denominator (all
quantities below 1e14, far within int64); diameters use the primitive
direction vector with a zero marker.  Keys for all pairs are produced by
a numba double loop, lexsorted, and run-lengths ``c`` are converted back
to point counts via ``k(k-1)/2 = c`` (integrality asserted).  The same
pipeline reproduces ``T(2)`` and ``T(3)``.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm

import numpy as np
from numba import njit


def points_scaled(n: int, scale: int) -> np.ndarray:
    vals = set()
    for b in range(1, n + 1):
        for a in range(-b + 1, b):
            if a == 0 or gcd(abs(a), b) == 1:
                vals.add(Fraction(a, b))
    pts = []
    for x in vals:
        for y in vals:
            if x * x + y * y < 1:
                pts.append((int(x * scale), int(y * scale)))
    pts.sort()
    return np.array(pts, dtype=np.int64)


@njit(cache=True)
def _gcd64(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


@njit(cache=True)
def _pair_keys(pts: np.ndarray, scale: int) -> np.ndarray:
    n = len(pts)
    keys = np.empty((n * (n - 1) // 2, 3), dtype=np.int64)
    t = 0
    ll = scale * scale
    for i in range(n):
        xp, yp = pts[i, 0], pts[i, 1]
        sp = xp * xp + yp * yp + ll
        for j in range(i + 1, n):
            xq, yq = pts[j, 0], pts[j, 1]
            cross = xp * yq - xq * yp
            if cross == 0:
                a, b = xq - xp, yq - yp
                g = _gcd64(a, b)
                a //= g
                b //= g
                if a < 0 or (a == 0 and b < 0):
                    a, b = -a, -b
                keys[t, 0] = 0
                keys[t, 1] = a
                keys[t, 2] = b
            else:
                sq = xq * xq + yq * yq + ll
                cxn = sp * yq - sq * yp
                cyn = xp * sq - xq * sp
                d = 2 * scale * cross
                g = _gcd64(_gcd64(cxn, cyn), d)
                cxn //= g
                cyn //= g
                d //= g
                if d < 0:
                    cxn, cyn, d = -cxn, -cyn, -d
                keys[t, 0] = d
                keys[t, 1] = cxn
                keys[t, 2] = cyn
            t += 1
    return keys


def t_count(n: int) -> int:
    scale = lcm(*range(1, n + 1))
    pts = points_scaled(n, scale)
    keys = _pair_keys(pts, scale)
    order = np.lexsort((keys[:, 2], keys[:, 1], keys[:, 0]))
    keys = keys[order]
    diff = np.any(keys[1:] != keys[:-1], axis=1)
    starts = np.concatenate(([0], np.nonzero(diff)[0] + 1, [len(keys)]))
    total = 0
    for c in np.diff(starts):
        c = int(c)
        k = int((1 + (1 + 8 * c) ** 0.5) / 2 + 0.5)
        assert k * (k - 1) // 2 == c, "pair count must be triangular"
        total += k * (k - 1) * (k - 2)
    return total


if __name__ == "__main__":
    assert t_count(2) == 24, "given checkpoint T(2)"
    assert t_count(3) == 1296, "given checkpoint T(3)"
    print(t_count(12))  # 3575508
