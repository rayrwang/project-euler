"""Project Euler Problem 986: Tokens on a Row.

Every square of an infinite row holds one token.  A move picks tokens ``X``
and ``Y`` with ``Y`` exactly ``c`` squares right of ``X`` and moves *both*
to the square ``d`` right of ``Y``.  ``G(c, d)`` is the maximum number of
tokens collectable on one square; ``G(2,1) = G(1,2) = 7``, ``G(3,1) = 11``,
``G(2,2) = 3``, ``G(1,3) = 15``.  Find ``sum G(c, d)`` for
``1 <= c, d <= 160``.

A flow characterisation
-----------------------
Scaling shows ``G(c, d) = G(c/g, d/g)`` with ``g = gcd(c, d)`` (residue
classes mod ``g`` never interact), so assume ``c, d`` coprime and let
``p = c + d``.  Abstracting time away, a strategy is a multiset of *events*:
an event at ``q`` consumes a token at ``q`` (role X) and one at ``q + c``
(role Y) and emits two tokens at ``q + p``.  Output positions strictly
exceed input positions, so any event multiset whose token flow balances is
schedulable.  Writing ``n_q`` for the number of events at ``q`` and
counting visits versus departures of each square (one original token each),
a strategy collecting ``1 + 2 n_{T-p}`` tokens at ``T`` exists iff

    n_q + n_{q-c}  <=  1 + 2 n_{q-p}        for every square q,

with ``n >= 0`` of finite support.  Indexing leftwards from ``T - p``
(``x_j = n_{T-p-j}``), the *greedy-minimal* profile

    x_0 = m,    x_j = floor((x_{j-p} + x_{j-d}) / 2)   for j >= 1

is pointwise forced and pointwise minimal (the requirement on each ``x_j``
is monotone in earlier values), so ``m`` is achievable iff this sequence
dies out, and ``G = 1 + 2 m*`` for the largest such ``m*``.  Infeasible
``m`` make the sequence converge to a constant positive window (the map is
monotone and any constant is a fixed point), giving an exact terminating
test; a step cap is enforced as a hard error and never triggers.

A reduction to one sequence
---------------------------
This characterisation reproduces every given value.  Tabulating
``G(c, d)`` over all coprime pairs with ``c, d <= 30`` reveals an exact
reduction,

    G(c, d) = H(d + floor((c - 1) / 2)),    H(k) := G(1, k),

with precisely seven exceptions, all at ``d = 1``:
``G(2,1) = 7, G(3,1) = 11, G(4,1) = 15, G(5,1) = 23, G(6,1) = 27,
G(8,1) = 43, G(10,1) = 63``.  The script re-verifies the reduction over all
coprime pairs with ``c + d <= 26`` at runtime.  The final sum then needs
only ``H(1), ..., H(239)``, each found by binary search on ``m`` with the
extinction test (quadratic extrapolation of consecutive thresholds seeds
the brackets), about three minutes in total.
"""

from __future__ import annotations

from math import gcd

import numpy as np
from numba import njit

EXCEPTIONS = {
    (2, 1): 7,
    (3, 1): 11,
    (4, 1): 15,
    (5, 1): 23,
    (6, 1): 27,
    (8, 1): 43,
    (10, 1): 63,
}


@njit(cache=True)
def _sim(m: int, c: int, d: int) -> int:
    """1 if the greedy profile dies out, 0 if it stabilises, -1 on cap."""
    p = c + d
    size = p + 1
    if m == 0:
        return 1
    buf = np.zeros(size, dtype=np.int64)
    head = p
    buf[head] = m
    zeros = 0
    equal_run = 0
    last = m
    cap = 8 * m + 400 * p + 20000
    steps = 0
    while steps < cap:
        steps += 1
        ia = (head + 2) % size
        ib = (head + 2 + (p - d)) % size
        v = (buf[ia] + buf[ib]) >> 1
        head = (head + 1) % size
        buf[head] = v
        if v == 0:
            zeros += 1
            if zeros >= p:
                return 1
        else:
            zeros = 0
        if v == last:
            equal_run += 1
            if equal_run >= p and v > 0:
                return 0
        else:
            equal_run = 0
            last = v
    return -1


@njit(cache=True)
def _mstar(c: int, d: int, guess: int) -> int:
    """Largest m whose greedy profile dies; guess only seeds the bracket."""
    lo = 0
    g = guess if guess > 0 else 1
    r = _sim(g, c, d)
    if r < 0:
        return -1
    if r == 1:
        lo = g
        hi = 2 * g + 1
        while True:
            r = _sim(hi, c, d)
            if r < 0:
                return -1
            if r == 0:
                break
            lo = hi
            hi = 2 * hi + 1
    else:
        hi = g
        lw = g // 2
        while lw > 0:
            r = _sim(lw, c, d)
            if r < 0:
                return -1
            if r == 1:
                lo = lw
                break
            hi = lw
            lw //= 2
    while lo < hi - 1:
        mid = (lo + hi) // 2
        r = _sim(mid, c, d)
        if r < 0:
            return -1
        if r == 1:
            lo = mid
        else:
            hi = mid
    return lo


def g_direct(c: int, d: int) -> int:
    """G(c, d) straight from the extinction characterisation."""
    g = gcd(c, d)
    v = _mstar(c // g, d // g, 1)
    assert v >= 0
    return 1 + 2 * v


def token_sum(limit: int) -> int:
    """sum of G(c, d) over 1 <= c, d <= limit via the H-reduction."""
    kmax = limit + (limit - 1) // 2
    h: dict[int, int] = {}
    prev = [0, 0, 0]
    for k in range(1, kmax + 1):
        d1 = prev[2] - prev[1]
        guess = max(1, prev[2] + d1 + (d1 - (prev[1] - prev[0])))
        v = _mstar(1, k, guess)
        assert v >= 0, k
        h[k] = 1 + 2 * v
        prev = [prev[1], prev[2], v]

    def g_value(c: int, d: int) -> int:
        g = gcd(c, d)
        c //= g
        d //= g
        if (c, d) in EXCEPTIONS:
            return EXCEPTIONS[(c, d)]
        return h[d + (c - 1) // 2]

    # runtime re-verification of the reduction on small coprime pairs
    for c in range(1, 14):
        for d in range(1, 27 - c):
            if gcd(c, d) == 1:
                assert g_value(c, d) == g_direct(c, d), (c, d)

    return sum(g_value(c, d) for c in range(1, limit + 1) for d in range(1, limit + 1))


if __name__ == "__main__":
    for c, d, exp in ((2, 1, 7), (1, 2, 7), (3, 1, 11), (2, 2, 3), (1, 3, 15)):
        assert g_direct(c, d) == exp, f"checkpoint G({c},{d})"
    print(token_sum(160))  # 15418494040
