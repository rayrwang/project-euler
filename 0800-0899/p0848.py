"""Project Euler 848: Guessing with Sets.

Each turn the mover queries a subset of the opponent's candidate
secrets and wins on a correct singleton.  If the mover draws the
queried k-subset uniformly at random, symmetry forces the answer to
be "yes" with probability exactly k/a regardless of how the opponent
chose their secret, so the value V(a, b) for the player about to move
- facing a candidates while their own secret hides among b - obeys

    V(a, b) = max_k [ (k/a) Y_k + ((a-k)/a)(1 - V(b, a-k)) ],

with Y_1 = 1 and Y_k = 1 - V(b, k) for k >= 2, and V(1, *) = 1.  This
reproduces the given p(1, n) = 1, p(m, 1) = 1/m and p(7, 5) = 18/35.

Computing the exact table reveals rigid structure.  The product
P = a b V(a, b) satisfies V(2a, 2b) = V(a, b) exactly, and splits into
just two regions separated by T(a), the unique number 3 * 2^t in
(a/2, a]: for b < T(a) the value is P = g(b) with no a-dependence at
all, while for b >= T(a) it is P = a b - g(a)/2.  Here g is the
piecewise-linear dyadic function with g(2 * 2^m) = 3 * 4^m and
g(3 * 2^m) = 6 * 4^m, except g(1) = 1.  The only stragglers are the
tiny arguments a = 1, b = 1 and a = 2, none of which matter for
powers of 7 and 5 beyond the explicitly handled cases i = 0 or j = 0.
The closed form is verified below against the exact game recursion on
all 3 <= a, b <= 60 (and was checked against a floating-point table up
to 320), after which the requested double sum is evaluated in exact
rational arithmetic and rounded to eight decimals.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from functools import lru_cache


@lru_cache(maxsize=None)
def value(a: int, b: int) -> Fraction:
    """Exact game value by direct recursion (small arguments only)."""
    if a == 1:
        return Fraction(1)
    best = Fraction(0)
    for k in range(1, a):
        yes = Fraction(1) if k == 1 else 1 - value(b, k)
        v = Fraction(k, a) * yes + Fraction(a - k, a) * (1 - value(b, a - k))
        if v > best:
            best = v
    return best


def g(b: int) -> int:
    if b == 1:
        return 1
    m = b.bit_length() - 2  # 2 * 2^m <= b < 4 * 2^m
    if b <= 3 * (1 << m):
        return 3 * 4**m + (b - 2 * (1 << m)) * 3 * 2**m
    return 6 * 4**m + (b - 3 * (1 << m)) * 6 * 2**m


def threshold(a: int) -> tuple[int, int]:
    """T(a) = the unique 3 * 2^t in (a/2, a], as (numerator, denominator)."""
    t = -2
    while 3 * 2 ** (t + 2) <= 2 * a:
        t += 1
    return (3 * 2**t, 1) if t >= 0 else (3, 2)


def win_probability(a: int, b: int) -> Fraction:
    """Closed form for p(a, b); valid for a not in {2} (handled cases aside)."""
    if a == 1:
        return Fraction(1)
    if b == 1:
        return Fraction(1, a)
    num, den = threshold(a)
    if b * den < num:
        return Fraction(g(b), a * b)
    return 1 - Fraction(g(a), 2 * a * b)


def main() -> None:
    sys.setrecursionlimit(100000)
    assert value(7, 5) == Fraction(18, 35)
    assert value(5, 1) == Fraction(1, 5)
    for a in range(3, 61):
        for b in range(2, 61):
            assert win_probability(a, b) == value(a, b), (a, b)
    total = sum(win_probability(7**i, 5**j) for i in range(21) for j in range(21))
    scaled = total * 10**8
    r = (scaled.numerator * 2 + scaled.denominator) // (2 * scaled.denominator)
    print(f"{r // 10**8}.{r % 10**8:08d}")  # 188.45503259


if __name__ == "__main__":
    main()
