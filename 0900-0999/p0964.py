"""Project Euler 964: Musical Chairs Revisited.

Round i applies a random permutation sigma_i: a uniform i-subset of the
n = k(k-1)/2 + 1 children is permuted uniformly. Each sigma_i is
conjugation-invariant, so Fourier analysis on S_n applies: with eigenvalues
E_i(lambda) = E[chi_lambda(sigma_i)] / d_lambda,

    P(k) = Pr[product = rho] = (1/n!) sum_lambda d_lambda chi_lambda(rho)
                                      prod_i E_i(lambda),

where rho is the one-step rotation, an n-cycle. Since chi_lambda(n-cycle) is
nonzero only for hook shapes lambda = (n-r, 1^r), where it equals (-1)^r and
d_lambda = C(n-1, r), only n terms survive. By the Pieri/branching rule,
E[chi_lambda(sigma_i)] = sum of d_nu over nu with lambda/nu a horizontal
i-strip; for a hook the only strips give nu = (n-i-r, 1^r) and
(n-i-r+1, 1^(r-1)), so the sum is C(n-i-1, r) + C(n-i-1, r-1) = C(n-i, r).
Hence E_i(hook_r) = C(n-i, r) / C(n-1, r) and

    P(k) = (1/n!) sum_{r=0}^{n-1} (-1)^r [prod_{i=1}^k C(n-i, r)]
                                     / C(n-1, r)^(k-1).

Verified exactly against full convolution over permutation distributions for
k = 2 (P = 1/2) and k = 3 (P = 1/72, matching the given 1.3888888889e-2).
P(7) comes out to exactly 1/21219647838989618324275200000.
"""

import decimal
from fractions import Fraction
from math import comb, factorial


def solve(k: int) -> str:
    n = k * (k - 1) // 2 + 1
    total = Fraction(0)
    for r in range(n):
        num = 1
        for i in range(1, k + 1):
            num *= comb(n - i, r)
        total += Fraction((-1) ** r * num, comb(n - 1, r) ** (k - 1))
    total /= factorial(n)
    decimal.getcontext().prec = 50
    d = decimal.Decimal(total.numerator) / decimal.Decimal(total.denominator)
    return f"{d:.10e}"


if __name__ == "__main__":
    print(solve(7))  # 4.7126135532e-29
