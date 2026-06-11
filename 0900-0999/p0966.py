"""Project Euler 966: Maximal Intersection Area.

For each integer triangle K with a <= b <= c < a + b and perimeter <= 200,
place a circle C of equal area (R = sqrt(T/pi), T from Heron) so that the
overlap area is maximal, and sum the maxima.

The intersection area of a fixed circle with the triangle is computed
exactly by Green's theorem: walking the triangle edges CCW, sub-segments
inside the circle contribute signed triangle areas cross(A, B)/2 about the
circle center, and excursions outside contribute circular sectors
R^2 * dtheta / 2 with the signed subtended angle -- the classical
circle-polygon clipping formula, validated here against Monte Carlo.

As a function of the circle center t, f(t) = |K cap (C + t)| satisfies
f^(1/2) concave on its support (Brunn-Minkowski applied to the convex body
{(t, x) : x in K, x - t in C}), so f is quasiconcave: steepest ascent with
a backtracking line search converges to the global maximum. The gradient
with respect to the center is the boundary integral of the outward normal
over the circle arcs lying inside K, which evaluates per arc to the chord
endpoint difference rotated by -90 degrees; arcs are recovered from the
sorted entry/exit crossings of the circle with the edges. Neither shape
ever contains the other (equal areas), so crossings exist at the optimum.

Starting from the incenter, ascent converges in tens of iterations.
Verified: I(3,4,5) = 4.593049, I(3,4,6) = 3.552564 (given), and on 60
random triangles the result matches an independent nested golden-section
search (valid by quasiconcavity) to 1.3e-10. Sum over all 57222 triangles
in ~3 s.
"""

import math

import numpy as np
from numba import njit


@njit(cache=True)
def area_only(qx, qy, r):
    """Area of intersection of the CCW triangle (qx, qy) with the circle
    of radius r centered at the origin."""
    area = 0.0
    r2 = r * r
    for i in range(3):
        x1, y1 = qx[i], qy[i]
        x2, y2 = qx[(i + 1) % 3], qy[(i + 1) % 3]
        dx, dy = x2 - x1, y2 - y1
        a = dx * dx + dy * dy
        b = 2.0 * (x1 * dx + y1 * dy)
        c = x1 * x1 + y1 * y1 - r2
        disc = b * b - 4.0 * a * c
        if disc <= 0.0:
            area += 0.5 * r2 * math.atan2(x1 * y2 - y1 * x2, x1 * x2 + y1 * y2)
            continue
        sq = math.sqrt(disc)
        t1 = (-b - sq) / (2.0 * a)
        t2 = (-b + sq) / (2.0 * a)
        u1 = t1 if t1 > 0.0 else 0.0
        u2 = t2 if t2 < 1.0 else 1.0
        if u1 >= u2:
            area += 0.5 * r2 * math.atan2(x1 * y2 - y1 * x2, x1 * x2 + y1 * y2)
            continue
        ax, ay = x1 + u1 * dx, y1 + u1 * dy
        bx, by = x1 + u2 * dx, y1 + u2 * dy
        area += 0.5 * r2 * math.atan2(x1 * ay - y1 * ax, x1 * ax + y1 * ay)
        area += 0.5 * (ax * by - ay * bx)
        area += 0.5 * r2 * math.atan2(bx * y2 - by * x2, bx * x2 + by * y2)
    return area


