import numpy as np

# The exponent |1e-6 (x^2 + y^2) - 0.0015 (x + y) + 0.7| vanishes on the
# circle centred (750, 750) with radius sqrt(425000) = 652, so the terrain
# is a closed mountain band around that circle (its crest stays above 10900
# everywhere). A(200, 200) and B(1400, 1400) both lie outside the band, so a
# constant-altitude flight must squeeze between the band and the square's
# edge. The outer level set {h = f} releases the west (and, symmetrically,
# the south) corridor last: connectivity opens at
#     f_min = max_y h(0, y) = 10396.4621932...,
# where the outer level curve touches the wall x = 0 at a single pinch point
# (verified by a grid BFS over altitudes). At that altitude the shortest
# path is the taut string from A over the west/north side of the band to B:
# straight to a tangent point, an arc of the level curve through the pinch,
# and straight to B. The relevant outer level curve is convex, so the
# geodesic is exactly the A-to-B portion of the convex hull of
# {A, B} + (densely polygonised level curve), computed with the curve
# sampled on 1.2 million rays from the band's centre (radius found by
# bisection), giving the length to well below millimetre precision.


def _h(x, y):
    return (5000 - 0.005 * (x * x + y * y + x * y) + 12.5 * (x + y)) * np.exp(
        -np.abs(0.000001 * (x * x + y * y) - 0.0015 * (x + y) + 0.7)
    )


def solve() -> str:
    # f_min = max over the wall x = 0 (ternary search)
    lo, hi = 800.0, 1000.0
    for _ in range(200):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if _h(0.0, m1) < _h(0.0, m2):
            lo = m1
        else:
            hi = m2
    f_min = float(_h(0.0, 0.5 * (lo + hi)))

    # outer level curve {h = f_min}, polar about the band centre
    cx = cy = 750.0
    n = 1_200_000
    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
    ct, st = np.cos(theta), np.sin(theta)
    r_in = np.full(n, 651.92)  # the crest circle: h > f_min everywhere
    r_out = np.full(n, 1075.0)  # beyond the band: h < f_min everywhere
    assert (_h(cx + r_in * ct, cy + r_in * st) > f_min).all()
    assert (_h(cx + r_out * ct, cy + r_out * st) < f_min).all()
    for _ in range(55):
        mid = 0.5 * (r_in + r_out)
        inside = _h(cx + mid * ct, cy + mid * st) > f_min
        r_in = np.where(inside, mid, r_in)
        r_out = np.where(inside, r_out, mid)
    radius = 0.5 * (r_in + r_out)
    curve = np.column_stack([cx + radius * ct, cy + radius * st])

    a = np.array([200.0, 200.0])
    b = np.array([1400.0, 1400.0])
    points = np.vstack([curve, a, b])

    def cross(o, p, q):
        return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])

    def hull(pts: np.ndarray) -> np.ndarray:
        pts = pts[np.lexsort((pts[:, 1], pts[:, 0]))]

        def half(seq):
            stack: list[np.ndarray] = []
            for p in seq:
                while len(stack) >= 2 and cross(stack[-2], stack[-1], p) <= 0:
                    stack.pop()
                stack.append(p)
            return stack

        lower = half(pts)
        upper = half(pts[::-1])
        return np.array(lower[:-1] + upper[:-1])

    hl = hull(points)
    m = len(hl)
    ia = int(np.where((hl == a).all(axis=1))[0][0])
    ib = int(np.where((hl == b).all(axis=1))[0][0])

    def walk(i: int, j: int) -> np.ndarray:
        out = [hl[i]]
        while i != j:
            i = (i + 1) % m
            out.append(hl[i])
        return np.array(out)

    p1 = walk(ia, ib)
    p2 = walk(ib, ia)[::-1]
    path = p1 if p1[:, 0].min() < p2[:, 0].min() else p2  # west-side wrap
    length = float(np.sum(np.linalg.norm(np.diff(path, axis=0), axis=1)))
    return f"{length:.3f}"


if __name__ == "__main__":
    print(solve())  # 2531.205
