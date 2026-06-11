import numpy as np


def bezier_polys(v: float) -> tuple[np.polynomial.Polynomial, np.polynomial.Polynomial]:
    """x(t), y(t) of the cubic Bezier with P0=(1,0) P1=(1,v) P2=(v,1) P3=(0,1)."""
    p = np.polynomial.Polynomial
    t = p([0.0, 1.0])
    b0 = (1 - t) ** 3
    b1 = 3 * t * (1 - t) ** 2
    b2 = 3 * t**2 * (1 - t)
    b3 = t**3
    x = b0 * 1 + b1 * 1 + b2 * v + b3 * 0
    y = b0 * 0 + b1 * v + b2 * 1 + b3 * 1
    return x, y


def area(v: float) -> float:
    """Area enclosed by O P0, the curve, and P3 O via Green's theorem.

    The two straight edges pass through the origin, so they contribute
    nothing to (1/2) closed-integral (x dy - y dx); only the curve does.
    """
    x, y = bezier_polys(v)
    integrand = x * y.deriv() - y * x.deriv()
    anti = integrand.integ()
    return 0.5 * float(anti(1.0) - anti(0.0))


def solve_v() -> float:
    """area(v) is quadratic in v; recover its coefficients and solve."""
    a0 = area(0.0)
    a1 = area(1.0)
    a2 = area(2.0)
    c = (a2 - 2 * a1 + a0) / 2  # quadratic coefficient
    b = a1 - a0 - c
    roots = np.roots([c, b, a0 - np.pi / 4])
    v = min(r.real for r in roots if r.real > 0)
    assert abs(area(v) - np.pi / 4) < 1e-15
    return v


def arc_length(v: float) -> float:
    x, y = bezier_polys(v)
    dx, dy = x.deriv(), y.deriv()
    nodes, weights = np.polynomial.legendre.leggauss(2000)
    t = 0.5 * (nodes + 1.0)  # map [-1, 1] -> [0, 1]
    speed = np.sqrt(dx(t) ** 2 + dy(t) ** 2)
    return 0.5 * float(weights @ speed)


if __name__ == "__main__":
    v = solve_v()
    length = arc_length(v)
    answer = 100 * (length - np.pi / 2) / (np.pi / 2)
    print(f"{answer:.10f}")  # 0.0000372091
