"""Project Euler 840: Sum of Products.

D is the arithmetic derivative — D(p) = 1 on primes with the Leibniz
rule D(pq) = D(p) q + p D(q) — except the problem sets D(1) = 1, which
conveniently makes parts equal to one act as neutral factors.  The
table of D up to N follows from a smallest-prime-factor sieve via
D(p m) = m + p D(m).

A partition's value multiplies D over its parts, so the generating
function of G is the weighted partition product
sum_n G(n) x^n = prod_{a >= 1} (1 - D(a) x^a)^{-1}.  Multiplying the
series by one factor at a time is the classic in-place forward
recurrence dp[i] += D(a) dp[i - a], an O(N^2) sweep (2.5 billion
modular updates for N = 5 * 10^4) that a numba-compiled loop finishes
in a few seconds.  G(n) is then dp[n] and S(N) the prefix sum; the
code reproduces the given G(10) = 164 and S(10) = 396 before printing
S(5 * 10^4) modulo 999676999.
"""

from __future__ import annotations

import numpy as np
from numba import njit

MOD = 999676999
LIMIT = 50000


def derivative_table(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    deriv = np.zeros(n + 1, dtype=np.int64)
    if n >= 1:
        deriv[1] = 1
    for i in range(2, n + 1):
        p = int(spf[i])
        m = i // p
        deriv[i] = 1 if m == 1 else m + p * deriv[m]
    return deriv


@njit(cache=True)
def partition_dp(n: int, deriv: np.ndarray, mod: int) -> np.ndarray:
    dp = np.zeros(n + 1, dtype=np.int64)
    dp[0] = 1
    for a in range(1, n + 1):
        c = deriv[a] % mod
        for i in range(a, n + 1):
            dp[i] = (dp[i] + c * dp[i - a]) % mod
    return dp


def main() -> None:
    deriv = derivative_table(LIMIT)
    small = partition_dp(10, deriv[:11], MOD)
    assert small[10] == 164
    assert int(small[1:].sum()) % MOD == 396
    dp = partition_dp(LIMIT, deriv, MOD)
    print(int(dp[1:].sum() % MOD))  # 194396971


if __name__ == "__main__":
    main()
