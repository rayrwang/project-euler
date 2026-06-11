"""Project Euler problem 527: Randomized Binary Search.

B(n) is the expected number of guesses to find a uniformly random target in
1..n with standard binary search (guess the floor midpoint); R(n) is the
same with a uniformly random guess in [L, H].  Find R(10^10) - B(10^10).

Standard search: with T(n) the total guess count summed over all n targets,
the midpoint splits an interval of size n into sizes floor((n-1)/2) and
ceil((n-1)/2), so T(n) = n + T(floor) + T(ceil), and only O(log^2 n)
distinct sizes arise, so the recursion memoizes instantly; B = T(n)/n is
exact as a rational.

Random search: picking a uniform pivot and recursing is exactly searching a
random binary search tree, whose successful-search cost has the classic
closed form R(n) = 2 (1 + 1/n) H_n - 3.  This is verified against the
direct expectation recurrence W(n) = n + (2/n) sum_{k<n} W(k) (with
W(n) = n R(n)) in exact rational arithmetic for all n <= 200.  For
n = 10^10 the harmonic number is evaluated with the Euler-Maclaurin
expansion H_n = ln n + gamma + 1/(2n) - 1/(12n^2) + 1/(120n^4), whose
truncation error is O(n^-6); the expansion is checked against an exact
summation at n = 10^6.

Also verified: the T-recursion against simulating the actual search loop
for every target for many n, and the given B(6) = 2.33333333 and
R(6) = 2.71666667.
"""

import math
import sys
from fractions import Fraction
from functools import lru_cache

sys.setrecursionlimit(10000)

GAMMA = 0.5772156649015328606


@lru_cache(maxsize=None)
def total_guesses(n: int) -> int:
    """Sum over all targets of the number of standard-binary-search guesses."""
    if n <= 0:
        return 0
    left = (n - 1) // 2
    return n + total_guesses(left) + total_guesses(n - 1 - left)


def b_brute(n: int) -> Fraction:
    tot = 0
    for t in range(1, n + 1):
        lo, hi, c = 1, n, 0
        while True:
            g = (lo + hi) // 2
            c += 1
            if g == t:
                break
            if g < t:
                lo = g + 1
            else:
                hi = g - 1
        tot += c
    return Fraction(tot, n)


def w_table(nmax: int) -> list[Fraction]:
    """W(n) = n * R(n) by the direct expectation recurrence."""
    w = [Fraction(0)] * (nmax + 1)
    pref = Fraction(0)
    for n in range(1, nmax + 1):
        w[n] = n + Fraction(2, n) * pref
        pref += w[n]
    return w


def h_asym(n: int) -> float:
    return math.log(n) + GAMMA + 1 / (2 * n) - 1 / (12 * n * n) + 1 / (120 * n**4)


def main() -> None:
    w = w_table(200)
    harmonic = Fraction(0)
    for n in range(1, 201):
        harmonic += Fraction(1, n)
        assert 2 * (1 + Fraction(1, n)) * harmonic - 3 == w[n] / n, n
    for n in list(range(1, 60)) + [997, 1000]:
        assert b_brute(n) == Fraction(total_guesses(n), n), n
    assert f"{float(Fraction(total_guesses(6), 6)):.8f}" == "2.33333333"
    assert f"{float(w[6] / 6):.8f}" == "2.71666667"
    exact = math.fsum(1 / k for k in range(1, 10**6 + 1))
    assert abs(h_asym(10**6) - exact) < 1e-12

    n = 10**10
    r = 2 * (1 + 1 / n) * h_asym(n) - 3
    b = total_guesses(n) / n
    print(f"{r - b:.8f}")  # 11.92412011


if __name__ == "__main__":
    main()
