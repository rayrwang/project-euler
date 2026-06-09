import numpy as np

# The locus equidistant from circle c (centre M, radius r) and interior
# point G satisfies |PM| + |PG| = r: an ellipse with foci M(-2000, 1500),
# G(8000, 1500) and 2a = 15000, hence centre (3000, 1500), a^2 = 56250000,
# c = 5000, b^2 = a^2 - c^2 = 31250000. Lattice points shift to integer
# centred coordinates (X, Y).
#
# For exterior P, the pair-of-tangents conic S S1 = T^2 has quadratic part
# with A + B = D / (a^2 b^2) and H^2 - A B = S1 / (a^2 b^2), where
# D = X^2 + Y^2 - (a^2 + b^2) (the director circle) and S1 is the exterior
# measure. So with E = X^2 b^2 + Y^2 a^2 - a^2 b^2 (E > 0 iff exterior,
# E = 0 on the ellipse - those points have no tangent pair and are excluded):
# the ray angle exceeds 90 deg iff D <= 0, and otherwise equals the line
# angle phi with tan^2(phi) = 4 E a^2 b^2 / D^2 / (a^2 b^2) = 4E / D^2, so
# angle > 45 deg iff D <= 0 or 4E > D^2 - exact integer arithmetic
# (verified against direct numeric tangent construction). On the boundary
# 4E = D^2 the angle is exactly 45 deg and is excluded.
#
# Bounding box: on the region boundary, D^2 = 4E <= 4 a^2 (X^2 + Y^2), so
# with r^2 = X^2 + Y^2: r^2 - (a^2 + b^2) <= 2 a r, giving
# r <= a + sqrt(2 a^2 + b^2) < 20000.


def solve() -> int:
    a2, b2 = 56_250_000, 31_250_000
    s = a2 + b2
    bound = 20_000
    xs = np.arange(0, bound + 1, dtype=np.int64)
    x2 = xs * xs
    x2b = x2 * b2
    total = 0
    for y in range(0, bound + 1):
        e = x2b + (y * y * a2 - a2 * b2)
        d = x2 + (y * y - s)
        good = (e > 0) & ((d <= 0) | (4 * e > d * d))
        c = int(np.count_nonzero(good))
        row = 2 * c - int(good[0])  # reflect X -> -X without double-counting 0
        total += row if y == 0 else 2 * row  # reflect Y -> -Y likewise
    return total


if __name__ == "__main__":
    print(solve())  # 810834388
