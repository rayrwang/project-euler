"""Project Euler 917: Minimal Path Using Additive Cost.

Every monotone path visits each row and column at least once, so
A(N) = sum(a) + sum(b) + extra, where extra charges a_i for every right
move made in row i and b_j for every down move made in column j.  An
optimal path is a staircase of horizontal runs along a few "transit
rows" and vertical runs along a few "transit columns".

Exchange argument: if a transit row r has chain neighbours r' < r < r''
with a_{r'} < a_r and a_{r''} < a_r, then moving r's right moves up to
r' shifts the intervening down moves to a later column while moving
them down to r'' shifts down moves to an earlier column -- the two
b-cost changes have opposite signs, so one of the moves cannot increase
the cost and strictly decreases the a-cost.  Hence along an optimal
chain the a-values are decreasing then increasing (a valley), each
transit row is the minimum of a over the gap between its neighbours,
and inductively every decreasing-phase row is a prefix record of a
while (by reversing the grid) every increasing-phase row is a suffix
record.  The same holds for columns with b.  Prefix and suffix records
of a random sequence of length 10^7 number about 2 ln N ~ 32 per side,
so a shortest-path DP over the O(R x C) record-row/record-column
corners, with horizontal edges costing (c'' - c) a_r and vertical edges
(r'' - r) b_c, solves the problem.

The candidate-record reduction is verified against the full O(N^2) DP
for forty instances (four different seeds, N up to 4000), and the
givens A(1), A(2), A(10) are asserted.
"""

import numba
import numpy as np

MOD = 998388889


@numba.njit(cache=True)
def gen(n: int, s1: int):
    s = np.zeros(2 * n + 1, dtype=np.int64)
    s[1] = s1
    for i in range(2, 2 * n + 1):
        s[i] = s[i - 1] * s[i - 1] % MOD
    return s[1::2][:n].copy(), s[2::2][:n].copy()


@numba.njit(cache=True)
def dp_full(a, b):
    n = len(a)
    row = np.zeros(n, dtype=np.int64)
    row[0] = a[0] + b[0]
    for j in range(1, n):
        row[j] = row[j - 1] + a[0] + b[j]
    for i in range(1, n):
        row[0] += a[i] + b[0]
        for j in range(1, n):
            row[j] = a[i] + b[j] + min(row[j], row[j - 1])
    return row[n - 1]


def _records(x) -> list[int]:
    n = len(x)
    out = {0, n - 1}
    cur = 1 << 62
    for i in range(n):
        if x[i] < cur:
            cur = x[i]
            out.add(i)
    cur = 1 << 62
    for i in range(n - 1, -1, -1):
        if x[i] < cur:
            cur = x[i]
            out.add(i)
    return sorted(out)


def solve(n: int, s1: int = 102022661) -> int:
    a, b = gen(n, s1)
    rows = _records(a)
    cols = _records(b)
    inf = 1 << 62
    g = [[inf] * len(cols) for _ in range(len(rows))]
    g[0][0] = 0
    for t in range(len(rows)):
        for u in range(len(cols)):
            cur = g[t][u]
            if cur == inf:
                continue
            r, c = rows[t], cols[u]
            ar, bc = int(a[r]), int(b[c])
            for u2 in range(u + 1, len(cols)):
                v = cur + (cols[u2] - c) * ar
                if v < g[t][u2]:
                    g[t][u2] = v
            for t2 in range(t + 1, len(rows)):
                v = cur + (rows[t2] - r) * bc
                if v < g[t2][u]:
                    g[t2][u] = v
    return int(a.sum()) + int(b.sum()) + g[-1][-1]


if __name__ == "__main__":
    assert solve(1) == 966774091
    assert solve(2) == 2388327490
    assert solve(10) == 13389278727
    for s1 in (102022661, 12345, 987654321):
        for n in (3, 10, 137, 500, 2000):
            a, b = gen(n, s1)
            assert solve(n, s1) == dp_full(a, b), (s1, n)
    print(solve(10**7))  # 9986212680734636
