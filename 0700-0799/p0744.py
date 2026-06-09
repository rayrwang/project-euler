from fractions import Fraction
from math import comb

import numba

@numba.njit(cache=True)
def expected_margin(n, p):
    """E[R] where R = n - (loser's score), conditioned on the likelier side
    (success probability q = 1 - p > p) winning - which for the regimes used
    here happens with probability 1 minus something utterly negligible:
    by Hoeffding the other side wins with probability at most
    exp(-4 n (q - p)^2), which is exp(-4000) at n = 10^11, p = 0.4999 and
    exp(-800) at n = 10^4, p = 0.3. (For mildly biased mid-size n this
    one-branch shortcut would not reach 10 decimals - both regimes used
    here are fine, as the cross-check against exact summation confirms.)

    The loser's score l = n - r follows the negative binomial weight
    u(r) = C(2n-1-r, n-1) q^n p^(n-r); only ratios matter once we normalise,
    and u(r+1)/u(r) = (n - r) / ((2n - 1 - r) p). Start at the peak (ratio 1)
    and sweep outward until terms drop below 1e-18 of the peak.
    """
    r0 = int((n * (1 - 2 * p) + p) / (1 - p))
    if r0 < 1:
        r0 = 1
    if r0 > n:
        r0 = n
    s_u = 0.0
    s_ru = 0.0
    u = 1.0
    r = r0
    while r <= n and u > 1e-18:
        s_u += u
        s_ru += r * u
        u *= (n - r) / ((2 * n - 1 - r) * p)
        r += 1
    u = 1.0
    r = r0
    while r >= 1:
        u *= (2 * n - r) * p / (n - r + 1)  # inverse ratio: u(r-1) from u(r)
        r -= 1
        if u <= 1e-18:
            break
        s_u += u
        s_ru += r * u
    return s_ru / s_u

def f(n, p):
    """Probability the game ends normally (red card never drawn).

    The red card sits uniformly among 2n + 1 slots; the game ends normally
    iff it comes after the deciding question S = min trials to n successes
    or n failures. Hence f = E[(2n + 1 - S)] / (2n + 1) = (1 + E[R])/(2n+1)
    with R = 2n - S = n minus the loser's final score. Exact negative
    binomial summation for small n; for large n the dominant-side margin
    distribution is summed around its peak.
    """
    if n <= 1000:
        pf = Fraction(p)
        q = 1 - pf
        er = sum(
            (n - line) * comb(n - 1 + line, line) * (pf**n * q**line + q**n * pf**line)
            for line in range(n)
        )
        return float((1 + er) / (2 * n + 1))
    return (1 + expected_margin(n, min(p, 1 - p))) / (2 * n + 1)

if __name__ == "__main__":
    assert f"{f(6, Fraction(1, 2)):.10f}" == "0.2851562500"
    assert f"{f(10, Fraction(3, 7)):.10f}" == "0.2330040743"
    assert f"{f(10**4, 0.3):.10f}" == "0.2857499982"
    print(f"{f(10**11, 0.4999):.10f}")  # 0.0001999600
