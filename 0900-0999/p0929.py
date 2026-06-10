"""Project Euler 929: Odd-Run Compositions.

A composition with all maximal runs of odd length is a sequence of
blocks (value v, odd multiplicity) in which adjacent blocks have
different values -- exactly a Smirnov word over the infinite alphabet of
blocks.  With block weight R_v(x) = x^v / (1 - x^{2v}) (odd repeats of
v), the Smirnov formula gives

    F(x) = 1 / (1 - sum_v R_v / (1 + R_v))
         = 1 / (1 - sum_v x^v / (1 + x^v - x^{2v})).

Since 1/(1 + y - y^2) = sum_k (-1)^k Fib(k+1) y^k, the subtracted series
has coefficients g[n] = sum_{d | n} (-1)^(d-1) Fib(d), filled by a
harmonic sieve in O(N log N); then F = 1/(1 - G) by the O(N^2)
convolution recurrence f[n] = sum_k g[k] f[n-k] (numba).

Validated against a direct recursive count of odd-run compositions for
n <= 30 (including the given F(5) = 10).
"""

import sys
from functools import lru_cache

import numpy as np
from numba import njit

M = 1111124111


@njit(cache=True)
def _series(n_max: int) -> np.ndarray:
    fib = np.zeros(n_max + 1, dtype=np.int64)
    if n_max >= 1:
        fib[1] = 1
    if n_max >= 2:
        fib[2] = 1
    for i in range(3, n_max + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % M
    g = np.zeros(n_max + 1, dtype=np.int64)
    for m in range(1, n_max + 1):
        t = fib[m] if m % 2 == 1 else (M - fib[m]) % M
        for n in range(m, n_max + 1, m):
            g[n] = (g[n] + t) % M
    f = np.zeros(n_max + 1, dtype=np.int64)
    f[0] = 1
    for n in range(1, n_max + 1):
        s = 0
        for k in range(1, n + 1):
            s = (s + g[k] * f[n - k]) % M
        f[n] = s
    return f


def solve(n: int) -> int:
    return int(_series(n)[n])


def _brute(n: int) -> int:
    sys.setrecursionlimit(100000)

    @lru_cache(maxsize=None)
    def t(rem: int, last: int) -> int:
        if rem == 0:
            return 1
        tot = 0
        for v in range(1, rem + 1):
            if v == last:
                continue
            k = 1
            while v * k <= rem:
                tot += t(rem - v * k, v)
                k += 2
        return tot

    return t(n, 0)


if __name__ == "__main__":
    f = _series(30)
    assert f[5] == 10  # given
    for m in range(1, 31):
        assert int(f[m]) == _brute(m) % M, m
    print(solve(10**5))  # 57322484
