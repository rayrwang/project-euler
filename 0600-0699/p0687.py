"""Project Euler Problem 687: Shuffling Cards.

A rank is perfect when its four cards are pairwise non-adjacent.  Work with
multiset arrangements (cards within a rank identical); the adjacency
structure only depends on the rank sequence.

Gluing inclusion-exclusion: the number of arrangements in which j specified
ranks are all perfect is

    A_j = sum over (b_1..b_j), b in {1..4} of
          prod_i w(b_i) * (sum_i b_i + 4 (13 - j))! / 24^(13 - j),

    w(b) = (-1)^(4 - b) C(3, b - 1) / b!,

where each constrained rank's four cards are merged into b blocks (the
C(3, b - 1) compositions, signed), all blocks and the 4 (13 - j) free cards
are permuted, and identical blocks/cards are divided out.  The classic
sanity case AABB gives 6 - 6 + 2 = 2 (ABAB and BABA), and A_0 is the total
52! / 24^13.

With B_j = C(13, j) A_j, the number of arrangements with exactly m perfect
ranks is E_m = sum_j (-1)^(j - m) C(j, m) B_j, and the answer is
sum E_m / A_0 over prime m, all in exact rational arithmetic.

Verified: sum_m E_m = A_0, the expected number of perfect ranks
sum_m m E_m / A_0 = 4324 / 425, and the full distribution against a direct
dynamic-programming count of multiset arrangements for a 3-rank deck.
"""

from fractions import Fraction
from math import comb, factorial

RANKS = 13
COPIES = 4

W = {b: Fraction((-1) ** (COPIES - b) * comb(COPIES - 1, b - 1),
                 factorial(b))
     for b in range(1, COPIES + 1)}


def a(j: int, ranks: int = RANKS) -> Fraction:
    """Arrangements (identical cards within rank) with j given ranks perfect."""
    total = Fraction(0)
    free = COPIES * (ranks - j)
    for j1 in range(j + 1):
        for j2 in range(j - j1 + 1):
            for j3 in range(j - j1 - j2 + 1):
                j4 = j - j1 - j2 - j3
                ways = (factorial(j) // factorial(j1) // factorial(j2)
                        // factorial(j3) // factorial(j4))
                blocks = j1 + 2 * j2 + 3 * j3 + 4 * j4
                total += (ways * W[1] ** j1 * W[2] ** j2 * W[3] ** j3
                          * W[4] ** j4 * factorial(blocks + free))
    return total / factorial(COPIES) ** (ranks - j)


def exact_counts(ranks: int = RANKS) -> list[Fraction]:
    """E_m = arrangements with exactly m perfect ranks, m = 0..ranks."""
    b = [comb(ranks, j) * a(j, ranks) for j in range(ranks + 1)]
    return [
        sum(((-1) ** (j - m) * comb(j, m) * b[j]
             for j in range(m, ranks + 1)), Fraction(0))
        for m in range(ranks + 1)
    ]


def brute_distribution(ranks: int) -> list[int]:
    """Perfect-rank distribution over all distinct multiset arrangements."""
    counts = [0] * (ranks + 1)
    remaining = [COPIES] * ranks
    arrangement: list[int] = []

    def rec() -> None:
        if not any(remaining):
            perfect = sum(
                all(x != r or y != r
                    for x, y in zip(arrangement, arrangement[1:]))
                for r in range(ranks)
            )
            counts[perfect] += 1
            return
        for r in range(ranks):
            if remaining[r]:
                remaining[r] -= 1
                arrangement.append(r)
                rec()
                arrangement.pop()
                remaining[r] += 1

    rec()
    return counts


def solve() -> str:
    e = exact_counts()
    total = a(0)
    assert sum(e) == total
    assert sum(m * e_m for m, e_m in enumerate(e)) / total == \
        Fraction(4324, 425)
    p = sum(e[m] for m in (2, 3, 5, 7, 11, 13)) / total
    scaled = (2 * p.numerator * 10**10 + p.denominator) \
        // (2 * p.denominator)
    return f"0.{scaled:010d}"


if __name__ == "__main__":
    small = exact_counts(3)
    norm = a(0, 3)
    brute = brute_distribution(3)
    assert [e / norm for e in small] == \
        [Fraction(c, sum(brute)) for c in brute]
    print(solve())  # 0.3285320869
