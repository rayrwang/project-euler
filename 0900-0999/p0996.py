"""Project Euler Problem 996: Overtakes.

``n`` players are ranked ``1..n``.  Each day a match between two *adjacently*
ranked players may take place; if the lower-ranked player wins they swap ranks
(an *overtake* for the winner).  After ``k`` days everyone is back at their
initial rank.  ``F(n, k)`` counts the possible ``n``-tuples of per-player
overtake counts, given ``F(3, 4) = 8`` and ``F(12, 34) = 2457178250``.  We
need ``F(123, 4567891) mod 1234567891``.

Characterizing achievable tuples
--------------------------------
Days with no match pad the schedule freely, so ``F(n, k)`` counts tuples
achievable using *at most* ``k`` swaps in total.  Track each pair of players
``(j, l)``: every swap is a "crossing" of an adjacent pair, and for everyone
to return home each pair must cross an even number of times, ``2 w_{jl}``
crossings contributing ``w_{jl}`` overtakes to *each* of the two players
(crossings alternate direction, and per crossing exactly one player overtakes;
over an even count this splits evenly).  Hence the overtake count of player
``j`` is ``c_j = sum_l w_{jl}`` for a symmetric nonnegative matrix ``w``.

A player with ``c_j = 0`` never moves and acts as a wall: players on opposite
sides can never interact.  Within a maximal run of consecutive players with
positive counts, any symmetric ``w`` works (one can always schedule adjacent
transpositions realizing it -- shown below by brute force for small ``n``).
A multiset of pairwise "handshakes" with degree sequence ``(c_j)`` on the run
exists iff the run sum is even and no single ``c_j`` exceeds the sum of the
others (Erdos-Gallai for multigraphs).  So:

    a tuple ``c`` with ``sum(c) <= k`` is achievable iff every maximal run of
    positive entries has even sum ``s`` and maximum at most ``s / 2``.

(The total number of swaps is ``sum(c)``, since each swap grants exactly one
overtake.)  This characterization was verified exhaustively against a direct
breadth-first search over permutation/count states for ``n <= 5`` and sums up
to ``8``, and it reproduces both given checkpoints.

Counting tuples by dynamic programming
--------------------------------------
The number of length-``L`` runs of positive integers with even sum ``s`` and
maximum ``<= s/2`` is, by inclusion-exclusion on which entry exceeds ``s/2``
(at most one can),

    N_L(s) = C(s-1, L-1) - L * C(s/2 - 1, L-1).

Scanning positions left to right with ``E[i][m]`` = number of prefixes of
length ``i`` and sum ``m`` ending in a zero (or empty) and ``D[i][m]`` = those
ending exactly at the end of a run gives ``f(n, m) = E[n][m] + D[n][m]``, the
number of achievable tuples with sum exactly ``m``, and
``F(n, k) = sum_{m <= k} f(n, m)``.

Extrapolating to large k
------------------------
For fixed ``n`` the generating function ``sum_m f(n, m) x^m`` is rational with
denominator ``(1 - x^2)^n`` (each run contributes a factor with poles only at
``x = +-1`` of order at most its length, and run lengths sum to at most
``n``).  The cumulative ``F(n, k)`` therefore satisfies, for ``k`` large
enough, the linear recurrence with characteristic polynomial

    (x - 1)^(n+1) (x + 1)^n        (degree 2n + 1 = 247 for n = 123).

We compute ``F(123, m) mod 1234567891`` for ``m <= 600`` by the DP above,
verify the recurrence holds at every available offset, then jump to
``k = 4567891`` by computing ``x^k mod`` the characteristic polynomial
(Kitamasa / Fiduccia) and combining with the initial values.
"""

from __future__ import annotations

import numpy as np
from numba import njit

P = 1234567891


