"""Project Euler Problem 644: Squares on the Line.

A straight square occupies length 1 of the segment, a diagonal one
sqrt(2); placements split the free length into independent gaps, so
Sprague-Grundy applies: a gap of length g has
G(g) = mex over w in {1, sqrt 2} and t in [0, g - w] of
G(t) xor G(g - w - t).  G is piecewise constant with breakpoints in the
ring Z + Z sqrt(2) (left-closed cells): for L strictly inside a cell,
S = L - w is never a ring translate of a ring point, so every reachable
value arises from a positive-measure range of t, and the per-cell mex
is found by a two-pointer sweep pairing the merged constant intervals
of t with those of S - t.  Up to 500 the 177k ring cells merge into
1829 intervals (max Grundy 211); the scan is numba-jitted.  An
independent discretised recursion (grid offset to dodge ring points)
reproduces G at random lengths below 12.

After Sam's random first move the position seen by Tom has Grundy
G(t) xor G(L - w - t); Sam wins iff it is 0, i.e. G(t) = G(S - t) with
S = L - w.  The winning measure W(S) = |{t in [0, S]: G(t) = G(S-t)}|
is piecewise linear: each ordered pair of equal-Grundy intervals
contributes a trapezoid (slope events at a1+a2, a1+b2, b1+a2, b1+b2,
weight 2 for distinct pairs).  Then

    e(L) = L/2 (W(L-1)/(L-1) + W(L-sqrt2)/(L-sqrt2)),

a smooth rational function between the breakpoints L in
(breakpoints of W) + {1, sqrt 2}.  On each piece e' = 0 is a quartic,
solved by numpy root finding; the maximum over [200, 500] is taken over
all interior critical points and breakpoints.

Verified: e(2) = 2, e(4) = 1.11974851 with branch probabilities
0.33333333 and 0.22654092, f(2,10) = 2.61969775 attained at
L = 7.82842712, and f(10,20) = 5.99374121, all to the stated 8 digits.
"""

import math
import random
from functools import lru_cache

import numba
import numpy as np

SQRT2 = math.sqrt(2.0)


def ring_values(max_l: float) -> np.ndarray:
    vals = []
    b = 0
    while b * SQRT2 <= max_l + 1e-9:
        base = b * SQRT2
        a = 0
        while a + base <= max_l + 1e-9:
            vals.append(a + base)
            a += 1
        b += 1
    return np.array(sorted(vals))


@numba.jit(nogil=True)
def grundy_scan(pts):
    n = len(pts) - 1
    starts = np.empty(n, dtype=np.float64)
    ends = np.empty(n, dtype=np.float64)
    gr = np.empty(n, dtype=np.int64)
    cnt = 0
    stamp = np.zeros(1024, dtype=np.int64)
    for idx in range(n):
        a = pts[idx]
        b = pts[idx + 1]
        mid = 0.5 * (a + b)
        for wi in range(2):
            w = 1.0 if wi == 0 else 1.4142135623730951
            s_av = mid - w
            if s_av <= 1e-12:
                continue
            ti = 0
            ui = cnt - 1
            while ui >= 0 and starts[ui] >= s_av:
                ui -= 1
            while ti <= ui:
                t1 = min(ends[ti], s_av)
                u1 = min(ends[ui], s_av)
                lo = max(starts[ti], s_av - u1)
                hi = min(t1, s_av - starts[ui])
                if lo < hi - 1e-12:
                    stamp[gr[ti] ^ gr[ui]] = idx + 1
                if t1 < s_av - starts[ui] - 1e-12:
                    ti += 1
                else:
                    ui -= 1
        g = 0
        while stamp[g] == idx + 1:
            g += 1
        if cnt > 0 and gr[cnt - 1] == g and abs(ends[cnt - 1] - a) < 1e-9:
            ends[cnt - 1] = b
        else:
            starts[cnt] = a
            ends[cnt] = b
            gr[cnt] = g
            cnt += 1
    return starts[:cnt], ends[:cnt], gr[:cnt]


def build_w(starts, ends, gr, max_s: float):
    """Piecewise-linear W(S) = measure{t in [0,S]: G(t) = G(S-t)}."""
    groups: dict[int, list[tuple[float, float]]] = {}
    for a, b, g in zip(starts, ends, gr):
        groups.setdefault(int(g), []).append((float(a), float(b)))
    events = []
    for ivs in groups.values():
        for i, (a1, b1) in enumerate(ivs):
            for j in range(i, len(ivs)):
                a2, b2 = ivs[j]
                p0 = a1 + a2
                if p0 > max_s:
                    break
                w = 1.0 if i == j else 2.0
                q1, q2 = sorted((a1 + b2, b1 + a2))
                events += [(p0, w), (q1, -w), (q2, -w), (b1 + b2, w)]
    events.sort()
    xs, slopes, vals = [0.0], [0.0], [0.0]
    cur_x, cur_slope, cur_val = 0.0, 0.0, 0.0
    for pos, dw in events:
        if pos > max_s + 5:
            break
        if pos > cur_x + 1e-12:
            cur_val += cur_slope * (pos - cur_x)
            cur_x = pos
            xs.append(pos)
            slopes.append(0.0)
            vals.append(cur_val)
        cur_slope += dw
        slopes[-1] = cur_slope
    return np.array(xs), np.array(slopes), np.array(vals)


