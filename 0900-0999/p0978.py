"""Project Euler 978: Random Walk Skewness.

Since the jump sign is a fresh fair coin, +-|X_{t-2}| has the same
conditional distribution as +-X_{t-2}, so the process is equal in law to the
random Fibonacci recurrence X_t = X_{t-1} + s_t X_{t-2} with s_t iid +-1
(the "stay put when X_{t-2} = 0" rule is the same thing, since +-0 = 0).

Joint moments close under this recurrence: averaging over s_t,

    E[X_t^a X_{t-1}^b] = sum_{j even} C(a, j) E[X_{t-1}^{a+b-j} X_{t-2}^j],

so tracking all E[X_t^a X_{t-1}^b] with a + b <= 3 as exact rationals gives
the first three moments at any t in O(t) steps. Skewness follows from
mu, var = E[X^2] - mu^2 and E[(X - mu)^3] = m3 - 3 mu m2 + 2 mu^3; to keep
full precision with the huge integers involved, the final value is computed
as sqrt of the exact rational (E[(X-mu)^3])^2 / var^3.

Verified against the exact distribution of the original |X_{t-2}| dynamics
for t <= 12 (matching the given X_5 table, Skew(X_5) = 0.75 and
Skew(X_10) = 2.50997097).
"""

from fractions import Fraction
from math import comb, sqrt


def moments(t_max: int) -> tuple[Fraction, Fraction, Fraction]:
    m = {(a, b): Fraction(1 if b == 0 else 0) for a in range(4) for b in range(4 - a)}
    for _ in range(2, t_max + 1):
        m = {
            (a, b): sum(
                (comb(a, j) * m[(a + b - j, j)] for j in range(0, a + 1, 2)),
                Fraction(0),
            )
            for a in range(4)
            for b in range(4 - a)
        }
    return m[(1, 0)], m[(2, 0)], m[(3, 0)]


def solve(t: int) -> str:
    m1, m2, m3 = moments(t)
    var = m2 - m1 * m1
    third = m3 - 3 * m1 * m2 + 2 * m1**3
    val = sqrt(float(third * third / var**3))
    if third < 0:
        val = -val
    return f"{val:.8f}"


if __name__ == "__main__":
    print(solve(50))  # 254.54470757
