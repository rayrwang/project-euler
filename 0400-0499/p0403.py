"""Project Euler 403: Lattice Points Enclosed by Parabola and Line.

D(a, b) is the region x^2 <= y <= ax + b, L(a, b) its lattice-point count;
sum L over |a|, |b| <= N = 10^12 with rational area, mod 10^8.

The chord meets the parabola at x = (a +- sqrt(disc))/2 with disc = a^2 + 4b,
and the area is disc^(3/2) / 6 - rational exactly when disc = d^2 is a perfect
square (d >= 0, d = a mod 2). Then both intersection abscissae are integers,
and with u = x - x_min the vertical gap is u(d - u), so
    L(a, b) = sum_{u=0}^{d} (u(d-u) + 1) = (d + 1) + (d^3 - d)/6 =: f(d),
a function of d alone (this reproduces L(1,2) = 8 and L(2,-1) = 1).

Substituting sigma = (d + a)/2, tau = (d - a)/2 (integers by parity) turns the
constraints into b = sigma tau, a = sigma - tau, d = sigma + tau >= 0, so
    S(N) = sum f(sigma + tau) over |sigma tau| <= N, |sigma - tau| <= N.
The axes give 2 G(N) - 1 with G = the prefix sum of f. The quadrant
sigma, tau >= 1 is a divisor-style sum handled with the standard sqrt(N)
split (two triangle sums minus the K x K box, K = floor(sqrt(N))), and the
mixed-sign quadrants give 2 sum_v G(floor(N/v) - v) (v = 1 binds at N - v
instead). Quotient blocks reduce everything to O(sqrt(N)) evaluations of the
prefix polynomials G, H = sum G and W = sum s f(s); each is evaluated modulo
720 * 10^8 by Horner and divided by the common denominator 720 at the end.
The whole computation is a few seconds of pure Python; S(5) = 344 and
S(100) = 26709528 are asserted, as is the closed form against brute force.
"""

from math import isqrt

MOD = 10**8
DEN = 720
M_ = DEN * MOD
# coefficients of 720*G, 720*H, 720*W (highest degree first); G(x) is the
# prefix sum of f, H of G, W of s*f(s)
CG = [30, 60, 330, 1020, 720]
CH = [6, 30, 150, 690, 1284, 720]
CW = [24, 60, 240, 660, 456, 0]


def poly_prefix(coeffs, x):
    if x < 0:
        return 0
    x %= M_
    r = 0
    for c in coeffs:
        r = (r * x + c) % M_
    return r // DEN % MOD


def g_pref(x):
    return poly_prefix(CG, x)


def h_pref(x):
    return poly_prefix(CH, x)


def w_pref(x):
    return poly_prefix(CW, x)


def f(d):
    return (d + 1) + (d**3 - d) // 6


def fast_s(n):
    k = isqrt(n)
    total = (2 * g_pref(n) - 1) % MOD
    # quadrant sigma, tau >= 1: 2 * sum_{s<=K} G(s + n//s) - 2*(H(K)-1) - box
    t1 = 0
    s = 1
    while s <= k:
        m = n // s
        s2 = min(n // m, k)
        t1 = (t1 + h_pref(s2 + m) - h_pref(s + m - 1)) % MOD
        s = s2 + 1
    box = (
        w_pref(k + 1)
        - w_pref(1)
        - (g_pref(k + 1) - g_pref(1))
        + (2 * k + 1) * (g_pref(2 * k) - g_pref(k + 1))
        - (w_pref(2 * k) - w_pref(k + 1))
    ) % MOD
    total = (total + 2 * t1 - 2 * (h_pref(k) - 1) - box) % MOD
    # mixed signs: v = 1 binds at N - v; v >= 2 contributes G(n//v - v)
    mx = g_pref(n - 2) if n >= 2 else 0
    v = 2
    while v * v <= n:
        m = n // v
        v2 = min(n // m, k)
        mx = (mx + h_pref(m - v) - h_pref(m - v2 - 1)) % MOD
        v = v2 + 1
    return (total + 2 * mx) % MOD


def brute_s(n):
    tot = 0
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            disc = a * a + 4 * b
            if disc >= 0:
                d = isqrt(disc)
                if d * d == disc:
                    tot += f(d)
    return tot % MOD


if __name__ == "__main__":
    for small in range(1, 41):
        assert fast_s(small) == brute_s(small)
    assert fast_s(5) == 344
    assert fast_s(100) == 26709528
    print(fast_s(10**12))  # 18224771
