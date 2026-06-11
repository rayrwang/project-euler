"""Project Euler Problem 975: A Path Through the Cube.

For coprime odd ``a, b`` let ``H_{a,b}(x) = 1/2 - (b cos(a pi x) +
a cos(b pi x)) / (2(a+b))``, which rises from 0 to 1 on [0, 1].  Paths fill
the set ``z = H_{a,b}(x) = H_{c,d}(y)`` inside the unit cube, and (0,0,0)
is connected to (1,1,1) -- uniquely so when ``gcd(a+b, c+d)`` is 2 or 4.
``F(a,b,c,d)`` is the total variation of the height z along that path;
``F(3,5,3,7) ~ 7.01772`` and ``F(7,17,9,19) ~ 26.79578``.  With
``G(m,n) = sum F(p, q, p, 2q - p)`` over prime pairs ``m <= p < q <= n``
and ``G(3,20) ~ 463.80866``, find ``G(500, 1000)`` to five decimals.

This is the classical *mountain climbing problem*: two climbers start at
opposite feet of two mountain profiles and move so their heights always
agree.  Here the profiles are the piecewise-monotone functions ``H_{a,b}``
and ``H_{c,d}``; only their sequences of critical values matter.  The
derivative factorises as ``H' ~ sin((a+b) pi x / 2) cos((a-b) pi x / 2)``,
so the critical points are ``x = 2k/(a+b)`` and ``x = (2k+1)/|a-b|``;
where the two families coincide the root is double and the point is not an
extremum, so the evaluated values are compressed to the alternating
sequence of strict extrema.

The synchronized walk has a simple event structure.  While z travels in
one direction, each coordinate slides along its current monotone piece;
the first piece-end (extremum) reached belongs to one coordinate, which
passes *over* its extremum onto the adjacent piece, while the other
coordinate reverses inside its piece and z's direction flips.  If both
coordinates reach extrema at exactly the same height, both pass over and
z continues (a saddle crossing; the gcd condition keeps the traced path
unique).  The walk ends when both coordinates stand at their final
endpoints with z = 1.  ``F`` is the accumulated |dz| over all events --
the actual abscissae never matter, only the critical values.

The simulation reproduces both given F values and ``G(3, 20)``; the 2628
prime pairs of ``G(500, 1000)`` need a few tens of thousands of events
each, a couple of minutes in total.
"""

from __future__ import annotations

import math


def crit_values(a: int, b: int) -> list[float]:
    """Alternating strict-extremum values of H_{a,b} on [0,1] (0 ... 1)."""
    s, d = a + b, abs(a - b)
    pts = {0.0, 1.0}
    for k in range(1, s // 2 + 1):
        x = 2 * k / s
        if 0 < x < 1:
            pts.add(x)
    for k in range(d // 2):
        x = (2 * k + 1) / d
        if 0 < x < 1:
            pts.add(x)
    xs = sorted(pts)
    vals = [
        0.5
        - (b * math.cos(a * math.pi * x) + a * math.cos(b * math.pi * x))
        / (2 * (a + b))
        for x in xs
    ]
    out = [vals[0]]
    for i in range(1, len(vals) - 1):
        if (vals[i] - out[-1]) * (vals[i + 1] - vals[i]) < 0:
            out.append(vals[i])
    out.append(vals[-1])
    return out


def path_variation(a: int, b: int, c: int, d: int, eps: float = 1e-12) -> float:
    """F(a, b, c, d): total height variation of the connecting path."""
    v = crit_values(a, b)
    w = crit_values(c, d)
    nv, nw = len(v) - 1, len(w) - 1
    ix, sx = 0, 1  # x: current piece, spatial direction
    jy, sy = 0, 1
    dz = 1
    z = 0.0
    total = 0.0
    while True:
        bx = ix + 1 if sx > 0 else ix
        by = jy + 1 if sy > 0 else jy
        ex, ey = v[bx], w[by]
        zstar = min(ex, ey) if dz > 0 else max(ex, ey)
        total += abs(zstar - z)
        z = zstar
        ax = abs(ex - zstar) < eps
        ay = abs(ey - zstar) < eps
        if ax and ay and bx == nv and by == nw and abs(z - 1.0) < 1e-9:
            return total
        if ax and ay:
            ix += sx
            jy += sy
        elif ax:
            ix += sx
            sy = -sy
            dz = -dz
        else:
            jy += sy
            sx = -sx
            dz = -dz


def G(m: int, n: int) -> float:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    ps = [p for p in range(m, n + 1) if sieve[p]]
    total = 0.0
    for i, p in enumerate(ps):
        for q in ps[i + 1 :]:
            total += path_variation(p, q, p, 2 * q - p)
    return total


if __name__ == "__main__":
    assert abs(path_variation(3, 5, 3, 7) - 7.01772) < 1e-5, "checkpoint F(3,5,3,7)"
    assert abs(path_variation(7, 17, 9, 19) - 26.79578) < 1e-5, (
        "checkpoint F(7,17,9,19)"
    )
    assert abs(G(3, 20) - 463.80866) < 1e-5, "checkpoint G(3,20)"
    print("%.5f" % G(500, 1000))  # 88597366.47748
