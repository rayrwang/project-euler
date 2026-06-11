"""Project Euler 857: Beautiful Graphs.

Every pair of vertices carries either a red/blue directed pair or an
undirected green or brown edge; every cycle must contain a red edge
iff it contains a blue one, and no triangle may be entirely green or
entirely brown.

The cycle condition forces rigid structure.  If two vertices are
joined by an undirected path, a red/blue pair between them would close
a cycle with a red edge and no blue one, so the connected components
of the green/brown graph are cliques.  Between two such blocks all red
edges must point the same way (otherwise two reds form a bad cycle
through the blocks), and the resulting tournament on blocks must be
acyclic — i.e. the blocks are linearly ordered, and conversely any
ordered sequence of blocks works.  The triangle condition then only
constrains the 2-colouring inside a block: the number of green/brown
colourings of K_m with no monochromatic triangle is t = 1, 2, 6, 18,
12 for m = 1..5 (verified by brute force below; for m = 5 both colour
classes must be 5-cycles) and zero for m >= 6 by Ramsey's R(3,3) = 6.

Hence G(n) counts ordered set partitions into blocks of size at most
five weighted by t, giving G(n) = sum_m binom(n, m) t_m G(n - m).
Dividing by n! turns this into a constant-coefficient linear
recurrence H(n) = sum_m (t_m / m!) H(n - m), iterated 10^7 times
modulo 10^9 + 7 in a few seconds.  The code reproduces the given
G(3) = 24, G(4) = 186 and G(15) = 12472315010483328.
"""

from __future__ import annotations

from itertools import combinations, product
from math import comb, factorial

MOD = 10**9 + 7
BLOCK_COLORINGS = [1, 1, 2, 6, 18, 12]  # index 0 is a dummy


def colorings_without_mono_triangle(m: int) -> int:
    edges = list(combinations(range(m), 2))
    triangles = list(combinations(range(m), 3))
    count = 0
    for colors in product((0, 1), repeat=len(edges)):
        col = dict(zip(edges, colors))
        if all(
            not (col[(a, b)] == col[(a, c)] == col[(b, c)]) for a, b, c in triangles
        ):
            count += 1
    return count


def beautiful_exact(n: int) -> int:
    g = [0] * (n + 1)
    g[0] = 1
    for k in range(1, n + 1):
        g[k] = sum(
            comb(k, m) * BLOCK_COLORINGS[m] * g[k - m] for m in range(1, min(5, k) + 1)
        )
    return g[n]


def beautiful_mod(n: int) -> int:
    coef = [
        BLOCK_COLORINGS[m] * pow(factorial(m), MOD - 2, MOD) % MOD for m in range(6)
    ]
    hist = [1, 0, 0, 0, 0]  # H(k-1), ..., H(k-5)
    for _ in range(n):
        h = (
            coef[1] * hist[0]
            + coef[2] * hist[1]
            + coef[3] * hist[2]
            + coef[4] * hist[3]
            + coef[5] * hist[4]
        ) % MOD
        hist = [h, hist[0], hist[1], hist[2], hist[3]]
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i % MOD
    return fact * hist[0] % MOD


def main() -> None:
    for m in range(1, 6):
        assert colorings_without_mono_triangle(m) == BLOCK_COLORINGS[m]
    assert beautiful_exact(3) == 24
    assert beautiful_exact(4) == 186
    assert beautiful_exact(15) == 12472315010483328
    assert beautiful_mod(15) == 12472315010483328 % MOD
    print(beautiful_mod(10**7))  # 966332096


if __name__ == "__main__":
    main()
