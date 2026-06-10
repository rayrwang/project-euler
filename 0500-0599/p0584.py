"""
https://projecteuler.net/problem=584

Expected number of people entering a room until 4 of them have
birthdays within 7 days of each other, on a 365-day circular year
(answer to 8 decimals).

On a circle, "c people pairwise within w days" is the same as "some
window of w+1 consecutive days holds c birthdays" (the span of a set
with pairwise circular distance <= w is <= w). So with W = 8 and cap
3, survival after m people means every circular 8-day window holds
at most 3 birthdays, and

  E[T] = sum_(m>=0) P(T > m) = sum_m (m! / 365^m) a_m,

where a_m sums prod 1/c_i! over valid day-count vectors (the
multinomial weight). The a_m come from a circular transfer over
days: the state is the count vector of the last W-1 = 7 days
(entries summing to at most 3: 120 states), each day appending a new
count c with weight x^c / c!, tracked as polynomials in x. The
circle closes by enumerating the 120 boundary (first-7-days) states
as a tensor axis and admitting only (final state, boundary) pairs
whose concatenation passes every seam-crossing window. Counts cap
the degree at ~140, all coefficients are nonnegative (no
cancellation), and 80-bit long doubles carry ample precision for the
Borel sum sum_m a_m m!/365^m.

The two given planets are asserted: 3 within 1 day on a 10-day year
gives 5.78688636, and 3 within 7 days on a 100-day year gives
8.48967364.
"""

from math import factorial

import numpy as np


def expected(days: int, window: int, cluster: int) -> float:
    w = window
    cap = cluster - 1
    states: list[tuple[int, ...]] = []
    sidx: dict[tuple[int, ...], int] = {}

    def gen(pos: int, cur: list[int], s: int) -> None:
        if pos == w - 1:
            sidx[tuple(cur)] = len(states)
            states.append(tuple(cur))
            return
        for c in range(cap - s + 1):
            cur.append(c)
            gen(pos + 1, cur, s + c)
            cur.pop()

    gen(0, [], 0)
    n_states = len(states)
    maxm = days * cap // w + w * cap + 5
    f128 = np.longdouble
    invfact = np.array([1.0 / factorial(c) for c in range(cap + 1)], dtype=f128)
    tens = np.zeros((n_states, n_states, maxm + 1), dtype=f128)
    for b, bs in enumerate(states):
        wgt = f128(1.0)
        for c in bs:
            wgt *= invfact[c]
        tens[b, b, sum(bs)] = wgt
    for _ in range(days - (w - 1)):
        nt = np.zeros_like(tens)
        for s, st in enumerate(states):
            ssum = sum(st)
            for c in range(cap - ssum + 1):
                ns = sidx[(*st[1:], c)]
                if c == 0:
                    nt[:, ns, :] += tens[:, s, :]
                else:
                    nt[:, ns, c:] += tens[:, s, :-c] * invfact[c]
        tens = nt
    poly = np.zeros(maxm + 1, dtype=f128)
    for b, bs in enumerate(states):
        for s, st in enumerate(states):
            seq = st + bs
            if all(sum(seq[i : i + w]) <= cap for i in range(len(seq) - w + 1)):
                poly += tens[b, s, :]
    total = f128(0.0)
    term = f128(1.0)
    for m in range(maxm + 1):
        if m > 0:
            term *= f128(m) / f128(days)
        total += poly[m] * term
    return float(total)


if __name__ == "__main__":
    assert f"{expected(10, 2, 3):.8f}" == "5.78688636"  # given (WimWi)
    assert f"{expected(100, 8, 3):.8f}" == "8.48967364"  # given (Joka)

    print(f"{expected(365, 8, 4):.8f}")  # 32.83822408
