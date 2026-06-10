from math import atan2, cos, gcd, sin

def dist_DE(ra, rb, rc):
    """Distance between the circumcentre D of the arc triangle and the
    centre E of its incircle.

    The circle through the three tangency points of three mutually
    externally tangent circles is the incircle of the triangle of their
    centres, so D is that incentre. The green circle externally tangent to
    all three is the inner Soddy circle: its curvature is given by the
    Descartes circle theorem k4 = k1+k2+k3 + 2 sqrt(k1k2+k2k3+k3k1) and
    its centre by the complex Descartes theorem
        z4 k4 = z1 k1 + z2 k2 + z3 k3 +- 2 sqrt(k1k2 z1z2 + ...),
    with the sign fixed by checking external tangency |z4 - z1| = 1/k4 + ra.
    """
    ab, ac, bc = ra + rb, ra + rc, rb + rc
    cx = (ab * ab + ac * ac - bc * bc) / (2.0 * ab)
    cy = (ac * ac - cx * cx) ** 0.5
    s = ab + ac + bc
    dx = (ac * ab + ab * cx) / s  # incentre with weights (bc, ac, ab)
    dy = (ab * cy) / s
    k1, k2, k3 = 1.0 / ra, 1.0 / rb, 1.0 / rc
    k4 = k1 + k2 + k3 + 2.0 * (k1 * k2 + k2 * k3 + k3 * k1) ** 0.5
    # with z1 = 0 only the z2 z3 cross term survives inside the sqrt
    pr = (ab * k2) * (cx * k3)
    pi = (ab * k2) * (cy * k3)
    m = (pr * pr + pi * pi) ** 0.25
    th = 0.5 * atan2(pi, pr)
    sr, si = m * cos(th), m * sin(th)
    best = -1.0
    for sgn in (-1.0, 1.0):
        z4r = (ab * k2 + cx * k3 + 2.0 * sgn * sr) / k4
        z4i = (cy * k3 + 2.0 * sgn * si) / k4
        if abs((z4r * z4r + z4i * z4i) ** 0.5 - (1.0 / k4 + ra)) < 1e-6:
            best = ((z4r - dx) ** 2 + (z4i - dy) ** 2) ** 0.5
    return best

def expected_d(limit):
    tot = 0.0
    cnt = 0
    for ra in range(1, limit + 1):
        for rb in range(ra + 1, limit + 1):
            g0 = gcd(ra, rb)
            for rc in range(rb + 1, limit + 1):
                if gcd(g0, rc) == 1:
                    tot += dist_DE(float(ra), float(rb), float(rc))
                    cnt += 1
    return tot / cnt

if __name__ == "__main__":
    print(f"{expected_d(100):.8f}")  # 3.64039141
