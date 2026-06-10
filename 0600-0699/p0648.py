"""Project Euler Problem 648: Skipping Squares.

A sum starts at 0 and repeatedly gains +1 with probability rho, else +2,
stopping on a perfect square (or past 10^18); f(rho) is the expected
number of squares skipped, a polynomial sum_k a_k rho^k, and we need
F(1000) = sum_(k<=1000) a_k mod 10^9.

With q = 1 - rho, the chance a +1/+2 walk ever visits a point d ahead is
h(d) = (1 + q(-q)^d)/(1 + q) (solve the two-term recurrence; roots 1 and
-q).  Skipping square m^2 -- having just landed on m^2 + 1 after the
previous skip -- happens with probability 1 - h(2m) = q(1 - q^(2m))/(1+q),
and skipping the first square from 0 has probability q.  Hence

    f = sum_(m>=1) q^m / (1+q)^(m-1) * prod_(j=1)^(m-1) (1 - q^(2j)).

Each factor (1 - q^(2j))/(1 + q) equals (1 - q)(1 + q^2 + ... + q^(2j-2)),
so the denominators cancel exactly:

    f = sum_(m>=1) rho^(m-1) q^m prod_(j=1)^(m-1) [j]_(q^2),

with [j]_(q^2) the q-square bracket -- an all-integer series, no division,
and term m starts at order rho^(m-1).  Modulo rho^1001 only m <= 1001
contribute (which is why the 10^18 cap does not disturb the coefficients),
and the running product needs ever fewer terms as m grows: the work is
sum (1001 - m)^2 ~ 3 * 10^8 int64 multiply-adds modulo 10^9 in numba.

Checks: a_0 = 1, a_1 = 0, a_5 = -18, a_10 = 45176 (signed via balanced
residues), F(10) = 53964 and F(50) == 842418857 (mod 10^9), all as given.
"""

import numba
import numpy as np

MOD = 10**9


@numba.jit(cache=True)
def coefficients(n: int) -> np.ndarray:
    """a_0..a_n of f(rho) modulo 10^9."""
    L = n + 1
    coef = np.zeros(L, dtype=np.int64)  # accumulates f
    P = np.zeros(L, dtype=np.int64)  # running product of [j]_{q^2}
    P[0] = 1
    A = np.zeros(L, dtype=np.int64)  # [m]_{q^2} = sum_{i<m} (1-rho)^{2i}
    B = np.zeros(L, dtype=np.int64)  # (1-rho)^{2m}
    A[0] = 0
    B[0] = 1
    qpow = np.zeros(L, dtype=np.int64)  # (1-rho)^m
    qpow[0] = 1
    tmp = np.zeros(L, dtype=np.int64)
    for m in range(1, n + 2):
        # qpow <- (1-rho)^m
        for i in range(min(m, L - 1), 0, -1):
            qpow[i] = (qpow[i] - qpow[i - 1]) % MOD
        # term_m = rho^(m-1) * qpow * P ; add into coef
        lim = L - (m - 1)  # needed length of qpow * P
        for i in range(lim):
            pi = P[i]
            if pi:
                for j in range(lim - i):
                    coef[m - 1 + i + j] = (
                        coef[m - 1 + i + j] + pi * qpow[j]
                    ) % MOD
        if m == n + 1:
            break
        # A <- [m]_{q^2} : add (1-rho)^{2(m-1)}
        for i in range(L):
            A[i] = (A[i] + B[i]) % MOD
        # B <- (1-rho)^{2m}
        for _ in range(2):
            for i in range(L - 1, 0, -1):
                B[i] = (B[i] - B[i - 1]) % MOD
        # P <- P * A, truncated to what later terms need
        lim = L - m
        tmp[:lim] = 0
        for i in range(lim):
            pi = P[i]
            if pi:
                for j in range(lim - i):
                    tmp[i + j] = (tmp[i + j] + pi * A[j]) % MOD
        P[:lim] = tmp[:lim]
        P[lim:] = 0
    return coef


if __name__ == "__main__":
    c = coefficients(1000)
    signed = lambda v: v if v < MOD // 2 else v - MOD  # noqa: E731
    assert signed(c[0]) == 1 and signed(c[1]) == 0
    assert signed(c[5]) == -18 and signed(c[10]) == 45176
    assert sum(int(x) for x in c[:11]) % MOD == 53964  # F(10)
    assert sum(int(x) for x in c[:51]) % MOD == 842418857  # F(50)
    print(sum(int(x) for x in c) % MOD)  # 301483197
