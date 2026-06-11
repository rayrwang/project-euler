from fractions import Fraction
from itertools import permutations
from math import gcd

# With time t in twelve-hour turns, the hands sit at angles t, 12t, 720t
# (mod 1).  The moment is ambiguous iff some rotation r and assignment of
# the three identical hands turn the picture into another valid time t',
# i.e. t' = pt + r, 12t' = qt + r, 720t' = wt + r (mod 1) with (p, q, w) a
# permutation of (1, 12, 720) and t' != t.  Subtracting eliminates r:
#     11 t' = (q - p) t  and  708 t' = (w - q) t  (mod 1),
# and eliminating t' shows K t must be an integer for K = 708(q-p) - 11(w-q),
# so each non-identity permutation contributes the t = k/|K|.  For every
# such t exactly one residue a in t' = ((q-p)t + a)/11 satisfies the second
# congruence, because 708 is invertible mod 11; the identity permutation
# only ever returns t' = t.  The answer is the size of the union of the six
# solution sets as exact fractions, dropping the self-readings t' = t.


def ambiguous_moments() -> set[tuple[int, int]]:
    sols: set[tuple[int, int]] = set()
    inv708 = pow(708 % 11, -1, 11)
    for p, q, w in permutations((1, 12, 720)):
        alpha, beta = q - p, w - q
        big_k = 708 * alpha - 11 * beta
        if big_k == 0:
            continue
        d = abs(big_k)
        sgn = 1 if big_k > 0 else -1
        for k in range(d):
            a = (-sgn * k) * inv708 % 11
            # t' equals t exactly when (alpha - 11) k + a d ≡ 0 (mod 11 d)
            if ((alpha - 11) * k + a * d) % (11 * d) == 0:
                continue
            g = gcd(k, d)
            sols.add((k // g, d // g))
    return sols


def reads_as(t: Fraction, p: int, q: int, w: int) -> list[Fraction]:
    """All times t' whose hour/minute/second hands lie at pt+r, qt+r, wt+r."""
    out = []
    for a in range(11):
        tp = ((q - p) * t + a) / 11  # 11 t' = (q - p) t  (mod 1)
        if (708 * tp - (w - q) * t) % 1 == 0:  # 708 t' = (w - q) t  (mod 1)
            out.append(tp % 1)  # rotation r = t' - p t works for all hands
    return out


if __name__ == "__main__":
    sols = ambiguous_moments()

    # given examples: 1:30:00 and 7:30:00 ambiguous, 3:00:00 / 9:00:00 not,
    # and the triple coincidence 12:00:00 is uniquely readable
    assert (1, 8) in sols and (5, 8) in sols
    assert (1, 4) not in sols and (3, 4) not in sols and (0, 1) not in sols

    # independently verify a sample: each claimed moment really has a second
    # reading, checked with exact fractions against all hand assignments
    sample = sorted(sols)[:: len(sols) // 997]
    for num, den in sample:
        t = Fraction(num, den)
        others = [
            tp
            for p, q, w in permutations((1, 12, 720))
            for tp in reads_as(t, p, q, w)
            if tp != t
        ]
        assert others

    print(len(sols))  # 1541414
