"""Project Euler Problem 577: Counting Hexagons.

An equilateral triangle of side n is divided into unit triangles, giving a
triangular lattice of (n+1)(n+2)/2 points.  H(n) counts the regular hexagons
with all 6 vertices on the lattice.  Find sum_{n=3}^{12345} H(n).

Every regular hexagon with lattice vertices (including tilted ones) inscribes
in a unique smallest *upright* lattice hexagon: rotating an upright hexagon's
vertices by the same offset 0 <= t < s along its sides traces out s distinct
regular hexagons sharing its centre, and every lattice hexagon arises this way
exactly once.  An upright hexagon of side s spans a triangle of side 3s, so it
fits in the side-n triangle in C(n-3s+2, 2) positions (the count of unit-
triangle lattices positions of a side-3s triangle, i.e. of a lattice point in
a side-(n-3s) triangle).  Hence

    H(n) = sum_{s>=1, 3s<=n} s * (n-3s+1)(n-3s+2)/2,

which reproduces H(3)=1, H(6)=12, H(20)=966.  Summing over n <= 12345 is a
cheap double loop.
"""

import numba


@numba.jit(cache=True)
def H(n: int) -> int:
    total = 0
    s = 1
    while 3 * s <= n:
        total += s * (n - 3 * s + 1) * (n - 3 * s + 2) // 2
        s += 1
    return total


@numba.jit(cache=True)
def _total(n_max: int) -> int:
    total = 0
    for n in range(3, n_max + 1):
        total += H(n)
    return total


if __name__ == "__main__":
    assert H(3) == 1, H(3)
    assert H(6) == 12, H(6)
    assert H(20) == 966, H(20)
    print(_total(12345))  # 265695031399260211
