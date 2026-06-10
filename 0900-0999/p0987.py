"""Project Euler Problem 987: Straight Eight.

A straight is five cards of sequential rank, not all of one suit, with the
ace ranking low (A-2-3-4-5) or high (10-J-Q-K-A) but never wrapping.  There
are 10200 straights and 31832952 ways to choose two disjoint straights from
one 52-card deck.  Count the ways to choose *eight* pairwise-disjoint
straights (unordered).

Setup
-----
A straight is a rank window ``w in 1..10`` (window ``w`` covering rank
positions ``w .. w+4``, where positions 1 and 14 are the *same* four
physical aces) plus a suit for each of its five ranks.  Disjointness means
every (rank, suit) card is used at most once; per rank at most four
straights can overlap, in distinct suits.

Inclusion-exclusion on flushes
------------------------------
Dropping the "not all one suit" rule makes counting easy, because then a
straight's suits are chosen *independently per rank position*.  By
inclusion-exclusion over a designated subset of flush straights,

    answer = sum_j (-1)^j  sum_{flush sets of size j}  P(8 - j; free suits),

where ``P(k; .)`` counts unordered sets of ``k`` disjoint *generalised*
straights (arbitrary suit tuples) in the deck minus the flush cards.

* Flush sets: a flush is (window, suit); flushes in windows within distance
  4 -- or in windows 1 and 10, which share the aces -- overlap and need
  distinct suits.  A depth-first enumeration over per-window suit subsets
  (any five consecutive windows hold at most 4 flushes in total) lists all
  configurations; only the per-window *counts* matter downstream, since the
  generalised count depends just on how many free suits remain per rank.

* Generalised packings: scan rank positions 2..13; the state is the
  expiry profile of active straights.  At each position the active
  straights take an ordered injection into the free suits
  (``perm(free, active)``), with ``1/s!`` per group of ``s`` straights
  starting together to count unordered sets (exact via fractions).  The
  shared aces are handled by conditioning on how many straights use window
  1 and window 10 and charging one joint injection ``perm(free_ace, g1 +
  g10)`` for the ace column.

The same routine reproduces both given values (10200 for one straight,
31832952 for two), and the full computation takes a few seconds.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import factorial, perm


def _gen_count(k: int, caps: dict[int, int], cap_ace: int) -> Fraction:
    """Unordered sets of k disjoint generalised straights.

    ``caps[p]`` is the number of free suits at rank position ``p`` (2..13);
    ``cap_ace`` is the shared free-suit count of the ace column."""
    total = Fraction(0)
    for g1 in range(5):
        for g10 in range(5):
            if g1 + g10 > cap_ace or g1 + g10 > k:
                continue
            ace_factor = perm(cap_ace, g1 + g10)
            # state entering position p: (expiry profile a[0..3], #started);
            # a[i] straights stop covering after position p + i.
            cur: dict[tuple[tuple[int, int, int, int], int], Fraction] = defaultdict(
                Fraction
            )
            cur[((0, 0, 0, g1), g1)] = Fraction(1, factorial(g1))
            for p in range(2, 14):
                nxt: dict[tuple[tuple[int, int, int, int], int], Fraction] = (
                    defaultdict(Fraction)
                )
                capp = caps[p]
                for (act, started), val in cur.items():
                    if 2 <= p <= 9:
                        s_choices = range(k - started + 1)
                    elif p == 10:
                        s_choices = (g10,)
                    else:
                        s_choices = (0,)
                    for s in s_choices:
                        if started + s > k:
                            continue
                        active = act[0] + act[1] + act[2] + act[3] + s
                        if active > capp:
                            continue
                        f = (
                            Fraction(perm(capp, active), factorial(s))
                            if s
                            else Fraction(perm(capp, active))
                        )
                        nxt[((act[1], act[2], act[3], s), started + s)] += val * f
                cur = nxt
            for (act, started), val in cur.items():
                if started == k and act == (g10, 0, 0, 0):
                    total += val * ace_factor
    return total


def _flush_configs() -> dict[tuple[int, ...], int]:
    """Count suit-set assignments per per-window flush-count vector.

    Windows within distance 4 (and the ace-sharing pair {1, 10}) must use
    disjoint suit sets."""
    results: dict[tuple[int, ...], int] = defaultdict(int)

    def rec(w: int, last4: list[int], s1: int, m: list[int]) -> None:
        if w == 11:
            results[tuple(m)] += 1
            return
        used = last4[0] | last4[1] | last4[2] | last4[3]
        if w == 10:
            used |= s1
        for mask in range(16):
            if mask & used:
                continue
            m.append(mask.bit_count())
            rec(w + 1, last4[1:] + [mask], s1 if w > 1 else mask, m)
            m.pop()

    rec(1, [0, 0, 0, 0], 0, [])
    return dict(results)


def straights(k: int) -> int:
    """Number of unordered sets of k pairwise-disjoint straights."""
    answer = Fraction(0)
    for m, weight in _flush_configs().items():
        j = sum(m)
        if j > k:
            continue
        caps = {
            p: 4 - sum(m[wi - 1] for wi in range(max(1, p - 4), min(10, p) + 1))
            for p in range(2, 14)
        }
        cap_ace = 4 - m[0] - m[9]
        if cap_ace < 0 or min(caps.values()) < 0:
            continue
        answer += (-1) ** j * weight * _gen_count(k - j, caps, cap_ace)
    assert answer.denominator == 1
    return int(answer)


if __name__ == "__main__":
    assert straights(1) == 10200, "checkpoint: one straight"
    assert straights(2) == 31832952, "checkpoint: two disjoint straights"
    print(straights(8))  # 11044580082199135512
