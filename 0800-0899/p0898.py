from fractions import Fraction
from itertools import product
from math import log

import numpy as np

# Claire guesses the maximum-likelihood outcome (uniform prior), so she is
# correct with probability sum_r max(P(r|H), P(r|T)) / 2.  Flipping every
# report swaps the two likelihoods, which turns this into
#     P(correct) = P_H(L > 1) + P_H(L = 1) / 2,
# where L = P(r|H) / P(r|T) is the likelihood ratio of the reports r drawn
# with the truth being heads.  A student with lying probability u/100 says
# heads with probability w/100 (w = 100 - u), contributing a factor w/u to
# L, and tails with probability u/100, contributing u/w.
#
# The class pairs up: students with lying probabilities u% and w% = (100-u)%
# contribute jointly (w/u)^2 with probability (w/100)^2, (u/w)^2 with
# probability (u/100)^2, and 1 otherwise; the 50% student never matters.
# A meet-in-the-middle over 13 + 12 pairs, done in exact integer arithmetic
# (each half value is a fraction n/d, each probability an integer over a
# power of 100), gives the exact rational answer.

BAND = 1e-9  # log window inside which comparisons are redone exactly


def brute_force(lying_percents: list[int]) -> Fraction:
    """P(correct) by enumerating every report vector exactly."""
    total = Fraction(0)
    for says_heads in product((False, True), repeat=len(lying_percents)):
        ph = pt = Fraction(1)
        for s, u in zip(says_heads, lying_percents):
            w = 100 - u
            ph *= Fraction(w if s else u, 100)  # truth heads
            pt *= Fraction(u if s else w, 100)  # truth tails
        total += max(ph, pt)
    return total / 2


def expand_half(pairs: list[tuple[int, int]]) -> list[tuple[int, int, int]]:
    """All (num, den, prob_numerator) over one half's pairs.

    The value of a combination is num/den and its probability is
    prob_numerator / 100^(2 * len(pairs)).
    """
    combos = [(1, 1, 1)]
    for u, w in pairs:
        nxt = []
        for n, d, p in combos:
            nxt.append((n * w, d * u, p * w * w))
            nxt.append((n, d, p * 2 * u * w))
            nxt.append((n * u, d * w, p * u * u))
        combos = nxt
    return combos


def p_correct(pairs: list[tuple[int, int]]) -> Fraction:
    """Exact P(correct) for a class made of (u, 100-u) pairs (plus a 50%)."""
    half_a = expand_half(pairs[: (len(pairs) + 1) // 2])
    half_b = expand_half(pairs[(len(pairs) + 1) // 2 :])

    half_b.sort(key=lambda t: log(t[0]) - log(t[1]))
    logs_b = np.array([log(n) - log(d) for n, d, _ in half_b])
    suffix = [0] * (len(half_b) + 1)  # exact suffix sums of probabilities
    for i in range(len(half_b) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + half_b[i][2]

    logs_a = np.array([log(n) - log(d) for n, d, _ in half_a])
    hi = np.searchsorted(logs_b, -logs_a + BAND, side="left")
    lo = np.searchsorted(logs_b, -logs_a - BAND, side="left")

    s_win = s_tie = 0
    for (na, da, pa), i_lo, i_hi in zip(half_a, lo.tolist(), hi.tolist()):
        s_win += pa * suffix[i_hi]
        for nb, db, pb in half_b[i_lo:i_hi]:  # resolve near-ties exactly
            left, right = na * nb, da * db
            if left > right:
                s_win += pa * pb
            elif left == right:
                s_tie += pa * pb
    denominator = 100 ** (2 * len(pairs))
    return Fraction(2 * s_win + s_tie, 2 * denominator)


if __name__ == "__main__":
    # Given example: lying probabilities 20%, 40%, 60%, 80% -> 0.832.
    example = brute_force([20, 40, 60, 80])
    assert example == Fraction(832, 1000)
    # The pairing machinery agrees with brute force (these are pairs too).
    assert p_correct([(20, 80), (40, 60)]) == example
    assert p_correct([(30, 70), (35, 65), (45, 55)]) == brute_force(
        [30, 35, 45, 50, 55, 65, 70]
    )

    answer = p_correct([(24 + j, 76 - j) for j in range(1, 26)])
    digits, rem = divmod(answer.numerator * 10**10, answer.denominator)
    if 2 * rem >= answer.denominator:
        digits += 1
    print(f"0.{digits:010d}")  # 0.9861343531
