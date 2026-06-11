"""
Project Euler Problem 767: Window into a Matrix
https://projecteuler.net/problem=767

B(k, n) counts 16 x n binary matrices in which every 2 x k window (two
consecutive rows, k consecutive columns) sums to k.  Given B(2, 4) = 65550
and B(3, 9) = 87273560 (mod 10^9 + 7), find B(10^5, 10^16) mod 10^9 + 7.

Column periodicity.  For consecutive rows i, i+1 let c_j(i) = M[i][j] +
M[i+1][j].  Comparing the windows at offsets j and j+1 gives c_{j+k} = c_j
for every pair i, so the constraint is equivalent to (a) the first window of
every row pair sums to k and (b) the c-values have period k.  Writing
d_i = M[i][j+k] - M[i][j], condition (b) per column means d_i + d_{i+1} = 0,
so either d = 0 (the columns are equal) or d alternates +-1, which forces
both columns to be the two alternating vectors A = 0101... and its
complement.  Alternating columns have all pair sums equal to 1, so swapping
A with its complement never affects any window sum.  Hence a matrix is: a
free choice of the first k columns satisfying (a), then each later column
must repeat the column k to its left, except that alternating columns may
be replaced by either alternating vector.  With n = qk the residue class of
each base column contains q columns, giving a factor 2^(q-1) per
alternating base column.

Base block.  Summing (a) over a row pair gives S_i + S_{i+1} = k for the
row sums S_i of the 16 x k base block, so S alternates between some a and
k - a; conversely any such block works, and rows are then independent:
there are C(k, a)^16 blocks for a given a.  Weighting alternating columns
via w = 1 + (2^(q-1) - 1)([col = A] + [col = A complement]) and expanding
the product over columns, a term that fixes s special columns (C(k, s)
placements, 2^s sign choices) leaves a free 16 x (k-s) block with shifted
alternating row sums, counted by G(k - s) where G(m) = sum_a C(m, a)^16.
Therefore, when k divides n with quotient q,

    B(k, n) = sum_{s=0}^{k} C(k, s) (2 (2^(q-1) - 1))^s G(k - s).

This reproduces both given values, and was also verified against a brute
force over all small matrices for a 4-row analogue of the problem.  The
only heavy step is G(m) for all m <= 10^5, a parallel O(k^2) sweep.
"""

import numpy as np
from numba import njit, prange

MOD = 10**9 + 7
K = 10**5
N = 10**16


@njit(cache=True, parallel=True)
def g_table(k, inv):
    """G(m) = sum_a C(m, a)^16 mod MOD for m = 0..k."""
    g = np.zeros(k + 1, dtype=np.int64)
    for m in prange(k + 1):  # ty: ignore[not-iterable]
        c = np.int64(1)  # C(m, 0)
        total = np.int64(0)
        half = (m - 1) // 2
        for a in range(half + 1):
            c2 = c * c % MOD
            c4 = c2 * c2 % MOD
            c8 = c4 * c4 % MOD
            total = (total + c8 * c8) % MOD
            c = c * ((m - a) % MOD) % MOD * inv[a + 1] % MOD
        total = total * 2 % MOD
        if m % 2 == 0:  # middle term C(m, m/2)^16
            c2 = c * c % MOD
            c4 = c2 * c2 % MOD
            c8 = c4 * c4 % MOD
            total = (total + c8 * c8) % MOD
        g[m] = total
    return g


def solve(k, n, g=None):
    assert n % k == 0
    q = n // k
    if g is None:
        inv = np.ones(k + 2, dtype=np.int64)
        for i in range(2, k + 2):
            inv[i] = -(MOD // i) * inv[MOD % i] % MOD
        g = g_table(k, inv)
    w = 2 * (pow(2, q - 1, MOD) - 1) % MOD
    answer = 0
    binom = 1  # C(k, s)
    ws = 1  # w^s
    for s in range(k + 1):
        answer = (answer + binom * ws % MOD * g[k - s]) % MOD
        binom = binom * (k - s) % MOD * pow(s + 1, MOD - 2, MOD) % MOD
        ws = ws * w % MOD
    return answer


def main():
    assert solve(2, 4) == 65550
    assert solve(3, 9) == 87273560
    return solve(K, N)


if __name__ == "__main__":
    print(main())  # 783976175
