"""Project Euler 933: Paper Cutting.

A cut of a w x h piece at (a, b) yields four independent pieces, so the
game is a disjunctive sum with Grundy values

    G(w, h) = mex_{a,b} G(a,b) ^ G(a,h-b) ^ G(w-a,b) ^ G(w-a,h-b),

G = 0 on strips (w = 1 or h = 1), and C(w, h) counts cuts whose XOR is
zero.  C(w, h) only references widths a, w-a <= w - 1, never width w.

Empirically every row G(a, .) with a <= 122 becomes CONSTANT, equal to
some K_a, for h beyond a transient T_a (max T = 3016, checked against a
table built to h = 8192).  Consequences for h large: a cut with both
b >= T and h - b >= T has XOR K_a ^ K_{w-a} ^ K_a ^ K_{w-a} = 0, i.e.
every "middle" cut wins, while for b <= B (any B >= max_a T_a) the XOR
equals G(a,b) ^ G(w-a,b) ^ K_a ^ K_{w-a}, independent of h.  Hence for
h >= 2B + 2:

    C(w, h) = (w - 1)(h - 1 - 2B) + 2 c_w(B),
    c_w(B)  = #{(a, b <= B) : G(a,b) ^ G(w-a,b) = K_a ^ K_{w-a}},

exactly linear in h with slope w - 1.  The answer sums exact C values
(four-fold orbit symmetry in (a, b)) up to a per-width threshold and the
arithmetic-series tail beyond; the linear formula is asserted against
exact counts at several h past each threshold.

Validated with the given C(5,3) = 4 and D(12,123) = 327398.
Runs in about three minutes (table build plus summation).
"""

import numpy as np
from numba import njit


@njit(cache=True)
def build(wmax: int, hmax: int) -> np.ndarray:
    g = np.zeros((wmax + 1, hmax + 1), dtype=np.int64)
    seen = np.zeros(8192, dtype=np.bool_)
    for w in range(2, wmax + 1):
        for h in range(2, hmax + 1):
            top = 0
            for a in range(1, w // 2 + 1):
                ga = g[a]
                gwa = g[w - a]
                for b in range(1, h // 2 + 1):
                    x = ga[b] ^ ga[h - b] ^ gwa[b] ^ gwa[h - b]
                    seen[x] = True
                    if x > top:
                        top = x
            v = 0
            while seen[v]:
                v += 1
            g[w, h] = v
            for i in range(top + 1):
                seen[i] = False
    return g


@njit(cache=True)
def c_exact(g: np.ndarray, w: int, h: int) -> int:
    cnt = 0
    for a in range(1, w // 2 + 1):
        ma = 2 if a != w - a else 1
        ga = g[a]
        gwa = g[w - a]
        for b in range(1, h // 2 + 1):
            if ga[b] ^ ga[h - b] ^ gwa[b] ^ gwa[h - b] == 0:
                cnt += ma * (2 if b != h - b else 1)
    return cnt


@njit(cache=True)
def exact_sum_upto(g: np.ndarray, w: int, h1: int) -> int:
    tot = 0
    for h in range(2, h1 + 1):
        tot += c_exact(g, w, h)
    return tot


@njit(cache=True)
def c_w_count(g: np.ndarray, w: int, bb: int, kvals: np.ndarray) -> int:
    cnt = 0
    for a in range(1, w):
        target = kvals[a] ^ kvals[w - a]
        ga = g[a]
        gwa = g[w - a]
        for b in range(1, bb + 1):
            if ga[b] ^ gwa[b] == target:
                cnt += 1
    return cnt


def solve(w_max: int, h_max: int) -> int:
    h0 = 8192
    g = build(w_max - 1, h0)
    k = g[:, h0].copy()
    trans = np.zeros(w_max, dtype=np.int64)
    for a in range(2, w_max):
        row = g[a]
        last = 0
        for h in range(2, h0 + 1):
            if row[h] != k[a]:
                last = h
        trans[a] = last + 1
    assert trans.max() + 200 < h0, "rows not stabilised within table"

    total = 0
    run_max = 0
    for w in range(2, w_max + 1):
        b = run_max + 8
        h1 = 2 * b + 8
        if h_max <= h1:
            total += exact_sum_upto(g, w, h_max)
        else:
            cw = c_w_count(g, w, b, k)
            for h in (h1 + 1, h1 + 13, h1 + 57):  # linearity asserts
                lin = (w - 1) * (h - 1 - 2 * b) + 2 * cw
                assert lin == c_exact(g, w, h), (w, h)
            n_terms = h_max - h1
            h_sum = (h1 + 1 + h_max) * n_terms // 2
            total += exact_sum_upto(g, w, h1) \
                + (w - 1) * (h_sum - (1 + 2 * b) * n_terms) \
                + 2 * cw * n_terms
        if w < w_max:
            run_max = max(run_max, int(trans[w]))
    return total


if __name__ == "__main__":
    gg = build(12, 256)
    assert c_exact(gg, 5, 3) == 4  # given
    assert solve(12, 123) == 327398  # given
    print(solve(123, 1234567))  # 5707485980743099
