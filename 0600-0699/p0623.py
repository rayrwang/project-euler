"""Project Euler Problem 623: Lambda Count.

Counting symbols (parentheses, lambda, dot, variables), the sizes are

    |x| = 1,    |(M N)| = |M| + |N| + 2,    |(lambda x. M)| = |M| + 5,

confirmed by Lambda(6) = 1 = #{(lambda x.x)}.  Alpha-equivalence classes are
counted by the de-Bruijn-style DP T(s, m) = number of terms of size s whose
free variables come from m available binders:

    T(s, m) = m [s = 1]                              (variable)
            + T(s - 5, m + 1)                        (abstraction)
            + sum_{a} T(a, m) T(s - 2 - a, m).       (application)

Each extra binder costs 5 symbols, so only states with 5 m + s <= n matter
and the table is computed for m = n/5 down to 0; the application convolution
makes the whole DP about sum_m (n - 5m)^2 / 2 = n^3 / 30 modular products,
fine for n = 2000 under numba.  The answer is sum_s T(s, 0) mod 10^9 + 7.

Checks: Lambda(6) = 1, Lambda(9) = 2, Lambda(15) = 20, Lambda(35) = 3166438.
"""

import numba
import numpy as np

MOD = 10**9 + 7


@numba.jit(cache=True)
def closed_term_counts(n: int) -> np.ndarray:
    """T(s, 0) for s = 0..n."""
    m_max = (n - 1) // 5
    T = np.zeros((m_max + 2, n + 1), dtype=np.int64)
    for m in range(m_max, -1, -1):
        s_max = n - 5 * m
        if s_max >= 1:
            T[m, 1] = m
        for s in range(2, s_max + 1):
            total = T[m + 1, s - 5] if s >= 5 else 0
            for a in range(1, s - 2):  # |M| = a, |N| = s - 2 - a >= 1
                total += T[m, a] * T[m, s - 2 - a] % MOD
            T[m, s] = total % MOD
    return T[0]


def Lambda(n: int, t0: np.ndarray) -> int:
    return int(np.sum(t0[: n + 1]) % MOD)


if __name__ == "__main__":
    t0 = closed_term_counts(2000)
    assert Lambda(6, t0) == 1, Lambda(6, t0)
    assert Lambda(9, t0) == 2
    assert Lambda(15, t0) == 20
    assert Lambda(35, t0) == 3166438
    print(Lambda(2000, t0))  # 3679796
