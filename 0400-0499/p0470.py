"""Project Euler 470: Super Ramvok.

F(20) = sum over 4 <= d <= 20, 0 <= c <= 20 of S(d, c), rounded.

Single Ramvok on a visible-face set V with cost constant c: choosing horizon
t and stopping optimally gives value E_t with E_1 = mean(V) and
E_{t+1} = E_t + sum_{v > E_t} (v - E_t)/|V|. The increments are strictly
decreasing, so the optimal horizon keeps extending while the increment
exceeds c, and R(V, c) = max(0, E_t - c t); for c = 0 the supremum is max(V)
with t infinite. This reproduces R(4, 0.2) = 2.65.

In Super Ramvok the die alteration is a random toggle of a uniform face, a
process completely independent of the player's choices. So
S(d, c) = sum_V E[visits to V] * R(V, c), where the visible-face process is
the Ehrenfest chain on levels k = |V| (down with probability k/d, up with
(d-k)/d), started at level d and absorbed at 0. By symmetry every size-k
subset has the same expected visit count v_k = L_k / C(d, k), with the level
visit counts L_k solved exactly over the rationals from the absorbed-chain
linear system. S(6, 1) = 208.3 checks out, and a Monte Carlo simulation
agrees for small cases.

The subset sums are accumulated in numba: for each of the 2^d - 1 masks the
increment trajectory of E_t is computed once (it is c-independent), then each
integer c = 1..20 reads off its stopping point; c = 0 contributes max(V).
About 2 * 10^6 subsets in total for d up to 20.
"""

from fractions import Fraction
from math import comb

import numpy as np
from numba import njit

N = 20


def level_visits(d):
    """Expected visits L[k] to level k (1..d), start at d, absorb at 0."""
    n = d
    mat = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    rhs = [Fraction(0)] * n
    for k in range(1, d + 1):
        i = k - 1
        mat[i][i] = Fraction(1)
        if k + 1 <= d:
            mat[i][k] -= Fraction(k + 1, d)
        if k - 1 >= 1:
            mat[i][k - 2] -= Fraction(d - k + 1, d)
        rhs[i] = Fraction(1 if k == d else 0)
    for col in range(n):
        piv = next(r for r in range(col, n) if mat[r][col] != 0)
        mat[col], mat[piv] = mat[piv], mat[col]
        rhs[col], rhs[piv] = rhs[piv], rhs[col]
        inv = 1 / mat[col][col]
        mat[col] = [x * inv for x in mat[col]]
        rhs[col] *= inv
        for r in range(n):
            if r != col and mat[r][col] != 0:
                f = mat[r][col]
                mat[r] = [x - f * y for x, y in zip(mat[r], mat[col])]
                rhs[r] -= f * rhs[col]
    return rhs  # rhs[k-1] = L_k


@njit(cache=True)
def subset_sums(d, cmax):
    """sums[k][c] = sum of R(V, c) over subsets V of {1..d} with |V| = k."""
    sums = np.zeros((d + 1, cmax + 1), np.float64)
    vals = np.empty(d, np.float64)
    traj = np.empty(300, np.float64)
    for mask in range(1, 1 << d):
        k = 0
        s = 0.0
        mx = 0.0
        for i in range(d):
            if mask >> i & 1:
                vals[k] = i + 1.0
                s += i + 1.0
                mx = i + 1.0
                k += 1
        # trajectory of E_t while increments exceed 1
        e = s / k
        traj[0] = e
        tn = 1
        while True:
            delta = 0.0
            for j in range(k - 1, -1, -1):
                if vals[j] > e:
                    delta += vals[j] - e
                else:
                    break
            delta /= k
            if delta <= 1.0 or tn >= 300:
                break
            e += delta
            traj[tn] = e
            tn += 1
        sums[k, 0] += mx  # c = 0: infinite horizon
        for c in range(1, cmax + 1):
            t = 1
            e = traj[0]
            while t < tn and traj[t] - traj[t - 1] > c:
                e = traj[t]
                t += 1
            profit = e - c * t
            if profit > 0.0:
                sums[k, c] += profit
    return sums


def total_f(n):
    total = 0.0
    for d in range(4, n + 1):
        lv = level_visits(d)
        sums = subset_sums(d, n)
        for k in range(1, d + 1):
            vk = float(lv[k - 1]) / comb(d, k)
            for c in range(n + 1):
                total += vk * sums[k, c]
    return total


def s_single(d, c):
    lv = level_visits(d)
    sums = subset_sums(d, max(1, c))
    return sum(float(lv[k - 1]) / comb(d, k) * sums[k, c] for k in range(1, d + 1))


if __name__ == "__main__":
    assert abs(s_single(6, 1) - 208.3) < 0.05
    print(round(total_f(N)))  # 147668794
