import math


def solve(x: float = 40.0) -> float:
    """E(x), the expected number of times Jeff repeats his slicing procedure when
    he stops once less than a fraction F = 1/x of the pie remains, rounded to 10
    decimals.

    Each round he makes two slices to uniformly random border points of the
    remaining sector and keeps only the counterclockwise-most piece. If U1, U2 are
    uniform on [0, 1], the kept fraction multiplies by r = 1 - max(U1, U2), whose
    density is 2(1 - r) on [0, 1]. Writing g(p) for the expected number of rounds
    when a fraction p remains (with F = 1/x), g(p) = 0 for p < F and otherwise
        g(p) = 1 + integral_0^1 g(p r) * 2(1 - r) dr.
    Converting the integral to run over q = p r and differentiating twice turns
    this into the Euler equation
        p^2 g''(p) + 4 p g'(p) = 2,
    with boundary conditions g(F) = 1 and g'(F) = 0 (at the threshold one more
    round always drops below F). The general solution is
        g(p) = C1 + C2 / p^3 + (2/3) ln p,
    and applying the boundary conditions then evaluating at p = 1 gives the closed
    form
        E(x) = 7/9 + (2/3) ln x + 2 / (9 x^3).
    This reproduces E(1) = 1, E(2) = 1.2676536759 and E(7.5) = 2.1215732071.
    """
    return 7 / 9 + (2 / 3) * math.log(x) + 2 / (9 * x**3)


if __name__ == "__main__":
    assert round(solve(1), 10) == 1.0
    assert round(solve(2), 10) == 1.2676536759
    assert round(solve(7.5), 10) == 2.1215732071
    print(f"{solve(40):.10f}")  # 3.2370342194
