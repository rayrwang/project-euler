"""Project Euler 842: Irregular Star Polygons.

An n-star polygon is a Hamiltonian cycle on the n-th roots of unity,
with (n-1)!/2 polygons in total.  By linearity, summing crossing PAIRS
of edges over all polygons is easy: every 4-subset of vertices yields
exactly one interleaved chord pair, and the number of polygons
containing two given disjoint chords is (n-3)! * 2, giving the main
term binom(n,4) * 2 (n-3)!.  This over-counts intersection POINTS
wherever m >= 3 polygon edges pass through a common interior point:
such a point contributes binom(m,2) pairs but should count once.

Chords of the regular n-gon through a common interior point are
pairwise vertex-disjoint, so with g(j) = (n-j-1)! 2^j / 2 polygons
containing j prescribed chords, inclusion-exclusion over the M
concurrent chords gives the number of polygons using at least two of
them, and the correction per concurrence point depends only on M:
binom(M,2) 2 (n-3)!  minus that count.  The concurrence spectrum of
the regular n-gon (the Poonen-Rubinstein coincidences, including n/2
diameters through the centre for even n) is computed directly: all
binom(n,4) chord-pair intersections via the unit-circle chord formula
z = (ab(c+d) - cd(a+b)) / (ab - cd), grouped by spatial hashing with
neighbour merging; the identity binom(M,2) = (group size) is asserted
for every group, which would fail loudly if floating-point grouping
ever merged or split points incorrectly.  The code verifies T(5) = 20,
T(6) = 164 and T(7) = 1680 against a brute force over all polygons and
reproduces the given T(8) = 14640.
"""

from __future__ import annotations

import cmath
from collections import defaultdict
from itertools import permutations
from math import comb, cos, factorial, pi, sin

MOD = 10**9 + 7


def concurrences(n: int) -> dict[int, int]:
    """Count interior points where exactly M >= 3 chords meet."""
    verts = [cmath.exp(2j * pi * k / n) for k in range(n)]
    buckets: dict[tuple[int, int], list] = defaultdict(list)
    scale = 10**6
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for ll in range(k + 1, n):
                    a, b = verts[i], verts[k]
                    c, d = verts[j], verts[ll]
                    ab, cd = a * b, c * d
                    z = (ab * (c + d) - cd * (a + b)) / (ab - cd)
                    key = (round(z.real * scale), round(z.imag * scale))
                    buckets[key].append((i, k, j, ll, z))

    items: list[tuple[tuple[int, int], tuple]] = []
    for key, lst in buckets.items():
        for rec in lst:
            items.append((key, rec))
    parent = list(range(len(items)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    pos: dict[tuple[int, int], list[int]] = defaultdict(list)
    for idx, (key, _) in enumerate(items):
        pos[key].append(idx)
    for idx, (key, rec) in enumerate(items):
        kx, ky = key
        z = rec[4]
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for jdx in pos.get((kx + dx, ky + dy), ()):
                    if jdx > idx and abs(z - items[jdx][1][4]) < 1e-9:
                        rx, ry = find(idx), find(jdx)
                        if rx != ry:
                            parent[rx] = ry

    groups: dict[int, list[int]] = defaultdict(list)
    for idx in range(len(items)):
        groups[find(idx)].append(idx)
    counts: dict[int, int] = defaultdict(int)
    for grp in groups.values():
        if len(grp) < 2:
            continue
        chords = set()
        for idx in grp:
            i, k, j, ll, _ = items[idx][1]
            chords.add((i, k))
            chords.add((j, ll))
        m = len(chords)
        assert comb(m, 2) == len(grp), (n, m, len(grp))
        counts[m] += 1
    return dict(counts)


def star_total(n: int) -> int:
    main = comb(n, 4) * 2 * factorial(n - 3)
    if n < 6:
        return main
    half = factorial(n - 1) // 2

    def g(j: int) -> int:
        return factorial(n - j - 1) * 2**j // 2

    correction = 0
    for m, c in concurrences(n).items():
        pairs = comb(m, 2) * 2 * factorial(n - 3)
        n0 = sum((-1) ** j * comb(m, j) * g(j) for j in range(m + 1))
        n1 = sum((-1) ** (j - 1) * j * comb(m, j) * g(j) for j in range(1, m + 1))
        correction += c * (pairs - (half - n0 - n1))
    return main - correction


def brute_total(n: int) -> int:
    pts = [(cos(2 * pi * k / n), sin(2 * pi * k / n)) for k in range(n)]

    def crossing(p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        den = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
        if abs(den) < 1e-12:
            return None
        t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / den
        u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / den
        if 1e-9 < t < 1 - 1e-9 and 1e-9 < u < 1 - 1e-9:
            return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
        return None

    total = 0
    for perm in permutations(range(1, n)):
        if perm[0] > perm[-1]:
            continue
        cyc = (0, *perm)
        edges = [(cyc[i], cyc[(i + 1) % n]) for i in range(n)]
        seen = set()
        for i in range(n):
            for j in range(i + 1, n):
                a, b = edges[i]
                c, d = edges[j]
                if len({a, b, c, d}) < 4:
                    continue
                p = crossing(pts[a], pts[b], pts[c], pts[d])
                if p:
                    seen.add((round(p[0], 7), round(p[1], 7)))
        total += len(seen)
    return total


def main() -> None:
    for n in (5, 6, 7):
        assert star_total(n) == brute_total(n)
    assert star_total(5) == 20
    assert star_total(8) == 14640
    print(sum(star_total(n) for n in range(3, 61)) % MOD)  # 885226002


if __name__ == "__main__":
    main()
