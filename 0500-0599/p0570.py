"""
https://projecteuler.net/problem=570

A snowflake of order n overlays a 180-degree-rotated equilateral
triangle onto each same-size equilateral triangle of the order n-1
snowflake (order 1 is a single triangle). A(n) counts unit triangles
exactly one layer thick, B(n) those three layers thick, and
G(n) = gcd(A(n), B(n)). Find the sum of G(n) for n = 3..10^7.

Construction (reverse-engineered from the problem's picture by
fitting the triangular lattice to the order-3 panel and reading the
per-cell colours, then confirmed by every given value): each step
refines the lattice by 3 (children inherit the parent thickness) and
then stamps +1 over the rotated-star footprint -- six hexagon cells
plus one tip cell poking into each edge-neighbour -- of every cell
that is *visible as a unit triangle*, i.e. whose thickness differs
from all three edge-neighbours. The explicit simulation below
reproduces the given A(3) = 30 and B(3) = 6 and yields

    A(n) = 3 * 4^(n-1) - 2 * 3^(n-1),
    B(n) = (9n - 69) * 2^(2n-3) + (4n + 26) * 3^(n-1),

(recurrences x^2-7x+12 and (x^2-7x+12)^2, fitted from an exact
1009-state local-configuration dynamics and checked against the
simulation for n <= 7); the given A(11) = 3027630 and
B(11) = 19862070 confirm both independently.

For the gcd, A(n)/6 = 2^(2n-3) - 3^(n-2) is coprime to 6, and modulo
it 2^(2n-3) = 3^(n-2), so 2 B(n)/6 = (3n-23) 2^(2n-3) +
(4n+26) 3^(n-2) = 3^(n-2) (7n+3); since 3^(n-2) is invertible,

    G(n) = 6 * gcd(2^(2n-3) - 3^(n-2), 7n + 3),

verified against exact big-integer gcd(A, B) for all n <= 300, with
the given G(3) = 6, G(11) = 30, G(500) = 186 and
sum_(n=3..500) G(n) = 5124 asserted. The final sum needs two modular
exponentiations mod 7n+3 < 2^27 per n, parallelised.
"""

from math import gcd

import numba
import numpy as np


@numba.njit(cache=True)
def _step(u: np.ndarray, d: np.ndarray):
    n0 = u.shape[0]
    nu = np.zeros((n0 * 3 + 8, n0 * 3 + 8), dtype=np.int8)
    nd = np.zeros((n0 * 3 + 8, n0 * 3 + 8), dtype=np.int8)
    for a in range(n0):
        for b in range(n0):
            t = u[a, b]
            if t:
                for i in range(3):
                    for j in range(3):
                        if i + j <= 2:
                            nu[3 * a + 4 + i, 3 * b + 4 + j] += t
                        if i + j <= 1:
                            nd[3 * a + 4 + i, 3 * b + 4 + j] += t
            t = d[a, b]
            if t:
                for i in range(3):
                    for j in range(3):
                        if i + j >= 2:
                            nd[3 * a + 4 + i, 3 * b + 4 + j] += t
                        if i + j >= 3:
                            nu[3 * a + 4 + i, 3 * b + 4 + j] += t
    for a in range(1, n0 - 1):
        for b in range(1, n0 - 1):
            t = u[a, b]  # visible up cell: stamp rotated (down) star
            if t >= 1 and t != d[a, b] and t != d[a - 1, b] and t != d[a, b - 1]:
                for i in range(3):
                    for j in range(3):
                        if i + j >= 2:
                            nd[3 * a + 3 + i, 3 * b + 3 + j] += 1
                        if i + j >= 3:
                            nu[3 * a + 3 + i, 3 * b + 3 + j] += 1
            t = d[a, b]  # visible down cell: stamp rotated (up) star
            if t >= 1 and t != u[a, b] and t != u[a + 1, b] and t != u[a, b + 1]:
                for i in range(3):
                    for j in range(3):
                        if i + j <= 2:
                            nu[3 * a + 5 + i, 3 * b + 5 + j] += 1
                        if i + j <= 1:
                            nd[3 * a + 5 + i, 3 * b + 5 + j] += 1
    return nu, nd


def _a_cf(n: int) -> int:
    return 3 * 4 ** (n - 1) - 2 * 3 ** (n - 1)


def _b_cf(n: int) -> int:
    return (9 * n - 69) * 2 ** (2 * n - 3) + (4 * n + 26) * 3 ** (n - 1)


@numba.njit(cache=True)
def _powmod(b: np.int64, e: np.int64, m: np.int64) -> np.int64:
    r = np.int64(1)
    b %= m
    while e > 0:
        if e & 1:
            r = (r * b) % m
        b = (b * b) % m
        e >>= 1
    return r


@numba.njit(cache=True, parallel=True)
def _total(n_max: int) -> np.int64:
    sums = np.zeros(64, dtype=np.int64)
    for tid in numba.prange(64):  # ty: ignore[not-iterable]
        sub = np.int64(0)
        for n in range(3 + tid, n_max + 1, 64):
            k = np.int64(7 * n + 3)
            x = _powmod(np.int64(2), np.int64(2 * n - 3), k)
            x = (x - _powmod(np.int64(3), np.int64(n - 2), k)) % k
            a, b = x, k
            while b:
                a, b = b, a % b
            sub += 6 * a
        sums[tid] = sub
    return sums.sum()


if __name__ == "__main__":
    u = np.zeros((4, 4), dtype=np.int8)
    d = np.zeros((4, 4), dtype=np.int8)
    u[1, 1] = 1
    for n in range(2, 8):
        u, d = _step(u, d)
        a = int((u == 1).sum() + (d == 1).sum())
        b = int((u == 3).sum() + (d == 3).sum())
        assert a == _a_cf(n) and b == _b_cf(n), n
        if n == 3:
            assert a == 30 and b == 6  # given

    assert _a_cf(11) == 3027630 and _b_cf(11) == 19862070  # given
    assert gcd(_a_cf(3), _b_cf(3)) == 6  # given
    assert gcd(_a_cf(11), _b_cf(11)) == 30  # given

    def g_fast(n: int) -> int:
        return 6 * gcd(2 ** (2 * n - 3) - 3 ** (n - 2), 7 * n + 3)

    for n in range(3, 301):  # the gcd reduction, exactly
        a6 = 2 ** (2 * n - 3) - 3 ** (n - 2)
        assert a6 % 2 == 1 and a6 % 3 != 0 and _a_cf(n) == 6 * a6
        assert gcd(_a_cf(n), _b_cf(n)) == g_fast(n)

    assert g_fast(500) == 186  # given
    assert sum(g_fast(n) for n in range(3, 501)) == 5124  # given

    print(_total(10**7))  # 271197444
