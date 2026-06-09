from math import atan, log, pi

import numpy as np

A = 4.0  # one leg (right angle at the origin, A = (4, 0))
B = 3.0  # other leg (B = (0, 3)); hypotenuse from (4,0) to (0,3) has length 5

def _inner3(x: float) -> float:
    """Integral over y in [0, B(1-x/A)] of arctan(y/(A-x)); singular pieces cancel."""
    u = A - x
    y = B * (1 - x / A)
    if u <= 0:
        return 0.0
    r = y / u
    return y * atan(r) - 0.5 * u * log(1 + r * r)

def _inner2(y: float) -> float:
    """Integral over x in [0, A(1-y/B)] of arctan(x/(B-y))."""
    w = B - y
    x = A * (1 - y / B)
    if w <= 0:
        return 0.0
    r = x / w
    return x * atan(r) - 0.5 * w * log(1 + r * r)

def _gauss(f, lo: float, hi: float, n: int = 256) -> float:
    nodes, wts = np.polynomial.legendre.leggauss(n)
    mid, half = (lo + hi) / 2, (hi - lo) / 2
    return float(half * np.sum(wts * np.array([f(mid + half * t) for t in nodes])))

def solve() -> float:
    """Probability the ant leaves the 3-4-5 triangle along the hypotenuse.

    From an interior point P the exit side is decided by the random direction, so the
    chance of leaving through a side equals the angle that side subtends at P divided by
    2*pi. Averaging over the uniform point gives prob = (1/(2*pi*Area)) * integral of the
    angle APB subtended by the hypotenuse, where A=(4,0), B=(0,3). Using the closed form
    angle = pi/2 + arctan(x/(B-y)) + arctan(y/(A-x)), the y- (resp. x-) integral is
    elementary and the remaining 1D integral is done by Gauss-Legendre. Area = 6.
    """
    integral = 3 * pi + _gauss(_inner2, 0.0, B) + _gauss(_inner3, 0.0, A)
    return integral / (12 * pi)

if __name__ == "__main__":
    print(f"{solve():.10f}")  # 0.3916721504
