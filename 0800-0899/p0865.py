"""Project Euler 865: Triplicate Numbers.

A triplicate number is a positive integer whose decimal string can be
emptied by repeatedly deleting three consecutive identical digits.

Deleting identical triples is a terminating and locally confluent
rewriting system (overlapping redexes only occur inside runs of one
digit, where every choice leaves the same result), hence confluent.  A
string therefore reduces to the empty word iff it represents the
identity in the free product of ten copies of Z_3, one per digit.

Counting neutral words: an atom is a nonempty neutral word whose
prefix stack never empties internally.  An atom starting with digit c
factors uniquely as c A c B c where A and B are neutral words none of
whose atoms starts with c.  With q = 10 digits and I the generating
function of atoms with a fixed first digit, this gives
I = x^3 / (1 - (q-1) I)^2, and neutral words form N = 1/(1 - q I).
Eliminating I yields the algebraic equation
    N^3 (1 - 1000 x^3) + 17 N^2 + 63 N - 81 = 0,
whose coefficients (in t = x^3) follow a quadratic-time recurrence by
tracking the series A, A^2 and A^3 simultaneously.  By digit symmetry
exactly 9/10 of the neutral words of each positive length avoid a
leading zero, so T(10^4) is 9/10 of the sum of all coefficients with
3m <= 10^4.  The code reproduces the given T(6) = 261 and
T(30) = 5576195181577716 in exact arithmetic.

Answer: T(10^4) mod 998244353.
"""

from __future__ import annotations

MOD = 998244353


def neutral_series(terms: int, mod: int | None) -> list[int]:
    """Coefficients a_0..a_terms of A(t), the neutral-word GF in t = x^3."""
    a = [1] + [0] * terms
    sq = [1] + [0] * terms
    cube = [1] + [0] * terms
    inv100 = pow(100, mod - 2, mod) if mod else None
    for m in range(1, terms + 1):
        s_sq = 0
        s_mix = 0
        for i in range(1, m):
            s_sq += a[i] * a[m - i]
            s_mix += a[i] * sq[m - i]
        c_star = s_sq + s_mix
        num = 1000 * cube[m - 1] - c_star - 17 * s_sq
        if mod and inv100 is not None:
            value = num % mod * inv100 % mod
        else:
            assert num % 100 == 0
            value = num // 100
        a[m] = value
        sq[m] = 2 * value + s_sq
        cube[m] = 3 * value + c_star
        if mod:
            sq[m] %= mod
            cube[m] %= mod
    return a


def triplicate_count(n: int, mod: int | None = None) -> int:
    """Number of triplicate numbers below 10**n (optionally modulo mod)."""
    coeffs = neutral_series(n // 3, mod)
    total = sum(coeffs[1:])
    if mod:
        return 9 * total % mod * pow(10, mod - 2, mod) % mod
    return 9 * total // 10


def main() -> None:
    assert triplicate_count(6) == 261
    assert triplicate_count(30) == 5576195181577716
    print(triplicate_count(10**4, MOD))  # 761181918


if __name__ == "__main__":
    main()
