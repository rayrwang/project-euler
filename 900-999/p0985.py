"""Project Euler 985.

The inscribed triangle whose vertices lie one per side, making equal angles
with each side, is the orthic (Fagnano) triangle. It exists iff T_k is acute.
The orthic map sends angles (A,B,C) -> (pi-2A, pi-2B, pi-2C), i.e. each angle
follows alpha -> pi - 2*alpha: linear, fixed point pi/3, multiplier -2.

Writing delta = angle - pi/3, we get delta_k = (-2)^k * delta_0, so deviations
from 60 degrees double (and flip sign) each step. T_k is acute iff every angle
< pi/2, i.e. every (-2)^k*delta_0 < pi/6.

Let m+ = (largest angle) - pi/3 and m- = pi/3 - (smallest angle). The first
non-acute triangle is T_K (so T_K exists, T_{K+1} does not) exactly when
  - even steps fail first at K:  2^(K-2)*m+ < pi/6 <= 2^K*m+
  - no odd step fails earlier:   2^(K-1)*m- < pi/6
For K = 20 this forces a near-equilateral integer triangle. Translate the angle
bounds into exact comparisons on rational cosines (law of cosines) versus
high-precision cosine thresholds, then search near-equilateral shapes for the
smallest perimeter.
"""
from decimal import Decimal as D, getcontext
from fractions import Fraction as Fr

getcontext().prec = 80
K = 20

def _pi():
    getcontext().prec += 10
    a, b, t, p = D(1), 1 / D(2).sqrt(), D(1) / 4, D(1)
    for _ in range(20):
        an = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - an) ** 2
        a = an
        p *= 2
    pi = (a + b) ** 2 / (4 * t)
    getcontext().prec -= 10
    return +pi

PI = _pi()
SQRT3 = D(3).sqrt()

def cos_60(eps):
    """cos(pi/3 + eps) for tiny eps, via series for cos/sin."""
    cs, t, k = D(0), D(1), 0
    while abs(t) > D(10) ** -72:
        cs += t; k += 1; t = -t * eps * eps / ((2 * k - 1) * (2 * k))
    sn, t, k = D(0), eps, 0
    while abs(t) > D(10) ** -72:
        sn += t; k += 1; t = -t * eps * eps / ((2 * k) * (2 * k + 1))
    return D("0.5") * cs - (SQRT3 / 2) * sn

base = PI / 6
U = cos_60(base / D(2) ** K)        # C >= 60+eps_lo  <=>  cosC <= U
L = cos_60(base / D(2) ** (K - 2))  # C <  60+eps_hi  <=>  cosC >  L
V = cos_60(-base / D(2) ** (K - 1)) # A >  60-eps_m   <=>  cosA <  V

def fdec(fr):
    getcontext().prec += 12
    d = D(fr.numerator) / D(fr.denominator)
    getcontext().prec -= 12
    return +d

def cosC(a, p, q):  # angle opposite the largest side a+q
    return fdec(Fr(a * a + (a + p) ** 2 - (a + q) ** 2, 2 * a * (a + p)))

def cosA(a, p, q):  # angle opposite the smallest side a
    return fdec(Fr((a + p) ** 2 + (a + q) ** 2 - a * a, 2 * (a + p) * (a + q)))

def bsearch(pred, hi):
    if not pred(hi):
        return None
    lo = 1
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

HI = 6_000_000
best = None
for q in range(1, 13):
    for p in range(0, q + 1):
        a_lowC = bsearch(lambda a: cosC(a, p, q) > L, HI)   # C < C_max
        a_lowA = bsearch(lambda a: cosA(a, p, q) < V, HI)   # A > A_min
        if a_lowC is None or a_lowA is None:
            continue
        start = max(a_lowC, a_lowA)
        for a in range(start, start + 6):
            if a <= q - p:                                   # triangle inequality
                continue
            cc = cosC(a, p, q)
            if cc <= U and cc > L and cosA(a, p, q) < V:
                per = 3 * a + p + q
                if best is None or per < best:
                    best = per
                break

print(best)  # 1734334
