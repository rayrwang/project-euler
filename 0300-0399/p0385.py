from collections import deque
from math import isqrt


def _cmul(p, q):
    return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])


def _cadd(p, q):
    return (p[0] + q[0], p[1] + q[1])


def _csub(p, q):
    return (p[0] - q[0], p[1] - q[1])


def _cneg(p):
    return (-p[0], -p[1])


# Fundamental relative unit of Z[i][omega]: a = 2+i, b = 2i  (a^2 - ab + b^2 = 1).
_A = (2, 1)
_B = (0, 2)
_AmB = _csub(_A, _B)
_Ai = _AmB
_Bi = _cneg(_B)
_AimBi = _csub(_Ai, _Bi)


def _unit(z1, z2):  # multiply alpha = z1 - omega z2 by the unit (grows solutions)
    return (
        _cadd(_cmul(_A, z1), _cmul(_B, z2)),
        _cadd(_cmul(_cneg(_B), z1), _cmul(_AmB, z2)),
    )


def _unit_inv(z1, z2):
    return (
        _cadd(_cmul(_Ai, z1), _cmul(_Bi, z2)),
        _cadd(_cmul(_cneg(_Bi), z1), _cmul(_AimBi, z2)),
    )


def _swap(z1, z2):
    return (z2, z1)


def _rot(z1, z2):  # relabel which vertex is z3
    return (z2, _cneg(_cadd(z1, z2)))


def _neg(z1, z2):
    return (_cneg(z1), _cneg(z2))


_MAPS = (_unit, _unit_inv, _swap, _rot, _neg)


def _gauss_sqrt(d1, d2):
    """All Gaussian integers w with w^2 = d1 + d2*i."""
    nn = d1 * d1 + d2 * d2
    m = isqrt(nn)
    if m * m != nn:
        return []
    a, b = m + d1, m - d1
    if a < 0 or b < 0 or a % 2 or b % 2:
        return []
    w1, w2 = isqrt(a // 2), isqrt(b // 2)
    if w1 * w1 != a // 2 or w2 * w2 != b // 2:
        return []
    out = []
    for s1 in ([0] if w1 == 0 else [w1, -w1]):
        for s2 in ([0] if w2 == 0 else [w2, -w2]):
            if 2 * s1 * s2 == d2:
                out.append((s1, s2))
    return out


def _coord_max(z1, z2):
    z3 = _cneg(_cadd(z1, z2))
    return max(abs(z1[0]), abs(z1[1]), abs(z2[0]), abs(z2[1]), abs(z3[0]), abs(z3[1]))


def _seeds(n0):
    """Every solution with all coordinates <= n0, found directly: for each z1,
    z2 solves z2^2 + z1 z2 + (z1^2 - 39) = 0, i.e. z2 = (-z1 +/- sqrt(156 - 3 z1^2))/2.
    """
    found = set()
    for x1 in range(-n0, n0 + 1):
        for y1 in range(-n0, n0 + 1):
            zx, zy = x1 * x1 - y1 * y1, 2 * x1 * y1
            for w1, w2 in _gauss_sqrt(156 - 3 * zx, -3 * zy):
                nx, ny = -x1 + w1, -y1 + w2
                if nx % 2 or ny % 2:
                    continue
                z1, z2 = (x1, y1), (nx // 2, ny // 2)
                if _coord_max(z1, z2) <= n0:
                    found.add((z1, z2))
    return found


def ellipse_triangle_area_sum(n: int) -> int:
    """Sum of areas of integer triangles (|coords| <= n) whose largest inscribed
    (Steiner) ellipse has foci (+/-sqrt(13), 0).

    By Marden's theorem the inellipse foci are the roots of p'(z) for
    p(z) = prod (z - z_k); foci +/- sqrt(13) force centroid 0
    (z1 + z2 + z3 = 0) and z1 z2 + z2 z3 + z3 z1 = -39, hence with z3 = -z1 - z2
    the single condition z1^2 + z1 z2 + z2^2 = 39 over the Gaussian integers, and
    the area equals (3/2)|Im(conj(z1) z2)|.  Writing alpha = z1 - omega z2 turns
    the condition into a relative norm 39 in Z[zeta_12]/Z[i]; its solutions form
    finitely many orbits under multiplication by the fundamental unit together
    with the triangle relabelling/reflection symmetries.  Each orbit grows
    geometrically, so the full bounded solution set (708 ordered tuples here) is
    reached by a breadth-first walk seeded from the small solutions.  Each
    geometric triangle appears as 6 ordered (z1, z2), so divide accordingly.
    """
    seen = _seeds(min(400, n))
    dq = deque(seen)
    seen = set(seen)
    while dq:
        z1, z2 = dq.popleft()
        for f in _MAPS:
            nxt = f(z1, z2)
            if nxt not in seen and _coord_max(*nxt) <= n:
                seen.add(nxt)
                dq.append(nxt)
    total = 0  # sum of 3*|cross| = sum of 2*area over all ordered tuples
    for (x1, y1), (x2, y2) in seen:
        total += 3 * abs(x1 * y2 - x2 * y1)
    return total // 12  # (total/2 = sum area over tuples) / 6 tuples per triangle


if __name__ == "__main__":
    assert ellipse_triangle_area_sum(8) == 72
    assert ellipse_triangle_area_sum(100) == 34632
    assert ellipse_triangle_area_sum(1000) == 3529008
    print(ellipse_triangle_area_sum(10**9))  # 3776957309612153700
