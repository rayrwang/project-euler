"""Project Euler Problem 973: Pile Game.

``n`` cards start as ``n`` single-card piles.  Each round picks a pile
uniformly at random, then a second pile uniformly among the rest; the top
card of the picked pile moves onto the second pile and the remaining
cards are dealt out as new singleton piles.  After every round the score
is the bitwise XOR of all pile sizes, and the game ends when one pile
holds all ``n`` cards.  ``X(n)`` is the expected total score;
``X(2) = 2``, ``X(4) = 14``, ``X(10) = 1418``.  Find ``X(10^4)`` modulo
10^9 + 7.

Expected visits have a closed form
----------------------------------
The chain lives on partitions of n.  Writing a state as its non-singleton
parts ``a_1 >= ... >= a_r >= 2`` plus ``m`` singletons, solving
``nu = delta_start + P^T nu`` exactly for small n reveals that the
expected number of times each state is *entered* is the multinomial

    nu(s) = (m + r)! / ( m! * prod_v mult_v! ),

the number of distinct arrangements of the multiset of non-singleton
parts and ``m`` indistinguishable blanks (verified exactly against the
linear system for all n <= 7 at runtime for n = 6).  Since every round
enters a state and the initial deal is not a round,
``X(n) = sum_s nu(s) score(s)`` over states with ``r >= 1``.

Generating functions
--------------------
Summing a function over partitions weighted by nu equals summing it over
*ordered* tuples of parts with weight ``C(m + r, r)``, since ordered
tuples count each multiset ``r!/prod mult!`` times.  With
``sum_m C(m+r, r) x^m = (1-x)^{-(r+1)}``, the totals become geometric
series in ``g(x)^r``.  The plain total uses ``g(x) = x^2/(1-x)`` and
collapses to ``sum_s nu(s) = [x^n] x^2 / ((1-x)(1-2x)) = 2^{n-1} - 1``.
For bit ``b`` of the score (the parity of parts with bit b set, XORed
with the parity of m when b = 0), the signed series

    U_b = [x^n]  g_-(x) / ( (1-wx) (1-wx-g_-(x)) ),

with ``g_-(x) = sum_{a>=2} (-1)^{bit_b(a)} x^a`` and ``w = -1`` exactly
for b = 0, gives ``sum_s nu(s) (-1)^{score bit}``.  For b = 0 everything
telescopes to ``U_0 = (-1)^n (2^{n-1} - 1)`` -- the score parity is just
n mod 2.  Hence

    X(n) = sum_b 2^b ( T - U_b ) / 2,    T = 2^{n-1} - 1,

with each remaining ``U_b`` computed by an O(n^2) power-series inversion
modulo the prime.  The pipeline reproduces the exact partition-system
values for n = 2, 4, 7, 10 (including all given checkpoints).
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import factorial

import numpy as np
from numba import njit

P = 10**9 + 7


def _partitions(n: int) -> list[tuple]:
    def gen(left: int, mx: int):
        if left == 0:
            yield ()
            return
        for k in range(min(left, mx), 0, -1):
            for rest in gen(left - k, k):
                yield (k,) + rest

    return list(gen(n, n))


def _transitions(state: tuple) -> dict[tuple, Fraction]:
    m = len(state)
    out: dict[tuple, Fraction] = {}
    for i in range(m):
        k = state[i]
        rest = state[:i] + state[i + 1 :]
        for j in range(m - 1):
            q = rest[j]
            new = list(rest[:j] + rest[j + 1 :]) + [q + 1] + [1] * (k - 1)
            ns = tuple(sorted(new, reverse=True))
            out[ns] = out.get(ns, Fraction(0)) + Fraction(1, m * (m - 1))
    return out


def _solve(n: int, visit_mode: bool):
    """Exact h(start) (expected total score) or entry counts nu."""
    states = _partitions(n)
    idx = {s: i for i, s in enumerate(states)}
    nn = len(states)
    final = (n,)
    start = tuple([1] * n)
    a = [[Fraction(0)] * nn for _ in range(nn)]
    b = [Fraction(0)] * nn
    for s in states:
        a[idx[s]][idx[s]] = Fraction(1)
    for s in states:
        if s == final:
            continue
        i = idx[s]
        for ns, p in _transitions(s).items():
            if visit_mode:
                a[idx[ns]][i] -= p
            else:
                a[i][idx[ns]] -= p
                b[i] += p * _score(ns)
    if visit_mode:
        b[idx[start]] = Fraction(1)
    for col in range(nn):
        piv = next(r for r in range(col, nn) if a[r][col] != 0)
        a[col], a[piv] = a[piv], a[col]
        b[col], b[piv] = b[piv], b[col]
        inv = 1 / a[col][col]
        a[col] = [x * inv for x in a[col]]
        b[col] *= inv
        for r in range(nn):
            if r != col and a[r][col] != 0:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
                b[r] -= f * b[col]
    if visit_mode:
        return {s: b[idx[s]] for s in states}
    return b[idx[start]]


def _score(state: tuple) -> int:
    x = 0
    for v in state:
        x ^= v
    return x


def _nu_formula(s: tuple) -> Fraction:
    parts = [v for v in s if v >= 2]
    m = len(s) - len(parts)
    r = len(parts)
    v = factorial(m + r) // factorial(m)
    for c in Counter(parts).values():
        v //= factorial(c)
    return Fraction(v)


@njit(cache=True)
def _u_bit(n: int, b: int, p: int) -> int:
    g = np.zeros(n + 1, dtype=np.int64)
    for a in range(2, n + 1):
        g[a] = p - 1 if (a >> b) & 1 else 1
    inv_a = np.zeros(n + 1, dtype=np.int64)
    inv_a[0] = 1
    for k in range(1, n + 1):
        s = (p - 1) * inv_a[k - 1] % p
        for j in range(2, k + 1):
            if g[j]:
                s += (p - g[j]) * inv_a[k - j] % p
        inv_a[k] = (p - s % p) % p
    tot = 0
    for k in range(2, n + 1):
        ck = 0
        for a in range(2, k + 1):
            if g[a]:
                ck += g[a] * inv_a[k - a] % p
        tot = (tot + ck) % p
    return tot % p


def x_mod(n: int) -> int:
    t = (pow(2, n - 1, P) - 1) % P
    total = 0
    for b in range(n.bit_length()):
        if b == 0:
            u = t if n % 2 == 0 else (P - t) % P
        else:
            u = _u_bit(n, b, P)
        total = (total + pow(2, b, P) * ((t - u) % P)) % P
    return total * pow(2, P - 2, P) % P


if __name__ == "__main__":
    nu = _solve(6, visit_mode=True)
    assert all(nu[s] == _nu_formula(s) for s in nu), "nu closed form"
    exact = {m: _solve(m, visit_mode=False) for m in (2, 4, 7, 10)}
    assert exact[2] == 2 and exact[4] == 14 and exact[10] == 1418, "given checkpoints"
    for m, v in exact.items():
        assert v.denominator == 1 and x_mod(m) == v % P, m
    print(x_mod(10**4))  # 427278142
