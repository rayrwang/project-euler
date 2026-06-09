"""Project Euler 970: Kangaroo Hopping over Sixes.

H(t) = sum_{j=0}^{t-1} (-1)^j (t-j)^j e^{t-j} / j! is the renewal function of
the renewal process with uniform(0,1) jumps: H(t) = 2t + 2/3 + eps(t), where

    eps(t) = sum over root pairs of  2 Re[ e^{s0 t} / s0 ],

the s0 being the complex roots of e^{-s} = 1 - s with Re(s0) < 0 (at every
root the derivative of 1 - (1 - e^{-s})/s equals 1, so each residue of
e^{st} / (s (1 - (1-e^{-s})/s)) is exactly e^{s0 t}/s0).

For t = 10^6 the dominant pair s0 ~ -2.08884 + 7.46149i utterly swamps the
rest (next pair is smaller by a factor ~ e^{-575000}), and |eps| ~ 10^{-907168}.
So the fractional part of H(t) is 0.666...6 with a tiny ripple starting about
907168 digits in; we add eps to 2/3 using exact integers and read off the
first eight digits that are not 6.

Validated against exact H(t) digit extraction for t = 20..100.
"""

import sys

import mpmath as mp


def eps_value(t: int, nroots: int) -> mp.mpf:
    tot = mp.mpf(0)
    for k in range(1, nroots + 1):
        guess = mp.mpc(-mp.log(2 * mp.pi * k), 2 * mp.pi * k + mp.pi / 2)
        s0 = mp.findroot(lambda z: mp.e ** (-z) - 1 + z, guess)
        tot += 2 * (mp.e ** (s0 * t) / s0).real
    return tot


def solve(t: int, num: int = 8, nroots: int = 2, extra: int = 40) -> str:
    mp.mp.dps = 200
    eps = eps_value(t, nroots)
    k = -int(mp.floor(mp.log10(abs(eps))))  # first significant digit position
    w = k + extra
    sys.set_int_max_str_digits(max(w + 10, 4300))
    base = (2 * 10**w) // 3  # digits of 2/3 to w decimal places
    corr = int(mp.nint(eps * mp.power(10, w)))
    s = str(base + corr).zfill(w)
    return "".join(ch for ch in s if ch != "6")[:num]


print(solve(10**6))  # 44754029
