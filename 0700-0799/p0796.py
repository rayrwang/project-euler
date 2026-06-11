"""
Project Euler Problem 796: A Grand Shuffle
https://projecteuler.net/problem=796

Ten 54-card decks (52 standard cards plus two suitless, rankless Jokers),
each with a distinct back design, are shuffled together.  Cards are drawn
without replacement until every rank (13), suit (4) and design (10) has
appeared.  Find the expected number of draws, rounded to 8 decimal places.

With T the stopping time, E[T] = sum_{t>=0} P(T > t).  By inclusion-
exclusion over which sets of ranks R, suits S and designs D are still
missing after t draws,

  P(T > t) = sum_{(R,S,D) != empty} (-1)^(|R|+|S|+|D|+1) C(M, t) / C(N, t),

where N = 540 and M = M(r, s, d) counts the cards avoiding all chosen
categories: (13-r)(4-s)(10-d) ordinary cards plus 2(10-d) jokers (jokers
have no rank or suit, so only a missing design constrains them).  Summing
over t with the identity sum_{t>=0} C(M,t)/C(N,t) = (N+1)/(N+1-M) gives

  E[T] = sum (-1)^(r+s+d+1) C(13,r) C(4,s) C(10,d) (N+1)/(N+1-M(r,s,d)),

an exact rational with a few hundred terms.  The same formula for a single
deck and ranks only reproduces the stated 29.05361725.
"""

from fractions import Fraction
from math import comb


def expected(ranks, suits, designs, jokers_per_deck):
    n = (ranks * suits + jokers_per_deck) * designs
    total = Fraction(0)
    for r in range(ranks + 1):
        for s in range(suits + 1):
            for d in range(designs + 1):
                if r == 0 and s == 0 and d == 0:
                    continue
                m = (ranks - r) * (suits - s) * (designs - d)
                m += jokers_per_deck * (designs - d)
                sign = -1 if (r + s + d) % 2 == 0 else 1
                w = comb(ranks, r) * comb(suits, s) * comb(designs, d)
                total += sign * w * Fraction(n + 1, n + 1 - m)
    return total


def round_dec(x, places):
    scale = 10**places
    v = (x * scale * 2 + 1) // 2  # round half up, exact rational arithmetic
    return f"{v // scale}.{v % scale:0{places}d}"


def single_deck_ranks_only():
    """One 54-card deck, waiting for all 13 ranks (suits/designs trivial)."""
    n = 54
    total = Fraction(0)
    for r in range(1, 14):
        m = (13 - r) * 4 + 2
        sign = -1 if r % 2 == 0 else 1
        total += sign * comb(13, r) * Fraction(n + 1, n + 1 - m)
    return total


def main():
    assert round_dec(single_deck_ranks_only(), 8) == "29.05361725"
    return round_dec(expected(13, 4, 10, 2), 8)


if __name__ == "__main__":
    print(main())  # 43.20649061
