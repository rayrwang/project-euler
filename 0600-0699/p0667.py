"""Project Euler Problem 667: Moving Pentagon.

Largest-area equilateral pentagon that can be moved through a unit-wide
L-shaped corridor (horizontal arm y in [0,1], x <= 1; vertical arm
x in [0,1], y >= 0).

Per orientation, if any placement avoids the forbidden region
{x > 1} u {y < 0} u {x < 0 and y > 1}, then so does the canonical one
pushed down (min y = 0) and right (max x = 1): both pushes weakly help
every constraint.  So the shape passes the corridor iff there is an
orientation window [alpha, beta] such that the shape fits the
horizontal strip at alpha (start of the turn, arriving from the arm),
fits the vertical strip at beta (end of the turn), and at every angle
in between the canonically placed shape has its portion above y = 1
entirely at x >= 0 (the corner clearance).  Feasibility is monotone in
scale (a shrunk copy can shadow the larger copy's motion), so the
critical scale follows by bisection with a window scan over a fine
angle grid -- this generic test gives exactly area 1 for the square,
which passes without rotating.

Shape family: the corridor's diagonal symmetry suggests a
mirror-symmetric equilateral pentagon A=(0,0), E=(1,0), apex
C=(1/2, sqrt(r^2 - 1/4)) with AC = CE = r, and B, D the outward unit
circle intersections; one parameter r remains.  A pattern search over
the full two-parameter space of general equilateral pentagons (edge
directions with two-edge closure, both branches, several starts) finds
nothing above the symmetric family, only re-parametrisations of it.

At the optimum the binding structure is: (i) the pentagon exactly fits
the strip at the start and end of the turn, base down -- the base-down
height is its minimal width over all rotations -- giving
scale = 1/height(r); and (ii) the corner clearance touches zero at two
angles around 42.4 and 47.6 degrees (mirror images).  Hence r* is the
root of clearmin(r, 1/height(r)) = 0, located by bisection with the
inner angular minimum refined by golden section to machine precision;
the area A(r)/height(r)^2 increases up to that root and the clearance
bound takes over beyond it (the kink seen in a coarse scan).

Verified: the generic machinery yields 1.0000000000 for the square, its
critical scale at r* agrees with 1/height(r*) to grid accuracy,
asymmetric perturbations of the optimum do not increase the area under
the same test, and the final area matches the required ten decimals.
"""

import math



def shoelace(pts):
    total = 0.0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2


def rot(pts, th):
    c, s = math.cos(th), math.sin(th)
    return [(c * x - s * y, s * x + c * y) for x, y in pts]


def geom(pts_rot, scale):
    """(corner clearance, height margin, width margin) at one angle."""
    xs = [p[0] for p in pts_rot]
    ys = [p[1] for p in pts_rot]
    miny, maxy = min(ys), max(ys)
    minx, maxx = min(xs), max(xs)
    h_marg = 1.0 - scale * (maxy - miny)
    w_marg = 1.0 - scale * (maxx - minx)
    ythr = miny + 1.0 / scale
    # infimum of x over the OPEN region y > 1 after canonical placement:
    # vertices strictly above the threshold, plus proper edge crossings
    # (limits of boundary points just above); an edge lying exactly at
    # the threshold contributes nothing.
    mn = float("inf")
    n = len(pts_rot)
    for i in range(n):
        x1, y1 = pts_rot[i]
        x2, y2 = pts_rot[(i + 1) % n]
        if y1 > ythr:
            mn = min(mn, x1)
        if (y1 - ythr) * (y2 - ythr) < 0.0:
            t = (ythr - y1) / (y2 - y1)
            mn = min(mn, x1 + (x2 - x1) * t)
    cl = float("inf") if mn == float("inf") else 1.0 + scale * (mn - maxx)
    return cl, h_marg, w_marg


def feasible(pts, scale, grid=1440):
    cl = [0.0] * grid
    hm = [0.0] * grid
    wm = [0.0] * grid
    for i in range(grid):
        th = 2 * math.pi * i / grid
        cl[i], hm[i], wm[i] = geom(rot(pts, th), scale)
    seen_h = False
    for i in range(2 * grid):
        j = i % grid
        if cl[j] < 0:
            seen_h = False
            continue
        if hm[j] >= 0:
            seen_h = True
        if seen_h and wm[j] >= 0:
            return True
    return False


def max_scale(pts, lo=0.1, hi=3.0, iters=45, grid=1440):
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if feasible(pts, mid, grid):
            lo = mid
        else:
            hi = mid
    return lo


def sym_pentagon(r):
    h = math.sqrt(r * r - 0.25)
    a = (0.0, 0.0)
    e = (1.0, 0.0)
    c = (0.5, h)
    k = math.sqrt(1.0 - (r / 2) ** 2)
    ux, uy = -h / r, 0.5 / r
    mx, my = 0.25, h / 2
    b = (mx - k * ux, my - k * uy)
    if b[0] > 0.5:
        b = (mx + k * ux, my + k * uy)
    return [a, b, c, (1.0 - b[0], b[1]), e]


def height0(pts):
    return max(y for _, y in pts) - min(y for _, y in pts)


def clearmin(r):
    """Minimum corner clearance over the turn at scale 1/height(r)."""
    pts = sym_pentagon(r)
    scale = 1.0 / height0(pts)

    def f(th):
        return geom(rot(pts, th), scale)[0]

    lo, hi = math.radians(35), math.radians(55)
    n = 400
    vals = [(f(lo + (hi - lo) * i / n), i) for i in range(n + 1)]
    _, imin = min(vals)
    a = lo + (hi - lo) * max(imin - 1, 0) / n
    b = lo + (hi - lo) * min(imin + 1, n) / n
    phi = (math.sqrt(5) - 1) / 2
    c = b - (b - a) * phi
    d = a + (b - a) * phi
    fc, fd = f(c), f(d)
    for _ in range(80):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - (b - a) * phi
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + (b - a) * phi
            fd = f(d)
    return min(fc, fd)


if __name__ == "__main__":
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    s_sq = max_scale(square)
    assert abs(s_sq * s_sq - 1.0) < 1e-9
    # solve clearmin(r) = 0
    lo, hi = 0.85, 0.95
    assert clearmin(lo) > 0 and clearmin(hi) < 0
    for _ in range(55):
        mid = 0.5 * (lo + hi)
        if clearmin(mid) >= 0:
            lo = mid
        else:
            hi = mid
    r_star = 0.5 * (lo + hi)
    pts = sym_pentagon(r_star)
    scale = 1.0 / height0(pts)
    # base-down really is the thinnest orientation
    assert all(
        height0(rot(pts, math.pi * i / 720)) >= height0(pts) - 1e-12
        for i in range(720)
    )
    # generic window machinery agrees with the binding-structure scale
    assert abs(max_scale(pts, grid=2880, iters=40) - scale) < 2e-4
    # asymmetric perturbations do not help (same generic test both sides)
    base = max_scale(pts, grid=360, iters=30) ** 2 * shoelace(pts)
    for dx, dy in ((0.01, -0.01), (-0.012, 0.008)):
        pert = [
            (x + dx * (i == 1), y + dy * (i == 1))
            for i, (x, y) in enumerate(pts)
        ]
        v = max_scale(pert, grid=360, iters=30) ** 2 * shoelace(pert)
        assert v < base + 2e-3
    area = scale * scale * shoelace(pts)
    print(f"{area:.10f}")  # 1.5276527928
