from itertools import combinations, product
from math import atan2

# A quadrilateral inscribed in a circle of radius r satisfies
# a^2 + b^2 + c^2 + d^2 = 8 r^2 iff the sum of the cosines of its four arcs
# vanishes; factoring that sum shows this happens exactly when a diagonal is
# a diameter or the diagonals are perpendicular.  So f(sqrt(d)) counts
# 4-subsets of the lattice points on x^2 + y^2 = d whose convex hull has a
# diameter diagonal (D) or perpendicular diagonals.
#
# D: an antipodal pair is a diagonal iff the other two vertices lie on
# opposite sides of it, giving (n/2) ((n-2)/2)^2 minus C(n/2, 2) for the
# double-counted rectangles, where n is the number of lattice points.
#
# The remaining count Q is over crossing perpendicular pairs of
# non-diameter chords.  A chord {A, C} is recovered uniquely from its sum
# s = A + C (the chord line meets the circle in only those two points), the
# chord is perpendicular to s, and two chords are perpendicular iff their
# sums are.  Writing the points as i^t * prod pi_j^(a_j) conj(pi_j)^(e_j - a_j)
# for the Gaussian primes pi_j over d = prod p_j^(e_j), perpendicularity of
# sums is the angle relation psi_A + psi_C = psi_B + psi_D + pi, which - the
# prime angles being independent over Q*pi - holds iff a_j(A) + a_j(C) =
# a_j(B) + a_j(D) for every j and t_A + t_C = t_B + t_D + 2 (mod 4).  Hence
# ordered solutions number 64 prod R(e_j) with R(e) = sum_s r_e(s)^2,
# r_e(s) = e + 1 - |s - e|; removing degenerate chords (A = C or A = -C,
# each contributing 16 prod W(e_j) with W(e) = sum_a r_e(2a), overlapping in
# 8n tuples) and shared-endpoint pairs (perpendicularity forces them to be
# {A, C}, {A, -C}: n(n-2)/2 pairs) leaves the perpendicular pairs on four
# distinct points.  Exactly half of them cross: two perpendicular chords
# cross iff |s_1|^2 + |s_2|^2 < 4d, and negating one chord's endpoints
# (suitably chosen when the pair contains a cross-antipodal coincidence)
# keeps perpendicularity while flipping that inequality, with equality
# impossible on distinct points.  Altogether
#     Q = 4 (prod R(e_j) - prod W(e_j)) + n/2 - n(n-2)/4.
#
# Everything depends only on the exponent signature of d, so S(N) is a sum
# of f over the 2688 divisor signatures.  The formula is verified below
# against a geometric brute force and all values given in the problem.


def lattice_points(d):
    pts = []
    x = 0
    while x * x <= d:
        y2 = d - x * x
        y = int(y2**0.5)
        while y * y < y2:
            y += 1
        if y * y == y2:
            for sx in (x,) if x == 0 else (x, -x):
                for sy in (y,) if y == 0 else (y, -y):
                    pts.append((sx, sy))
        x += 1
    return sorted(set(pts))


def brute_f(d):
    """Geometric reference count of pythagorean lattice grid quadrilaterals."""
    pts = lattice_points(d)
    cnt = 0
    for quad in combinations(pts, 4):
        p1, p2, p3, p4 = sorted(quad, key=lambda p: atan2(p[1], p[0]))
        diam = p3 == (-p1[0], -p1[1]) or p4 == (-p2[0], -p2[1])
        dot = (p3[0] - p1[0]) * (p4[0] - p2[0]) + (p3[1] - p1[1]) * (p4[1] - p2[1])
        if diam or dot == 0:
            cnt += 1
    return cnt


def f(sig):
    """f(sqrt(d)) for d with exponent signature sig over primes = 1 mod 4."""
    n, pr, pw = 4, 1, 1
    for e in sig:
        n *= e + 1
        pr *= sum((e + 1 - abs(s - e)) ** 2 for s in range(2 * e + 1))
        pw *= sum(e + 1 - abs(2 * a - e) for a in range(e + 1))
    diam = (n // 2) * ((n - 2) // 2) ** 2 - (n // 2) * (n // 2 - 1) // 2
    perp = 4 * (pr - pw) + n // 2 - n * (n - 2) // 4
    return diam + perp


if __name__ == "__main__":
    for d_val, sig in [(1, ()), (2, ()), (5, (1,)), (25, (2,)), (65, (1, 1)),
                    (125, (3,)), (325, (2, 1)), (1105, (1, 1, 1))]:
        assert brute_f(d_val) == f(sig)
    assert f(()) + 2 * f((1,)) + f((2,)) + f((1, 1)) + f((2, 1)) == 2370  # S(325)
    assert f(()) + 3 * f((1,)) + 3 * f((1, 1)) + f((1, 1, 1)) == 5535  # S(1105)

    exponents = (6, 3, 2, 1, 1, 1, 1, 1)  # 5^6 * 13^3 * 17^2 * 29 * 37 * 41 * 53 * 61
    s = sum(f(tuple(a for a in combo if a > 0))
            for combo in product(*[range(e + 1) for e in exponents]))
    print(s)  # 1395793419248
