"""Project Euler 855: Delphi Paper.

Each round Alex splits the current rectangle into an a x b grid with
freely chosen (possibly degenerate) cut positions and Bianca picks a
grid cell, never reusing a cell index over the ab rounds; Bianca
minimises and Alex maximises the final area.

The round factor is u_i v_j where u and v are the row and column
fraction vectors, so the logarithm of the area splits into a row part
and a column part.  Consider the "quota game" on k options where
option i may be chosen q_i more times and Alex picks a simplex vector
each round: with c_i = W(q - e_i), Alex's optimal play equalises
u_i c_i over the active options, giving W(q) = 1 / sum_i 1/W(q - e_i).
Writing R = 1/W turns this into the lattice-path recurrence
R(q) = sum R(q - e_i) with R(0) = 1, hence R(q) is the multinomial
coefficient (sum q_i)! / prod q_i!.

The full game separates into the two quota games.  Alex's product
strategy guarantees the product of the two quota values, because any
cell sequence projects to legal row and column sequences.  Conversely,
when Alex equalises, every active option is an optimal reply in each
quota game, and every remaining cell has an active row and an active
column, so Bianca can realise both adversaries simultaneously by
taking any remaining cell.  Therefore

    S(a, b) = (b!)^a (a!)^b / ((ab)!)^2,

which reproduces the given S(2,2) = 1/36 and S(2,3) = 1/1800 exactly.
The answer S(5, 8) is evaluated in exact rational arithmetic and
rounded to ten significant digits after the decimal point.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def final_area(a: int, b: int) -> Fraction:
    return Fraction(factorial(b) ** a * factorial(a) ** b, factorial(a * b) ** 2)


def sci_notation(value: Fraction, digits: int) -> str:
    """value > 0 in scientific notation, `digits` digits after the point."""
    num, den = value.numerator, value.denominator
    exp = len(str(num)) - len(str(den))

    def at_least_pow(e: int) -> bool:
        return num >= den * 10**e if e >= 0 else num * 10**-e >= den

    while not at_least_pow(exp):
        exp -= 1
    while at_least_pow(exp + 1):
        exp += 1
    shift = digits - exp
    if shift >= 0:
        mant = (2 * num * 10**shift + den) // (2 * den)
    else:
        mant = (2 * num + den * 10**-shift) // (2 * den * 10**-shift)
    s = str(mant)
    if len(s) == digits + 2:  # rounding overflowed to the next power of ten
        exp += 1
        s = s[:-1]
    return f"{s[0]}.{s[1:]}e{exp}"


def main() -> None:
    assert final_area(2, 2) == Fraction(1, 36)
    assert final_area(2, 3) == Fraction(1, 1800)
    print(sci_notation(final_area(5, 8), 10))  # 6.8827571976e-57


if __name__ == "__main__":
    main()
