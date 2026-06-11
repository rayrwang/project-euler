"""Project Euler 453: Lattice Quadrilaterals.

Q(m, n) counts simple quadrilaterals with vertices in the lattice grid
[0, m] x [0, n]; find Q(12345, 6789) mod 135707531.

Brute force on small grids (asserted below for Q(2, 2) = 94) pins down the
convention: a 4-point subset in strictly general position yields 1 simple
quadrilateral if convex and 3 if one point lies strictly inside the triangle
of the others, while subsets with three or more collinear points yield none.
Hence Q = CV + 3 * OI with CV + OI = C(P, 4) - A3 - A4, i.e.

    Q = C(P, 4) - (P - 3) T3 + 3 A4 + 2 OI,

where P = (m+1)(n+1), T3 = number of collinear triples, A4 = number of
collinear 4-subsets and A3 = (P - 3) T3 - 4 A4. Collinear statistics come
from pair-gcd sums: T3 = sum_{d >= 2} phi(d) R(d) and A4 = sum h(d) R(d)
with h the Moebius inversion of C(e-1, 2), and R(d) the closed-form count
of point pairs whose coordinate differences are both divisible by d.

OI is summed by Pick's theorem over all N_T = C(P, 3) - T3 triangles:
OI = S_A - S_B / 2 + N_T. The boundary sum is exact via
(c-2)(c^3-c)/6 = 4 C(c,3) + 4 C(c,4) per line, giving
S_B = (C(P,2) + T3)(P - 2) - 4 T3 - 4 A4. The area sum S_A = D / 12 with
D = sum over ordered vertex triples of |det| = sum over difference-vector
pairs (d, e) of |d x e| (m+1-spanx)(n+1-spany). Splitting the 16 sign
classes of (dx, ex, dy, ey): when the two determinant terms have opposite
signs the absolute value disappears and the class is a separable product of
small 1D sums; the two coupled classes (same/same and opposite/opposite
sign relations) have weights (m+1-max(a,u)) or (m+1-a-u)+ and reduce to
2 * sum_{a v > b u} (a v - b u) Wx Wy, computed by sorting the (n+1)^2
y-pairs (b, v) by the exact ratio v/b (float64 is provably exact here:
distinct fractions with these denominators differ by >= 1/(m n), far above
rounding error, and ties contribute zero), building suffix sums of v*Wy and
b*Wy mod 12*MOD, then sweeping all (a, u) with vectorised binary searches.
Zero-variable boundary slabs are restored by inclusion-exclusion with
closed-form pinned sums. Working modulo L = 12 * MOD keeps the exact
divisions by 6 and 2 valid. All four given values are asserted.
"""

import numpy as np
from itertools import combinations, product
from math import comb

MOD = 135707531
L = 12 * MOD


def brute_q(m, n):
    """Direct simple-quadrilateral count for tiny grids."""
    pts = [(x, y) for x in range(m + 1) for y in range(n + 1)]

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def on_seg(a, b, c):
        return (
            cross(a, b, c) == 0
            and min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
        )

    def seg_int(p1, p2, p3, p4):
        d1, d2 = cross(p3, p4, p1), cross(p3, p4, p2)
        d3, d4 = cross(p1, p2, p3), cross(p1, p2, p4)
        if ((d1 > 0) != (d2 > 0) and d1 != 0 and d2 != 0) and (
            (d3 > 0) != (d4 > 0) and d3 != 0 and d4 != 0
        ):
            return True
        return any(
            on_seg(a, b, c)
            for a, b, c in ((p1, p2, p3), (p1, p2, p4), (p3, p4, p1), (p3, p4, p2))
        )

    def simple(a, b, c, d):
        if seg_int(a, b, c, d) or seg_int(b, c, d, a):
            return False
        for p, q, r in ((a, b, c), (b, c, d), (c, d, a), (d, a, b)):
            if cross(p, q, r) == 0 and (p[0] - q[0]) * (r[0] - q[0]) + (
                p[1] - q[1]
            ) * (r[1] - q[1]) > 0:
                return False
            if cross(p, q, r) == 0:  # 180-degree vertex: degenerate, excluded
                return False
        return True

    total = 0
    for quad in combinations(pts, 4):
        for perm in ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)):
            if simple(*(quad[k] for k in perm)):
                total += 1
    return total


