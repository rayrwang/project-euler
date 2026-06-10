"""
https://projecteuler.net/problem=507

From tribonacci residues r_i = t_i mod 10^7, each n yields vectors
V_n = (r-r, r+r, r*r) and W_n (the next six residues), and S(n) is
the minimal Manhattan length of k V_n + l W_n over integer
(k, l) != (0, 0). Find sum_(n=1..2*10^7) S(n).

Each instance is a shortest-vector problem in a rank-2 lattice
under the L1 norm, solved by generalized Gauss (Kaib-Schnorr)
reduction, which works for any symmetric convex norm: repeatedly
swap so |V| <= |W| and replace W by W - tV with the integer t
minimizing |W - tV|_1. That objective is convex piecewise-linear in
t with minimum at the weighted median of the ratios w_i / v_i
(weights |v_i|); a float median estimate is corrected by evaluating
a +-2 integer window, so exactness never relies on floating point.
Norms strictly decrease, giving Euclidean-style convergence, and a
final scan over |k|, |l| <= 2 of the reduced basis guards the
terminal case. Degenerate inputs are handled separately: a zero
vector makes the minimum 0 (take the unit coefficient on it), and
collinear V = cU, W = dU (primitive U) give gcd(c, d) |U|_1.
Magnitudes stay within int64: components are at most 10^14 and
optimal-window evaluations are bounded by |V|_1 + |W|_1.

Verified against the given S(1) = 32 and
sum_(n<=10) S(n) = 130762273722, and against literal minimisation
over |k|, |l| <= 150 for 3000 random small-entry instances
(including degenerate ones).
"""

import numba
import numpy as np


@numba.njit(cache=True, inline="always")
def _l1(x, y, z):
    return abs(x) + abs(y) + abs(z)


@numba.njit(cache=True, inline="always")
def _gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def min_l1(v1, v2, v3, w1, w2, w3):
    nv = _l1(v1, v2, v3)
    nw = _l1(w1, w2, w3)
    if nv == 0 or nw == 0:
        return np.int64(0)
    if v2 * w3 == v3 * w2 and v3 * w1 == v1 * w3 and v1 * w2 == v2 * w1:
        g = _gcd(_gcd(v1, v2), v3)
        u1, u2, u3 = v1 // g, v2 // g, v3 // g
        d = w1 // u1 if u1 != 0 else (w2 // u2 if u2 != 0 else w3 // u3)
        return _gcd(g, d) * _l1(u1, u2, u3)
    rats = np.empty(3)
    wts = np.empty(3)
    for _ in range(200):
        nv = _l1(v1, v2, v3)
        nw = _l1(w1, w2, w3)
        if nv > nw:
            v1, w1 = w1, v1
            v2, w2 = w2, v2
            v3, w3 = w3, v3
            nv, nw = nw, nv
        cnt = 0
        vv = (v1, v2, v3)
        ww = (w1, w2, w3)
        for i in range(3):
            if vv[i] != 0:
                rats[cnt] = ww[i] / vv[i]
                wts[cnt] = abs(vv[i])
                cnt += 1
        for i in range(cnt):
            for j in range(i + 1, cnt):
                if rats[j] < rats[i]:
                    rats[i], rats[j] = rats[j], rats[i]
                    wts[i], wts[j] = wts[j], wts[i]
        half = 0.0
        for i in range(cnt):
            half += wts[i]
        half *= 0.5
        acc = 0.0
        med = rats[0]
        for i in range(cnt):
            acc += wts[i]
            if acc >= half:
                med = rats[i]
                break
        t0 = np.int64(med)
        best_t = np.int64(0)
        best = nw
        for dt in range(-2, 4):
            t = t0 + dt
            if t == 0:
                continue
            val = _l1(w1 - t * v1, w2 - t * v2, w3 - t * v3)
            if val < best:
                best = val
                best_t = t
        if best_t == 0:
            break
        w1 -= best_t * v1
        w2 -= best_t * v2
        w3 -= best_t * v3
    res = min(_l1(v1, v2, v3), _l1(w1, w2, w3))
    for k in range(-2, 3):
        for el in range(-2, 3):
            if k == 0 and el == 0:
                continue
            val = _l1(k * v1 + el * w1, k * v2 + el * w2, k * v3 + el * w3)
            if val < res:
                res = val
    return res


@numba.njit(cache=True)
def total_s(n_max):
    mod = 10**7
    u0, u1, u2 = 0, 0, 1  # t_0, t_1, t_2 residues
    grp = np.zeros(12, dtype=np.int64)
    g = 0
    total = np.int64(0)
    for j in range(1, 12 * n_max + 1):
        if j == 1:
            tj = u1
        elif j == 2:
            tj = u2
        else:
            tj = (u0 + u1 + u2) % mod
            u0, u1, u2 = u1, u2, tj
        grp[g] = tj
        g += 1
        if g == 12:
            g = 0
            total += min_l1(
                grp[0] - grp[1],
                grp[2] + grp[3],
                grp[4] * grp[5],
                grp[6] - grp[7],
                grp[8] + grp[9],
                grp[10] * grp[11],
            )
    return total


@numba.njit(cache=True)
def _brute_min(v1, v2, v3, w1, w2, w3, bound):
    best = np.int64(2**62)
    for k in range(-bound, bound + 1):
        for el in range(-bound, bound + 1):
            if k == 0 and el == 0:
                continue
            val = _l1(k * v1 + el * w1, k * v2 + el * w2, k * v3 + el * w3)
            if val < best:
                best = val
    return best


if __name__ == "__main__":
    assert int(total_s(1)) == 32  # given S(1)
    assert int(total_s(10)) == 130762273722  # given sum to 10
    rng = np.random.default_rng(507)
    for _ in range(3000):
        v = rng.integers(-30, 31, 3).astype(np.int64)
        w = rng.integers(-30, 31, 3).astype(np.int64)
        assert min_l1(v[0], v[1], v[2], w[0], w[1], w[2]) == _brute_min(
            v[0], v[1], v[2], w[0], w[1], w[2], 150
        )

    print(int(total_s(20000000)))  # 316558047002627270
