"""Project Euler 904: Pythagorean Angle.

For a right triangle with legs a, b and hypotenuse c, the acute angle
between the two medians drawn to the legs satisfies

    tan(theta) = 3 a b / (2 c^2) <= 3/4,

which is scale-invariant: theta depends only on the shape of the
triangle.  Every shape is realised by a unique coprime pair (p, q),
0 < p < q, and writing t = p/q one gets
tan(theta) = g(t) = 3 t (1 - t^2) / (1 + t^2)^2, since the primitive
triple is

    p + q odd:  (a, b, c) = (q^2 - p^2, 2 p q, q^2 + p^2)
    p, q odd:   (a, b, c) = ((q^2 - p^2)/2, p q, (q^2 + p^2)/2)

(the involution t <-> (1 - t)/(1 + t) maps the two parities onto each
other and fixes the shape, so restricting to t in (0, sqrt(2) - 1), where
g is strictly increasing with maximum 3/4 at t = sqrt(2) - 1, loses
nothing).  theta determines the shape uniquely, and for alpha = cbrt(n)
no two symmetric shapes can tie (Niven / Gelfond-Schneider), so f is
well-defined: among shapes with primitive hypotenuse c <= L closest in
theta to alpha, take the largest multiple d = L // c; then
f = d (a + b + c).

The search: solve g(t) = tan(alpha) for the target t1 (float bisection
plus Newton steps in stdlib decimal), then find the coprime p/q closest
to t1 subject to feasibility.  Crucially, feasibility depends on the
parity class: opposite parity needs p^2 + q^2 <= L, both odd only
p^2 + q^2 <= 2L.  Because of this split, the best feasible fraction is
NOT always a (semi)convergent of t1 -- a both-odd fraction slightly
farther in the Stern-Brocot tree can beat every feasible spine node
(first seen at n = 26176, L = 10^8).  So we do it in two passes: a cheap
spine walk yields the distance D0 of the best feasible spine node, then a
windowed Stern-Brocot enumeration (with run jumps, so it is fast) lists
ALL coprime p/q with q <= sqrt(2L) within 1.05 * D0 of t1; the window is
tiny, so only a handful of candidates survive.

No mpmath: the only transcendental needed to full precision is
tau = tan(alpha), computed with the stdlib decimal module (Taylor
sin/cos, decimal-docs pi recipe, Newton cube root) and then frozen as an
exact Fraction.  Everything downstream is exact integer arithmetic:
window walks compare p/q against the Fraction t1 by cross-multiplication,
and candidates are ranked by the tangent of their angular distance to
alpha, |u - tau| / (1 + u tau) with u = 3ab/(2c^2) exact -- a strictly
monotone proxy for |theta - alpha| on (-90, 90) degrees, so the exact
Fraction comparison decides the true ordering.  Near-ties are separated
by recomputing tau at escalating precision (50 -> 150 -> 400 digits),
recomputing alpha = cbrt(n) fresh at each precision.  Verified against
the problem's examples and the original solution's spot checks.
"""

import math
import sys
from decimal import Decimal, getcontext, localcontext
from fractions import Fraction

SQRT2M1 = math.sqrt(2) - 1
_PI_CACHE: dict[int, Decimal] = {}


def dec_pi() -> Decimal:
    """pi at current context precision (decimal docs recipe, cached)."""
    prec = getcontext().prec
    if prec in _PI_CACHE:
        return _PI_CACHE[prec]
    with localcontext() as ctx:
        ctx.prec = prec + 4
        three = Decimal(3)
        lasts, t, s, n, na, d, da = Decimal(0), three, Decimal(3), 1, 0, 0, 24
        while s != lasts:
            lasts = s
            n, na = n + na, na + 8
            d, da = d + da, da + 32
            t = (t * n) / d
            s += t
    _PI_CACHE[prec] = +s
    return _PI_CACHE[prec]


