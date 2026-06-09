from fractions import Fraction
from itertools import product
from math import comb

# One unit has 7 vertices: 0=TL, 1=BL (the shared left pair), 2..4 the middle
# chain top-to-bottom, 5=TR, 6=BR. Unit A additionally has the bottom edge.
_EDGES = ((0, 1), (5, 6), (0, 5), (0, 2), (5, 2), (2, 3), (3, 4), (1, 4), (6, 4))
_BOTTOM = (1, 6)


def _extensions(c: int, with_bottom: bool) -> int:
    # Number of proper colourings of the 5 right-hand vertices once the left
    # pair is fixed to two distinct colours (the count is colour-symmetric).
    edges = _EDGES + ((_BOTTOM,) if with_bottom else ())
    col = [0, 1, 0, 0, 0, 0, 0]
    cnt = 0
    for assign in product(range(c), repeat=5):
        col[2:] = assign
        if all(col[u] != col[v] for u, v in edges):
            cnt += 1
    return cnt


def _interpolate(xs: list[int], ys: list[int], x: int) -> int:
    # Exact Lagrange interpolation; the extension count is a degree-5
    # polynomial in c, so 7 sample points pin it down.
    total = Fraction(0)
    for i, (xi, yi) in enumerate(zip(xs, ys)):
        term = Fraction(yi)
        for j, xj in enumerate(xs):
            if j != i:
                term *= Fraction(x - xj, xi - xj)
        total += term
    assert total.denominator == 1
    return total.numerator


def solve(a: int = 25, b: int = 75, c: int = 1984) -> int:
    # A configuration is an ordering of the units (C(a+b, a) choices) times a
    # colouring: c(c-1) for the first vertical pair, then an independent
    # extension factor per unit.
    xs = list(range(2, 9))
    e_a = _interpolate(xs, [_extensions(x, True) for x in xs], c)
    e_b = _interpolate(xs, [_extensions(x, False) for x in xs], c)
    return comb(a + b, a) * c * (c - 1) * e_a**a * e_b**b % 10**8


if __name__ == "__main__":
    print(solve())  # 61190912
