"""Project Euler 852: Coins in a Box.

A box holds N fair coins (heads 1/2) and N unfair coins (heads 3/4).
Each round a uniformly random coin is drawn; the player may toss it
repeatedly at a cost of 1 per toss, then guesses its type for +20 or
-50, after which the true type is revealed and the coin discarded.

Because the type is revealed every round regardless of play, the box
composition (f, u) evolves as a pure random discard process that the
player cannot influence: from (f, u) the next state is (f-1, u) with
probability f/(f+u).  The total expected score therefore decomposes as
sum over compositions of P(visit (f, u)) * V(f / (f + u)), where V(p)
is the optimal value of a single round with prior p of being fair and
the visit probabilities follow a Pascal-style recursion from (N, N).

The single round is an optimal stopping problem on the posterior:
a head multiplies the fair:unfair odds by (1/2)/(3/4) = 2/3 and a
tail by (1/2)/(1/4) = 2, so after h heads in d tosses the posterior is
determined by (h, d).  Backward induction from a depth T at which the
player is forced to guess gives V; tossing can never profitably exceed
the 70-point swing between a right and a wrong guess, so T = 200 is
far beyond the continue region, and the result is unchanged between
T = 160 and T = 220.  Compositions with f = 0 or u = 0 are known coins
worth a guaranteed +20.  The code reproduces the given S(1) =
20.558591 and computes S(50) in a few seconds.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np

LOG2 = float(np.log(2.0))
LOG3 = float(np.log(3.0))


def single_round_value(odds_fair: float, depth: int = 200) -> float:
    """Optimal expected round score given prior odds fair:unfair."""

    def layer(d: int) -> tuple[np.ndarray, np.ndarray]:
        h = np.arange(d + 1, dtype=np.float64)
        unfair_over_fair = np.exp(h * LOG3 - d * LOG2) / odds_fair
        q = 1.0 / (1.0 + unfair_over_fair)
        return q, np.maximum(70.0 * q - 50.0, 20.0 - 70.0 * q)

    _, values = layer(depth)
    for d in range(depth - 1, -1, -1):
        q, guess = layer(d)
        p_heads = 0.5 * q + 0.75 * (1.0 - q)
        cont = -1.0 + p_heads * values[1 : d + 2] + (1.0 - p_heads) * values[: d + 1]
        values = np.maximum(guess, cont)
    return float(values[0])


def expected_score(n: int) -> float:
    cache: dict[Fraction, float] = {}

    def round_value(f: int, u: int) -> float:
        if f == 0 or u == 0:
            return 20.0
        key = Fraction(f, u)
        if key not in cache:
            cache[key] = single_round_value(f / u)
        return cache[key]

    visit = np.zeros((n + 1, n + 1))
    visit[n][n] = 1.0
    total = 0.0
    for s in range(2 * n, 0, -1):
        for f in range(max(0, s - n), min(n, s) + 1):
            u = s - f
            p = visit[f][u]
            if p == 0.0:
                continue
            total += p * round_value(f, u)
            if f > 0:
                visit[f - 1][u] += p * f / s
            if u > 0:
                visit[f][u - 1] += p * u / s
    return total


def main() -> None:
    assert abs(expected_score(1) - 20.558591) < 5e-7
    print(f"{expected_score(50):.6f}")  # 130.313496


if __name__ == "__main__":
    main()
