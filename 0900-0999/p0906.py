"""Project Euler 906: A Collective Decision.

The chosen option is exactly a Condorcet winner over the three random
preference orders, and a Condorcet winner is unique (two winners would
each need a strict majority against the other), so
P(n) = n * Pr(option 1 wins).

Condition on the number r_v of options that voter v prefers over option
1; r_v is uniform on {0, ..., n-1}, and given r_v the set S_v of those
options is a uniform r_v-subset of the other m = n - 1 options.  Option
1 wins iff every other option is preferred over it by at most one voter,
i.e. iff S_1, S_2, S_3 are pairwise disjoint.  Counting ordered disjoint
triples gives

    Pr(win) = (1/n^3) sum_{r1+r2+r3 <= m}
              [C(m - r1, r2) / C(m, r2)] [C(m - r1 - r2, r3) / C(m, r3)].

The inner sum collapses by the identity
sum_{k <= b} C(b, k)/C(m, k) = (m + 1)/(m + 1 - b), leaving (with
a = m - r1)

    P(n) = (1/n) sum_{a=0}^{m} sum_{r=0}^{a}
           [C(a, r) / C(m, r)] / (m - a + r + 1),

an O(n^2) double sum in which the binomial ratio follows the one-step
recurrence ratio *= (a - r + 1)/(m - r + 1).  Kahan compensation keeps
the 4 * 10^8-term float sum far below the required 10-decimal accuracy
(the 11th decimal of the result is a 0, so rounding is not borderline).
Verified against the given P(3) = 17/18 and P(10).
"""

import numba


@numba.njit(cache=True)
def solve(n: int) -> float:
    m = n - 1
    total = 0.0
    c_outer = 0.0
    for a in range(m + 1):
        ratio = 1.0
        s = 1.0 / (m - a + 1)  # r = 0 term
        c = 0.0
        for r in range(1, a + 1):
            ratio *= (a - r + 1) / (m - r + 1)
            y = ratio / (m - a + r + 1) - c
            t = s + y
            c = (t - s) - y
            s = t
        y = s - c_outer
        t = total + y
        c_outer = (t - total) - y
        total = t
    return total / n


if __name__ == "__main__":
    assert abs(solve(3) - 17 / 18) < 1e-14
    assert abs(solve(10) - 0.6760292265) < 5e-11
    print(f"{solve(20000):.10f}")  # 0.0195868911
