"""
https://projecteuler.net/problem=560

Coprime Nim: a move removes y stones from a pile of m only if
gcd(m, y) = 1; last stone wins. L(n, k) counts the losing starting
positions over k piles of 1..n-1 stones. Find L(10^7, 10^7) mod
1000000007.

Grundy values (verified below against the literal mex recursion for
all m <= 2000): g(m) = 0 for even m, g(1) = 1, and for odd m >= 3,
g(m) = pi(spf(m)), the index of m's smallest prime factor. Intuition:
from even m every legal y is odd, landing on odd positions which all
have positive Grundy value, so even piles are losing; from an odd pile
the reachable Grundy set is exactly {0, 1, ..., pi(spf(m)) - 1}.

A position loses iff the XOR of its pile values is 0, so L(n, k) is
the XOR-zero count of the k-fold XOR convolution of the value counts
c_v = #{1 <= m <= n-1 : g(m) = v}. The counts come from one
smallest-prime-factor sieve: c_0 = #evens, c_1 = 1 (only m = 1), and
c_(pi(p)) counts odd m with spf(m) = p. With W the Walsh-Hadamard
transform of c (length 2^20 covers the largest prime index below
10^7),

    L(n, k) = 2^(-20) * sum_i W_i^k  (mod 1000000007).

|W_i| <= n keeps the exact transform in int64. The pipeline is checked
against direct enumeration for L(5, 2) = 6 and L(10, 5) = 9964, and
against the given L(10, 10) = 472400303 and
L(10^3, 10^3) = 954021836 (mod 10^9 + 7).
"""

import sys
from functools import reduce
from itertools import product
from math import gcd
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))

MOD = 1_000_000_007


@numba.njit(cache=True)
def _spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def _counts(n_max: int, spf: np.ndarray, prime_index: np.ndarray, size: int):
    c = np.zeros(size, dtype=np.int64)
    for m in range(1, n_max + 1):
        if m == 1:
            c[1] += 1
        elif m % 2 == 0:
            c[0] += 1
        else:
            c[prime_index[spf[m]]] += 1
    return c


@numba.njit(cache=True)
def _wht_pow_sum(c: np.ndarray, k: int, mod: int) -> int:
    size = len(c)
    w = c.copy()
    h = 1
    while h < size:
        for start in range(0, size, 2 * h):
            for i in range(start, start + h):
                x, y = w[i], w[i + h]
                w[i] = x + y
                w[i + h] = x - y
        h *= 2
    total = 0
    for i in range(size):
        base = w[i] % mod
        r = 1
        e = k
        while e:
            if e & 1:
                r = r * base % mod
            base = base * base % mod
            e >>= 1
        total = (total + r) % mod
    return total


def l_of(n: int, k: int) -> int:
    n_max = n - 1
    spf = _spf_sieve(max(n_max, 3))
    # prime_index[p] = pi(p) for primes p
    prime_index = np.zeros(n_max + 1, dtype=np.int64)
    cnt = 0
    for p in range(2, n_max + 1):
        if spf[p] == p:
            cnt += 1
            prime_index[p] = cnt
    size = 1
    while size <= cnt:
        size <<= 1
    c = _counts(n_max, spf, prime_index, size)
    total = int(_wht_pow_sum(c, k, MOD))
    return total * pow(size, -1, MOD) % MOD


def grundy_brute(n_max: int) -> list[int]:
    g = [0] * (n_max + 1)
    for m in range(1, n_max + 1):
        opts = {g[m - y] for y in range(1, m + 1) if gcd(m, y) == 1}
        mex = 0
        while mex in opts:
            mex += 1
        g[m] = mex
    return g


def l_direct(n: int, k: int, g: list[int]) -> int:
    return sum(
        1
        for t in product(range(1, n), repeat=k)
        if reduce(lambda a, b: a ^ b, (g[x] for x in t)) == 0
    )


if __name__ == "__main__":
    # Grundy formula vs the literal recursion
    g = grundy_brute(2000)
    spf = _spf_sieve(2000)
    prime_index = {}
    cnt = 0
    for p in range(2, 2001):
        if spf[p] == p:
            cnt += 1
            prime_index[p] = cnt
    for m in range(1, 2001):
        expect = 0 if m % 2 == 0 else (1 if m == 1 else prime_index[int(spf[m])])
        assert g[m] == expect, m

    assert l_direct(5, 2, g) == l_of(5, 2) == 6
    assert l_direct(10, 5, g) == l_of(10, 5) == 9964
    assert l_of(10, 10) == 472400303
    assert l_of(10**3, 10**3) == 954021836

    print(l_of(10**7, 10**7))  # 994345168