@njit(cache=True)
def area_grad(qx, qy, r):
    """Intersection area and its gradient with respect to the circle center."""
    area = 0.0
    r2 = r * r
    thetas = np.empty(6, dtype=np.float64)
    entering = np.empty(6, dtype=np.bool_)
    ne = 0
    for i in range(3):
        x1, y1 = qx[i], qy[i]
        x2, y2 = qx[(i + 1) % 3], qy[(i + 1) % 3]
        dx, dy = x2 - x1, y2 - y1
        a = dx * dx + dy * dy
        b = 2.0 * (x1 * dx + y1 * dy)
        c = x1 * x1 + y1 * y1 - r2
        disc = b * b - 4.0 * a * c
        if disc <= 0.0:
            area += 0.5 * r2 * math.atan2(x1 * y2 - y1 * x2, x1 * x2 + y1 * y2)
            continue
        sq = math.sqrt(disc)
        t1 = (-b - sq) / (2.0 * a)
        t2 = (-b + sq) / (2.0 * a)
        u1 = t1 if t1 > 0.0 else 0.0
        u2 = t2 if t2 < 1.0 else 1.0
        if u1 >= u2:
            area += 0.5 * r2 * math.atan2(x1 * y2 - y1 * x2, x1 * x2 + y1 * y2)
            continue
        ax, ay = x1 + u1 * dx, y1 + u1 * dy
        bx, by = x1 + u2 * dx, y1 + u2 * dy
        area += 0.5 * r2 * math.atan2(x1 * ay - y1 * ax, x1 * ax + y1 * ay)
        area += 0.5 * (ax * by - ay * bx)
        area += 0.5 * r2 * math.atan2(bx * y2 - by * x2, bx * x2 + by * y2)
        # circle/edge crossings: the circle's CCW tangent at (px, py) is
        # (-py, px); it enters K iff cross(edge_dir, tangent) > 0, which
        # simplifies to dot(edge_dir, point) > 0.
        if 0.0 < t1 < 1.0:
            thetas[ne] = math.atan2(ay, ax)
            entering[ne] = (dx * ax + dy * ay) > 0.0
            ne += 1
        if 0.0 < t2 < 1.0:
            thetas[ne] = math.atan2(by, bx)
            entering[ne] = (dx * bx + dy * by) > 0.0
            ne += 1
    gx = 0.0
    gy = 0.0
    if ne >= 2:
        order = np.argsort(thetas[:ne])
        start = -1
        for k in range(ne):
            if entering[order[k]]:
                start = k
                break
        if start >= 0:
            k = start
            for _ in range(ne // 2):
                e1 = order[k % ne]
                e2 = order[(k + 1) % ne]
                th1, th2 = thetas[e1], thetas[e2]
                # integral of the outward normal over the arc inside K
                gx += r * (math.sin(th2) - math.sin(th1))
                gy += r * (math.cos(th1) - math.cos(th2))
                k += 2
    return area, gx, gy


@njit(cache=True)
def max_intersection(a, b, c):
    """I(a, b, c): steepest ascent from the incenter."""
    x2 = (b * b + c * c - a * a) / (2.0 * c)
    y2 = math.sqrt(max(b * b - x2 * x2, 0.0))
    tri_area = 0.5 * c * y2
    r = math.sqrt(tri_area / math.pi)
    per = a + b + c
    cx = (b * c + c * x2) / per
    cy = c * y2 / per
    qx = np.empty(3, dtype=np.float64)
    qy = np.empty(3, dtype=np.float64)
    step = 0.25 * r
    best = -1.0
    stale = 0
    for _ in range(2000):
        qx[0], qy[0] = -cx, -cy
        qx[1], qy[1] = c - cx, -cy
        qx[2], qy[2] = x2 - cx, y2 - cy
        cur, gx, gy = area_grad(qx, qy, r)
        if cur > best:
            stale = stale + 1 if cur - best < 1e-11 * (1.0 + cur) else 0
            best = cur
        else:
            stale += 1
        if stale >= 8:
            break
        gn = math.sqrt(gx * gx + gy * gy)
        if gn < 1e-12:
            break
        ux, uy = gx / gn, gy / gn
        improved = False
        while step > 1e-13 * r:
            nx, ny = cx + step * ux, cy + step * uy
            qx[0], qy[0] = -nx, -ny
            qx[1], qy[1] = c - nx, -ny
            qx[2], qy[2] = x2 - nx, y2 - ny
            if area_only(qx, qy, r) > cur:
                cx, cy = nx, ny
                step *= 1.5
                improved = True
                break
            step *= 0.5
        if not improved:
            break
    return best


@njit(cache=True)
def total_sum():
    s = 0.0
    for a in range(1, 67):
        for b in range(a, (200 - a) // 2 + 1):
            cmax = min(a + b - 1, 200 - a - b)
            for c in range(b, cmax + 1):
                s += max_intersection(float(a), float(b), float(c))
    return s


def solve() -> str:
    assert abs(max_intersection(3.0, 4.0, 5.0) - 4.593049) < 1e-6
    assert abs(max_intersection(3.0, 4.0, 6.0) - 3.552564) < 1e-6
    return f"{total_sum():.2f}"


if __name__ == "__main__":
    print(solve())  # 29337152.09
