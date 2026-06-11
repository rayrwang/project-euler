"""Project Euler Problem 620: Planetary Gears.

Work in circumference units (lengths scaled by 2 pi), so radii become
tooth counts.  With c = s + p + q, a p-planet's centre sits at distances
a = s + q from the outer centre O_C and b = s + p from the inner centre
O_S; the q-planet's distances are the same two numbers swapped, so both
planet triangles over the centre offset D are congruent.  Tangency
exists for q - p <= D <= 2s + p + q, the two planets of equal size are
the mirror pair of triangle apexes, and the 1 cm boundary gap means
D <= p + q - 2 pi.

Meshing: marking teeth at unit arc spacing, the phase-interleaving
conditions at a planet's two contacts (internal with C, external with
S) combine -- after eliminating the planet's own phase -- into one
condition modulo 1 per planet, involving only the angles of its centre
triangle and the free sum t of the phases of C and S.  Writing
u = [(s+q) beta + (s+p)(pi - gamma)] / (2 pi) for the p-planet (beta,
gamma the angles at O_C and O_S), the four planets' conditions reduce,
via the congruence identity u_p + u_q = s + (p+q)/2, to the single
requirement W(D) = 2 u_p in Z.  W increases monotonically (asserted by
dense sampling) from W = 0 at the excluded coincident position
D = q - p to its maximum at the gap-1 offset D = p + q - 2 pi, so

    g = floor(W_max) = floor(((s+p) alpha + (2s+p+q) beta) / pi)

with alpha, beta two angles of the triangle with sides s+q, s+p,
p+q-2pi (law of cosines).  Summing over the O(n^3 / 6) triples with
numpy takes a few seconds.  A handful of triples land within 1e-6 of an
integer (the closest about 3.6e-9); these are re-evaluated in 80-bit
long-double precision, which confirms the double-precision floors with
margin far above the asserted 1e-10.

Verified: g(16, 5, 5, 6) = 9, G(16) = 9, G(20) = 205 from the
statement, plus the monotone sweep of W for assorted triples.
"""

import math

import numpy as np

N = 500


def g_one(s: int, p: int, q: int) -> int:
    a, b, c = s + q, s + p, p + q - 2 * math.pi
    al = math.acos(max(-1.0, min(1.0, (a * a + b * b - c * c) / (2 * a * b))))
    be = math.acos(max(-1.0, min(1.0, (a * a + c * c - b * b) / (2 * a * c))))
    return int(((s + p) * al + (2 * s + p + q) * be) / math.pi + 1e-12)


def w_of_d(s: int, p: int, q: int, d: np.ndarray) -> np.ndarray:
    a, b = s + q, s + p
    beta = np.arccos(np.clip((d * d + a * a - b * b) / (2 * d * a), -1, 1))
    gamma = np.arccos(np.clip((d * d + b * b - a * a) / (2 * d * b), -1, 1))
    return ((s + q) * beta + (s + p) * (np.pi - gamma)) / np.pi


def w_longdouble(s: int, p: int, q: int) -> float:
    """W at the gap-1 offset in 80-bit precision for borderline cases."""
    ld = np.longdouble
    pi = np.arccos(ld(-1))
    a, b, c = ld(s + q), ld(s + p), ld(p + q) - 2 * pi
    al = np.arccos((a * a + b * b - c * c) / (2 * a * b))
    be = np.arccos((a * a + c * c - b * b) / (2 * a * c))
    return float(((ld(s) + p) * al + (2 * ld(s) + p + q) * be) / pi)


def big_g(n: int) -> int:
    total = 0
    min_margin = 1.0
    for s in range(5, n - 10 + 1):
        for p in range(5, (n - s - 1) // 2 + 1):
            qmax = n - s - p
            if qmax < p + 1:
                continue
            q = np.arange(p + 1, qmax + 1, dtype=np.float64)
            a, b = s + q, float(s + p)
            c = p + q - 2 * np.pi
            al = np.arccos(np.clip((a * a + b * b - c * c) / (2 * a * b),
                                   -1, 1))
            be = np.arccos(np.clip((a * a + c * c - b * b) / (2 * a * c),
                                   -1, 1))
            w = ((s + p) * al + (2 * s + p + q) * be) / np.pi
            frac = np.abs(w - np.round(w))
            for i in np.nonzero(frac < 1e-6)[0]:
                w[i] = w_longdouble(s, p, int(q[i]))
                margin = abs(w[i] - round(float(w[i])))
                min_margin = min(min_margin, margin)
            total += int(np.floor(w + 1e-12).sum())
    assert min_margin > 1e-10, min_margin
    return total


if __name__ == "__main__":
    assert g_one(5, 5, 6) == 9
    # W sweeps monotonically from 0 (coincident planets, excluded) to
    # its value at the 1 cm gap, for assorted triples
    for s, p, q in ((5, 5, 6), (7, 5, 9), (20, 11, 30), (100, 50, 77)):
        lo, hi = q - p, p + q - 2 * math.pi
        dd = np.linspace(lo + 1e-9, hi, 100001)
        ww = w_of_d(s, p, q, dd)
        assert (np.diff(ww) > -1e-12).all()
        assert ww[0] < 1e-3
        assert int(ww[-1] + 1e-12) == g_one(s, p, q)
    assert big_g(16) == 9
    assert big_g(20) == 205
    print(big_g(N))  # 1470337306
