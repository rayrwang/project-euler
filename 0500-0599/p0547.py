"""Project Euler problem 547: Distance of Random Points Within Hollow
Square Laminae.

A hollow square lamina of size n is an n x n square of unit cells with an
x by y rectangle (1 <= x, y <= n - 2) removed strictly inside (not
touching the border).  S(n) sums, over every distinct lamina (all sizes
and positions), the expected distance between two uniform random points
in the lamina.  Find S(40) to four decimal places.

For a lamina L = Q \\ R (full square minus hole), the distance integral
I(U, V) = double integral of |P1 - P2| over P1 in U, P2 in V satisfies
I(L, L) = I(Q,Q) - 2 I(Q,R) + I(R,R), and E[dist] = I(L, L) / area(L)^2.

Everything is integer-aligned, so each I decomposes over unit-cell pairs
into J(p, q), the distance integral between two unit squares offset by
(p, q).  J has a closed form: the offset differences have triangular
densities, and integrating (linear u)(linear v) sqrt(u^2 + v^2) over the
pieces uses the elementary primitives
  K00 = uvr/3 + u^3 asinh(v/u)/6 + v^3 asinh(u/v)/6,
  K10 = v r^3/12 + u^2 v r/8 + u^4 asinh(v/u)/8   (K01 symmetric),
  K11 = r^5/15,
verified analytically against the classical unit-square value
(2 + sqrt(2) + 5 asinh 1)/15 ~= 0.521405.  Corner evaluation of the
primitives cancels heavily at large offsets, so the table is built in
80-bit long double (~1e-19 eps), giving J to ~1e-12 - sufficient since
S aggregates ~5.5e5 laminae and needs 5e-5 absolute accuracy.

The lamina sum never iterates over positions times cells: for a fixed
hole extent x, the row-overlap counts summed over all horizontal
positions form a vector W_x of length 2n - 1, and the position-summed
cross term is the bilinear form W_x^T J W_y, making S(n) an O(n^4)-ish
computation overall.

Verified: the closed-form J matches Gauss-Legendre quadrature; the given
unit-square 0.521405 and 2 x 3 rectangle 1.317067 expectations are
reproduced; S(3) = 1.6514 and S(4) = 19.6564 match the given values; and
a Monte Carlo estimate of the single n = 3 lamina agrees.
"""

import numpy as np

LD = np.longdouble


def k00(u: LD, v: LD) -> LD:
    r = np.sqrt(u * u + v * v)
    t = u * v * r / 3
    if u != 0:
        t += u**3 * np.arcsinh(v / u) / 6
    if v != 0:
        t += v**3 * np.arcsinh(u / v) / 6
    return t


def k10(u: LD, v: LD) -> LD:
    r = np.sqrt(u * u + v * v)
    t = v * r**3 / 12 + u * u * v * r / 8
    if u != 0:
        t += u**4 * np.arcsinh(v / u) / 8
    return t


def k11(u: LD, v: LD) -> LD:
    return (u * u + v * v) ** LD(2.5) / 15


def pieces(p: int) -> list[tuple[LD, LD, LD, LD]]:
    """(lo, hi, const, slope) pieces of the triangular density on u >= 0."""
    pl = LD(p)
    if p == 0:
        return [(LD(0), LD(1), LD(2), LD(-2))]  # folded: weight 2(1 - u)
    return [(pl - 1, pl, 1 - pl, LD(1)), (pl, pl + 1, 1 + pl, LD(-1))]


def j_closed(p: int, q: int) -> LD:
    tot = LD(0)
    for a, b, c1, s1 in pieces(p):
        for g, d, c2, s2 in pieces(q):
            for kf, w in (
                (k00, c1 * c2),
                (k10, s1 * c2),
                (lambda u, v: k10(v, u), c1 * s2),
                (k11, s1 * s2),
            ):
                if w != 0:
                    tot += w * (kf(b, d) - kf(a, d) - kf(b, g) + kf(a, g))
    return tot


