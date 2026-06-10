"""
https://projecteuler.net/problem=589

Two sticks repeatedly float under a bridge (journey times uniform
integers in [n, m], 5 seconds to refloat). The game ends when a
stick emerges having made one more journey than the other; E(m, n)
is the expected game duration from first drop to that emergence.
Find S(100) = sum_(m=2..100) sum_(n=1..m-1) E(m, n) to 2 decimals.

Stick A's j-th journey finishes at sum(a_(<=j)) + 5(j-1), so A laps
B at round j exactly when sum(a_(<=j)) + 5 < sum(b_(<=j-1)), i.e.
W + a <= -6 where W = sum_(i<j) (a_i - b_i); symmetrically B laps
when b <= W - 6. The two can never trigger in the same round (they
need W <= -n-6 and W >= n+6 respectively), so the game is a Markov
chain on W, which on continuing rounds stays within [-5-m, 5+m].

The ending time equals (winner's journey sum) + 5(J-1) =
sum over rounds of (winner's t_i + 5), minus 5. Each round's a
counts only if A eventually wins, so with p(W) = P(A wins from W)
(one linear solve), the expected remaining weighted time
g(W) = E[(a+5) 1_Alap + (b+5) 1_Blap
        + ((a+5) p(W') + (b+5)(1-p(W')) + g(W')) 1_cont]
is a second linear solve, and E(m, n) = g(0) - 5.

Verified against the given E(60, 30) = 1036.15 and S(5) = 7722.82,
and against a 4 * 10^5-game direct simulation of the lap rules for
(m, n) = (5, 2).
"""

import numba
import numpy as np


@numba.njit(cache=True)
def _build_p(m, n, lo, size):
    r = m - n + 1
    inv2 = 1.0 / (r * r)
    trans = np.zeros((size, size))
    pa = np.zeros(size)
    for wi in range(size):
        w = lo + wi
        for a in range(n, m + 1):
            if a <= -w - 6:
                pa[wi] += inv2 * r
                continue
            for b in range(n, m + 1):
                if b > w - 6:
                    trans[wi, w + a - b - lo] += inv2
    return trans, pa


@numba.njit(cache=True)
def _build_c0(m, n, lo, size, p):
    r = m - n + 1
    inv2 = 1.0 / (r * r)
    c0 = np.zeros(size)
    for wi in range(size):
        w = lo + wi
        for a in range(n, m + 1):
            if a <= -w - 6:
                c0[wi] += inv2 * r * (a + 5)
                continue
            for b in range(n, m + 1):
                if b <= w - 6:
                    c0[wi] += inv2 * (b + 5)
                else:
                    pp = p[w + a - b - lo]
                    c0[wi] += inv2 * ((a + 5) * pp + (b + 5) * (1.0 - pp))
    return c0


def e_mn(m: int, n: int) -> float:
    lo = -5 - m
    size = 2 * (5 + m) + 1
    trans, pa = _build_p(m, n, lo, size)
    mat = np.eye(size) - trans
    p = np.linalg.solve(mat, pa)
    c0 = _build_c0(m, n, lo, size, p)
    g = np.linalg.solve(mat, c0)
    return float(g[-lo]) - 5.0


@numba.njit(cache=True)
def _simulate(m, n, games, seed):
    np.random.seed(seed)
    total = 0.0
    for _ in range(games):
        sa = 0.0
        sb = 0.0
        j = 0
        while True:
            j += 1
            a = np.random.randint(n, m + 1)
            b = np.random.randint(n, m + 1)
            if sa + a + 5 * (j - 1) < sb + 5 * (j - 2):
                total += sa + a + 5 * (j - 1)
                break
            if sb + b + 5 * (j - 1) < sa + 5 * (j - 2):
                total += sb + b + 5 * (j - 1)
                break
            sa += a
            sb += b
    return total / games


if __name__ == "__main__":
    assert f"{e_mn(60, 30):.2f}" == "1036.15"  # given
    s5 = sum(e_mn(m, n) for m in range(2, 6) for n in range(1, m))
    assert f"{s5:.2f}" == "7722.82"  # given
    sim = _simulate(5, 2, 400000, 589)
    assert abs(sim - e_mn(5, 2)) / e_mn(5, 2) < 0.01

    s100 = sum(e_mn(m, n) for m in range(2, 101) for n in range(1, m))
    print(f"{s100:.2f}")  # 131776959.25
