"""Project Euler Problem 993: Banana Beaver.

A beaver starts at position 0 of an integer line carrying ``N`` bananas; at
each step it inspects positions ``x`` and ``x + 1`` (cells may hold several
bananas):

* bananas at both: pick one up from ``x + 1``, move to ``x - 1``;
* banana only at ``x``: pick it up, move to ``x + 2``;
* banana only at ``x + 1``: shift it to ``x``, move to ``x + 2``;
* neither: drop one banana on each of ``x - 1, x, x + 1`` and move to
  ``x - 2`` if at least three are carried, else the game ends.

``BB(N)`` is the final position; ``BB(1000) = 1499``.  Find ``BB(10^18)``.

One trajectory serves every N
-----------------------------
Only the *fourth* rule consults the carried count, and only through the
test ``carry >= 3``.  Two beavers whose loads differ by a constant therefore
walk the identical trajectory until the lighter one dies.  Running a single
simulation with an unbounded load and tracking ``spent`` (three per drop,
minus one per pickup), the beaver with initial load ``N`` ends at the *first*
rule-4 event where ``spent in {N - 2, N - 1, N}``, at that event's position.
One linear-time pass thus yields ``BB(N)`` for every ``N`` up to a bound
simultaneously; the pass reproduces ``BB(1000) = 1499`` and agrees with
independent single-``N`` simulations at random checkpoints.

Eventual linearity
------------------
The banana field organises itself into a quasi-periodic word swept by the
beaver in self-similar cycles, and the residual
``E(N) = 118 N - 71 BB(N)`` turns out to be *exactly periodic*:

    BB(N + 71) = BB(N) + 118        for all N >= 514,

verified for the entire simulated range ``514 <= N <= 10^6`` (close to
14000 full periods, with no exception after the pre-period).  Hence for
large ``N``, fold back to the stored window:
``BB(N) = BB(r) + 118 (N - r) / 71`` with ``r = 514 + (N - 514) mod 71``.
"""

from __future__ import annotations

import numpy as np
from numba import njit

PERIOD = 71
STEP = 118
PRE = 514


@njit(cache=True)
def _bb_single(N: int, span: int) -> int:
    """Direct simulation of one beaver (for cross-checks)."""
    cells = np.zeros(span, dtype=np.int16)
    off = span // 2
    x = off
    carry = N
    while True:
        a = cells[x] > 0
        b = cells[x + 1] > 0
        if a and b:
            cells[x + 1] -= 1
            carry += 1
            x -= 1
        elif a:
            cells[x] -= 1
            carry += 1
            x += 2
        elif b:
            cells[x + 1] -= 1
            cells[x] += 1
            x += 2
        elif carry >= 3:
            carry -= 3
            cells[x - 1] += 1
            cells[x] += 1
            cells[x + 1] += 1
            x -= 2
        else:
            return x - off


@njit(cache=True)
def _bb_all(n_max: int, span: int) -> np.ndarray:
    """BB(1..n_max) from a single shared unbounded-load trajectory."""
    out = np.full(n_max + 1, np.int64(-(10**15)), dtype=np.int64)
    cells = np.zeros(span, dtype=np.int16)
    off = span // 2
    x = off
    spent = 0
    remaining = n_max
    while remaining > 0:
        a = cells[x] > 0
        b = cells[x + 1] > 0
        if a and b:
            cells[x + 1] -= 1
            spent -= 1
            x -= 1
        elif a:
            cells[x] -= 1
            spent -= 1
            x += 2
        elif b:
            cells[x + 1] -= 1
            cells[x] += 1
            x += 2
        else:
            lo = spent if spent > 1 else 1
            for N in range(lo, spent + 3):
                if N <= n_max and out[N] == -(10**15):
                    out[N] = x - off
                    remaining -= 1
            spent += 3
            cells[x - 1] += 1
            cells[x] += 1
            cells[x + 1] += 1
            x -= 2
    return out[1:]


def banana_beaver(n: int) -> int:
    """BB(n) for any n, via the verified period-71 linear recurrence."""
    n_max = 1_000_000
    table = _bb_all(n_max, 8 * n_max)
    # verify the recurrence BB(N + 71) = BB(N) + 118 on the whole tail
    tail = table[PRE - 1 :]
    assert (tail[PERIOD:] - tail[:-PERIOD] == STEP).all(), "period check"
    if n <= n_max:
        return int(table[n - 1])
    r = PRE + (n - PRE) % PERIOD
    return int(table[r - 1]) + STEP * ((n - r) // PERIOD)


if __name__ == "__main__":
    assert _bb_single(1000, 100_000) == 1499, "checkpoint BB(1000) direct"
    assert banana_beaver(1000) == 1499, "checkpoint BB(1000)"
    for n in (3, 57, 1234, 99991):  # cross-check shared pass vs direct sim
        assert banana_beaver(n) == _bb_single(n, 2_000_000), n
    print(banana_beaver(10**18))  # 1661971830985915304
