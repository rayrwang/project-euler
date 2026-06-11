"""Project Euler 499: St. Petersburg Lottery.

A gambler with fortune s repeatedly plays a game costing m: the pot starts at 1
and doubles for every consecutive head; on the first tail he collects the pot.
He wins 2^k with probability 2^-(k+1), and is ruined when his fortune drops
below m. p_m(s) is the probability he is never ruined; find p_15(10^9).

The ruin probability q(s) = 1 - p_m(s) satisfies
    q(s) = sum_k 2^-(k+1) * q(s - m + 2^k),  q(s) = 1 for s < m,  q -> 0.
The truncated mean step at capital scale 2^t is about t/2 - m, which changes
sign at t = 2m - 1 = 29, i.e. right at s ~ 10^9: the problem sits at the
critical scale, so naive iteration mixes far too slowly. Instead we solve the
linear system directly on a hybrid grid: exact integer states m <= s < 2^b,
then a geometric grid with K nodes per octave up to a cutoff 2^T where
q is utterly negligible (super-exponential decay above the critical scale;
T = 36 and T = 42 agree to ten digits). Off-node jump targets are evaluated
with cubic Lagrange interpolation in log2(s). The dense system is solved by
LU, with one round of iterative refinement using extended-precision residuals
to absorb the system's poor conditioning near criticality.
"""

import numpy as np


def survival(m, b, K, T):
    """Return a function s -> p_m(s) on a (2^b, K-per-octave, 2^T) grid."""
    B = 1 << b
    ints = np.arange(m, B, dtype=np.float64)
    geo = np.exp2(b + np.arange(1, K * (T - b) + 1) / K)
    X = np.concatenate([ints, geo])
    U = np.log2(X)
    N = len(X)
    topv = float(1 << T)

    def stencil(t):
        """(lo, weights, const): q(t) ~ weights . q[lo:lo+4] + const."""
        if t < m:
            return -1, None, 1.0
        if t >= topv:
            return -1, None, 0.0
        i = int(np.searchsorted(X, t, side="right")) - 1
        lo = min(max(i - 1, 0), N - 4)
        ut = np.log2(t)
        us = U[lo : lo + 4]
        w = np.empty(4)
        for a in range(4):
            p = 1.0
            for c in range(4):
                if a != c:
                    p *= (ut - us[c]) / (us[a] - us[c])
            w[a] = p
        return lo, w, 0.0

    A = np.zeros((N, N))
    rhs = np.zeros(N)
    for row in range(N - 1):  # last node (s = 2^T) is pinned to q = 0
        x = X[row]
        A[row, row] += 1.0
        k = 0
        while True:
            t = x - m + float(2**k)
            if t >= topv:
                break
            wk = 0.5 ** (k + 1)
            lo, w, const = stencil(t)
            if lo < 0:
                rhs[row] += wk * const
            else:
                A[row, lo : lo + 4] -= wk * w
            k += 1
    A[N - 1, N - 1] = 1.0

    q = np.linalg.solve(A, rhs)
    r = rhs.astype(np.longdouble) - A.astype(np.longdouble) @ q.astype(np.longdouble)
    q = q + np.linalg.solve(A, r.astype(np.float64))

    def p_at(t):
        lo, w, const = stencil(float(t))
        qt = const if lo < 0 else float(np.dot(w, q[lo : lo + 4]))
        return 1.0 - qt

    return p_at


if __name__ == "__main__":
    p2 = survival(2, 8, 128, 24)
    assert round(p2(2), 4) == 0.2522
    assert round(p2(5), 4) == 0.6873
    p6 = survival(6, 10, 192, 32)
    assert round(p6(10**4), 4) == 0.9952

    p15 = survival(15, 10, 224, 36)
    print(f"{p15(10**9):.7f}")  # 0.8660312
