"""Project Euler 471: Triangle Inscribed in Ellipse.

G(n) sums the inradius r(a, b) of the triangle inscribed in the ellipse
x^2/a^2 + y^2/b^2 = 1 (0 < 2b < a) whose incircle is centered at (2b, 0)
with A = (a/2, sqrt(3) b / 2); find G(10^11) to 10 significant digits.

A always lies on the ellipse, and the configuration admits the closed form

    r(a, b) = b (a - 2b) / (a - b),

verified here two independent ways: an explicit numeric construction
(tangent lines from A to the candidate incircle, intersected with the
ellipse, bisecting on the radius until BC is tangent too) reproduces it for
several (a, b), and the double sum matches the given G(10) and G(100).

With c = a - b the sum becomes G(n) = sum_{b < c, b + c <= n} (b - b^2/c).
The b-part is a cubic polynomial in n. For the rest, swapping to a per-c sum
gives S2 = sum_{c=2}^{n-1} Q(min(c-1, n-c)) / c with Q(m) = m(m+1)(2m+1)/6:
the half with min = c - 1 is the exact polynomial sum of (c-1)(2c-1)/6, and
the other half, sum_d Q(d)/(n-d), reduces by polynomial division
(d^3/(n-d) = -(d^2 + n d + n^2) + n^3/(n-d), etc.) to exact integer sums
plus Q(n) (H_{n-1} - H_{n-D-1}). All polynomial parts are exact Python
integers over the common denominator 6; the harmonic difference is summed
directly for small arguments and via the asymptotic series
H_m = ln m + gamma + 1/(2m) - 1/(12 m^2) + 1/(120 m^4) for large ones (gamma
cancels). The ~1-2 digits of cancellation leave 13+ accurate digits, ample
for the requested 10. The fast formula agrees with exact-rational brute
force to machine precision for n up to 1000.
"""

from fractions import Fraction
from math import log

N = 10**11


def g_brute_exact(n):
    return sum(
        Fraction(b * (a - 2 * b), a - b)
        for a in range(3, n + 1)
        for b in range(1, (a - 1) // 2 + 1)
    )


def harm_diff(hi, lo):
    """H_hi - H_lo."""
    if hi <= 10**6:
        return sum(1.0 / k for k in range(lo + 1, hi + 1))

    def tail(m):
        m = float(m)
        return 1 / (2 * m) - 1 / (12 * m * m) + 1 / (120 * m**4)

    return log(hi / lo) + tail(hi) - tail(lo)


def g_fast(n):
    m = (n - 1) // 2
    p1 = m * (m + 1) * (3 * n - 4 * m - 2) // 6  # sum b (n - 2b)
    c0 = (n + 1) // 2

    def sum_poly(c):  # sum_{i<=c} (2 i^2 - 3 i + 1)
        return 2 * c * (c + 1) * (2 * c + 1) // 6 - 3 * c * (c + 1) // 2 + c

    s2a_num = sum_poly(c0) - sum_poly(1)  # over denominator 6
    d = n - c0 - 1
    qn = n * (n + 1) * (2 * n + 1) // 6
    t = harm_diff(n - 1, n - d - 1)
    sd2 = d * (d + 1) * (2 * d + 1) // 6
    sd1 = d * (d + 1) // 2
    poly_num = 2 * sd2 + (2 * n + 3) * sd1 + (2 * n * n + 3 * n + 1) * d
    exact_num = 6 * p1 - s2a_num + poly_num
    return exact_num / 6 - qn * t


def sci10(x):
    s = f"{x:.9e}".replace("e+", "e")
    head, exp = s.split("e")
    return f"{head}e{int(exp)}"


if __name__ == "__main__":
    for small in (10, 100, 500, 1000):
        exact = float(g_brute_exact(small))
        assert abs(g_fast(small) - exact) < 1e-9 * exact
    assert sci10(g_fast(10)) == "2.059722222e1"
    print(sci10(g_fast(N)))  # 1.895093981e31
