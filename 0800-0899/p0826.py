from fractions import Fraction

from sympy import primerange


def painted_expectation(n: int) -> Fraction:
    """F(n): expected painted wire length for n birds, each painting to its nearest neighbour.

    Order the birds; the wire splits into n + 1 spacings (two to the posts, n - 1
    between consecutive birds), jointly a symmetric Dirichlet(1, ..., 1) on the
    simplex, so each spacing has mean 1 / (n + 1). Only the n - 1 internal gaps
    can be painted (posts are not birds).

    The two outer internal gaps are always painted: the leftmost bird's only
    neighbour is to its right and the rightmost bird's only neighbour is to its
    left. Each contributes its mean 1 / (n + 1).

    An interior gap g (with internal neighbours on both sides, lengths x and z)
    is painted unless g is the largest of the three, i.e. unless neither adjacent
    bird prefers it. Its painted contribution is E[g] - E[g . 1(g >= x, g >= z)].
    Writing W = x + g + z ~ Beta(3, n - 2) independent of the normalised triple
    (uniform on the 2-simplex), E[g . 1(g max)] = E[W] . E[g-hat . 1(g-hat max)]
    = (3 / (n + 1)) . (11 / 18) / 3 = 11 / (18 (n + 1)), using E[max of three
    uniform-simplex parts] = 11 / 18. Hence the contribution is
    1 / (n + 1) - 11 / (18 (n + 1)) = 7 / (18 (n + 1)).

    Summing the two outer gaps and the n - 3 interior gaps:
        F(n) = 2 / (n + 1) + (n - 3) . 7 / (18 (n + 1)) = (7 n + 15) / (18 (n + 1)).
    Matches F(3) = 1/2 and Monte-Carlo values for n up to 7.
    """
    return Fraction(7 * n + 15, 18 * (n + 1))


def average_over_odd_primes(limit: int) -> Fraction:
    primes = list(primerange(3, limit))
    total = sum((painted_expectation(p) for p in primes), Fraction(0))
    return total / len(primes)


if __name__ == "__main__":
    assert painted_expectation(3) == Fraction(1, 2)
    avg = average_over_odd_primes(10**6)
    scaled = avg.numerator * 10**11 // avg.denominator
    print(f"0.{(scaled + 5) // 10:010d}")  # 0.3889014797
