"""
Project Euler Problem 774: Conjunctive Sequences
https://projecteuler.net/problem=774

A sequence of non-negative integers is conjunctive when every two
consecutive terms have non-zero bitwise AND; c(n, b) counts conjunctive
sequences of length n with all terms <= b.  Given c(3, 4) = 18,
c(10, 6) = 2496120 and c(100, 200) = 268159379 (mod 998244353), find
c(123, 123456789) modulo 998244353.

Transfer operator.  c(n, b) = 1^T T^(n-1) 1 where T is the 0/1 matrix on
states 0..b with T[x][y] = [x AND y != 0] = J - Z, J the all-ones matrix
and Z the disjointness matrix Z[x][y] = [x AND y = 0].  The point is
that both parts apply to a vector cheaply even though b is over 10^8:
(J v)(x) is the total sum of v, and

    (Z v)(x) = sum over y subset of complement(x), y <= b, of v(y),

which is one subset-sum (SOS / zeta) transform of v over the
2^27-element hypercube (b = 123456789 < 2^27, entries above b kept at
zero) followed by reading the transform at the complemented index.  One
application of T therefore costs 27 in-place passes over the 2^27
array; values stay below 2^30 * 2^27 < 2^63, so the transform needs no
intermediate reductions.  The passes are organised cache-friendly: the
low 16 bits are folded inside 64K blocks in a single sweep (fused with
the input copy), the high 11 bits as block-strided vector additions,
all parallelised across threads.

Halving.  T is symmetric, so with v = T^61 1 the answer is
c(123, b) = v^T v: 61 operator applications and one dot product, about
three seconds each.  The implementation reproduces the three given
values, and was additionally cross-checked at odd lengths against a
direct iteration for small b (e.g. c(123, 999)).
"""

import numpy as np
from numba import njit, prange

MOD = 998244353
N_LEN = 123
B = 123456789


@njit(cache=True, parallel=True)
def apply_t(v, work, b, nbits):
    """v <- (J - Z) v on [0, 2^nbits); entries above b stay zero."""
    n = 1 << nbits
    low = 16 if nbits > 16 else nbits
    lown = 1 << low
    nblk = n // lown
    total = np.int64(0)
    for x in range(n):
        total += v[x]
        if total >= (np.int64(1) << 62):
            total %= MOD
    total %= MOD
    # low bits: in-cache subset sums per 2^low block, fused with the copy
    for blk in prange(nblk):  # ty: ignore[not-iterable]
        base = blk * lown
        for i in range(lown):
            work[base + i] = v[base + i]
        for bit in range(low):
            stp = 1 << bit
            for i0 in range(0, lown, 2 * stp):
                for i in range(base + i0 + stp, base + i0 + 2 * stp):
                    work[i] += work[i - stp]
    # high bits: block-strided vector additions
    for bit in range(low, nbits):
        stp = 1 << (bit - low)
        nb2 = nblk // (2 * stp)
        for sb in prange(nb2):  # ty: ignore[not-iterable]
            sbase = sb * 2 * stp
            for tb in range(sbase + stp, sbase + 2 * stp):
                dst = tb * lown
                src = (tb - stp) * lown
                for i in range(lown):
                    work[dst + i] += work[src + i]
    mask = n - 1
    for x in prange(n):  # ty: ignore[not-iterable]
        if x <= b:
            w = (total - work[mask ^ x] % MOD) % MOD
            v[x] = w if w >= 0 else w + MOD
        else:
            v[x] = 0


def conjunctive(n_len, b):
    """c(n_len, b) mod MOD; n_len must be odd (uses T-symmetry halving)."""
    assert n_len % 2 == 1
    nbits = max(1, b.bit_length())
    n = 1 << nbits
    v = np.zeros(n, dtype=np.int64)
    v[: b + 1] = 1
    work = np.empty(n, dtype=np.int64)
    for _ in range((n_len - 1) // 2):
        apply_t(v, work, b, nbits)
    acc = 0
    for x in range(0, b + 1, 1 << 22):
        chunk = v[x : min(b + 1, x + (1 << 22))]
        acc = (acc + int((chunk * chunk % MOD).sum() % MOD)) % MOD
    return acc


def conjunctive_direct(n_len, b):
    """reference without the halving, for the even-length given values."""
    nbits = max(1, b.bit_length())
    n = 1 << nbits
    v = np.zeros(n, dtype=np.int64)
    v[: b + 1] = 1
    work = np.empty(n, dtype=np.int64)
    for _ in range(n_len - 1):
        apply_t(v, work, b, nbits)
    return int(v[: b + 1].sum() % MOD)


def main():
    assert conjunctive(3, 4) == 18
    assert conjunctive_direct(10, 6) == 2496120
    assert conjunctive_direct(100, 200) == 268159379
    assert conjunctive(123, 999) == conjunctive_direct(123, 999)
    return conjunctive(N_LEN, B)


if __name__ == "__main__":
    print(main())  # 459155763
