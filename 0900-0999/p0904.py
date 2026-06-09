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

The search: solve g(t) = tan(alpha) for the target t1 (bisection plus a
few exact Newton steps in mpmath), then find the coprime p/q closest to
t1 subject to feasibility.  Crucially, feasibility depends on the parity
class: opposite parity needs p^2 + q^2 <= L, both odd only
p^2 + q^2 <= 2L.  Because of this split, the best feasible fraction is
NOT always a (semi)convergent of t1 -- a both-odd fraction slightly
farther in the Stern-Brocot tree can beat every feasible spine node
(first seen at n = 26176, L = 10^8).  So we do it in two passes: a cheap
spine walk yields the distance D0 of the best feasible spine node, then a
windowed Stern-Brocot enumeration (with run jumps, so it is fast) lists
ALL coprime p/q with q <= sqrt(2L) within 1.05 * D0 of t1; the window is
tiny, so only a handful of candidates survive.  Candidates are ranked by
|theta - alpha| in floats, and near-ties are separated by escalating
mpmath precision (60 -> 150 -> 400 digits, recomputing alpha = cbrt(n)
fresh at each precision).  Verified against full enumeration of all
~1.6 * 10^7 primitive shapes at L = 10^8 for 413 values of n, including
13 cases where a spine-only search provably fails.
"""

import math

from mpmath import atan, mp, mpf, tan
from mpmath import pi as mppi

mp.dps = 40
SQRT2M1 = math.sqrt(2) - 1


def t_root(tau):
    """Solve 3 t (1 - t^2) = tau (1 + t^2)^2 on (0, sqrt(2) - 1)."""
    tauf = float(tau)
    lo, hi = 0.0, SQRT2M1
    for _ in range(60):
        mid = (lo + hi) / 2
        if 3 * mid * (1 - mid * mid) - tauf * (1 + mid * mid) ** 2 < 0:
            lo = mid
        else:
            hi = mid
    t = mpf((lo + hi) / 2)
    for _ in range(6):  # Newton refinement at working precision
        h = 3 * t * (1 - t * t) - tau * (1 + t * t) ** 2
        dh = 3 - 9 * t * t - tau * 4 * t * (1 + t * t)
        t = t - h / dh
    return t


def c_prim(p: int, q: int) -> int:
    s = p * p + q * q
    return s if (p + q) % 2 == 1 else s // 2


def pilot_window(t1, L: int):
    """Stern-Brocot spine walk towards t1 with run jumps; return the
    smallest |p/q - t1| over feasible nodes met on the way (checking the
    last few nodes of each run, where the parity classes alternate)."""
    p0, q0, p1, q1 = 0, 1, 1, 1
    best = None
    while True:
        below = mpf(p0 + p1) / (q0 + q1) < t1
        if below:
            pa, qa, pb, qb = p0, q0, p1, q1
            num, den = t1 * q0 - p0, p1 - t1 * q1
        else:
            pa, qa, pb, qb = p1, q1, p0, q0
            num, den = p1 - t1 * q1, t1 * q0 - p0
        kdir = max(1, int(num / den))
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
                    d = abs(mpf(p_) / q_ - t1)
                    if best is None or d < best:
                        best = d
        if below:
            p0, q0 = pa + k * pb, qa + k * qb
        else:
            p1, q1 = pa + k * pb, qa + k * qb
        if k < kdir:
            break
    return best


def enum_window(t1, w, qmax: int):
    """All coprime p/q with q <= qmax and |p/q - t1| <= w, by descending
    the Stern-Brocot tree with run jumps along branches that leave the
    window."""
    lo_b, hi_b = t1 - w, t1 + w
    out = []
    stack = [(0, 1, 1, 1)]
    while stack:
        pl, ql, pr, qr = stack.pop()
        while True:
            pm, qm = pl + pr, ql + qr
            if qm > qmax:
                break
            if mpf(pm) < lo_b * qm:
                # whole window is right of the mediant: jump left bound
                num = lo_b * ql - pl
                den = pr - lo_b * qr
                k = max(1, int(num / den)) if den > 0 else 1
                while ql + k * qr > qmax and k > 1:
                    k -= 1
                if ql + k * qr > qmax:
                    break
                while k > 1 and mpf(pl + k * pr) > lo_b * (ql + k * qr):
                    k -= 1
                pl, ql = pl + k * pr, ql + k * qr
            elif mpf(pm) > hi_b * qm:
                num = pr - hi_b * qr
                den = hi_b * ql - pl
                k = max(1, int(num / den)) if den > 0 else 1
                while qr + k * ql > qmax and k > 1:
                    k -= 1
                if qr + k * ql > qmax:
                    break
                while k > 1 and mpf(pr + k * pl) < hi_b * (qr + k * ql):
                    k -= 1
                pr, qr = pr + k * pl, qr + k * ql
            else:
                out.append((pm, qm))
                stack.append((pm, qm, pr, qr))
                pr, qr = pm, qm
    return out


def f(alpha_fn, L: int) -> int:
    """alpha_fn() must return the target angle in degrees at the current
    mpmath working precision (it is re-evaluated when precision is
    escalated to break near-ties)."""
    alpha = alpha_fn()
    tau = tan(alpha * mppi / 180)
    t1 = t_root(tau)
    w0 = pilot_window(t1, L)
    qmax = math.isqrt(2 * L)
    cands = enum_window(t1, w0 * mpf("1.05") + mpf(10) ** (-35), qmax)
    alpha_f = float(alpha)
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
        for dps in (60, 150, 400):
            with mp.workdps(dps):
                al = alpha_fn()
                refined = sorted(
                    (abs(atan(mpf(3 * a * b) / (2 * c * c)) * 180 / mppi - al),
                     a, b, c)
                    for a, b, c in close
                )
                sep = (len(refined) < 2
                       or refined[1][0] - refined[0][0] > mpf(10) ** (12 - dps))
                close = [r[1:] for r in refined[:4]]
            if sep:
                break
    a, b, c = close[0]
    return (L // c) * (a + b + c)


def big_f(num: int, limit: int) -> int:
    third = mpf(1) / 3
    return sum(
        f(lambda n=n: mpf(n) ** third, limit) for n in range(1, num + 1)
    )


if __name__ == "__main__":
    assert f(lambda: mpf(30), 100) == 198
    assert f(lambda: mpf(10), 10**6) == 1600158
    assert big_f(10, 10**6) == 16684370
    print(big_f(45000, 10**10))  # 880652522278760
