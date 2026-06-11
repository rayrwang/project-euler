import math

import numba
import numpy as np

# The region {x^4 <= y <= 1} is convex, so the maximum-area n-gon is convex
# with every vertex on the boundary.  Vertices strictly inside the straight
# top edge y = 1 are wasted (three collinear vertices never beat moving one
# onto the curve), so the optimum is a chain of n vertices on y = x^4 with
# x_0 = -1 < x_1 < ... < x_(n-1) = 1, closed by the chord along y = 1.
#
# The shoelace area is stationary in an interior vertex exactly when the
# tangent there is parallel to the chord joining its neighbours:
#     4 x_k^3 = (x_(k+1)^4 - x_(k-1)^4) / (x_(k+1) - x_(k-1)),
# which solves for x_k by a real cube root.  Gauss-Seidel sweeps of this
# update converge to the unique such interior configuration.


@numba.njit(cache=True)
def relax(x: np.ndarray) -> None:
    """Sweep the stationarity update until the vertices stop moving."""
    for _ in range(10**7):
        delta = 0.0
        for k in range(1, len(x) - 1):
            a, b = x[k - 1], x[k + 1]
            slope4 = (a + b) * (a * a + b * b) / 4.0  # (b^4-a^4)/(4(b-a))
            new = np.cbrt(slope4)
            delta = max(delta, abs(new - x[k]))
            x[k] = new
        if delta < 1e-16:
            break


def largest_area(n: int) -> float:
    x = np.linspace(-1.0, 1.0, n)
    relax(x)
    y = x**4
    # Shoelace around the closed polygon (the top edge closes it).
    terms = x[:-1] * y[1:] - x[1:] * y[:-1]
    return (math.fsum(terms.tolist()) + (x[-1] * y[0] - x[0] * y[-1])) / 2.0


if __name__ == "__main__":
    assert f"{largest_area(3):.9f}" == "1.000000000"  # given G(3) = 1
    assert f"{largest_area(5):.9f}" == "1.477309771"  # given G(5)
    print(f"{largest_area(101):.9f}")  # 1.599827123