def j_quad(p: int, q: int, m: int = 48) -> float:
    xs, ws = np.polynomial.legendre.leggauss(m)
    tot = 0.0
    for a, b, c1, s1 in pieces(p):
        u = (float(a) + float(b)) / 2 + (float(b) - float(a)) / 2 * xs
        wu = ws * (float(b) - float(a)) / 2 * (float(c1) + float(s1) * u)
        for g, d, c2, s2 in pieces(q):
            v = (float(g) + float(d)) / 2 + (float(d) - float(g)) / 2 * xs
            wv = ws * (float(d) - float(g)) / 2 * (float(c2) + float(s2) * v)
            r = np.sqrt(u[:, None] ** 2 + v[None, :] ** 2)
            tot += float((wu[:, None] * wv[None, :] * r).sum())
    return tot


def s_value(n: int) -> LD:
    m = 2 * n - 1
    j_tab = np.zeros((n, n), dtype=LD)
    for p in range(n):
        for q in range(p, n):
            j_tab[p, q] = j_tab[q, p] = j_closed(p, q)
    j2 = np.zeros((m, m), dtype=LD)
    for di in range(-(n - 1), n):
        for dj in range(-(n - 1), n):
            j2[di + n - 1, dj + n - 1] = j_tab[abs(di), abs(dj)]
    mult = np.array([n - abs(d) for d in range(-(n - 1), n)], dtype=LD)
    iqq = mult @ j2 @ mult

    wvecs = {}
    for x in range(1, n - 1):
        wv = np.zeros(m, dtype=LD)
        for a in range(1, n - 1 - x + 1):
            for d in range(-(n - 1), n):
                lo, hi = max(a, d), min(a + x, n + d)
                if hi > lo:
                    wv[d + n - 1] += hi - lo
        wvecs[x] = wv
    jw = {y: j2 @ wvecs[y] for y in wvecs}

    total = LD(0)
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            npos = (n - 1 - x) * (n - 1 - y)
            irr = LD(0)
            for di in range(-(x - 1), x):
                for dj in range(-(y - 1), y):
                    irr += (x - abs(di)) * (y - abs(dj)) * j_tab[abs(di), abs(dj)]
            cross = wvecs[x] @ jw[y]
            total += (npos * (iqq + irr) - 2 * cross) / LD(n * n - x * y) ** 2
    return total


def monte_carlo_n3(samples: int = 4_000_000) -> float:
    rng = np.random.default_rng(12345)
    pts = []
    need = 2 * samples
    while len(pts) < 1 or sum(len(a) for a in pts) < need:
        cand = rng.uniform(0, 3, size=(need, 2))
        inside = ~((cand[:, 0] > 1) & (cand[:, 0] < 2) & (cand[:, 1] > 1) & (cand[:, 1] < 2))
        pts.append(cand[inside])
    all_pts = np.concatenate(pts)[:need]
    d = np.linalg.norm(all_pts[:samples] - all_pts[samples:], axis=1)
    return float(d.mean())


def main() -> None:
    e_unit = float(j_closed(0, 0))
    assert abs(e_unit - (2 + 2**0.5 + 5 * float(np.arcsinh(1))) / 15) < 1e-14
    assert f"{e_unit:.6f}" == "0.521405"  # given

    tot = LD(0)
    for di in range(-1, 2):
        for dj in range(-2, 3):
            tot += (2 - abs(di)) * (3 - abs(dj)) * j_closed(abs(di), abs(dj))
    assert f"{float(tot / 36):.6f}" == "1.317067"  # given

    for p, q in [(0, 3), (2, 2), (5, 1), (10, 7), (25, 30), (39, 39)]:
        assert abs(float(j_closed(p, q)) - j_quad(p, q)) < 1e-9, (p, q)

    s3 = float(s_value(3))
    assert f"{s3:.4f}" == "1.6514"  # given; n=3 has a single lamina
    assert abs(monte_carlo_n3() - s3) < 2e-3
    assert f"{float(s_value(4)):.4f}" == "19.6564"  # given

    print(f"{float(s_value(40)):.4f}")  # 11730879.0023


if __name__ == "__main__":
    main()
