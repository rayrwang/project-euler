"""Project Euler Problem 661: A Long Chess Match.

After every game the match continues with probability q = 1 - p, and we
count the games after which A is strictly leading.  With S_t the score
difference after t games (steps +1, -1, 0 with probabilities p_A, p_B,
p_d = 1 - p_A - p_B),

    E_A = sum_{t>=1} q^(t-1) P(S_t >= 1).

Resolvent / generating function: P(S_t = s) = [x^s] phi(x)^t with
phi(x) = p_A x + p_d + p_B / x, so summing the geometric series,
sum_t q^t P(S_t >= 1) extracts the positive-power coefficients of
1 / (1 - q phi(x)).  Writing 1 - q phi(x) = -(q p_A / x)(x - r1)(x - r2)
with r1 < 1 < r2 the roots of

    q p_A x^2 - (1 - q p_d) x + q p_B = 0,

a Laurent expansion in the annulus r1 < |x| < r2 gives
[x^s] = r2^(-s) / (q p_A (r2 - r1)) for s >= 1, and the geometric sum in
s collapses everything to the closed form

    E_A(p_A, p_B, p) = 1 / (q^2 p_A (r2 - r1)(r2 - 1)).

Sanity: E_A(0.25, 0.25, 0.5) = 2 - sqrt(2) ~ 0.585786 exactly.  The
discriminant (1 - q p_d)^2 - 4 q^2 p_A p_B suffers ~9 digits of
cancellation for the H-sum's parameters (p_B - p_A = 1/k^2, p = 1/k^3),
so everything is evaluated in extended-precision long doubles.

Checks: the two given E_A examples, a direct O(T * range) distribution
DP cross-check at moderate parameters, and H(3) ~ 6.8345 as given.
"""

import numpy as np

LD = np.longdouble


def E_A(pa: LD, pb: LD, p: LD) -> LD:
    q = LD(1) - p
    pd = LD(1) - pa - pb
    b = LD(1) - q * pd
    disc = b * b - LD(4) * q * q * pa * pb
    s = np.sqrt(disc)
    r2 = (b + s) / (LD(2) * q * pa)
    r1 = (b - s) / (LD(2) * q * pa)
    return LD(1) / (q * q * pa * (r2 - r1) * (r2 - LD(1)))


def E_A_dp(pa: float, pb: float, p: float, tmax: int) -> float:
    """Direct distribution DP, truncated at tmax games."""
    q = 1.0 - p
    pd = 1.0 - pa - pb
    off = tmax  # index offset for S = 0
    dist = np.zeros(2 * tmax + 3)
    dist[off] = 1.0
    total = 0.0
    w = 1.0  # q^(t-1)
    for t in range(1, tmax + 1):
        nxt = np.zeros_like(dist)
        nxt[2:] += dist[1:-1] * pa
        nxt[:-2] += dist[1:-1] * pb
        nxt += dist * pd
        nxt[off + 1 - t : off + t][: max(0, 0)] = 0  # no-op clarity
        dist = nxt
        total += w * dist[off + 1 :].sum()
        w *= q
    return total


def H(n: int) -> LD:
    acc = LD(0)
    for k in range(3, n + 1):
        kk = LD(k)
        pa = LD(1) / np.sqrt(kk + LD(3))
        pb = pa + LD(1) / (kk * kk)
        p = LD(1) / (kk * kk * kk)
        acc += E_A(pa, pb, p)
    return acc


if __name__ == "__main__":
    assert abs(E_A(LD(0.25), LD(0.25), LD(0.5)) - (2 - np.sqrt(LD(2)))) < 1e-12
    assert round(float(E_A(LD(0.25), LD(0.25), LD(0.5))), 6) == 0.585786
    assert round(float(E_A(LD(0.47), LD(0.48), LD(0.001))), 6) == 377.471736
    # independent DP check (p large enough for fast truncation)
    dp = E_A_dp(0.3, 0.35, 0.05, 800)
    cf = float(E_A(LD(0.3), LD(0.35), LD(0.05)))
    assert abs(dp - cf) < 1e-9, (dp, cf)
    assert round(float(H(3)), 4) == 6.8345
    print(f"{float(H(50)):.4f}")  # 646231.2177
