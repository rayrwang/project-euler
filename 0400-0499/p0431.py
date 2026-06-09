import math

import numba

@numba.jit(cache=True)
def wasted_volume(x: float, radius: float, tan_a: float, n_steps: int) -> float:
    """V(x): wasted space when grain is dropped at distance x from centre.

    The grain surface is a cone of repose with apex at the drop point P:
    depth tan(alpha) * |q - P| below the silo top at each point q. So
    V = tan(alpha) * integral over the disk of |q - P|. In polar
    coordinates centred at P the integral collapses to
    (1/3) * int_0^{2pi} L(theta)^3 dtheta with L the distance from P to
    the wall: L = -x cos(theta) + sqrt(R^2 - x^2 sin^2(theta)).
    The integrand is smooth and periodic, so the trapezoid (here midpoint)
    rule converges to machine precision quickly.
    """
    total = 0.0
    h = 2.0 * math.pi / n_steps
    for i in range(n_steps):
        th = (i + 0.5) * h
        s = x * math.sin(th)
        ell = -x * math.cos(th) + math.sqrt(radius * radius - s * s)
        total += ell * ell * ell
    return tan_a * total * h / 3.0

@numba.jit(cache=True)
def solve_x(target: float, radius: float, tan_a: float) -> float:
    """The unique x in [0, R) with V(x) = target (V is increasing in x)."""
    lo, hi = 0.0, radius
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if wasted_volume(mid, radius, tan_a, 1 << 14) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

@numba.jit(cache=True)
def sum_square_wastage_x(radius: float, alpha_deg: float) -> float:
    """Sum of all x giving perfect-square wasted volume."""
    tan_a = math.tan(alpha_deg * math.pi / 180.0)
    v_lo = wasted_volume(0.0, radius, tan_a, 1 << 14)
    v_hi = wasted_volume(radius - 1e-12, radius, tan_a, 1 << 14)
    total = 0.0
    n = 1
    while n * n <= v_hi:
        if n * n >= v_lo:
            total += solve_x(float(n * n), radius, tan_a)
        n += 1
    return total

if __name__ == "__main__":
    t30 = math.tan(math.pi / 6.0)
    # given: alpha = 30 deg, diameter 6 (R = 3), centre delivery
    assert abs(wasted_volume(0.0, 3.0, t30, 1 << 14) - 32.648388556) < 1e-8
    # given: the two square-wastage points for that silo
    assert abs(solve_x(36.0, 3.0, t30) - 1.114785284) < 1e-8
    assert abs(solve_x(49.0, 3.0, t30) - 2.511167869) < 1e-8
    print(f"{sum_square_wastage_x(6.0, 40.0):.9f}")  # 23.386029052
