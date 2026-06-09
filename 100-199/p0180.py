from fractions import Fraction
from math import isqrt


def _rational_sqrt(value: Fraction) -> Fraction | None:
    n, d = value.numerator, value.denominator
    sn, sd = isqrt(n), isqrt(d)
    if sn * sn == n and sd * sd == d:
        return Fraction(sn, sd)
    return None


def solve(order: int = 35) -> int:
    # f_n(x,y,z) = (x+y+z)(x^n + y^n - z^n); by Fermat only n in {-2,-1,1,2}
    # give rational zeros, so z is x+y, sqrt(x^2+y^2), xy/(x+y) or xy/sqrt(...).
    # Sum the distinct x+y+z over golden triples of order 35 in lowest terms.
    rationals = {Fraction(a, b) for b in range(2, order + 1) for a in range(1, b)}
    sums: set[Fraction] = set()
    for x in rationals:
        for y in rationals:
            root = _rational_sqrt(x * x + y * y)
            candidates = [x + y, (x * y) / (x + y)]
            if root is not None:
                candidates += [root, (x * y) / root]
            for z in candidates:
                if z in rationals:
                    sums.add(x + y + z)
    total = sum(sums, Fraction(0))
    return total.numerator + total.denominator


if __name__ == "__main__":
    print(solve())  # 285196020571078987
