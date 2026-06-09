"""
https://projecteuler.net/problem=537

T(n, k) counts the k-tuples (x_1, ..., x_k) of positive integers with
pi(x_1) + ... + pi(x_k) = n. Find T(20000, 20000) mod 1004535809.

The number of positive integers x with pi(x) = j is c_0 = 1 (only
x = 1) and c_j = p_(j+1) - p_j for j >= 1 (the integers from p_j up to
the one before the next prime). The coordinates are independent, so

    T(n, k) = [z^n] f(z)^k,   f(z) = sum_j c_j z^j,

and only coefficients up to degree n matter, requiring the primes up
to p_(n+1). The power is computed by binary exponentiation of the
truncated polynomial; each product of two degree <= n polynomials is a
single length-2^16 NTT multiplication (no aliasing since 2n < 2^16).
The modulus 1004535809 = 479 * 2^21 + 1 supports NTTs up to length
2^21 with primitive root 3 (both verified in the asserts).
"""

import sys
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402

MOD = 1004535809  # 479 * 2^21 + 1
ROOT = 3


@numba.njit(cache=True)
def _modpow(a: int, e: int, m: int) -> int:
    r = 1
    a %= m
    while e:
        if e & 1:
            r = r * a % m
        a = a * a % m
        e >>= 1
    return r


@numba.njit(cache=True)
def _ntt(a: np.ndarray, invert: bool) -> None:
    n = len(a)
    # bit-reversal permutation
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        w = _modpow(ROOT, (MOD - 1) // length, MOD)
        if invert:
            w = _modpow(w, MOD - 2, MOD)
        for start in range(0, n, length):
            wn = 1
            half = length >> 1
            for i in range(start, start + half):
                u = a[i]
                v = a[i + half] * wn % MOD
                a[i] = (u + v) % MOD
                a[i + half] = (u - v) % MOD
                wn = wn * w % MOD
        length <<= 1
    if invert:
        n_inv = _modpow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * n_inv % MOD


@numba.njit(cache=True)
def _mul_trunc(a: np.ndarray, b: np.ndarray, n_keep: int, size: int) -> np.ndarray:
    fa = np.zeros(size, dtype=np.int64)
    fb = np.zeros(size, dtype=np.int64)
    fa[: len(a)] = a
    fb[: len(b)] = b
    _ntt(fa, False)
    _ntt(fb, False)
    for i in range(size):
        fa[i] = fa[i] * fb[i] % MOD
    _ntt(fa, True)
    return fa[:n_keep].copy()


@numba.njit(cache=True)
def _poly_pow(f: np.ndarray, k: int, n_keep: int) -> np.ndarray:
    size = 1
    while size < 2 * n_keep:
        size <<= 1
    result = np.zeros(n_keep, dtype=np.int64)
    result[0] = 1
    base = f[:n_keep].copy()
    e = k
    while e:
        if e & 1:
            result = _mul_trunc(result, base, n_keep, size)
        e >>= 1
        if e:
            base = _mul_trunc(base, base, n_keep, size)
    return result


def t_of(n: int, k: int) -> int:
    # primes p_1 .. p_(n+1)
    limit = 32
    while True:
        primes = prime_sieve_int(limit)
        if len(primes) >= n + 1:
            break
        limit *= 2
    f = np.zeros(n + 1, dtype=np.int64)
    f[0] = 1  # x = 1
    for j in range(1, n + 1):
        f[j] = (primes[j] - primes[j - 1]) % MOD
    return int(_poly_pow(f, k, n + 1)[n])


def t_brute(n: int, k: int) -> int:
    """Direct dynamic programming, one coordinate at a time."""
    limit = 32
    while True:
        primes = prime_sieve_int(limit)
        if len(primes) >= n + 1:
            break
        limit *= 2
    c = [1] + [int(primes[j] - primes[j - 1]) for j in range(1, n + 1)]
    dp = [0] * (n + 1)
    dp[0] = 1
    for _ in range(k):
        nxt = [0] * (n + 1)
        for s in range(n + 1):
            if dp[s]:
                for j in range(n + 1 - s):
                    nxt[s + j] = (nxt[s + j] + dp[s] * c[j]) % MOD
        dp = nxt
    return dp[n]


if __name__ == "__main__":
    # NTT modulus sanity: 2^21 | MOD - 1 and 3 is a primitive root
    assert (MOD - 1) % 2**21 == 0
    for q in (2, 479):
        assert pow(ROOT, (MOD - 1) // q, MOD) != 1

    assert t_of(3, 3) == t_brute(3, 3) == 19
    assert t_of(10, 10) == t_brute(10, 10) == 869985
    for nn, kk in [(7, 4), (12, 9), (25, 13)]:
        assert t_of(nn, kk) == t_brute(nn, kk)
    assert t_of(1000, 1000) == 578270566

    print(t_of(20000, 20000))  # 779429131
