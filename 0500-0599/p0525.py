"""Project Euler problem 525: Rolling Ellipse.

An ellipse with semi-axes a and b rolls without slipping along the x-axis
for one complete turn; C(a, b) is the length of the curve traced by the
ellipse's centre.  Find C(1, 4) + C(3, 4) to eight decimal places.

When a convex curve rolls on a line, the body instantaneously rotates
about the contact point, so a rigid point P moves with speed
|P - contact| dphi, where the rotation angle satisfies ds = rho dphi
(rho the radius of curvature at the contact, s arc length).  Hence the
roulette length of the centre is the closed integral of |Q| kappa ds over
the boundary point Q in the body frame.  Parametrising
Q = (a cos t, b sin t), with |Q'| = sqrt(a^2 sin^2 t + b^2 cos^2 t) and
kappa = a b / |Q'|^3, the integrand simplifies to

    a b sqrt(a^2 cos^2 t + b^2 sin^2 t) / (a^2 sin^2 t + b^2 cos^2 t),

integrated over t in [0, 2 pi].  The integrand is smooth and periodic, so
the trapezoidal rule converges faster than any power of the step size.

Verified three ways: the same formula applied to a focus reproduces the
given fact F(a, b) = 2 pi max(a, b); C(2, 4) matches the given
21.38816906; and a direct simulation of the rolling motion — placing the
centre at horizontal position s(t) - Q . T and height |Q x T| for unit
tangent T, then summing polyline segment lengths — agrees with the
integral to 1e-8 for all three ellipses involved.
"""

import numpy as np


def c_integral(a: float, b: float, n: int = 200001) -> float:
    """Roulette length of the centre over one full turn."""
    th = np.linspace(0.0, 2 * np.pi, n)
    num = a * b * np.sqrt(a**2 * np.cos(th) ** 2 + b**2 * np.sin(th) ** 2)
    den = a**2 * np.sin(th) ** 2 + b**2 * np.cos(th) ** 2
    return float(np.trapezoid(num / den, th))


def f_integral(a: float, b: float, n: int = 200001) -> float:
    """Roulette length of a focus over one full turn."""
    hi, lo = max(a, b), min(a, b)
    c = np.sqrt(hi**2 - lo**2)
    th = np.linspace(0.0, 2 * np.pi, n)
    r = hi - c * np.cos(th)  # distance from focus to boundary point
    den = hi**2 * np.sin(th) ** 2 + lo**2 * np.cos(th) ** 2
    return float(np.trapezoid(r * hi * lo / den, th))


def c_simulate(a: float, b: float, n: int = 2000001) -> float:
    """Direct rolling simulation: trace the centre and measure the path."""
    th = np.linspace(0.0, 2 * np.pi, n)
    qx, qy = a * np.cos(th), b * np.sin(th)
    tx, ty = -a * np.sin(th), b * np.cos(th)
    tn = np.hypot(tx, ty)
    s = np.concatenate([[0.0], np.cumsum((tn[1:] + tn[:-1]) / 2 * np.diff(th))])
    cx = s - (qx * tx + qy * ty) / tn
    cy = np.abs(qx * ty - qy * tx) / tn
    return float(np.sum(np.hypot(np.diff(cx), np.diff(cy))))


def main() -> None:
    assert abs(f_integral(2, 4) - 8 * np.pi) < 1e-9
    assert abs(f_integral(3, 1) - 6 * np.pi) < 1e-9
    assert abs(c_integral(2, 4) - 21.38816906) < 5e-9
    for a, b in [(2, 4), (1, 4), (3, 4)]:
        assert abs(c_integral(a, b) - c_simulate(a, b)) < 1e-7
    ans = c_integral(1, 4) + c_integral(3, 4)
    print(f"{ans:.8f}")  # 44.69921807


if __name__ == "__main__":
    main()
