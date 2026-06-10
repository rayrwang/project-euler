"""Project Euler Problem 990: Addition Equations.

An *addition equation* is a string ``x_1+...+x_k = y_1+...+y_m`` of positive
integers without leading zeros (one ``=``, a ``+`` between adjacent
integers) whose two sides have equal sums.  ``A(n)`` counts such strings of
length at most ``n``; given ``A(3) = 9``, ``A(5) = 171``, ``A(7) = 4878``,
find ``A(50) mod 10^9 + 7``.

Column dynamic programming
--------------------------
The numbers can be up to 48 digits long, so the sums cannot be enumerated --
but equality of sums can be *verified column by column*.  Align every number
at its units digit and scan columns from least significant to most
significant.  In each column, every still-active term contributes one digit;
a term whose most significant digit lies in this column contributes a digit
``1..9`` and then retires, while continuing terms contribute ``0..9``.
Writing ``s_A, s_B`` for the column digit sums of the two sides and ``c``
for the running borrow/carry of ``sum(A) - sum(B)``,

    s_A - s_B + c  must be divisible by 10,   c' = (s_A - s_B + c) / 10,

and the equation holds iff after all terms retire the carry is zero.

The DP state is ``(a_A, a_B, c, R)``: the number of active terms on each
side, the carry, and the remaining length budget (each column consumes
``a_A + a_B`` characters; the ``k_A + k_B - 1`` separators and the ``=`` are
charged up front, so every initial term count pair ``(k_A, k_B)`` seeds one
start state).  A column transition picks how many terms retire on each side
(``binom(a, t)`` ways to choose which, since active terms are exchangeable)
and weights the carry transition by the number of digit assignments with the
required column-sum difference -- precomputed as the coefficient lists of
``(1 + x + ... + x^9)^cont (x + ... + x^9)^t`` cross-correlated between the
two sides.  Since the total length is at most 50, there are at most 25 terms
overall and carries stay within ``+-25``; the state space is tiny.

A string of length below ``n`` simply leaves budget unspent, so terminal
states (no active terms, zero carry) are accumulated directly, giving
``A(n)`` in one pass.  The DP reproduces all three given checkpoints, which
were additionally confirmed by an independent brute-force enumeration of
integer sequences.
"""

from __future__ import annotations

from collections import defaultdict
from math import comb

MOD = 10**9 + 7


def count_equations(n: int, mod: int = MOD) -> int:
    """A(n): addition-equation strings of length <= n, mod `mod`."""
    maxterms = (n + 1) // 2
    polycache: dict[tuple[int, int], list[int]] = {}

    def poly(cont: int, t: int) -> list[int]:
        """Digit-sum distribution of `cont` digits 0-9 and `t` digits 1-9."""
        key = (cont, t)
        if key in polycache:
            return polycache[key]
        p = [1]
        for lo in (0,) * cont + (1,) * t:
            q = [0] * (len(p) + 9)
            for i, v in enumerate(p):
                if v:
                    for d in range(lo, 10):
                        q[i + d] += v
            p = q
        polycache[key] = p
        return p

    lagcache: dict[tuple[int, int, int, int], dict[int, int]] = {}

    def lags(c_a: int, t_a: int, c_b: int, t_b: int) -> dict[int, int]:
        """Weight of each column-sum difference s_A - s_B."""
        key = (c_a, t_a, c_b, t_b)
        if key in lagcache:
            return lagcache[key]
        pa, pb = poly(c_a, t_a), poly(c_b, t_b)
        out: dict[int, int] = defaultdict(int)
        for sa, va in enumerate(pa):
            if va:
                for sb, vb in enumerate(pb):
                    if vb:
                        out[sa - sb] += va * vb
        lagcache[key] = dict(out)
        return lagcache[key]

    cur: dict[tuple[int, int, int, int], int] = defaultdict(int)
    for k_a in range(1, maxterms + 1):
        for k_b in range(1, maxterms + 1):
            budget = n - (k_a + k_b - 1)
            if budget >= k_a + k_b:
                cur[(k_a, k_b, 0, budget)] += 1
    answer = 0
    while cur:
        nxt: dict[tuple[int, int, int, int], int] = defaultdict(int)
        for (a_a, a_b, c, budget), cnt in cur.items():
            cost = a_a + a_b
            if budget < cost:
                continue
            left = budget - cost
            for t_a in range(a_a + 1):
                w_a = comb(a_a, t_a)
                for t_b in range(a_b + 1):
                    w0 = w_a * comb(a_b, t_b) % mod
                    for lag, wt in lags(a_a - t_a, t_a, a_b - t_b, t_b).items():
                        tot = lag + c
                        if tot % 10:
                            continue
                        c2 = tot // 10
                        n_a, n_b = a_a - t_a, a_b - t_b
                        w = cnt * w0 % mod * (wt % mod) % mod
                        if n_a == 0 and n_b == 0:
                            if c2 == 0:
                                answer = (answer + w) % mod
                        elif left >= n_a + n_b:
                            nxt[(n_a, n_b, c2, left)] = (
                                nxt[(n_a, n_b, c2, left)] + w
                            ) % mod
        cur = nxt
    return answer


if __name__ == "__main__":
    assert count_equations(3) == 9, "checkpoint A(3)"
    assert count_equations(5) == 171, "checkpoint A(5)"
    assert count_equations(7) == 4878, "checkpoint A(7)"
    print(count_equations(50))  # 50322750
