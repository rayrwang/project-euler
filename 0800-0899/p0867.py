"""Project Euler 867: Tiling Dodecagon.

Count tilings of a regular dodecagon of side n by unit-side regular
polygons (triangles, squares, hexagons and dodecagons fit).

Structure theorem (found empirically with an exact-arithmetic region
enumerator, then verified): refining each hexagon into 6 triangles and
each unit dodecagon tile into a fixed canonical square/triangle
refinement gives a bijection between tilings and pairs (S, M) where S
is a pure square-triangle "skeleton" and M a set of pairwise disjoint
marked patches (hexagram stars and canonical dodecagon wheels).

The skeletons biject with words w in {A,B}^(2n) containing n of each
letter, read from the centre outwards: triangles come in two phases, A
(edges at 0/60/120 degrees) and B (30/90/150), and the contour after a
prefix with a A's and b B's is the Minkowski sum of a phase-A and b
phase-B unit hexagons.  An A-row adds 6 trapezoids of 2a+1 phase-A
triangles on the even-direction sides and 6 rectangles of b squares on
the odd-direction sides (and symmetrically for B), so every word yields
a valid C6-symmetric tiling and every pure tiling arises exactly once:
there are C(2n, n) skeletons.

Patches factor over the triangle-only regions of the skeleton: the
leading run of length k0 gives a triangulated hexagon of side k0 and
every later maximal run (length k, preceded by c letters of its own
kind) gives 6 disjoint trapezoids Trap(c, k).  Hexagram stars sit on
interior lattice vertices of these regions and conflict exactly when
the centres are lattice-adjacent, so the number of patch sets is a
product of independent-set counts of small triangular-lattice graphs.
The only canonical dodecagon wheel is the central one, available iff
k0 = 1 with leading letter A; choosing it blocks just the central star
(the wedge apex triangles it uses touch no interior vertex).

Answer: T(10) mod 1_000_000_007.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

MOD = 10**9 + 7

# Triangular-lattice neighbourhoods for the two coordinate systems used
# below: centred hexagon coordinates and trapezoid line/offset coords.
NEIGH_HEX = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))
NEIGH_TRAP = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))


def count_independent_sets(
    vertices: list[tuple[int, int]], neigh: tuple[tuple[int, int], ...]
) -> int:
    """Count independent sets of the induced triangular-lattice graph."""
    vs = sorted(vertices, key=lambda p: (p[1], p[0]))
    index = {v: i for i, v in enumerate(vs)}
    if not vs:
        return 1
    prev: list[list[int]] = []
    for i, v in enumerate(vs):
        offs = []
        for dx, dy in neigh:
            j = index.get((v[0] + dx, v[1] + dy))
            if j is not None and j < i:
                offs.append(i - j)
        prev.append(offs)
    window = max((max(p) for p in prev if p), default=1)
    frontier = {0: 1}
    for offs in prev:
        nxt: dict[int, int] = {}
        for mask, cnt in frontier.items():
            shifted = (mask << 1) & ((1 << window) - 1)
            nxt[shifted] = (nxt.get(shifted, 0) + cnt) % MOD
            if all(not (mask >> (off - 1)) & 1 for off in offs):
                taken = shifted | 1
                nxt[taken] = (nxt.get(taken, 0) + cnt) % MOD
        frontier = nxt
    return sum(frontier.values()) % MOD


@lru_cache(maxsize=None)
def is_hexagon(k: int) -> int:
    """Independent sets of interior vertices of a side-k triangulated hexagon."""
    verts = [
        (x, y)
        for x in range(-k + 1, k)
        for y in range(-k + 1, k)
        if abs(x + y) <= k - 1
    ]
    return count_independent_sets(verts, NEIGH_HEX)


@lru_cache(maxsize=None)
def is_trapezoid(c: int, k: int) -> int:
    """Independent sets of interior vertices of a (c, c + k) trapezoid stack."""
    verts = [(i, j) for j in range(1, k) for i in range(1, c + j)]
    return count_independent_sets(verts, NEIGH_TRAP)


def runs_of(word: list[str]) -> list[tuple[str, int]]:
    runs: list[tuple[str, int]] = []
    i = 0
    while i < len(word):
        j = i
        while j < len(word) and word[j] == word[i]:
            j += 1
        runs.append((word[i], j - i))
        i = j
    return runs


def tilings(n: int) -> int:
    """Number of tilings of the side-n regular dodecagon, modulo MOD."""
    total = 0
    for pos_a in combinations(range(2 * n), n):
        word = ["B"] * (2 * n)
        for i in pos_a:
            word[i] = "A"
        runs = runs_of(word)
        leading, k0 = runs[0]
        a = k0 if leading == "A" else 0
        b = k0 - a
        prod = is_hexagon(k0)
        wheel = 1 if k0 == 1 and leading == "A" else 0
        for letter, k in runs[1:]:
            c = a if letter == "A" else b
            factor = pow(is_trapezoid(c, k), 6, MOD)
            prod = prod * factor % MOD
            wheel = wheel * factor % MOD
            if letter == "A":
                a += k
            else:
                b += k
        total = (total + prod + wheel) % MOD
    return total


def main() -> None:
    assert tilings(1) == 5
    assert tilings(2) == 48
    # Cross-checked against an exact-arithmetic brute-force enumerator:
    assert tilings(3) == 228912
    assert tilings(4) == 33065063
    print(tilings(10))  # 870557257


if __name__ == "__main__":
    main()
