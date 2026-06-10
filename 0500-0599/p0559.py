"""
https://projecteuler.net/problem=559

P(k, r, n) counts r x n matrices whose rows are permutations of
{1..n} and where a column ascent (every row increasing from column j
to j+1) occurs exactly at the columns j < n not divisible by k.
Q(n) = sum_(k=1..n) P(k, n, n); find Q(50000) mod 1000000123.

The columns split into ceil(n/k) base blocks of length k (last block
of length l = n - (m-1)k); within blocks all rows ascend, and each
boundary must fail to ascend in some row. Inclusion-exclusion over
the boundaries relaxed to "all ascend" merges consecutive blocks: a
matrix where rows ascend within prescribed blocks of sizes c_i is
counted by (n! / prod c_i!)^r per matrix, so

  P(k, r, n) = (n!)^r * sum over compositions (a_1..a_s) of m of
               (-1)^(m-s) prod ((a_i k)!)^(-r),

with the last group's size (a_s - 1)k + l. A linear DP over the
number of consumed regular blocks computes the signed composition
sum in O((n/k)^2), and summing over k costs
sum_k (n/k)^2 ~ zeta(2) n^2 ~ 4 * 10^9 multiply-adds for n = 50000.

Verified against literal enumeration of all r-tuples of permutations
for six small (k, r, n), exact rational evaluation of the given
P(1,2,3) = 19, P(2,4,6) = 65508751 and Q(5) = 21879393751, and the
given modular values P(7,5,30) = 161858102 and Q(50) = 819573537.
"""

import itertools
from fractions import Fraction
from math import factorial

import numba
import numpy as np

MOD = 1000000123


@numba.njit(cache=True)
def _powmod(b: np.int64, e: np.int64, m: np.int64) -> np.int64:
    r = np.int64(1)
    b %= m
    while e > 0:
        if e & 1:
            r = r * b % m
        b = b * b % m
        e >>= 1
    return r


@numba.njit(cache=True)
def _q_mod(n: int, fact: np.ndarray, invfact: np.ndarray) -> np.int64:
    total = np.int64(0)
    fnr = _powmod(fact[n], np.int64(n), np.int64(MOD))
    f = np.zeros(n + 2, dtype=np.int64)
    u = np.zeros(n + 2, dtype=np.int64)
    w = np.zeros(n + 2, dtype=np.int64)
    for k in range(1, n + 1):
        m = (n + k - 1) // k
        ell = n - (m - 1) * k
        for a in range(1, m + 1):
            u[a] = _powmod(invfact[a * k] if a * k <= n else 0, n, MOD)
            w[a] = _powmod(invfact[(a - 1) * k + ell], n, MOD)
        f[0] = 1
        for t in range(1, m + 1):
            s = np.int64(0)
            for a in range(1, t + 1):
                term = u[a] * f[t - a] % MOD
                s = (s + term) % MOD if a % 2 == 1 else (s - term) % MOD
            f[t] = s
        h = np.int64(0)
        for a in range(1, m + 1):
            term = w[a] * f[m - a] % MOD
            h = (h + term) % MOD if a % 2 == 1 else (h - term) % MOD
        total = (total + fnr * h) % MOD
    return total % MOD


def _facts(n: int) -> tuple[np.ndarray, np.ndarray]:
    fact = np.ones(n + 1, dtype=np.int64)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = np.ones(n + 1, dtype=np.int64)
    invfact[n] = pow(int(fact[n]), MOD - 2, MOD)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return fact, invfact


def p_exact(k: int, r: int, n: int) -> int:
    m = -(-n // k)
    ell = n - (m - 1) * k
    f = [Fraction(0)] * (m + 1)
    f[0] = Fraction(1)
    for t in range(1, m + 1):
        f[t] = sum(
            (-1) ** (a - 1) * Fraction(1, factorial(a * k) ** r) * f[t - a]
            for a in range(1, t + 1)
        )
    h = sum(
        (-1) ** (a - 1) * Fraction(1, factorial((a - 1) * k + ell) ** r) * f[m - a]
        for a in range(1, m + 1)
    )
    return int(h * factorial(n) ** r)


def p_mod(k: int, r: int, n: int) -> int:
    fact, invfact = _facts(n)
    m = -(-n // k)
    ell = n - (m - 1) * k
    u = [pow(int(invfact[a * k]) if a * k <= n else 0, r, MOD) for a in range(m + 1)]
    w = [pow(int(invfact[(a - 1) * k + ell]), r, MOD) for a in range(m + 1)]
    f = [0] * (m + 1)
    f[0] = 1
    for t in range(1, m + 1):
        f[t] = (
            sum((1 if a % 2 else -1) * u[a] * f[t - a] for a in range(1, t + 1)) % MOD
        )
    h = sum((1 if a % 2 else -1) * w[a] * f[m - a] for a in range(1, m + 1))
    return h % MOD * pow(int(fact[n]), r, MOD) % MOD


def _brute_p(k: int, r: int, n: int) -> int:
    perms = list(itertools.permutations(range(1, n + 1)))
    cnt = 0
    for rows in itertools.product(perms, repeat=r):
        if all(
            all(row[j] < row[j + 1] for row in rows) == ((j + 1) % k != 0)
            for j in range(n - 1)
        ):
            cnt += 1
    return cnt


if __name__ == "__main__":
    assert p_exact(1, 2, 3) == 19 == _brute_p(1, 2, 3)  # given
    assert p_exact(2, 4, 6) == 65508751  # given
    for krn in ((2, 2, 4), (3, 2, 5), (2, 3, 4), (1, 3, 3), (4, 2, 5), (3, 3, 4)):
        assert p_exact(*krn) == _brute_p(*krn), krn
    assert sum(p_exact(k, 5, 5) for k in range(1, 6)) == 21879393751  # given Q(5)
    assert p_mod(7, 5, 30) == 161858102  # given
    f50, i50 = _facts(50)
    assert int(_q_mod(50, f50, i50)) == 819573537  # given Q(50)

    fact, invfact = _facts(50000)
    print(int(_q_mod(50000, fact, invfact)))  # 684724920
