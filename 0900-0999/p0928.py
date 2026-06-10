"""Project Euler 928: Cribbage.

Suits never affect the score, so a hand is a rank-count vector
(c_1..c_13) with c_r in 0..4, weighted by prod C(4, c_r).  We count
vectors with hand score = cribbage score by a DP over ranks processed
from king down to ace, tracking the difference D = crib - hand together
with exactly the information the remaining ranks need:

  - runs: the length and count-product of the run of consecutive
    present ranks currently open (a gap closes it, scoring len * prod
    when len >= 3 -- "all locally maximum runs" is precisely this);
  - fifteens: the vector f[1..14] counting card subsets of the
    processed suffix with each value sum (f[15 - j*v] new subsets are
    completed when j cards of value v are added, each worth 2);
  - pairs contribute 2*C(c, 2) immediately and the hand score
    subtracts c * min(r, 10).

Both scores only grow, and the total hand score is at most 340, so any
state whose D plus the pending run score exceeds the maximum remaining
hand score is dead; this prunes the run-product explosion of dense low
hands.  Entries f[s] that no remaining card values can complete are
zeroed, collapsing states near the end.  The empty hand (D = 0) is
subtracted at the end.

Validated against direct enumeration of all 5^R count vectors for
reduced decks with ranks 1..R, R <= 6, and on the two worked examples.
"""

from collections import defaultdict
from math import comb


def _val(r: int) -> int:
    return min(r, 10)


def score_counts(counts: dict[int, int]) -> tuple[int, int]:
    """(hand score, cribbage score) of a rank-count multiset."""
    ranks = sorted(counts)
    hand = sum(counts[r] * _val(r) for r in ranks)
    crib = sum(2 * comb(counts[r], 2) for r in ranks)
    present = [r for r in ranks if counts[r] > 0]
    i = 0
    while i < len(present):
        j = i
        while j + 1 < len(present) and present[j + 1] == present[j] + 1:
            j += 1
        if j - i + 1 >= 3:
            prod = 1
            for r in present[i:j + 1]:
                prod *= counts[r]
            crib += (j - i + 1) * prod
        i = j + 1
    f = [0] * 16
    f[0] = 1
    for r in ranks:
        c, v = counts[r], _val(r)
        if c:
            nf = f[:]
            for j in range(1, c + 1):
                w = comb(c, j)
                for s in range(15, j * v - 1, -1):
                    nf[s] += w * f[s - j * v]
            f = nf
    return hand, crib + 2 * f[15]


def solve(num_ranks: int = 13) -> int:
    fh = [0] * (num_ranks + 2)  # max remaining hand score below rank r
    for r in range(1, num_ranks + 1):
        fh[r] = sum(4 * _val(j) for j in range(1, r))
    c4 = [comb(4, c) for c in range(5)]
    cc = [[comb(c, j) for j in range(c + 1)] for c in range(5)]

    states: dict[tuple, int] = {(0, 0, 1, (0,) * 14): 1}
    for r in range(num_ranks, 0, -1):
        v = _val(r)
        new: dict[tuple, int] = defaultdict(int)
        cap = fh[r]
        for (d, rl, rp, f), w in states.items():
            for c in range(5):
                if c == 0:
                    d2 = d + (rl * rp if rl >= 3 else 0)
                    rl2, rp2, f2 = 0, 1, f
                else:
                    d2 = d + 2 * cc[c][2] - c * v if c >= 2 else d - c * v
                    ff = (1,) + f
                    add15 = 0
                    j = 1
                    while j <= c and j * v <= 15:
                        if 15 - j * v <= 14:
                            add15 += cc[c][j] * ff[15 - j * v]
                        j += 1
                    d2 += 2 * add15
                    nf = list(ff)
                    for s in range(14, 0, -1):
                        tot = ff[s]
                        j = 1
                        while j <= c and j * v <= s:
                            tot += cc[c][j] * ff[s - j * v]
                            j += 1
                        nf[s] = tot
                    f2 = tuple(nf[1:])
                    rl2, rp2 = rl + 1, rp * c
                min_run = rl2 * rp2 if rl2 >= 3 else 0
                if d2 + min_run > fh[r]:
                    continue
                f2 = tuple(x if 1 <= 15 - (s + 1) <= cap else 0
                           for s, x in enumerate(f2))
                new[(d2, rl2, rp2, f2)] += w * c4[c]
        states = dict(new)
    total = 0
    for (d, rl, rp, _f), w in states.items():
        if d + (rl * rp if rl >= 3 else 0) == 0:
            total += w
    return total - 1  # exclude the empty hand


def _brute(num_ranks: int) -> int:
    total = 0
    counts: dict[int, int] = {}

    def rec(r: int) -> None:
        nonlocal total
        if r > num_ranks:
            if any(counts.values()):
                h, c = score_counts(counts)
                if h == c:
                    w = 1
                    for x in counts.values():
                        w *= comb(4, x)
                    total += w
            return
        for c0 in range(5):
            counts[r] = c0
            rec(r + 1)
        counts[r] = 0

    rec(1)
    return total


if __name__ == "__main__":
    assert score_counts({5: 3, 13: 1}) == (25, 14)  # given crib 14
    assert score_counts({1: 2, 2: 1, 3: 1, 4: 1, 5: 1}) == (16, 16)  # given
    for nr in (3, 4, 5, 6):
        assert solve(nr) == _brute(nr), nr
    print(solve())  # 81108001093
