"""Project Euler Problem 645: Every Day Is a Holiday.

The gap-filling rule closes gaps of exactly one day, so the year is all
holidays exactly when the set of drawn birthdays leaves no two cyclically
adjacent days both un-drawn -- the missed set M must be an independent set
of the cycle C_D.  With T the number of emperors needed and
q_k = ((D - k)/D)^t the chance a fixed k-set is missed after t draws,

    P(T <= t) = sum_k N_k * Surj(t, D - k) / D^t,

where N_k = D/(D-k) * binom(D-k, k) counts independent k-sets of C_D and
Surj counts surjections.  Expanding the surjection inclusion-exclusion and
summing E[T] = sum_t P(T > t) as geometric series leaves inner sums of the
form sum_j (-1)^j binom(m, j)/(k + j), which the Beta-integral identity
evaluates to (k-1)! m! / (m+k)!.  Everything collapses to the closed form

    E(D) = D H_D - D^2 sum_{k=1}^{floor(D/2)} r_k / k,
    r_k = (D-k-1)! (D-k)! / ((D-2k)! D!),   r_1 = 1/D,
    r_{k+1}/r_k = (D-2k)(D-2k-1) / ((D-k)(D-k-1)).

All terms are positive (no cancellation) and long-double accumulation gives
far more than the 4 required decimals.  Checks: E(2) = 1, E(5) = 31/6, and
E(365) = 1174.3501 (rounded), all as given.
"""

import numpy as np


def E(D: int) -> float:
    one = np.longdouble(1)
    h = sum(one / k for k in range(1, D + 1))
    total = D * h
    r = one / D  # r_1
    for k in range(1, D // 2 + 1):
        total -= D * D * r / k
        if k < D // 2:
            r *= np.longdouble((D - 2 * k) * (D - 2 * k - 1)) / (
                np.longdouble(D - k) * (D - k - 1)
            )
    return float(total)


if __name__ == "__main__":
    assert abs(E(2) - 1) < 1e-12, E(2)
    assert abs(E(5) - 31 / 6) < 1e-12, E(5)
    assert f"{E(365):.4f}" == "1174.3501", E(365)
    print(f"{E(10000):.4f}")  # 48894.2174
