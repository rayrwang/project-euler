from decimal import Decimal, getcontext
from fractions import Fraction

def expected_empty_fraction(n: int, line: list[Fraction]) -> Fraction:
    """E(N) for the ring: the first knight (placed uniformly) occupies one chair
    and forbids its two neighbours, leaving a line of N-3 free chairs. So the
    expected number occupied is M = 1 + g(N-3), and the empty fraction is
    (N - M)/N, where g is the line version below."""
    occupied = 1 + (line[n - 3] if n - 3 >= 0 else Fraction(0))
    return (Fraction(n) - occupied) / n

def line_occupancy(limit: int) -> list[Fraction]:
    """g(m) = expected number of occupied chairs in a row of m chairs under the
    same random non-adjacent seating. Splitting on the first knight's seat gives
    g(m) = 1 + (2/m) * sum_{j=0}^{m-2} g(j)."""
    g = [Fraction(0)] * (limit + 1)
    prefix = [Fraction(0)] * (limit + 1)
    for m in range(1, limit + 1):
        s = prefix[m - 2] if m - 2 >= 0 else Fraction(0)
        g[m] = 1 + 2 * s / m
        prefix[m] = prefix[m - 1] + g[m]
    return g

if __name__ == "__main__":
    g = line_occupancy(20)
    assert expected_empty_fraction(4, g) == Fraction(1, 2)
    assert expected_empty_fraction(6, g) == Fraction(5, 9)

    # The occupied density converges to (1 - e^-2)/2 with a correction that decays
    # faster than any power (already matching to 16+ digits by N=100), so for
    # N = 10^18 the empty fraction equals (1 + e^-2)/2 well beyond 14 places.
    getcontext().prec = 60
    value = (1 + Decimal(-2).exp()) / 2
    print(value.quantize(Decimal("1." + "0" * 14)))  # 0.56766764161831
