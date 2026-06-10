"""
https://projecteuler.net/problem=562

Among triangles with lattice vertices inside or on the circle of
radius r that contain no other lattice point (inside or on edges),
take the one of maximum perimeter; T(r) is its circumradius over r.
Find T(10^7) rounded to the nearest integer.

By Pick's theorem an empty lattice triangle has area 1/2, so with
longest side v = B - A (primitive) the third vertex C satisfies
cross(v, C - A) = +-1, i.e. C lies on one of the two lattice lines
adjacent to AB, at position s = (C - A) . v with s fixed modulo v^2
(s = v_y v_x^(-1) mod v^2). Then |C-A|^2 = (s^2+1)/v^2 and
|C-B|^2 = ((v^2-s)^2+1)/v^2, the circumradius is
R = sqrt((s^2+1)((v^2-s)^2+1)) / (2|v|) (since R = abc/(4K), K=1/2),
and the perimeter is P = |v| + (sqrt(s^2+1) + sqrt((v^2-s)^2+1))/|v|
= 2|v| + O(1/v^2) because s >= sqrt(v^2 - 1) (lattice C has
|C-A| >= 1). Consecutive achievable |v| differ by at least
1/(2 |v|) >> 1/v^2, so the maximum perimeter first maximises
N = v^2 over feasible placements, then (within equal N) maximises
the correction, i.e. minimises min(s, N - s).

Feasibility of v needs a lattice A with A, A + v, A + p all in the
disk (p = C - A). Since |A + v/2|^2 <= r^2 - N/4, the valid A lie in
a disk of radius sqrt(4r^2 - N)/2 around -v/2, so each test scans
only ~sqrt(gap) columns. Candidates (all primitive vectors with N in
a window below 4r^2, four sign/line variants each) are tested in
decreasing N; the winner at r = 10^7 has gap 4r^2 - N = 2718, far
inside the 2*10^5 window. T is produced exactly as
sqrt(X / (4 r^2 N)) with X = (s^2+1)((N-s)^2+1), rounded by integer
comparison of (2m +- 1)^2 * 4 r^2 N against 4X.

Verified against a literal maximum-perimeter brute force over all
empty triangles for r = 10 (same triangle up to congruence) and the
given T(10) ~ 97.26729 and T(100) ~ 9157.64707.
"""

from decimal import Decimal, getcontext
from itertools import combinations
from math import gcd, isqrt

import numba
import numpy as np

getcontext().prec = 80


def _ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x, y = _ext_gcd(b, a % b)
    return g, y, x - (a // b) * y


@numba.njit(cache=True, inline="always")
def _isq(x: np.int64) -> np.int64:
    if x < 0:
        return np.int64(-1)
    r = np.int64(np.sqrt(x))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


@numba.njit(cache=True)
def _feasible(vx, vy, px, py, r2):
    s1 = _isq(r2)
    delta = 4 * r2 - (vx * vx + vy * vy)
    half = _isq(delta) // 2 + 2
    xlo = max(-s1, -vx - s1, -px - s1, -vx // 2 - half)
    xhi = min(s1, -vx + s1, -px + s1, -vx // 2 + half)
    if xlo > xhi:
        return False
    xc = -vx // 2
    for d in range(0, xhi - xlo + 1):
        for sgn in range(2):
            if sgn == 1 and d == 0:
                continue
            x = xc - d if sgn == 0 else xc + d
            if x < xlo or x > xhi:
                continue
            t1 = r2 - x * x
            t2 = r2 - (x + vx) * (x + vx)
            t3 = r2 - (x + px) * (x + px)
            if t1 < 0 or t2 < 0 or t3 < 0:
                continue
            y_hi = min(_isq(t1), -vy + _isq(t2), -py + _isq(t3))
            y_lo = max(-_isq(t1), -vy - _isq(t2), -py - _isq(t3))
            if y_lo <= y_hi:
                return True
    return False


def _p_vec(vx: int, vy: int, v2: int, sign: int) -> tuple[int, int, int]:
    _, a, b = _ext_gcd(vx, -vy)
    x0, y0 = b * sign, a * sign
    s_raw = vx * x0 + vy * y0
    s0 = s_raw % v2
    k = (s0 - s_raw) // v2
    return x0 + k * vx, y0 + k * vy, s0


def solve(r: int, delta: int) -> tuple[int, int, int, Decimal]:
    r2 = r * r
    w_lo = 4 * r2 - delta
    cands = []
    for vx in range(0, 2 * r + 1):
        hi2 = 4 * r2 - vx * vx
        if hi2 < 1:
            break
        vy_lo = max(isqrt(max(w_lo - vx * vx, 0)) - 1, 1)
        for vy in range(vy_lo, isqrt(hi2) + 1):
            n = vx * vx + vy * vy
            if w_lo <= n <= 4 * r2 and gcd(vx, vy) == 1:
                cands.append((n, vx, vy))
    cands.sort(reverse=True)
    best_n = None
    finalists = []
    for n, vx, vy in cands:
        if best_n is not None and n < best_n:
            break
        for sy in (1, -1) if (vx > 0 and vy > 0) else (1,):
            vyy = vy * sy
            for sign in (1, -1):
                px, py, s0 = _p_vec(vx, vyy, n, sign)
                if _feasible(vx, vyy, px, py, r2):
                    best_n = n
                    finalists.append((n, s0))
    assert best_n is not None, "increase delta"
    n, s0 = min(finalists, key=lambda f: min(f[1], f[0] - f[1]))
    x = (s0 * s0 + 1) * ((n - s0) ** 2 + 1)
    k = 4 * r2 * n
    m = isqrt(x // k)
    while (2 * m + 1) ** 2 * k <= 4 * x:
        m += 1
    while m >= 1 and (2 * m - 1) ** 2 * k > 4 * x:
        m -= 1
    return n, s0, m, (Decimal(x) / Decimal(k)).sqrt()


def _brute_t(r: int) -> Decimal:
    pts = [
        (x, y)
        for x in range(-r, r + 1)
        for y in range(-r, r + 1)
        if x * x + y * y <= r * r
    ]
    best = None
    for a, b, c in combinations(pts, 3):
        cr = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        if abs(cr) == 1:
            a2 = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2
            b2 = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
            c2 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
            per = Decimal(a2).sqrt() + Decimal(b2).sqrt() + Decimal(c2).sqrt()
            if best is None or per > best[0]:
                best = (per, a2 * b2 * c2)
    assert best is not None
    return (Decimal(best[1]) / 4).sqrt() / r


if __name__ == "__main__":
    _, _, _, t10 = solve(10, 200)
    assert f"{float(t10):.5f}" == "97.26729"  # given
    assert f"{float(_brute_t(10)):.5f}" == "97.26729"
    _, _, _, t100 = solve(100, 20000)
    assert f"{float(t100):.5f}" == "9157.64707"  # given

    _, _, m, _ = solve(10**7, 2 * 10**5)
    print(m)  # 51208732914368
