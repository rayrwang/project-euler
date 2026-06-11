"""Project Euler Problem 633: Square Prime Factors II.

The conditions p^2 | n for distinct primes p are independent in natural
density (each has density exactly p^-2, and any finite combination
follows from CRT on residues mod the product of the squares; the
inclusion-exclusion over the remaining primes converges absolutely).
Hence the densities have the generating function

    sum_k c_k x^k = prod_p (1 - p^-2 + x p^-2)
                  = (6 / pi^2) prod_p (1 + x t_p),   t_p = 1/(p^2 - 1),

so c_k = (6/pi^2) e_k(t), the k-th elementary symmetric function of all
t_p.  The e_k follow from Newton's identities applied to the power sums
P_j = sum_p (p^2 - 1)^-j for j = 1..7, each summed over the primes
below 10^8; the truncation error of P_1 is below 10^-9 (the tail is
about 1/(X log X)) and even smaller for j >= 2, comfortably inside the
five significant digits requested.

Verified: c_1..c_4 match the four constants in the statement's table to
their printed precision, and a direct sieve count of square prime
factors reproduces the entire C_k(10^7) table row
(6079291, 3353956, 533140, 32777, 834) exactly.
"""

import math

import numpy as np

LIM = 10**8


def sci5(x: float) -> str:
    mant, ex = f"{x:.4e}".split("e")
    return f"{mant}e{int(ex)}"


if __name__ == "__main__":
    sieve = np.ones(LIM + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(LIM) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    primes = np.nonzero(sieve)[0].astype(np.float64)

    t = 1.0 / (primes * primes - 1.0)
    power_sums = [0.0] + [float((t**j).sum()) for j in range(1, 8)]

    e = [1.0]
    for k in range(1, 8):
        acc = 0.0
        for j in range(1, k + 1):
            acc += (-1) ** (j - 1) * power_sums[j] * e[k - j]
        e.append(acc / k)
    c = [6 / math.pi**2 * ek for ek in e]

    assert abs(c[1] - 3.3539e-1) < 1e-5
    assert abs(c[2] - 5.3293e-2) < 1e-6
    assert abs(c[3] - 3.2921e-3) < 1e-7
    assert abs(c[4] - 9.7046e-5) < 1e-9

    n = 10**7
    cnt = np.zeros(n + 1, dtype=np.uint8)
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            cnt[p * p :: p * p] += 1
    hist = np.bincount(cnt[1:])
    assert list(hist[:5]) == [6079291, 3353956, 533140, 32777, 834]

    print(sci5(c[7]))  # 1.0012e-10
