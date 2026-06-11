"""Project Euler Problem 976: A Grand Drawing Game.

X and O alternately (X first) draw their own symbol in red or blue on k
strips of lengths n_1 <= ... <= n_k.  Adjacent squares of a strip must
differ in both symbol and colour; while any strip is still blank, the move
must open a blank strip; a player with no valid move loses.  ``P(K, N)``
counts the tuples with ``k <= K``, ``n_i <= N`` for which X wins;
``P(2,4) = 7`` and ``P(5,10) = 901``.  Find ``P(10^7, 10^7)`` mod
1234567891.

The winning rule
----------------
The four cell states split into two compatibility classes {Xr, Ob} and
{Xb, Or}: adjacent filled cells are opposite members of one class, so the
game is symmetric under (X <-> O, r <-> b).  A memoised solver over
multisets of strip states (canonicalised up to reversal, strip order and
the global colour swap) shows that the outcome depends only on a residue
computation:

* cancel pairs of strips of equal length, and pairs of odd lengths
  congruent mod 4;
* let ``E`` be the number of remaining even lengths and ``O1, O3`` the
  parities of remaining lengths ``= 1, 3 (mod 4)``;
* X wins iff ``r = E + O1 + O3`` is even and nonzero, or ``r = 1`` with
  the single residue ``= 1 (mod 4)`` (i.e. ``E = 0, O1 = 1, O3 = 0``).

The rule reproduces the solver on every game with ``k <= 3, n <= 6`` and
``k <= 4, n <= 5`` (checked at runtime on a smaller sample), and gives
``P(2,4) = 7`` and ``P(5,10) = 901`` exactly.

Counting
--------
Group the values 1..N into evens (``mE = N/2`` of them) and odd residue
classes mod 4 (``m = N/4`` each, N divisible by 4).  In the generating
function over the multiset size, a value contributes ``1/(1-x^2)`` for an
even multiplicity and ``x/(1-x^2)`` for odd.  Splitting by the parity of
the number of odd-multiplicity values in each class and simplifying (the
two odd classes have equal size, so the cross terms cancel),

    W(x) = 1/2 [ (1-x)^-N + (1+x)^-N ]
         - 1/2 (1-x)^-mE (1+x)^-N  -  1/2 (1-x^2)^-(mE+m),

whose ``x^0`` coefficient vanishes as it must.  The answer is
``[x^K] W(x)/(1-x)``, a sum of four coefficients of
``(1-x)^-a (1+x)^-b``; each satisfies the order-2 recurrence
``(k+1) c_{k+1} = (a-b) c_k + (a+b+k-1) c_{k-1}`` (from
``(1-x^2) f' = ((a-b)+(a+b)x) f``), evaluated mod the prime 1234567891 in
O(K) with a batch inverse table.  The closed form is cross-checked against
a direct rule count for (K,N) = (6,8) and (7,12).
"""

from __future__ import annotations

import sys
from collections import Counter
from itertools import combinations_with_replacement as cwr

import numpy as np
from numba import njit

MOD = 1234567891
COMPAT = {(1, 2), (2, 1), (3, 4), (4, 3)}  # Xr=1 Ob=2 Xb=3 Or=4
X_STATES = (1, 3)
O_STATES = (2, 4)


def _swap_colors(s: tuple) -> tuple:
    m = {0: 0, 1: 3, 3: 1, 2: 4, 4: 2}
    return tuple(m[c] for c in s)


def _canon(strips: tuple, turn: int) -> tuple:
    a = tuple(sorted(min(s, s[::-1]) for s in strips))
    b = tuple(sorted(min(t := _swap_colors(s), t[::-1]) for s in strips))
    return (min(a, b), turn)


_memo: dict = {}


def _win(strips: tuple, turn: int) -> bool:
    key = _canon(strips, turn)
    if key in _memo:
        return _memo[key]
    my = X_STATES if turn == 0 else O_STATES
    any_blank = any(all(c == 0 for c in s) for s in strips)
    res = False
    for i, s in enumerate(strips):
        if res:
            break
        if any_blank and not all(c == 0 for c in s):
            continue
        n = len(s)
        for j in range(n):
            if s[j] != 0:
                continue
            for v in my:
                if j > 0 and s[j - 1] != 0 and (s[j - 1], v) not in COMPAT:
                    continue
                if j + 1 < n and s[j + 1] != 0 and (s[j + 1], v) not in COMPAT:
                    continue
                ns = list(strips)
                ns[i] = s[:j] + (v,) + s[j + 1 :]
                if not _win(tuple(ns), 1 - turn):
                    res = True
                    break
            if res:
                break
    _memo[key] = res
    return res


def x_wins_solver(lengths: tuple) -> bool:
    return _win(tuple((0,) * n for n in lengths), 0)


def x_wins_rule(lengths: tuple) -> bool:
    c = Counter(lengths)
    res = [v for v, mult in c.items() if mult % 2]
    o1 = sum(1 for v in res if v % 4 == 1) % 2
    o3 = sum(1 for v in res if v % 4 == 3) % 2
    e = sum(1 for v in res if v % 2 == 0)
    r = e + o1 + o3
    if r == 0:
        return False
    if r == 1:
        return e == 0 and o1 == 1
    return r % 2 == 0


@njit(cache=True)
def _coeff_k(a: int, b: int, K: int, mod: int, inv: np.ndarray) -> int:
    c0 = 1
    c1 = (a - b) % mod
    if K == 0:
        return 1
    for k in range(1, K):
        c2 = ((a - b) % mod * c1 + (a + b + k - 1) % mod * c0) % mod * inv[k + 1] % mod
        c0, c1 = c1, c2
    return c1


@njit(cache=True)
def _inv_table(K: int, mod: int) -> np.ndarray:
    inv = np.zeros(K + 2, dtype=np.int64)
    inv[1] = 1
    for i in range(2, K + 2):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod
    return inv


def p_closed_form(K: int, N: int, mod: int) -> int:
    assert N % 4 == 0
    me, m = N // 2, N // 4
    inv = _inv_table(K, mod)
    t1 = _coeff_k(N + 1, 0, K, mod, inv)
    t2 = _coeff_k(1, N, K, mod, inv)
    t3 = _coeff_k(me + 1, N, K, mod, inv)
    t4 = _coeff_k(me + m + 1, me + m, K, mod, inv)
    return (t1 + t2 - t3 - t4) % mod * pow(2, mod - 2, mod) % mod


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    # rule == solver on small games
    for k in (1, 2, 3):
        for t in cwr(range(1, 6 if k < 3 else 5), k):
            assert x_wins_solver(t) == x_wins_rule(t), t
    # given checkpoints via the rule
    assert sum(1 for k in (1, 2) for t in cwr(range(1, 5), k) if x_wins_rule(t)) == 7
    assert (
        sum(1 for k in range(1, 6) for t in cwr(range(1, 11), k) if x_wins_rule(t))
        == 901
    )
    # closed form vs direct rule count
    for kk, nn in ((6, 8), (7, 12)):
        direct = sum(
            1
            for k in range(1, kk + 1)
            for t in cwr(range(1, nn + 1), k)
            if x_wins_rule(t)
        )
        assert p_closed_form(kk, nn, MOD) == direct % MOD, (kk, nn)
    print(p_closed_form(10**7, 10**7, MOD))  # 675608326
