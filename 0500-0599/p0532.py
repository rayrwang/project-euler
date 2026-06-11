"""Project Euler problem 532: Nanobots on Geodesics.

n bots sit equidistantly on a small circle of radius 0.999 on a unit
sphere, each chasing the next counterclockwise along the current geodesic
at unit speed.  Find the smallest n for which each bot's drawn line
exceeds 1000, and output the total length of all lines.

By symmetry the bots stay a regular n-gon on a shrinking circle of common
colatitude theta (measured from the pole they converge to).  For a bot at
(theta, 0) chasing the bot at (theta, dphi), the unit tangent toward the
target along the great circle is proportional to P2 - (P1.P2) P1, whose
meridian component gives, with k = 1 - cos(dphi) = 2 sin^2(pi/n),

    dtheta/dt = -cos(theta) sqrt(k / (2 - k sin^2(theta))).

At unit speed the path length of one bot is the convergence time

    T(n) = integral_0^{theta_0} sqrt((2 - k sin^2 t)/k) / cos t dt,

with sin(theta_0) = 0.999.  Substituting u = sin t and then u = tanh s
turns this into a bounded smooth integral over [0, atanh(0.999)], where
the trapezoidal rule converges rapidly.

T(n) is increasing in n (k decreases), so the threshold n is found by
bisection; the answer is n * T(n).

Verified: a direct simulation of the full n-bot pursuit on the sphere
(stepping every bot toward its target's instantaneous geodesic direction
and renormalising) reproduces the integral to the step-size accuracy for
n = 3 and n = 4; the given values for three bots (each line 2.84, total
8.52) match; and the final quadrature is checked for convergence by
doubling the grid.
"""

import numpy as np


def path_length(n: int, m: int = 20001) -> float:
    k = 2 * np.sin(np.pi / n) ** 2
    s = np.linspace(0.0, np.arctanh(0.999), m)
    u = np.tanh(s)
    return float(np.trapezoid(np.sqrt((2 - k * u * u) / k), s))


def simulate(n: int, dt: float = 1e-5) -> float:
    th0 = np.arcsin(0.999)
    ang = 2 * np.pi * np.arange(n) / n
    pos = np.stack(
        [np.sin(th0) * np.cos(ang), np.sin(th0) * np.sin(ang), np.cos(th0) * np.ones(n)],
        axis=1,
    )
    total = 0.0
    while total < 10:
        tgt = np.roll(pos, -1, axis=0)
        dots = (pos * tgt).sum(axis=1, keepdims=True)
        if dots.min() > 1 - 1e-8:
            break
        d = tgt - dots * pos
        d /= np.linalg.norm(d, axis=1, keepdims=True)
        pos = pos + dt * d
        pos /= np.linalg.norm(pos, axis=1, keepdims=True)
        total += dt
    return total


def main() -> None:
    for n in (3, 4):
        assert abs(path_length(n) - simulate(n)) < 1e-3, n
    assert f"{path_length(3):.2f}" == "2.84"
    assert f"{3 * path_length(3):.2f}" == "8.52"

    lo, hi = 2, 10**7
    while lo < hi:
        mid = (lo + hi) // 2
        if path_length(mid) > 1000:
            hi = mid
        else:
            lo = mid + 1
    n = lo
    assert path_length(n) > 1000 > path_length(n - 1)

    ans = n * path_length(n, m=2_000_001)
    assert abs(ans - n * path_length(n, m=1_000_001)) < 1e-4  # converged
    print(f"{ans:.2f}")  # 827306.56


if __name__ == "__main__":
    main()
