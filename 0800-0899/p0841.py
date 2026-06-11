"""Project Euler 841: Regular Star Polygons.

With inradius 1, every edge of {p/q} lies on a tangent line to the
unit circle, and the p tangent points are equally spaced.  Tangent
lines m steps apart meet at distance d_m = sec(pi m / p) from the
centre, so the curve's winding-number-(j) ring is the zigzag 2p-gon
between radii d_{q-j} and d_{q-j+1}, with area
p sin(pi/p) d_{q-j} d_{q-j+1}.  The alternating shading is exactly the
even-odd fill: rings with odd winding number are shaded, hence

    A(p, q) = p sin(pi/p) sum_{m=1}^{q} (-1)^(q-m) sec(pi m/p) sec(pi (m-1)/p).

For {8/3} this telescopes to 24(sqrt 2 - 1), matching the statement.

Numerically the alternating sum is brutal for Fibonacci stars (q up to
3.5 million, with p sin(pi/p) amplifying any cancellation), so
consecutive terms are paired analytically:

  sec_m sec_{m-1} - sec_{m-1} sec_{m-2}
      = 2 sin(pi (m-1)/p) sin(pi/p) / (cos_m cos_{m-1} cos_{m-2}),

which is positive, leaving a sum of like-signed quantities that numpy's
pairwise summation evaluates to full double precision.  The code
reproduces A(8, 3) = 24(sqrt 2 - 1) and the given
A(130021, 50008) = 10.9210371479 before summing the Fibonacci stars.
"""

from __future__ import annotations

from math import cos, fsum, pi, sin

import numpy as np


def shaded_area(p: int, q: int) -> float:
    sp = sin(pi / p)
    ms = np.arange(q, 1, -2, dtype=np.float64)
    a_m = ms * pi / p
    a_m1 = (ms - 1) * pi / p
    a_m2 = (ms - 2) * pi / p
    pairs = 2.0 * np.sin(a_m1) * sp / (np.cos(a_m) * np.cos(a_m1) * np.cos(a_m2))
    total = float(pairs.sum())
    if q % 2 == 1:
        total += 1.0 / cos(pi / p)  # leftover m = 1 term: sec(pi/p) sec(0)
    return p * sp * total


def main() -> None:
    assert abs(shaded_area(8, 3) - 24 * (2**0.5 - 1)) < 1e-12
    assert f"{shaded_area(130021, 50008):.10f}" == "10.9210371479"
    fib = [0, 1, 1]
    for _ in range(40):
        fib.append(fib[-1] + fib[-2])
    total = fsum(shaded_area(fib[n + 1], fib[n - 1]) for n in range(3, 35))
    print(f"{total:.10f}")  # 381.7860132854


if __name__ == "__main__":
    main()
