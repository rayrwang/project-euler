import math

# Sort the three points by x: the two x-gaps (u, v) have density 6(1-u-v) on
# the simplex, the y-gaps (p, q) are independent with the same law, and the
# y-ranks of the x-sorted points form an independent uniform permutation.
# For fixed gaps and permutation the three rectangle areas are linear forms
# in (p, q), so the median switches along rays through the origin; a sector
# meets the simplex in a triangle O-V1-V2 with V1, V2 on p+q = 1, where
#   integral over the triangle of (Ap+Bq)(1-p-q) = |det(V1,V2)|(L(V1)+L(V2))/24.
# The inner sum M(u, v) is homogeneous of degree 1, so with tau = v/u the
# answer collapses to a one-dimensional integral:
#   E = 3 * integral_0^inf mean_sigma m_sigma(tau) / (1+tau)^3 dtau.

PERMS = ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0))
Y_DIFF = {(0, 1): (1, 0), (1, 2): (0, 1), (0, 2): (1, 1)}


def forms_for_perm(perm, u, v):
    """Areas as (alpha, beta) with area = alpha*p + beta*q."""
    x_diff = {(0, 1): u, (1, 2): v, (0, 2): u + v}
    out = []
    for (i, j), width in x_diff.items():
        ca, cb = Y_DIFF[tuple(sorted((perm[i], perm[j])))]
        out.append((width * ca, width * cb))
    return out


def sector_sum(forms):
    """Integral of the median form times (1-p-q) over the gap simplex."""
    slopes = set()
    for i in range(3):
        for j in range(i + 1, 3):
            da = forms[i][0] - forms[j][0]
            db = forms[i][1] - forms[j][1]
            if db != 0:  # equality ray q/p = -da/db
                s = -da / db
                if s > 1e-15:
                    slopes.add(s)
    angles = sorted({0.0, math.pi / 2, *(math.atan(s) for s in slopes)})

    def vertex(theta):
        c, s = math.cos(theta), math.sin(theta)
        return (c / (c + s), s / (c + s))

    total = 0.0
    for a0, a1 in zip(angles, angles[1:]):
        mid = (a0 + a1) / 2
        pm, qm = math.cos(mid), math.sin(mid)
        order = sorted(range(3), key=lambda i: forms[i][0] * pm + forms[i][1] * qm)
        alpha, beta = forms[order[1]]
        v1, v2 = vertex(a0), vertex(a1)
        det = abs(v1[0] * v2[1] - v1[1] * v2[0])
        total += det * (alpha * (v1[0] + v2[0]) + beta * (v1[1] + v2[1])) / 24.0
    return total


def m_avg(tau):
    return sum(sector_sum(forms_for_perm(p, 1.0, tau)) for p in PERMS) / 6.0


def gl_nodes(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        dp = 1.0
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        nodes.append(x)
        weights.append(2 / ((1 - x * x) * dp * dp))
    return nodes, weights


def expected_median(npanels):
    nodes, weights = gl_nodes(24)

    def gl(f, a, b):
        h, c = (b - a) / 2, (a + b) / 2
        return h * sum(w * f(c + h * x) for x, w in zip(nodes, weights))

    def direct(t):  # tau in (0, 1]
        return m_avg(t) / (1 + t) ** 3

    def inverted(w):  # tau = 1/w covers [1, inf)
        t = 1 / w
        return m_avg(t) / (1 + t) ** 3 / (w * w)

    total = 0.0
    for k in range(npanels):
        a, b = k / npanels, (k + 1) / npanels
        total += gl(direct, a, b) + gl(inverted, max(a, 1e-12), b)
    return 3 * total


if __name__ == "__main__":
    coarse = expected_median(200)
    fine = expected_median(400)
    assert abs(coarse - fine) < 1e-11, (coarse, fine)

    print(f"{fine:.10f}")  # 0.1017786859
