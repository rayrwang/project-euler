"""
Project Euler Problem 782: Distinct Rows and Columns
https://projecteuler.net/problem=782

The complexity of an n x n binary matrix is the number of distinct
strings among its rows and columns together; c(n, k) is the minimum
complexity over matrices with exactly k ones, and C(n) sums c(n, k) for
k = 0..n^2.  Given C(5) = 64, C(10) = 274, C(20) = 1150, find C(10^4).

Structure of low-complexity matrices.  Group equal rows and equal
columns: a matrix with p distinct rows and q distinct columns is a p x q
binary pattern P with positive row multiplicities r (summing to n) and
column multiplicities w, and k = sum P_ab r_a w_b.  Its complexity is
p + q minus the number of row strings that coincide with column strings.
Because position t of a row string is column t and position t of a
column string is row t, a set M of identifications row i = column j is
realisable iff every index t can be given a (row type, column type) pair
(a, b) that is allowed -- meaning P[i][b] = P[a][j] for all (i, j) in M
-- with the prescribed marginals r and w; by max-flow this is exactly a
Hall condition over the at most 2^3 row-type subsets.  Enumerating all
patterns with p, q <= 3, all identification sets, and all margins
reproduces the brute-force c(n, k) for every k at n = 3, 4, 5, and the
given C(10) and C(20).

Closed forms.  Complexity 1 happens only for k = 0, n^2.  The machinery
shows complexity <= 2 occurs exactly for k or n^2 - k of the form a^2 or
2t(n - t) (corner squares and the two-string complementary-split
matrices).  For complexity <= 3 the 1570 enumerated (pattern, matching)
types collapse, by a greedy covering of their value sets, to a handful
of two-parameter families: k or n^2 - k equal to

    x y                          (x, y <= n)
    x^2 + y^2                    (x + y < n)
    y (2x + y)                   (x + y < n)
    b^2 + c (2n - 2b - c)        (b + c < n)
    2xy + z^2,  xy + yz + zx,  x^2 + y^2 + z^2   (x + y + z = n).

The closed-form union agrees with the exhaustive machinery for every
n <= 60 (and the brute force for n <= 5).  Everything else is
achievable with complexity 4 -- already at n = 20 the six exceptional
counts 59, 71, 83, 317, 329, 341 need it, and C(20) = 1150 confirms no
count requires five.  Hence

    C(n) = 4 (n^2 + 1) - |K1| - |K2| - |K3|,

with the K3 size found by an O(n^2) sieve over the families above --
about five seconds at n = 10^4.
"""

import numpy as np
from numba import njit

N = 10**4


@njit(cache=True)
def count_k3(n):
    """number of k in [0, n^2] achievable with complexity <= 3."""
    n2 = n * n
    mark = np.zeros(n2 + 1, dtype=np.uint8)
    mark[0] = 1
    mark[n2] = 1
    for x in range(1, n + 1):  # rectangles
        for y in range(x, n + 1):
            k = x * y
            mark[k] = 1
            mark[n2 - k] = 1
    for x in range(1, n):  # two opposite corner squares
        for y in range(x, n - x):
            k = x * x + y * y
            mark[k] = 1
            mark[n2 - k] = 1
    for x in range(1, n):  # self-conjugate two-step staircases
        for y in range(1, n - x):
            k = y * (2 * x + y)
            mark[k] = 1
            mark[n2 - k] = 1
    for b in range(1, n):  # staircase with a full frame
        for c in range(1, n - b):
            k = b * b + c * (2 * n - 2 * b - c)
            mark[k] = 1
            mark[n2 - k] = 1
    for x in range(1, n - 1):  # three-part identities x + y + z = n
        for y in range(1, n - x):
            z = n - x - y
            if z < 1:
                break
            k = 2 * x * y + z * z
            mark[k] = 1
            mark[n2 - k] = 1
            k = x * y + y * z + z * x
            mark[k] = 1
            mark[n2 - k] = 1
            k = x * x + y * y + z * z
            mark[k] = 1
            mark[n2 - k] = 1
    total = 0
    for k in range(n2 + 1):
        total += mark[k]
    return total


def count_k2(n):
    """number of k achievable with complexity <= 2."""
    vals = {0, n * n}
    for a in range(1, n + 1):
        vals.add(a * a)
        vals.add(n * n - a * a)
    for t in range(1, n):
        vals.add(2 * t * (n - t))
        vals.add(n * n - 2 * t * (n - t))
    return len(vals)


def complexity_sum(n):
    """C(n) = sum of minimum complexities over k = 0..n^2."""
    return 4 * (n * n + 1) - 2 - count_k2(n) - int(count_k3(n))


def main():
    assert complexity_sum(5) == 64
    assert complexity_sum(10) == 274
    assert complexity_sum(20) == 1150
    return complexity_sum(N)


if __name__ == "__main__":
    print(main())  # 318313204
