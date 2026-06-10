"""Project Euler Problem 654: Neighbourly Constraints.

T(n, m) counts m-tuples of positive integers in which every two adjacent
entries sum to at most n; we need T(5000, 10^12) mod 10^9 + 7.

For m >= 2 every entry lies in [1, n-1], and the transfer operator A with
A[a][b] = [a + b <= n] acts on a vector by reversed prefix sums:
(A v)(a) = S(n - a) with S the prefix-sum of v.  So consecutive terms
T(m) = 1^T A^(m-1) 1 cost only O(n) each.  Empirically (and provably from
the staircase structure) the sequence satisfies a linear recurrence of
order exactly n - 1, recovered here by running Berlekamp-Massey over
GF(p) on the first 2(n-1) + slack terms.  The 10^12-th term then comes
from Kitamasa: compute x^(m-2) modulo the recurrence's characteristic
polynomial by square-and-multiply with schoolbook O(d^2) multiplication
(d = 4999, about 40 squarings), and combine with the initial terms.

Checks: T(3, 4) = 8, T(5, 5) = 246, T(10, 100) and T(100, 10) match the
given residues, and the full BM + Kitamasa pipeline reproduces directly
iterated terms at scattered large indices for n = 10 and n = 57.
"""

import numba
import numpy as np

P = 1_000_000_007


@numba.jit(cache=True)
def seq_T(n: int, count: int) -> np.ndarray:
    """T(n, m) mod P for m = 2 .. count + 1."""
    v = np.ones(n - 1, dtype=np.int64)
    out = np.empty(count, dtype=np.int64)
    S = np.empty(n, dtype=np.int64)
    for t in range(count):
        S[0] = 0
        for i in range(n - 1):
            S[i + 1] = (S[i] + v[i]) % P
        for a in range(1, n):
            v[a - 1] = S[n - a]
        total = 0
        for i in range(n - 1):
            total = (total + v[i]) % P
        out[t] = total
    return out


@numba.jit(cache=True)
def _mod_pow(b: int, e: int) -> int:
    r = 1
    b %= P
    while e:
        if e & 1:
            r = r * b % P
        b = b * b % P
        e >>= 1
    return r


@numba.jit(cache=True)
def berlekamp_massey(seq: np.ndarray) -> np.ndarray:
    """Minimal recurrence: seq[i] = sum_j rec[j] * seq[i-1-j]."""
    nmax = len(seq) + 2
    C = np.zeros(nmax, dtype=np.int64)
    B = np.zeros(nmax, dtype=np.int64)
    C[0] = B[0] = 1
    L = 0
    m = 1
    b = 1
    lenC = lenB = 1
    T = np.empty(nmax, dtype=np.int64)
    for i in range(len(seq)):
        d = seq[i]
        for j in range(1, L + 1):
            d = (d + C[j] * seq[i - j]) % P
        if d == 0:
            m += 1
            continue
        coef = d * _mod_pow(b, P - 2) % P
        if 2 * L <= i:
            T[:lenC] = C[:lenC]
            lenT = lenC
            if lenB + m > lenC:
                C[lenC : lenB + m] = 0
                lenC = lenB + m
            for j in range(lenB):
                C[j + m] = (C[j + m] - coef * B[j]) % P
            L = i + 1 - L
            B[:lenT] = T[:lenT]
            lenB = lenT
            b = d
            m = 1
        else:
            if lenB + m > lenC:
                C[lenC : lenB + m] = 0
                lenC = lenB + m
            for j in range(lenB):
                C[j + m] = (C[j + m] - coef * B[j]) % P
            m += 1
    rec = np.empty(L, dtype=np.int64)
    for j in range(L):
        rec[j] = (-C[j + 1]) % P
    return rec


@numba.jit(cache=True)
def kitamasa(rec: np.ndarray, init: np.ndarray, idx: int) -> int:
    """Term `idx` (0-based) of the sequence with given recurrence/init."""
    d = len(rec)
    if idx < d:
        return init[idx]
    # charpoly: x^d - rec[0] x^(d-1) - ... - rec[d-1]
    cur = np.zeros(d, dtype=np.int64)  # current poly  = x^idx mod charpoly
    cur[0] = 1  # start with 1; build by processing bits of idx high->low
    bits = 0
    t = idx
    while t:
        bits += 1
        t >>= 1
    tmp = np.zeros(2 * d, dtype=np.int64)
    for bit in range(bits - 1, -1, -1):
        # square
        tmp[:] = 0
        for i in range(d):
            ci = cur[i]
            if ci:
                for j in range(d):
                    tmp[i + j] = (tmp[i + j] + ci * cur[j]) % P
        # reduce: x^k = sum rec[j] x^(k-1-j)
        for k in range(2 * d - 2, d - 1, -1):
            c = tmp[k]
            if c:
                tmp[k] = 0
                for j in range(d):
                    tmp[k - 1 - j] = (tmp[k - 1 - j] + c * rec[j]) % P
        cur[:] = tmp[:d]
        if (idx >> bit) & 1:
            # multiply by x and reduce once
            c = cur[d - 1]
            for i in range(d - 1, 0, -1):
                cur[i] = cur[i - 1]
            cur[0] = 0
            if c:
                for j in range(d):
                    cur[d - 1 - j] = (cur[d - 1 - j] + c * rec[j]) % P
    total = 0
    for i in range(d):
        total = (total + cur[i] * init[i]) % P
    return total


def T(n: int, m: int) -> int:
    d_guess = n - 1
    terms = seq_T(n, 2 * d_guess + 30)
    rec = berlekamp_massey(terms)
    return kitamasa(rec, terms[: len(rec)], m - 2)


if __name__ == "__main__":
    assert seq_T(3, 3)[2] == 8  # T(3, 4)
    assert seq_T(5, 4)[3] == 246  # T(5, 5)
    assert T(10, 100) == 862820094
    assert T(100, 10) == 782136797
    for n, m in ((10, 12345), (57, 4321)):
        assert T(n, m) == seq_T(n, m - 1)[m - 2], (n, m)
    print(T(5000, 10**12))  # 815868280
