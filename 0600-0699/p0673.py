"""Project Euler Problem 673: Beds and Desks.

A valid permutation must map bed pairs onto bed pairs and desk pairs onto
desk pairs (the conditions only demand pairs stay together, but a
bijection mapping the finitely many pairs into pairs is onto them, and
then singles necessarily go to singles).  So the valid permutations are
exactly the color-preserving automorphisms of the graph with blue edges
the bed pairs and red edges the desk pairs.

Every vertex meets at most one blue and one red edge, so components are
isolated vertices, paths with alternating edge colors, and even
alternating cycles.  Automorphisms permute components within
isomorphism classes and act internally, hence the count is the product
over classes of (internal automorphisms)^count * count!.  Internal
automorphisms are found by brute force over the dihedral candidates: a
path admits only identity and (if its color sequence is a palindrome)
reversal; a cycle's rotations and reflections are checked against the
cyclic color sequence.  Classes are keyed by the canonical (reversal- or
rotation-minimal) color sequence.

Verified: the three worked examples from the statement (2 valid
permutations for n = 4, 8 for n = 6, and 663552 for the n = 36 data),
plus exhaustive permutation checks against random bed/desk pairings for
n <= 7.
"""

import random
from itertools import permutations
from pathlib import Path

MOD = 999_999_937
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def solve(n: int, beds: list[tuple[int, int]],
          desks: list[tuple[int, int]], mod: int) -> int:
    partner: list[list[int]] = [[0] * (n + 1), [0] * (n + 1)]
    for color, pairs in enumerate((beds, desks)):
        for a, b in pairs:
            partner[color][a] = b
            partner[color][b] = a

    def walk(start: int, first_color: int) -> tuple[list[int], list[int]]:
        """Vertices and edge colors along the component from start."""
        verts = [start]
        colors = []
        color = first_color
        while True:
            nxt = partner[color][verts[-1]]
            if nxt == 0 or nxt == start:
                return verts, colors
            verts.append(nxt)
            colors.append(color)
            color ^= 1

    classes: dict[tuple, list[int]] = {}
    seen = [False] * (n + 1)
    for v in range(1, n + 1):
        if seen[v]:
            continue
        degree = (partner[0][v] != 0) + (partner[1][v] != 0)
        if degree == 0:
            seen[v] = True
            sig, autos = ("isolated",), 1
        elif degree == 1:
            first = 0 if partner[0][v] else 1
            verts, colors = walk(v, first)
            for u in verts:
                seen[u] = True
            sig = ("path", min(tuple(colors), tuple(reversed(colors))))
            autos = 1 + (colors == colors[::-1])
        else:
            continue  # cycle vertices are collected below
        classes.setdefault(sig, []).append(autos)
    for v in range(1, n + 1):
        if seen[v]:
            continue
        verts, colors = walk(v, 0)
        colors.append(1)  # closing edge of the alternating cycle
        for u in verts:
            seen[u] = True
        k = len(colors)
        rotations = [tuple(colors[i:] + colors[:i]) for i in range(k)]
        rev = colors[::-1]
        reflections = [tuple(rev[i:] + rev[:i]) for i in range(k)]
        autos = sum(r == rotations[0] for r in rotations)
        autos += sum(r == rotations[0] for r in reflections)
        sig = ("cycle", min(rotations + reflections))
        classes.setdefault(sig, []).append(autos)

    answer = 1
    for members in classes.values():
        for i, autos in enumerate(members, start=1):
            answer = answer * autos % mod * i % mod
    return answer


def solve_brute(n: int, beds: list[tuple[int, int]],
                desks: list[tuple[int, int]]) -> int:
    bed_set = {frozenset(p) for p in beds}
    desk_set = {frozenset(p) for p in desks}
    count = 0
    for perm in permutations(range(1, n + 1)):
        sigma = (0, *perm)
        ok = all(
            frozenset((sigma[a], sigma[b])) in pairs
            for pairs, src in ((bed_set, beds), (desk_set, desks))
            for a, b in src
        )
        count += ok
    return count


def read_pairs(name: str) -> list[tuple[int, int]]:
    pairs = []
    for line in (ASSETS / name).read_text().split():
        a, b = line.split(",")
        pairs.append((int(a), int(b)))
    return pairs


EXAMPLE_36_BEDS = [(2, 13), (4, 30), (5, 27), (6, 16), (10, 18), (12, 35),
                   (14, 19), (15, 20), (17, 26), (21, 32), (22, 33),
                   (24, 34), (25, 28)]
EXAMPLE_36_DESKS = [(1, 35), (2, 22), (3, 36), (4, 28), (5, 25), (7, 18),
                    (9, 23), (13, 19), (14, 33), (15, 34), (20, 24),
                    (26, 29), (27, 30)]

if __name__ == "__main__":
    big = 10**9  # effectively exact for the checks
    assert solve(4, [(2, 3)], [(1, 3), (2, 4)], big) == 2
    assert solve(6, [(1, 2), (3, 4), (5, 6)], [(3, 6), (4, 5)], big) == 8
    assert solve(36, EXAMPLE_36_BEDS, EXAMPLE_36_DESKS, big) == 663552

    rng = random.Random(673)
    for _ in range(60):
        n = rng.randint(1, 7)
        def random_pairing() -> list[tuple[int, int]]:
            verts = list(range(1, n + 1))
            rng.shuffle(verts)
            count = rng.randint(0, n // 2)
            return [(verts[2 * i], verts[2 * i + 1]) for i in range(count)]

        rb, rd = random_pairing(), random_pairing()
        assert solve(n, rb, rd, big) == solve_brute(n, rb, rd)

    beds = read_pairs("0673_beds.txt")
    desks = read_pairs("0673_desks.txt")
    print(solve(500, beds, desks, MOD))  # 700325380
