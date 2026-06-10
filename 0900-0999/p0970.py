"""Project Euler 970: Kangaroo Hopping over Sixes.

H(t) = sum_{j=0}^{t-1} (-1)^j (t-j)^j e^{t-j} / j! is the renewal function of
the renewal process with uniform(0,1) jumps: H(t) = 2t + 2/3 + eps(t), where

    eps(t) = sum over root pairs of  2 Re[ e^{s0 t} / s0 ]
           = sum of 2 e^{a t} (a cos bt + b sin bt) / (a^2 + b^2),

the s0 = a + bi being the complex roots of e^{-s} = 1 - s with a < 0 (at
every root the derivative of 1 - (1 - e^{-s})/s equals 1, so each residue of
the Laplace inversion is exactly e^{s0 t}/s0).

For t = 10^6 the dominant pair s0 ~ -2.08884 + 7.46149i utterly swamps the
rest (the next pair is smaller by a factor ~ e^{-575000}) and |eps| ~
10^{-907168}, so the fractional part of H(t) is 0.666...6 with a tiny ripple
starting about 907168 digits in. We add eps to 2/3 using exact integers and
read off the first eight digits that are not 6.

Everything runs in 130-digit decimal fixed point on Python integers: pi by
Machin's formula, ln 10 = 2 atanh(9/11), exp/sin/cos by Taylor series with
range reduction, and the root s0 polished by complex Newton iteration from a
float seed (matching the true root to 33+ digits). Validated against exact
digit extraction from the closed-form H(t) for t in {50, 60, 75, 100}.
"""

import cmath
import math
import sys

D = 130  # working decimal digits
S = 10**D


def mul(x: int, y: int) -> int:
    return x * y // S


def div(x: int, y: int) -> int:
    return x * S // y


def compute_pi() -> int:
    def atan_inv(n: int) -> int:  # atan(1/n), Machin building block
        total, term, k = 0, S // n, 0
        while term:
            total += term // (2 * k + 1) if k % 2 == 0 else -(term // (2 * k + 1))
            term //= n * n
            k += 1
        return total

    return 16 * atan_inv(5) - 4 * atan_inv(239)


def compute_ln10() -> int:
    total, num, k = 0, S * 9 // 11, 0  # 2 atanh(9/11)
    while num:
        total += num // (2 * k + 1)
        num = num * 81 // 121
        k += 1
    return 2 * total


PI = compute_pi()
LN10 = compute_ln10()


def exp_fp(x: int) -> int:
    j = 0
    while abs(x) > S // 4:  # range reduction by repeated squaring
        x //= 2
        j += 1
    total = term = S
    k = 1
    while term:
        term = mul(term, x) // k
        total += term
        k += 1
    for _ in range(j):
        total = mul(total, total)
    return total


def sincos_fp(x: int) -> tuple[int, int]:
    m = (x + PI) // (2 * PI)
    r = x - m * 2 * PI  # in [-pi, pi)
    q = (r + PI // 4) // (PI // 2)  # quadrant
    r2 = r - q * (PI // 2)  # in [-pi/4, pi/4)
    c, s_ = S, r2
    term_c, term_s = S, r2
    k = 1
    while term_c or term_s:
        term_c = -mul(mul(term_c, r2), r2) // ((2 * k - 1) * (2 * k))
        term_s = -mul(mul(term_s, r2), r2) // ((2 * k) * (2 * k + 1))
        c += term_c
        s_ += term_s
        k += 1
    return [(c, s_), (-s_, c), (-c, -s_), (s_, -c)][q % 4]


def root(k: int) -> tuple[int, int]:
    """k-th upper-half-plane root of e^{-s} = 1 - s, in fixed point."""
    s = complex(-math.log(2 * math.pi * k), 2 * math.pi * k + math.pi / 2)
    for _ in range(60):  # float seed
        s -= (cmath.exp(-s) - 1 + s) / (1 - cmath.exp(-s))
    x = int(s.real * 10**15) * 10 ** (D - 15)
    y = int(s.imag * 10**15) * 10 ** (D - 15)
    for _ in range(12):  # fixed-point Newton
        ex = exp_fp(-x)
        cy, sy = sincos_fp(y)
        e_re, e_im = mul(ex, cy), -mul(ex, sy)
        f_re, f_im = e_re - S + x, e_im + y
        g_re, g_im = S - e_re, -e_im
        den = mul(g_re, g_re) + mul(g_im, g_im)
        x -= div(mul(f_re, g_re) + mul(f_im, g_im), den)
        y -= div(mul(f_im, g_re) - mul(f_re, g_im), den)
    return x, y


def solve(t: int, num: int = 8, nroots: int = 2, extra: int = 40) -> str:
    contributions = []  # eps_i = (m2 / S) * 10^k0
    for k in range(1, nroots + 1):
        a, b = root(k)
        e10 = div(a * t, LN10)  # log10 of e^{a t}
        k0 = e10 // S
        mant = exp_fp(mul(e10 - k0 * S, LN10))  # 10^frac in [1, 10)
        cb, sb = sincos_fp(b * t)
        c_val = div(mul(a, cb) + mul(b, sb), mul(a, a) + mul(b, b))
        contributions.append((int(k0), 2 * mul(mant, c_val)))
    k0max = max(k0 for k0, _ in contributions)
    m2 = sum(
        v // 10 ** (k0max - k0) if k0max - k0 < 200 else 0
        for k0, v in contributions
    )
    g = len(str(abs(m2))) - 1 - D  # floor(log10 |m2/S|)
    w = -(k0max + g) + extra  # digits past the first deviation, plus guard
    corr = (2 * m2 * 10 ** (extra - g) + S) // (2 * S)  # round(eps * 10^w)
    sys.set_int_max_str_digits(max(w + 10, 4300))
    base = (2 * 10**w) // 3  # digits of 2/3 to w decimal places
    s = str(base + corr).zfill(w)
    return "".join(ch for ch in s if ch != "6")[:num]


print(solve(10**6))  # 44754029
