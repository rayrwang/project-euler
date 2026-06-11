import numpy as np

# Circle C_k has radius s^k and centre at distance d s^k from the origin at
# angle k theta, so external tangency of C_0 and C_m reads
#     d^2 (1 + s^(2m) - 2 s^m cos(m theta)) = (1 + s^m)^2,
# and by self-similarity the same then holds between C_k and C_(k+m) for
# every k.  The three given tangencies (m = 1, 7, 8) determine (s, theta, d):
# a coarse residual scan locates the basins and Newton iterations in 80-bit
# floats polish the root; the physical solution is the one with d > 1 (the
# origin is outside C_0) and no overlapping circles.
#
# Every consecutive pair of the tangencies bounds a curvilinear triangle, so
# the gaps come in two families per index k, (C_k, C_k+7, C_k+8) and
# (C_k, C_k+1, C_k+8), whose areas scale by s^(2k).  A gap between three
# mutually tangent circles is the area of the triangle of centres minus the
# three circular sectors, so the total green area is
#     (A(1, s^7, s^8) + A(1, s, s^8)) / (1 - s^2).

LD = np.longdouble


def factors(s, th, m):
    """d^2 required to make C_0 and C_m externally tangent."""
    return (1 + s**m) ** 2 / (1 + s ** (2 * m) - 2 * s**m * np.cos(m * th))


def residual(v):
    s, th = v
    return np.array(
        [
            factors(s, th, 1) - factors(s, th, 7),
            factors(s, th, 1) - factors(s, th, 8),
        ],
        dtype=v.dtype,
    )


def newton(s0: float, th0: float):
    v = np.array([s0, th0], dtype=LD)
    h = LD(1e-12)
    for _ in range(80):
        r = residual(v)
        jac = np.empty((2, 2), dtype=LD)
        for j in range(2):
            vp = v.copy()
            vp[j] += h
            jac[:, j] = (residual(vp) - r) / h
        det = jac[0, 0] * jac[1, 1] - jac[0, 1] * jac[1, 0]
        if det == 0:
            return None
        dv0 = (jac[1, 1] * r[0] - jac[0, 1] * r[1]) / det
        dv1 = (jac[0, 0] * r[1] - jac[1, 0] * r[0]) / det
        v[0] -= dv0
        v[1] -= dv1
        if max(abs(dv0), abs(dv1)) < LD(1e-19):
            break
    return v


def physical(s, th) -> bool:
    """Origin outside C_0 and no two of the first circles overlap."""
    if not (0 < s < 1 and 0 < th < 2 * np.pi):
        return False
    d = np.sqrt(factors(s, th, 1))
    if d <= 1:
        return False
    n = 80
    k = np.arange(n)
    x = d * s**k * np.cos(k * th)
    y = d * s**k * np.sin(k * th)
    r = s ** k.astype(LD)
    for i in range(n):
        dist = np.sqrt((x - x[i]) ** 2 + (y - y[i]) ** 2)
        if np.any((dist < r + r[i] - LD(1e-12)) & (k != i)):
            return False
    return True


def gap_area(r1, r2, r3):
    """Curvilinear triangle between three mutually tangent circles."""
    a, b, c = r2 + r3, r1 + r3, r1 + r2
    sp = (a + b + c) / 2
    heron = np.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    a1 = np.arccos((b * b + c * c - a * a) / (2 * b * c))
    a2 = np.arccos((a * a + c * c - b * b) / (2 * a * c))
    a3 = np.arccos((a * a + b * b - c * c) / (2 * a * b))
    return heron - (a1 * r1 * r1 + a2 * r2 * r2 + a3 * r3 * r3) / 2


if __name__ == "__main__":
    # locate root basins as local minima of the relative residual surface
    ss, ths = np.meshgrid(
        np.linspace(0.55, 0.99, 250), np.linspace(0.05, np.pi, 400), indexing="ij"
    )
    r1 = factors(ss, ths, 1) - factors(ss, ths, 7)
    r2 = factors(ss, ths, 1) - factors(ss, ths, 8)
    err = (r1 * r1 + r2 * r2) / factors(ss, ths, 1) ** 2
    minima = np.ones_like(err, dtype=bool)
    minima[0, :] = minima[-1, :] = minima[:, 0] = minima[:, -1] = False
    core = err[1:-1, 1:-1]
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di or dj:
                minima[1:-1, 1:-1] &= core <= err[1 + di : 249 + di, 1 + dj : 399 + dj]
    roots = []
    for i, j in np.argwhere(minima & (err < 1e-3)):
        v = newton(float(ss[i, j]), float(ths[i, j]))
        if v is None:
            continue
        rel = np.max(np.abs(residual(v))) / factors(v[0], v[1], 1)
        if rel > LD(1e-16) or not physical(v[0], v[1]):
            continue
        if all(abs(v[0] - u[0]) > 1e-9 or abs(v[1] - u[1]) > 1e-9 for u in roots):
            roots.append(v)
    assert len(roots) == 1
    s, th = roots[0]
    d = np.sqrt(factors(s, th, 1))

    # all claimed tangencies hold for many k (self-similarity sanity check)
    for k in range(15):
        for m in (1, 7, 8):
            cx = d * s**k * np.cos(k * th) - d * s ** (k + m) * np.cos((k + m) * th)
            cy = d * s**k * np.sin(k * th) - d * s ** (k + m) * np.sin((k + m) * th)
            gap = np.sqrt(cx * cx + cy * cy) - (s**k + s ** (k + m))
            assert abs(gap) < 1e-15

    total = (gap_area(LD(1), s**7, s**8) + gap_area(LD(1), s, s**8)) / (1 - s * s)
    # the rounding to 10 places must not sit on a knife edge
    scaled = total * LD(10) ** 10
    assert abs(scaled - np.floor(scaled) - 0.5) > 1e-3
    print(np.format_float_positional(total, precision=10, unique=False))  # 0.7718678168