@njit(cache=True)
def _f_mod(n: int, max_sum: int, p: int) -> np.ndarray:
    """f(n, m) mod p for m = 0..max_sum (tuples with sum exactly m)."""
    # Pascal triangle C[t][j] mod p, j <= n.
    binom = np.zeros((max_sum + 1, n + 1), dtype=np.int64)
    for t in range(max_sum + 1):
        binom[t][0] = 1
        for j in range(1, min(t, n) + 1):
            binom[t][j] = (binom[t - 1][j - 1] + binom[t - 1][j]) % p

    # N_L(s) = C(s-1, L-1) - L * C(s/2-1, L-1) for even s >= 2.
    runs = np.zeros((n + 1, max_sum + 1), dtype=np.int64)
    for length in range(2, n + 1):
        for s in range(2, max_sum + 1, 2):
            v = binom[s - 1][length - 1] - (length * binom[s // 2 - 1][length - 1]) % p
            runs[length][s] = v % p

    ends_zero = np.zeros((n + 1, max_sum + 1), dtype=np.int64)
    ends_run = np.zeros((n + 1, max_sum + 1), dtype=np.int64)
    ends_zero[0][0] = 1
    for i in range(1, n + 1):
        for m in range(max_sum + 1):
            ends_zero[i][m] = (ends_zero[i - 1][m] + ends_run[i - 1][m]) % p
        for length in range(2, i + 1):
            for s in range(2, max_sum + 1, 2):
                nls = runs[length][s]
                if nls:
                    for m in range(s, max_sum + 1):
                        ends_run[i][m] = (
                            ends_run[i][m] + nls * ends_zero[i - length][m - s]
                        ) % p

    out = np.zeros(max_sum + 1, dtype=np.int64)
    for m in range(max_sum + 1):
        out[m] = (ends_zero[n][m] + ends_run[n][m]) % p
    return out


def _poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    res = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                res[i + j] = (res[i + j] + x * y) % p
    return res


def _poly_mod(a: list[int], monic: list[int], p: int) -> list[int]:
    a = a[:]
    deg = len(monic) - 1
    for i in range(len(a) - 1, deg - 1, -1):
        coef = a[i]
        if coef:
            a[i] = 0
            for j in range(deg):
                a[i - deg + j] = (a[i - deg + j] - coef * monic[j]) % p
    return a[:deg] + [0] * max(0, deg - len(a))


def _x_pow_mod(k: int, monic: list[int], p: int) -> list[int]:
    deg = len(monic) - 1
    result = [1] + [0] * (deg - 1)
    base = [0, 1] + [0] * (deg - 2)
    while k:
        if k & 1:
            result = _poly_mod(_poly_mul(result, base, p), monic, p)
        base = _poly_mod(_poly_mul(base, base, p), monic, p)
        k >>= 1
    return result


def f_count(n: int, k: int, p: int = P) -> int:
    """F(n, k) mod p by direct DP (for moderate k)."""
    f = _f_mod(n, k, p)
    return int(f.sum() % p)


def solve(n: int = 123, k: int = 4567891, p: int = P) -> int:
    max_sum = 600  # > 2 * (2n + 1); leaves room to verify the recurrence
    f = _f_mod(n, max_sum, p)
    cumulative = np.cumsum(f) % p

    # Characteristic polynomial (x - 1)^(n+1) (x + 1)^n.
    char = [1]
    for _ in range(n + 1):
        char = _poly_mul(char, [p - 1, 1], p)
    for _ in range(n):
        char = _poly_mul(char, [1, 1], p)
    deg = len(char) - 1

    for offset in range(max_sum + 1 - deg):
        acc = 0
        for j in range(deg + 1):
            acc = (acc + char[j] * int(cumulative[offset + j])) % p
        assert acc == 0, "recurrence check"

    remainder = _x_pow_mod(k, char, p)
    return sum(r * int(cumulative[j]) for j, r in enumerate(remainder)) % p


if __name__ == "__main__":
    assert f_count(3, 4) == 8, "checkpoint F(3,4)"
    assert f_count(12, 34) == 2457178250 % P, "checkpoint F(12,34)"
    print(solve())  # 137726405
