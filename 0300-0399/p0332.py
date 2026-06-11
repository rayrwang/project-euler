import numpy as np


def _lattice_points(r: int) -> list[tuple[int, int, int]]:
    """Integer points on the sphere of radius r centred at the origin."""
    points: set[tuple[int, int, int]] = set()
    r2 = r * r
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            z2 = r2 - x * x - y * y
            if z2 < 0:
                continue
            z = int(round(z2**0.5))
            if z * z == z2:
                points.add((x, y, z))
                points.add((x, y, -z))
    return list(points)


def smallest_area(r: int) -> float:
    """Area of the smallest non-degenerate spherical triangle with integer vertices on radius r.

    The area of a spherical triangle equals its solid angle times r^2; for unit vertex vectors
    a, b, c the solid angle is 2*atan2(|a.(b x c)|, 1 + a.b + b.c + c.a). Three points are
    degenerate (on a common great circle) exactly when they are coplanar with the centre, i.e.
    the integer scalar triple product is zero -- tested exactly to avoid floating-point
    misclassification of very thin slivers. All triples are scanned with one vertex fixed and the
    other two vectorised over the upper triangle."""
    pts = _lattice_points(r)
    n = len(pts)
    if n < 3:
        return 0.0
    ints = np.array(pts, dtype=np.int64)
    unit = ints.astype(float)
    unit /= np.linalg.norm(unit, axis=1, keepdims=True)

    best = np.inf
    for i in range(n - 2):
        ai_int = ints[i]
        ai = unit[i]
        js, ks = np.triu_indices(n - i - 1, k=1)
        js += i + 1
        ks += i + 1
        b, c = unit[js], unit[ks]
        det = np.cross(ints[js], ints[ks]) @ ai_int  # exact: zero iff degenerate
        triple = np.abs(np.cross(b, c) @ ai)
        denom = 1 + (b @ ai) + np.einsum("ij,ij->i", b, c) + (c @ ai)
        excess = np.where(det == 0, np.inf, 2 * np.arctan2(triple, denom))
        if excess.size:
            m = excess.min()
            if m < best:
                best = m
    return best * r * r


def solve(limit: int = 50) -> float:
    return sum(smallest_area(r) for r in range(1, limit + 1))


if __name__ == "__main__":
    assert abs(smallest_area(14) - 3.294040) < 1e-6
    print(f"{solve():.6f}")  # 2717.751525
