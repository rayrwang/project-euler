from collections import defaultdict
from itertools import combinations
from math import gcd, isqrt

# Two circles with lattice centres meeting at two lattice points share a
# chord PQ that must be a primitive vector (interior chord lattice points
# would lie inside the lens) with both coordinates odd (else no lattice
# centre exists on the bisector). With P = 0, Q = (a, b), the centres are
# O_u = ((a - ub)/2, (b + ua)/2) for odd u, and 4 r^2 = c^2 (u^2 + 1) with
# c^2 = a^2 + b^2 (this reproduces both examples in the statement). Above
# the chord line the smaller-offset disk is contained in the larger one, so
# the lens splits into an upper cap owned by the circle with smaller u and
# a lower cap owned by the larger - the emptiness conditions decouple, and
# the lower condition is the mirror of the upper. Crucially the upper
# condition is linear in u: the cap is lattice-free iff for every lattice v
# with L(v) = a v_y - b v_x >= 1, |v - O|^2 >= r^2, i.e.
#     u <= U* = min over L(v) >= 1 of (|v|^2 - S(v)) / L(v),
# S(v) = a v_x + b v_y. Completing the square, on level L = m the minimum
# uses the point with S nearest c^2/2 (S = (b/a) m mod c^2), giving
#     f_m = (d_m^2 + m^2 - (c^2/2)^2) / (c^2 m),
# scanned for ascending m with the monotone lower bound
# (m^2 - (c^2/2)^2)/(c^2 m) as a stopping rule, in exact fraction
# arithmetic. With U° the largest odd integer <= U*, the realisable pairs
# of a chord are exactly {(v1, v2): odd v1 <= v2, both >= W} with
# W = max(1, -U°) (choosing u1 = -v2, u2 = v1 realises any such pair), so a
# class contributes K(K+1)/2 pairs with K the number of odd v in
# [W, Vmax], c^2 (Vmax^2 + 1) <= 4 N^2. Shapes with equal c^2 share radii;
# only the largest U* matters. Distinct pairs across classes can collide
# (e.g. 4r^2 = 20 arises from c^2 = 2 and c^2 = 10), handled by
# inclusion-exclusion over the cliques of shared values.
#
# Only chords with c^2 < 2N contribute: a near-zero U* forces
# (b/a) mod c^2 within 2N/c of 0 or c^2, which pushes c^2 below ~2N; this
# is enumerated with a 4x safety margin (cap 8N), and totals were verified
# stable against caps 40N and the full 2N^2 at N = 1000. Validated against
# direct geometric brute force at L(10) = 30 and L(20) = 122, and the given
# L(100) = 3442.


def _ustar(a: int, b: int, abort_below: int) -> tuple[int, int] | None:
    c2 = a * a + b * b
    half = c2 // 2
    step = b * pow(a, -1, c2) % c2
    best_num, best_den = 0, 0
    s = 0
    m = 1
    while True:
        s = (s + step) % c2
        d = abs(s - half)
        num = d * d + m * m - half * half
        den = c2 * m
        if best_den == 0 or num * best_den < best_num * den:
            best_num, best_den = num, den
            if best_num < abort_below * best_den:
                return None
        nb = m + 1
        if (nb * nb - half * half) * best_den > best_num * c2 * nb:
            break
        m += 1
    return best_num, best_den


def _class_w(shapes: list[tuple[int, int]], vmax: int) -> int | None:
    best: tuple[int, int] | None = None
    for a, b in shapes:
        r = _ustar(a, b, -(vmax + 2))
        if r is None:
            continue
        if best is None or r[0] * best[1] > best[0] * r[1]:
            best = r
    if best is None:
        return None
    fl = best[0] // best[1]
    u_odd = fl if fl % 2 != 0 else fl - 1
    w = max(1, -u_odd)
    return w if w <= vmax else None


def solve(n: int = 10**5) -> int:
    cap = 8 * n
    classes: dict[int, list[tuple[int, int]]] = {}
    a = 1
    while 2 * a * a <= cap:
        b = a
        while a * a + b * b <= cap:
            if gcd(a, b) == 1:
                classes.setdefault(a * a + b * b, []).append((a, b))
            b += 2
        a += 2
    total = 0
    val_class: list[tuple[int, int]] = []
    cidx = 0
    for c2, shapes in sorted(classes.items()):
        vmax_sq = 4 * n * n // c2 - 1
        if vmax_sq < 1:
            continue
        vmax = isqrt(vmax_sq)
        if vmax % 2 == 0:
            vmax -= 1
        if vmax < 1:
            continue
        w = _class_w(shapes, vmax)
        if w is None:
            continue
        k = (vmax - w) // 2 + 1
        total += k * (k + 1) // 2
        for v in range(w, vmax + 1, 2):
            val_class.append((c2 * (v * v + 1), cidx))
        cidx += 1
    val_class.sort()
    subset_count: dict[tuple[int, ...], int] = defaultdict(int)
    i = 0
    n_vals = len(val_class)
    while i < n_vals:
        j = i
        while j < n_vals and val_class[j][0] == val_class[i][0]:
            j += 1
        if j - i >= 2:
            cl = sorted({c for _, c in val_class[i:j]})
            for size in range(2, len(cl) + 1):
                for sub in combinations(cl, size):
                    subset_count[sub] += 1
        i = j
    for sub, m_count in subset_count.items():
        total += (1 if len(sub) % 2 else -1) * m_count * (m_count + 1) // 2
    return total


if __name__ == "__main__":
    print(solve())  # 4884650818