def dec_sin(x: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec += 4
        i, last, s, fact, num, sign = 1, Decimal(0), x, 1, x, 1
        while s != last:
            last = s
            i += 2
            fact *= i * (i - 1)
            num *= x * x
            sign = -sign
            s += sign * num / fact
    return +s


def dec_cos(x: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec += 4
        i, last, s, fact, num, sign = 0, Decimal(0), Decimal(1), 1, Decimal(1), 1
        while s != last:
            last = s
            i += 2
            fact *= i * (i - 1)
            num *= x * x
            sign = -sign
            s += sign * num / fact
    return +s


def dec_cbrt(n: int) -> Decimal:
    """Cube root of the integer n at current context precision (Newton).

    Fixed iteration count: Newton doubles correct digits each step, so from
    a float seed (~15 digits) twelve steps exceed 400-digit precision; a
    convergence test like ``x != last`` can oscillate between two adjacent
    representable values and never terminate."""
    with localcontext() as ctx:
        ctx.prec += 6
        x = Decimal(repr(float(n) ** (1.0 / 3.0)))
        dn = Decimal(n)
        for _ in range(12):
            x = (2 * x + dn / (x * x)) / 3
    return +x


def tan_of_degrees(alpha_deg: Decimal) -> Decimal:
    rad = alpha_deg * dec_pi() / 180
    return dec_sin(rad) / dec_cos(rad)


def t_root(tau_f: float) -> float:
    """Solve 3 t (1 - t^2) = tau (1 + t^2)^2 on (0, sqrt(2) - 1), float."""
    lo, hi = 0.0, SQRT2M1
    for _ in range(80):
        mid = (lo + hi) / 2
        if 3 * mid * (1 - mid * mid) - tau_f * (1 + mid * mid) ** 2 < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def t1_fraction(tau: Decimal) -> Fraction:
    """Refine the float root by Newton in decimal, freeze as a Fraction."""
    with localcontext() as ctx:
        ctx.prec += 4
        t = Decimal(repr(t_root(float(tau))))
        for _ in range(7):
            h = 3 * t * (1 - t * t) - tau * (1 + t * t) ** 2
            dh = 3 - 9 * t * t - tau * 4 * t * (1 + t * t)
            t = t - h / dh
    return Fraction(+t)


def c_prim(p: int, q: int) -> int:
    s = p * p + q * q
    return s if (p + q) % 2 == 1 else s // 2


def pilot_window(T: int, S: int, L: int):
    """Stern-Brocot spine walk towards t1 = T/S with run jumps; return the
    smallest |p/q - t1| over feasible nodes met on the way (checking the
    last few nodes of each run, where the parity classes alternate).
    Exact integer arithmetic throughout; distance returned as a Fraction."""
    p0, q0, p1, q1 = 0, 1, 1, 1
    best = None  # (|p*S - T*q|, q), compare by cross-multiplication
    while True:
        below = (p0 + p1) * S < T * (q0 + q1)
        if below:
            pa, qa, pb, qb = p0, q0, p1, q1
            num, den = T * q0 - p0 * S, p1 * S - T * q1
        else:
            pa, qa, pb, qb = p1, q1, p0, q0
            num, den = p1 * S - T * q1, T * q0 - p0 * S
        kdir = max(1, num // den) if den > 0 else 1
        # largest k that stays within the loosest bound p^2 + q^2 <= 2L
        a_ = pb * pb + qb * qb
        b_ = 2 * (pa * pb + qa * qb)
        c_ = pa * pa + qa * qa - 2 * L
        disc = b_ * b_ - 4 * a_ * c_
        kf = -1
        if disc >= 0:
            kf = (-b_ + math.isqrt(disc)) // (2 * a_) + 2
            while kf >= 0 and (pa + kf * pb) ** 2 + (qa + kf * qb) ** 2 > 2 * L:
                kf -= 1
        k = min(kdir, kf)
        if k < 1:
            break
        for kk in (k, k - 1, k - 2, k - 3):
            if kk >= 1:
                p_, q_ = pa + kk * pb, qa + kk * qb
                if c_prim(p_, q_) <= L:
                    d = (abs(p_ * S - T * q_), q_)
                    if best is None or d[0] * best[1] < best[0] * d[1]:
                        best = d
        if below:
            p0, q0 = pa + k * pb, qa + k * qb
        else:
            p1, q1 = pa + k * pb, qa + k * qb
        if k < kdir:
            break
    return Fraction(best[0], best[1] * S) if best else None


def enum_window(lo_b: Fraction, hi_b: Fraction, qmax: int):
    """All coprime p/q with q <= qmax and lo_b <= p/q <= hi_b, by descending
    the Stern-Brocot tree with run jumps along branches that leave the
    window.  Exact integer arithmetic over a common denominator."""
    D = lo_b.denominator * hi_b.denominator // math.gcd(
        lo_b.denominator, hi_b.denominator
    )
    LN = lo_b.numerator * (D // lo_b.denominator)
    HN = hi_b.numerator * (D // hi_b.denominator)
    out = []
    stack = [(0, 1, 1, 1)]
    while stack:
        pl, ql, pr, qr = stack.pop()
        while True:
            pm, qm = pl + pr, ql + qr
            if qm > qmax:
                break
            if pm * D < LN * qm:
                # whole window is right of the mediant: jump left bound to the
                # last node still left of lo_b (conditions are linear in k)
                A = pr * D - LN * qr
                B = LN * ql - pl * D
                k_q = (qmax - ql) // qr
                k = k_q if A <= 0 else min(k_q, B // A)
                k = max(1, k)
                if ql + k * qr > qmax:
                    break
                pl, ql = pl + k * pr, ql + k * qr
            elif pm * D > HN * qm:
                # mirror image: jump right bound to the last node still right
                # of hi_b
                A = HN * ql - pl * D
                B = pr * D - HN * qr
                k_q = (qmax - qr) // ql
                k = k_q if A <= 0 else min(k_q, B // A)
                k = max(1, k)
                if qr + k * ql > qmax:
                    break
                pr, qr = pr + k * pl, qr + k * ql
            else:
                out.append((pm, qm))
                stack.append((pm, qm, pr, qr))
                pr, qr = pm, qm
    return out


def f(alpha_dec_fn, L: int) -> int:
    """alpha_dec_fn() must return the target angle in degrees as a Decimal
    at the current decimal context precision (it is re-evaluated when
    precision is escalated to break near-ties)."""
    getcontext().prec = 50
    tau = tan_of_degrees(alpha_dec_fn())
    tau_fr = Fraction(tau)
    t1 = t1_fraction(tau)
    T, S = t1.numerator, t1.denominator
    w0 = pilot_window(T, S, L)
    qmax = math.isqrt(2 * L)
    w = w0 * Fraction(21, 20) + Fraction(1, 10**40)
    cands = enum_window(t1 - w, t1 + w, qmax)
    alpha_f = float(alpha_dec_fn())
    finalists = []
    for p, q in cands:
        if (p + q) % 2 == 1:
            a, b, c = q * q - p * p, 2 * p * q, q * q + p * p
        else:
            a, b, c = (q * q - p * p) // 2, p * q, (q * q + p * p) // 2
        if c > L:
            continue
        th = math.degrees(math.atan2(3 * a * b, 2 * c * c))
        finalists.append((abs(th - alpha_f), a, b, c))
    finalists.sort()
    bestd = finalists[0][0]
    close = [x[1:] for x in finalists if x[0] <= bestd + 1e-12]
    if len(close) > 1:
        # exact ranking by tan of the angular distance:
        # |theta - alpha| is monotone in |u - tau| / (1 + u tau), u = 3ab/2c^2
        for prec in (50, 150, 400):
            getcontext().prec = prec
            tau_fr = Fraction(tan_of_degrees(alpha_dec_fn()))
            refined = sorted(
                (abs(Fraction(3 * a * b, 2 * c * c) - tau_fr)
                 / (1 + Fraction(3 * a * b, 2 * c * c) * tau_fr), a, b, c)
                for a, b, c in close
            )
            sep = (len(refined) < 2
                   or refined[1][0] - refined[0][0] > Fraction(1, 10 ** (prec - 12)))
            close = [r[1:] for r in refined[:4]]
            if sep:
                break
    a, b, c = close[0]
    return (L // c) * (a + b + c)


def big_f(num: int, limit: int, start: int = 1) -> int:
    return sum(
        f(lambda n=n: dec_cbrt(n), limit) for n in range(start, num + 1)
    )


if __name__ == "__main__":
    if len(sys.argv) == 4:  # partial range: start num limit (for chunked runs)
        print(big_f(int(sys.argv[2]), int(sys.argv[3]), start=int(sys.argv[1])))
        sys.exit()
    assert f(lambda: Decimal(30), 100) == 198
    assert f(lambda: Decimal(10), 10**6) == 1600158
    assert big_f(10, 10**6) == 16684370
    print(big_f(45000, 10**10))  # 880652522278760
