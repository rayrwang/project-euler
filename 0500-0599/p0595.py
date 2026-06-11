"""Project Euler problem 595: Incremental Random Sort.

A deck 1..n is uniformly shuffled.  Maximal runs of consecutive values
standing in correct adjacent order are glued into bundles; the bundles
are then rearranged uniformly at random, regluing happens, and so on
until one bundle remains.  S(n) is the expected number of shuffles;
S(2) = 1 and S(5) = 4213/871 are given.  Find S(52) to 8 decimals.

The only relevant state is the number of bundles k, because bundles are
value-intervals and a uniform rearrangement of k labelled bundles is a
uniform permutation of [k].  Gluing contracts each "succession" - a
position where item i is immediately followed by item i + 1 - so from
state k the chain moves to k - s, where the number of permutations of
[k] with exactly s successions is C(k-1, s) Q(k-s), with
Q(m) = sum_j (-1)^j C(m-1, j) (m-j)! the succession-free count (choose
which s of the k - 1 adjacent value pairs are glued and contract them).
Solving E_k = 1 + sum_s p_{k,s} E_{k-s} with the s = 0 self-loop moved
to the left side gives the expected shuffles from each state, and the
initial uniform deck lands on k bundles with probability
C(n-1, n-k) Q(k) / n!.  Everything is computed in exact rationals.

Verified: S(1) = 0, S(2) = 1, S(5) = 4213/871 exactly, plus direct
Monte Carlo simulation of the whole process for n = 4 and 6.
"""

import random
from fractions import Fraction
from math import comb, factorial


def q_no_succ(m: int) -> int:
    """Permutations of m items with no successions."""
    return sum((-1) ** j * comb(m - 1, j) * factorial(m - j) for j in range(m))


def s_exact(n: int) -> Fraction:
    e = [Fraction(0)] * (n + 1)
    for k in range(2, n + 1):
        kf = factorial(k)
        tot = Fraction(1)
        for s in range(1, k):
            tot += Fraction(comb(k - 1, s) * q_no_succ(k - s), kf) * e[k - s]
        e[k] = tot / (1 - Fraction(q_no_succ(k), kf))
    nf = factorial(n)
    return sum(
        (
            Fraction(comb(n - 1, n - k) * q_no_succ(k), nf) * e[k]
            for k in range(1, n + 1)
        ),
        start=Fraction(0),
    )


def monte_carlo(n: int, trials: int) -> float:
    rng = random.Random(595)
    tot = 0
    for _ in range(trials):
        cards = list(range(1, n + 1))
        rng.shuffle(cards)
        shuffles = 0
        while True:
            bundles: list[list[int]] = []
            for x in cards:
                if bundles and x == bundles[-1][-1] + 1:
                    bundles[-1].append(x)
                else:
                    bundles.append([x])
            if len(bundles) == 1:
                break
            shuffles += 1
            rng.shuffle(bundles)
            cards = [x for b in bundles for x in b]
        tot += shuffles
    return tot / trials


def main() -> None:
    assert s_exact(1) == 0
    assert s_exact(2) == 1  # given
    assert s_exact(5) == Fraction(4213, 871)  # given
    for n in (4, 6):
        assert abs(monte_carlo(n, 200_000) - float(s_exact(n))) < 0.05

    print(f"{float(s_exact(52)):.8f}")  # 54.17529329


if __name__ == "__main__":
    main()
