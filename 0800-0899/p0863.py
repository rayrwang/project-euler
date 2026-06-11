"""Project Euler 863: Different Dice.

Emulate a fair n-sided die with a D5 and a D6, where the sequence of
dice to roll is fixed in advance and only the stopping rule may depend
on outcomes; R(n) is the minimal expected number of rolls.

For a fixed sequence with partial products D_k, the accumulated state
after k rolls is uniform over some m_k surviving outcomes.  A stopping
rule is fair iff every face has been assigned the same total
probability, and at level k at most n * floor(D_k / n) outcomes can
ever be resolved, so m_k >= D_k mod n; the greedy rule that peels off
the largest multiple of n at every step attains this bound for all k
simultaneously.  Hence the expected roll count of a sequence is
sum_k (D_k mod n) / D_k, by summing survival probabilities.

Minimising over sequences is a discounted Bellman problem whose state
is the residue r = D_k mod n: choosing die d costs (r d mod n)/(D d)
plus the future, giving W(r) = min_d (r d mod n + W(r d mod n)) / d
with W(0) = 0 and R(n) = 1 + W(1).  The minimum operator combined with
the 1/5 discount is a contraction, so value iteration converges
geometrically and sixty sweeps leave errors far below the required
six decimals.  The code reproduces the given R(8), R(28) and S(30).

Answer: S(1000) rounded to 6 decimal places.
"""

from __future__ import annotations

import numpy as np


def expected_rolls(n: int, sweeps: int = 60) -> float:
    """Minimal expected rolls R(n) via value iteration on residues."""
    res5 = (np.arange(n) * 5) % n
    res6 = (np.arange(n) * 6) % n
    w = np.zeros(n)
    for _ in range(sweeps):
        w = np.minimum((res5 + w[res5]) / 5.0, (res6 + w[res6]) / 6.0)
        w[0] = 0.0
    return 1.0 + w[1]


def cumulative(n: int) -> float:
    return sum(expected_rolls(k) for k in range(2, n + 1))


def main() -> None:
    assert abs(expected_rolls(8) - 2.083333) < 5e-7
    assert abs(expected_rolls(28) - 2.142476) < 5e-7
    assert abs(cumulative(30) - 56.054622) < 5e-6
    print(f"{cumulative(1000):.6f}")  # 3862.871397


if __name__ == "__main__":
    main()
