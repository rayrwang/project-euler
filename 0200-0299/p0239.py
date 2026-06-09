from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb, factorial


def solve() -> str:
    # 25 of the 100 disks are prime-numbered. Exactly 22 primes away from
    # their natural positions means exactly 3 primes fixed: choose them in
    # C(25, 3) ways, then count permutations of the other 97 disks in which
    # none of the remaining 22 prime disks sits in its own position (the 75
    # non-prime disks are unrestricted). By inclusion-exclusion over which of
    # those 22 are fixed, that count is sum_j (-1)^j C(22, j) (97 - j)!.
    favourable = comb(25, 3) * sum(
        (-1) ** j * comb(22, j) * factorial(97 - j) for j in range(23)
    )
    prob = Fraction(favourable, factorial(100))
    getcontext().prec = 40
    dec = Decimal(prob.numerator) / Decimal(prob.denominator)
    return str(dec.quantize(Decimal("1.000000000000")))


if __name__ == "__main__":
    print(solve())  # 0.001887854841
