"""Project Euler Problem 682: 5-Smooth Pairs.

A Hamming number is p = 2^a 3^b 5^c with Omega = a + b + c and
s = 2a + 3b + 5c, so f(n) counts sextuples (a, b, c, a', b', c') >= 0 with
equal coordinate sums and total weight n.  Tagging weight with x and the
Omega difference with y, the pair generating function is
A(x, y) A(x, 1/y) with A = 1 / ((1 - x^2 y)(1 - x^3 y)(1 - x^5 y)), and
f(n) = [x^n][y^0] of it.  The y^0 coefficient is the contour integral of
A(x, y) A(x, 1/y) / y, whose poles inside |y| < 1 (as a formal power
series in x) sit at y = x^2, x^3, x^5; summing the three residues,

    B(x) = 1 / ((1-x)(1-x^3)(1-x^4)(1-x^5)(1-x^7))
         - x / ((1-x)(1-x^2)(1-x^5)(1-x^6)(1-x^8))
         + x^5 / ((1-x^2)(1-x^3)(1-x^7)(1-x^8)(1-x^10)).

Each 1/(1 - x^d) factor is a strided prefix sum, so [x^n] B(x) for
n = 10^7 is fifteen passes over an array modulo 10^9 + 7.

Verified: f(10) = 4, f(100) = 3629, and the full series against direct
enumeration of the sextuples for all n <= 120.
"""

import numba
import numpy as np

N = 10**7
MOD = 1_000_000_007


@numba.jit(cache=True)
def rational_coeffs(n: int, ds: np.ndarray, mod: int) -> np.ndarray:
    """Coefficients of 1 / prod_d (1 - x^d) up to x^n, modulo mod."""
    coef = np.zeros(n + 1, dtype=np.int64)
    coef[0] = 1
    for d in ds:
        for i in range(d, n + 1):
            coef[i] = (coef[i] + coef[i - d]) % mod
    return coef


def f_series(n: int, mod: int) -> np.ndarray:
    t1 = rational_coeffs(n, np.array([1, 3, 4, 5, 7]), mod)
    t2 = rational_coeffs(n, np.array([1, 2, 5, 6, 8]), mod)
    t3 = rational_coeffs(n, np.array([2, 3, 7, 8, 10]), mod)
    out = t1
    out[1:] = (out[1:] - t2[:-1]) % mod
    out[5:] = (out[5:] + t3[:-5]) % mod
    return out


def f_brute(n: int) -> int:
    from collections import defaultdict

    counts: dict[tuple[int, int], int] = defaultdict(int)
    for a in range(n // 2 + 1):
        for b in range((n - 2 * a) // 3 + 1):
            for c in range((n - 2 * a - 3 * b) // 5 + 1):
                counts[a + b + c, 2 * a + 3 * b + 5 * c] += 1
    return sum(
        v * counts.get((k, n - s), 0) for (k, s), v in counts.items()
    )


if __name__ == "__main__":
    series = f_series(N, MOD)
    assert series[10] == 4 and series[100] == 3629
    assert all(series[n] == f_brute(n) % MOD for n in range(121))
    print(int(series[N]))  # 290872710
