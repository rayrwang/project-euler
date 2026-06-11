"""Project Euler problem 573: Unfair Race.

Runner k of n has speed k/n; n starting distances are drawn uniformly on
[0, 1] and the sorted distances are assigned nearest-first, so runner k
starts at the k-th order statistic U_(k) and finishes in time
n U_(k) / k.  The winner minimises U_(k) / k.  With P_{n,k} the winning
probability of runner k and E_n = sum k P_{n,k}, find E_1000000.

Condition on U_(k) = u.  The k - 1 smaller positions are order statistics
of iid uniforms on (0, u) and the n - k larger ones of iid uniforms on
(u, 1), and the two sides are independent.  Runner k wins iff
U_(j) > (j / k) u on both sides.

Past: rescaling by u, we need W_(j) > j / k for k - 1 uniforms, which by
the ballot theorem (cycle lemma) equals 1/k, independent of u.

Future: rescaling (u, 1) to (0, 1), we need Y_(i) > c i for the n - k
uniforms with c = u / (k (1 - u)); Daniels' theorem gives the exact
linear-boundary survival probability (1 - c m)^+ for m uniforms.  Hence

  P_{n,k} = (1/k) Integral f_k(u) (1 - (n-k) u / (k (1-u)))^+ du

with f_k the Beta(k, n-k+1) density of U_(k).  Writing
f_k(u) u / (1 - u) as a multiple of the Beta(k+1, n-k) density turns
e_k = k P_{n,k} into a difference of regularized incomplete Beta values
at x = k/n, which by the order-statistic / binomial duality
I_x(a, n - a + 1) = P(Bin(n, x) >= a) collapses to a single binomial
point probability:

  e_k = P(Bin(n, k/n) = k),    E_n = sum_{k=1}^n C(n,k) (k/n)^k ((n-k)/n)^(n-k).

Sanity: E_3 = 4/9 + 4/9 + 1 = 17/9 reproduces the given P_{3,k}, and
E_n ~ sqrt(pi n / 2) by Stirling, matching the magnitude of the answer.
The sum is evaluated with lgamma; the exponent combines O(n log n)-sized
logarithms, so float64 keeps each term's relative error near 1e-10.

Verified: the given E_3, E_4, E_5, E_10 exactly via Fraction arithmetic,
lgamma agreement with the exact value at n = 10, and direct Monte Carlo
simulation of the race itself for n = 5 and 10.
"""

from fractions import Fraction
from math import comb, exp, lgamma, log

import numpy as np


def e_exact(n: int) -> Fraction:
    return sum(
        (
            Fraction(comb(n, k)) * Fraction(k, n) ** k * Fraction(n - k, n) ** (n - k)
            for k in range(1, n + 1)
        ),
        start=Fraction(0),
    )


def e_float(n: int) -> float:
    tot = 1.0  # the k = n term
    for k in range(1, n):
        ll = (
            lgamma(n + 1)
            - lgamma(k + 1)
            - lgamma(n - k + 1)
            + k * (log(k) - log(n))
            + (n - k) * (log(n - k) - log(n))
        )
        tot += exp(ll)
    return tot


def monte_carlo(n: int, trials: int) -> float:
    rng = np.random.default_rng(573)
    batch = 100_000
    tot = 0
    for _ in range(trials // batch):
        u = np.sort(rng.random((batch, n)), axis=1)
        t = u / (np.arange(1, n + 1) / n)
        tot += int((np.argmin(t, axis=1) + 1).sum())
    return tot / (trials // batch * batch)


def main() -> None:
    assert e_exact(3) == Fraction(17, 9)  # given (= sum k P_{3,k})
    assert float(e_exact(4)) == 2.21875  # given
    assert float(e_exact(5)) == 2.5104  # given
    assert abs(float(e_exact(10)) - 3.66021568) < 1e-9  # given
    assert abs(e_float(10) - float(e_exact(10))) < 1e-10
    for n in (5, 10):
        assert abs(monte_carlo(n, 2_000_000) - float(e_exact(n))) < 5e-3

    print(f"{e_float(1_000_000):.4f}")  # 1252.9809


if __name__ == "__main__":
    main()