def collinear_stats(m, n):
    p_cnt = (m + 1) * (n + 1)
    dmax = max(m, n)

    def sq(length, d):
        q, r = divmod(length + 1, d)
        return r * (q + 1) ** 2 + (d - r) * q * q

    phi = list(range(dmax + 1))
    for p in range(2, dmax + 1):
        if phi[p] == p:
            for k in range(p, dmax + 1, p):
                phi[k] -= phi[k] // p
    mu = [0] * (dmax + 1)
    mu[1] = 1
    spf = [0] * (dmax + 1)
    primes = []
    for i in range(2, dmax + 1):
        if spf[i] == 0:
            primes.append(i)
            spf[i] = i
            mu[i] = -1
        for p in primes:
            if p > spf[i] or i * p > dmax:
                break
            spf[i * p] = p
            mu[i * p] = 0 if i % p == 0 else -mu[i]
    h = [0] * (dmax + 1)
    for e in range(3, dmax + 1):
        ce = comb(e - 1, 2)
        for d in range(e, dmax + 1, e):
            h[d] += mu[d // e] * ce
    t3 = 0
    a4 = 0
    for d in range(2, dmax + 1):
        r = (sq(m, d) * sq(n, d) - p_cnt) // 2
        t3 += phi[d] * r
        a4 += h[d] * r
    return p_cnt, t3, a4


def sweeps(m, n):
    """Coupled-class full-range sums (max/max and sum/sum weights), mod L."""
    big = (n + 1) * (n + 1)
    idx_all = np.arange(big, dtype=np.int32)
    b = idx_all // (n + 1)
    v = idx_all % (n + 1)
    del idx_all
    ratio = np.where(
        b > 0, v.astype(np.float64) / np.maximum(b, 1), np.where(v > 0, np.inf, -1.0)
    )
    order = np.argsort(ratio, kind="stable")
    rs = ratio[order]
    del ratio
    bo = b[order]
    vo = v[order]
    del b, v, order
    sufs = {}
    for tag in ("ss", "oo"):
        if tag == "ss":
            w = ((n + 1) - np.maximum(bo, vo)).astype(np.int64)
        else:
            w = np.maximum(0, (n + 1) - bo.astype(np.int64) - vo)
        suf_v = np.zeros(big + 1, np.int32)
        cs = np.cumsum((vo * w)[::-1])
        suf_v[:big] = (cs[::-1] % L).astype(np.int32)
        del cs
        suf_b = np.zeros(big + 1, np.int32)
        cs = np.cumsum((bo * w)[::-1])
        suf_b[:big] = (cs[::-1] % L).astype(np.int32)
        del cs, w
        sufs[tag] = (suf_v, suf_b)
    del bo, vo
    tot = {"ss": 0, "oo": 0}
    u = np.arange(0, m + 1, dtype=np.int64)
    for a in range(1, m + 1):
        idx = np.searchsorted(rs, u / a, side="right")
        wmax = (m + 1) - np.maximum(a, u)
        wsum = np.maximum(0, (m + 1) - a - u)
        for tag, wx in (("ss", wmax), ("oo", wsum)):
            suf_v, suf_b = sufs[tag]
            c = (a * suf_v[idx].astype(np.int64) - u * suf_b[idx]) % L
            c = (wx * c) % L
            tot[tag] = (tot[tag] + int(c.sum())) % L
    return (2 * tot["ss"]) % L, (2 * tot["oo"]) % L


def d_mod(m, n):
    ss_full, oo_full = sweeps(m, n)
    full = {"max": ss_full, "sum": oo_full}

    def xsum2(mode, coef):
        u = np.arange(0, m + 1, dtype=np.int64)
        tot = 0
        for a in range(0, m + 1):
            if mode == "max":
                w = (m + 1) - np.maximum(a, u)
            else:
                w = np.maximum(0, (m + 1) - a - u)
            tot += int(a * w.sum()) if coef == "a" else int((u * w).sum())
        return tot

    def ysum2(mode, coef):
        v = np.arange(0, n + 1, dtype=np.int64)
        tot = 0
        for b in range(0, n + 1):
            if mode == "max":
                w = (n + 1) - np.maximum(b, v)
            else:
                w = np.maximum(0, (n + 1) - b - v)
            tot += int(b * w.sum()) if coef == "b" else int((v * w).sum())
        return tot

    def pin1d(length):
        t = np.arange(0, length + 1, dtype=np.int64)
        return int((t * ((length + 1) - t)).sum())

    xc, yc = {}, {}

    def xv(mode, coef):
        if (mode, coef) not in xc:
            xc[(mode, coef)] = xsum2(mode, coef)
        return xc[(mode, coef)]

    def yv(mode, coef):
        if (mode, coef) not in yc:
            yc[(mode, coef)] = ysum2(mode, coef)
        return yc[(mode, coef)]

    def cc_pin(s, mode):
        s = frozenset(s)
        if s == frozenset(["a"]):
            return pin1d(m) * yv(mode, "b")
        if s == frozenset(["u"]):
            return pin1d(m) * yv(mode, "v")
        if s == frozenset(["b"]):
            return xv(mode, "a") * pin1d(n)
        if s == frozenset(["v"]):
            return xv(mode, "u") * pin1d(n)
        if s in (frozenset(["a", "v"]), frozenset(["u", "b"])):
            return pin1d(m) * pin1d(n)
        return 0

    # SEP variants need restricted-range x/y sums; build via slab subtraction
    def xv_r(mode, coef, a0, u0):
        val = xv(mode, coef)
        if a0:  # remove a = 0 slab: weight (m+1-u), coefficient a=0 or u
            u = np.arange(0, m + 1, dtype=np.int64)
            val -= 0 if coef == "a" else int((u * ((m + 1) - u)).sum())
        if u0:
            a = np.arange(0, m + 1, dtype=np.int64)
            val -= 0 if coef == "u" else int((a * ((m + 1) - a)).sum())
        return val  # a=u=0 cell has zero coefficient either way

    def yv_r(mode, coef, b0, v0):
        val = yv(mode, coef)
        if b0:
            v = np.arange(0, n + 1, dtype=np.int64)
            val -= 0 if coef == "b" else int((v * ((n + 1) - v)).sum())
        if v0:
            b = np.arange(0, n + 1, dtype=np.int64)
            val -= 0 if coef == "v" else int((b * ((n + 1) - b)).sum())
        return val

    tot = 0
    for s1, s2, s3, s4 in product((1, -1), repeat=4):
        a0 = 0 if s1 == 1 else 1
        u0 = 0 if s2 == 1 else 1
        b0 = 0 if s3 == 1 else 1
        v0 = 0 if s4 == 1 else 1
        xsame = s1 == s2
        ysame = s3 == s4
        if s1 * s4 == s3 * s2:
            mode = "max" if xsame else "sum"
            restricted = [
                name for name, z in (("a", a0), ("u", u0), ("b", b0), ("v", v0)) if z
            ]
            cc = full[mode]
            for k in range(1, len(restricted) + 1):
                for s in combinations(restricted, k):
                    cc = (cc + (-1) ** k * cc_pin(s, mode)) % L
            tot = (tot + cc) % L
        else:
            xm = "max" if xsame else "sum"
            ym = "max" if ysame else "sum"
            sep = xv_r(xm, "a", a0, u0) * yv_r(ym, "v", b0, v0) + xv_r(
                xm, "u", a0, u0
            ) * yv_r(ym, "b", b0, v0)
            tot = (tot + sep) % L
    return tot


def solve(m, n):
    p_cnt, t3, a4 = collinear_stats(m, n)
    n_t = comb(p_cnt, 3) - t3
    s_b = (comb(p_cnt, 2) + t3) * (p_cnt - 2) - 4 * t3 - 4 * a4
    dm = d_mod(m, n)
    assert dm % 6 == 0
    two_oi = (dm // 6 - s_b + 2 * n_t) % (2 * MOD)
    assert two_oi % 2 == 0
    oi = two_oi // 2
    return (comb(p_cnt, 4) - (p_cnt - 3) * t3 + 3 * a4 + 2 * oi) % MOD


if __name__ == "__main__":
    assert brute_q(2, 2) == 94  # convention check by direct geometry
    assert solve(2, 2) == 94
    assert solve(3, 7) == 39590
    assert solve(12, 3) == 309000
    assert solve(123, 45) == 70542215894646 % MOD
    print(solve(12345, 6789))  # 104354107
