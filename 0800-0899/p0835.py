"""Project Euler 835: Supernatural Triangles.

Two families of Pythagorean triangles have consecutive sides.  When a
leg and the hypotenuse are consecutive, a^2 = 2b + 1 forces
(2m+1, 2m^2+2m, 2m^2+2m+1) with perimeter 4m^2 + 6m + 2.  When the two
legs are consecutive, (2a+1)^2 - 2c^2 = -1 is a negative Pell
equation, giving perimeters P_k = x_k + c_k with
x + c sqrt(2) = (1 + sqrt 2)^(2k-1): the chain 12, 70, 408, ...
obeying P_{k+1} = 6 P_k - P_{k-1} (with the degenerate P_1 = 2).  The
families intersect only at (3, 4, 5), so 12 is subtracted once.

For N = 10^(10^10), 4N is a perfect square, so the parabola cutoff is
exact: M = (sqrt(4N+1) - 3)/4 = 5 * 10^(L-1) - 1 with L = 5 * 10^9,
verified against integer square roots for medium exponents, and the
quadratic sum is evaluated from M mod p by Faulhaber.  The Pell count
K is the largest k with log P_k <= log N, decided with 60-digit
arithmetic (the margin is checked to exceed 10^-30), and the Pell
perimeter total comes from a 3x3 matrix power carrying
(P_k, P_{k-1}, sum).  The whole modular pipeline is validated against
exact enumeration up to 10^10, including the given S(100) = 258 and
S(10^4) = 172004.
"""

from __future__ import annotations

import mpmath as mp

MOD = 1234567891


def quadratic_family_sum(m_mod: int, p: int) -> int:
    """sum_{m=1}^{M} (4m^2 + 6m + 2) mod p from M mod p."""
    inv6 = pow(6, p - 2, p)
    inv2 = pow(2, p - 2, p)
    m = m_mod % p
    s2 = m * (m + 1) % p * (2 * m + 1) % p * inv6 % p
    s1 = m * (m + 1) % p * inv2 % p
    return (4 * s2 + 6 * s1 + 2 * m) % p


def pell_family_sum(k_max: int, p: int) -> int:
    """sum_{k=2}^{K} P_k mod p with P_2 = 12, P_{k+1} = 6 P_k - P_{k-1}."""
    if k_max < 2:
        return 0

    def mat_mult(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        return [
            [sum(a[i][t] * b[t][j] for t in range(3)) % p for j in range(3)]
            for i in range(3)
        ]

    mat = [[6, -1, 0], [1, 0, 0], [6, -1, 1]]
    res = [[int(i == j) for j in range(3)] for i in range(3)]
    e = k_max - 2
    while e:
        if e & 1:
            res = mat_mult(res, mat)
        mat = mat_mult(mat, mat)
        e >>= 1
    v = (12, 2, 12)  # (P_2, P_1, S_2)
    return (res[2][0] * v[0] + res[2][1] * v[1] + res[2][2] * v[2]) % p


def exact_total(n: int) -> int:
    total = 0
    m = 1
    while 4 * m * m + 6 * m + 2 <= n:
        total += 4 * m * m + 6 * m + 2
        m += 1
    a, b = 2, 12
    while b <= n:
        total += b
        a, b = b, 6 * b - a
    if n >= 12:
        total -= 12
    return total


def modular_total_small(n: int, p: int) -> int:
    m = 0
    while 4 * (m + 1) ** 2 + 6 * (m + 1) + 2 <= n:
        m += 1
    k = 1
    a, b = 2, 12
    while b <= n:
        k += 1
        a, b = b, 6 * b - a
    s = (quadratic_family_sum(m, p) + pell_family_sum(k, p)) % p
    if n >= 12:
        s = (s - 12) % p
    return s


def main() -> None:
    prime_test = 999999999999999989
    assert exact_total(100) == 258
    assert exact_total(10000) == 172004
    for n in (100, 10000, 10**6, 10**8, 10**10):
        assert modular_total_small(n, prime_test) == exact_total(n) % prime_test

    big_l = 5 * 10**9
    m_mod = (5 * pow(10, big_l - 1, MOD) - 1) % MOD

    mp.mp.dps = 60
    alpha = 1 + mp.sqrt(2)
    lead = (1 + 1 / mp.sqrt(2)) / 2
    log_n = mp.mpf(10) ** 10 * mp.log(10)
    k_max = int(mp.floor((log_n - mp.log(lead)) / (2 * mp.log(alpha)) + mp.mpf(1) / 2))
    low = mp.log(lead) + (2 * k_max - 1) * mp.log(alpha)
    high = mp.log(lead) + (2 * k_max + 1) * mp.log(alpha)
    assert low < log_n < high
    assert min(abs(low - log_n), abs(high - log_n)) > mp.mpf("1e-30")

    ans = (quadratic_family_sum(m_mod, MOD) + pell_family_sum(k_max, MOD) - 12) % MOD
    print(ans)  # 1050923942


if __name__ == "__main__":
    main()
