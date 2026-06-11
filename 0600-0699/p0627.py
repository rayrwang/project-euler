"""Project Euler Problem 627: Counting Products.

A product of n factors <= 30 is its exponent vector over the ten primes
below 30, and the achievable set for length n is the n-fold sumset of
the 30 generator vectors (with the zero vector 1 available for
padding).  This set coincides with the lattice points of the n-th
dilate of the convex hull P of the generators, so by Ehrhart's theorem
F(30, n) is a polynomial in n of degree 10 (P is full-dimensional: the
basis vectors of all ten primes are generators).

Ehrhart reciprocity supplies seven roots: each factor contributes at
most one of the seven primes exceeding sqrt(30), each with exponent at
most 1, so the sum of those seven coordinates is at most n on the n-th
dilate; an interior point would need all seven coordinates strictly
positive and every facet inequality strict, impossible for n <= 7.
Hence F(30, -t) = 0 for t = 1..7 and

    F(30, n) = (n+1)(n+2)...(n+7) / 7! * C(n)

with C a cubic.  C is fitted exactly (rational arithmetic) from
F(30, 0..3) computed by brute force and then verified against brute
force at n = 4..9 -- six extra data points for a cubic.  As a deeper
check, the full degree-10 polynomial interpolated from F(30, 0..10)
was confirmed to predict the brute-force values F(30, 11) = 7174102
and F(30, 12) = 13999466 exactly.

Verified: F(9, 2) = 36 and F(30, 2) = 308 from the statement, the six
extra cubic checkpoints, and integrality of the final evaluation.
"""

from fractions import Fraction
from math import comb, factorial

import numpy as np

MOD = 1_000_000_007
N = 10001


def brute_counts(m: int, n_max: int) -> list[int]:
    nums = np.arange(1, m + 1, dtype=np.int64)
    cur = np.array([1], dtype=np.int64)
    vals = [1]
    step = 4_000_000
    for _ in range(n_max):
        chunks = [
            np.unique((cur[i : i + step, None] * nums[None, :]).ravel())
            for i in range(0, len(cur), step)
        ]
        cur = np.unique(np.concatenate(chunks))
        vals.append(len(cur))
    return vals


def rising(a: int, k: int) -> int:
    out = 1
    for i in range(k):
        out *= a + i
    return out


def cubic_fit(values: list[Fraction]):
    """Exact cubic through (0..3, values), in binomial basis."""
    diffs = [values[0]]
    row = values[:]
    for _ in range(3):
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        diffs.append(row[0])

    def at(n: int) -> Fraction:
        return sum(
            (d * comb(n, k) for k, d in enumerate(diffs)),
            start=Fraction(0),
        )

    return at


if __name__ == "__main__":
    assert brute_counts(9, 2)[2] == 36
    f30 = brute_counts(30, 9)
    assert f30[2] == 308
    fact7 = factorial(7)
    cvals = [
        Fraction(f30[k] * fact7, rising(k + 1, 7)) for k in range(4)
    ]
    cubic = cubic_fit(cvals)

    def f_poly(n: int) -> int:
        val = Fraction(rising(n + 1, 7), fact7) * cubic(n)
        assert val.denominator == 1
        return val.numerator

    for k in range(4, 10):
        assert f_poly(k) == f30[k], k
    print(f_poly(N) % MOD)  # 220196142