def w_at(xs, slopes, vals, x):
    i = int(np.searchsorted(xs, x, side="right")) - 1
    return vals[i] + slopes[i] * (x - xs[i]), slopes[i]


def e_of(xs, slopes, vals, length):
    tot = 0.0
    for w in (1.0, SQRT2):
        s_av = length - w
        if s_av > 0:
            tot += w_at(xs, slopes, vals, s_av)[0] / s_av
    return length / 2 * tot


def f_max(xs, slopes, vals, lo, hi):
    bps = {float(lo), float(hi)}
    for w in (1.0, SQRT2):
        i0 = max(int(np.searchsorted(xs, lo - w)) - 1, 0)
        i1 = int(np.searchsorted(xs, hi - w)) + 1
        for x in xs[i0:i1]:
            if lo < x + w < hi:
                bps.add(float(x + w))
    pieces = sorted(bps)
    best = -1.0
    pp = np.polynomial.polynomial
    for k in range(len(pieces) - 1):
        a, b = pieces[k], pieces[k + 1]
        mid = 0.5 * (a + b)
        coef = []
        for w in (1.0, SQRT2):
            v, sl = w_at(xs, slopes, vals, mid - w)
            coef.append((sl, v - sl * (mid - w), w))
        (a1, b1, c1), (a2, b2, c2) = coef
        poly = (
            pp.polymul(np.array([-b1 * c1, -2 * a1 * c1, a1]),
                       pp.polyfromroots([c2, c2]))
            + pp.polymul(np.array([-b2 * c2, -2 * a2 * c2, a2]),
                         pp.polyfromroots([c1, c1]))
        )
        cands = [a, b]
        cands += [
            float(r.real)
            for r in pp.polyroots(poly)
            if abs(r.imag) < 1e-9 and a < r.real < b
        ]
        best = max(best, max(e_of(xs, slopes, vals, c) for c in cands))
    return best


def grundy_discretised_check(starts, ends, gr) -> None:
    """Independent recursion on an offset grid reproduces G below 12."""
    step = 1 / 64

    @lru_cache(maxsize=None)
    def g_eval(key: float) -> int:
        seen = set()
        for w in (1.0, SQRT2):
            s_av = key - w
            if s_av < -1e-12:
                continue
            s_av = max(s_av, 0.0)
            k = 0
            while True:
                t = k * step + 0.0037
                if t > s_av - 0.0037:
                    break
                seen.add(g_eval(round(t, 9)) ^ g_eval(round(s_av - t, 9)))
                k += 1
            seen.add(g_eval(0.0) ^ g_eval(round(s_av, 9)))
        m = 0
        while m in seen:
            m += 1
        return m

    def g_interval(x: float) -> int:
        i = 0
        while not (starts[i] - 1e-9 <= x < ends[i] - 1e-9):
            i += 1
        return int(gr[i])

    rng = random.Random(1)
    for _ in range(40):
        length = rng.uniform(0.2, 11.5)
        if any(abs(length - x) < 0.02 for x in list(starts) + list(ends)):
            continue
        assert g_interval(length) == g_eval(round(length, 9)), length


if __name__ == "__main__":
    starts, ends, gr = grundy_scan(ring_values(500.0))
    grundy_discretised_check(starts, ends, gr)
    xs, slopes, vals = build_w(starts, ends, gr, 500.0)
    assert abs(e_of(xs, slopes, vals, 2.0) - 2.0) < 1e-9
    assert round(w_at(xs, slopes, vals, 3.0)[0] / 3, 8) == 0.33333333
    s_d = 4 - SQRT2
    assert round(w_at(xs, slopes, vals, s_d)[0] / s_d, 8) == 0.22654092
    assert round(e_of(xs, slopes, vals, 4.0), 8) == 1.11974851
    assert round(f_max(xs, slopes, vals, 2, 10), 8) == 2.61969775
    assert round(f_max(xs, slopes, vals, 10, 20), 8) == 5.99374121
    print(f"{f_max(xs, slopes, vals, 200, 500):.8f}")  # 20.11208767
