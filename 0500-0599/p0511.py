"""
https://projecteuler.net/problem=511

Seq(n, k) counts the sequences (a_1, ..., a_n) of positive integers
with every a_i a divisor of n and n + a_1 + ... + a_n divisible by k.
Find the last nine digits of Seq(1234567898765, 4321).

Only the residue of each a_i modulo k matters. Let f be the vector
indexed by Z_k with f[d mod k] incremented once per divisor d of n.
Choosing the n terms independently corresponds to the n-fold cyclic
convolution power of f, and we need the coefficient at residue
(-n) mod k:

    Seq(n, k) = (f^(*n))[(-n) mod k]  (mod 10^9).

f^(*n) is computed by binary exponentiation with O(k^2) cyclic
convolutions, O(k^2 log n) total. n = 1234567898765 = 5 * 41 * 25343 *
237631 has only 16 divisors.
"""

import sys
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import divisors  # noqa: E402

MOD = 10**9


@numba.njit(cache=True)
def _conv(a: np.ndarray, b: np.ndarray, k: int) -> np.ndarray:
    out = np.zeros(k, dtype=np.int64)
    for i in range(k):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(k):
            r = i + j
            if r >= k:
                r -= k
            out[r] = (out[r] + ai * b[j]) % MOD
    return out


@numba.njit(cache=True)
def _seq(n: int, k: int, divs: np.ndarray) -> int:
    f = np.zeros(k, dtype=np.int64)
    for d in divs:
        f[d % k] += 1
    # binary exponentiation of the convolution power f^(*n)
    result = np.zeros(k, dtype=np.int64)
    result[0] = 1  # identity for cyclic convolution
    e = n
    while e:
        if e & 1:
            result = _conv(result, f, k)
        f = _conv(f, f, k)
        e >>= 1
    return result[(-n) % k]


def seq(n: int, k: int) -> int:
    return _seq(n, k, np.array(divisors(n), dtype=np.int64))


def seq_brute(n: int, k: int) -> int:
    """Direct dynamic programming over sequence positions, for checks."""
    divs = [d for d in range(1, n + 1) if n % d == 0]
    cnt = [0] * k
    cnt[0] = 1
    for _ in range(n):
        nxt = [0] * k
        for r, c in enumerate(cnt):
            if c:
                for d in divs:
                    nxt[(r + d) % k] = (nxt[(r + d) % k] + c) % MOD
        cnt = nxt
    return cnt[(-n) % k]


if __name__ == "__main__":
    assert seq(3, 4) == seq_brute(3, 4) == 4
    assert seq(4, 11) == seq_brute(4, 11) == 8
    for nn, kk in [(6, 7), (12, 5), (10, 13), (16, 9)]:
        assert seq(nn, kk) == seq_brute(nn, kk)
    assert seq(1111, 24) == 840643584

    print(seq(1234567898765, 4321))  # 935247012
