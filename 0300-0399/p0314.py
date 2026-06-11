import math


def best_ratio(half: int = 250, x_min: int = 170, max_edge: int = 25) -> float:
    """Maximum enclosed-area / perimeter ratio for a grid-post polygon.

    The optimal wall is convex and symmetric under the eight symmetries of the
    square, so it is fixed by its boundary in one octant: a convex lattice chain
    from the x-axis (a symmetry line) to the diagonal y = x, centred on the
    square's centre.  With the centre at the origin the full area is 8x the fan
    area sum_edges (1/2)(P_i x P_{i+1}) and the perimeter is 8x the chain length,
    so the ratio to maximise is sum (1/2)cross / sum len.

    This is a fractional objective, handled by Dinkelbach: for a guess lambda,
    maximise sum[(1/2)cross - lambda*len] by a DP over octant points ordered by
    angle from the centre (a convex chain visits strictly increasing angles), then
    update lambda to the achieved ratio.  The optimum's corner radius is ~132, so
    only points near the corner matter; collinear runs reproduce the flat sides, so
    bounding edge length is exact.
    """
    pts = [
        (x, y)
        for x in range(x_min, half + 1)
        for y in range(0, x + 1)
    ]
    pts.sort(key=lambda p: (math.atan2(p[1], p[0]), p[0] * p[0] + p[1] * p[1]))
    index = {p: i for i, p in enumerate(pts)}
    vecs = [
        (vx, vy)
        for vx in range(-max_edge, 1)
        for vy in range(0, max_edge + 1)
        if 0 < vx * vx + vy * vy <= max_edge * max_edge
    ]

    neg = -1e18

    def dinkelbach_step(lam: float) -> tuple[float, float, float]:
        value = [neg] * len(pts)
        acc_a = [0.0] * len(pts)
        acc_l = [0.0] * len(pts)
        for i, (x, y) in enumerate(pts):
            if y == 0 and value[i] < 0.0:  # chain may start anywhere on the axis
                value[i] = 0.0
            best, b_a, b_l = value[i], acc_a[i], acc_l[i]
            for vx, vy in vecs:
                qx, qy = x - vx, y - vy
                if qy < 0 or qx > half or qy > qx:
                    continue
                j = index.get((qx, qy))
                if j is None or value[j] <= neg / 2:
                    continue
                cross = 0.5 * (qx * y - x * qy)
                length = math.hypot(vx, vy)
                val = value[j] + cross - lam * length
                if val > best:
                    best, b_a, b_l = val, acc_a[j] + cross, acc_l[j] + length
            value[i], acc_a[i], acc_l[i] = best, b_a, b_l
        best_v, area, perim = neg, 0.0, 1.0
        for i, (x, y) in enumerate(pts):
            if x == y and value[i] > best_v:
                best_v, area, perim = value[i], acc_a[i], acc_l[i]
        return best_v, area, perim

    lam = 130.0
    for _ in range(30):
        _, area, perim = dinkelbach_step(lam)
        new_lam = area / perim
        if abs(new_lam - lam) < 1e-12:
            lam = new_lam
            break
        lam = new_lam
    return lam


if __name__ == "__main__":
    print(f"{best_ratio():.8f}")  # 132.52756426
