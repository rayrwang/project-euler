"""Project Euler 476: Circle Packing II.

R(a, b, c) is the maximum total area of three non-overlapping circles inside a
triangle with sides a, b, c; S(n) averages R over integer triples with
1 <= a <= b <= c < a + b <= n. Find S(1803) to 5 decimal places.

For three circles in a triangle the greedy packing is optimal (Zalgaller-Los;
it always beats Malfatti's circles): take the incircle of radius r, then the
largest circle in a corner gap - a circle tangent to the incircle and the two
sides of corner angle theta has radius r * k(theta) with
    k(theta) = (1 - sin(theta/2)) / (1 + sin(theta/2)),
which is largest at the smallest angle A (opposite the shortest side a). The
third circle is the better of the next corner gap, r * k(B), and the gap
nested deeper in corner A beyond the second circle, r * k(A)^2. Hence
    R = pi r^2 (1 + k_A^2 + max(k_B, k_A^2)^2).
Half-angle identities give sin(A/2) = sqrt((s-b)(s-c)/(bc)) etc., so each
triple needs only square roots. The ~2.4e8 triples are summed with numba.
"""

import numpy as np
from numba import njit, prange


@njit(parallel=True, cache=True)
def total_and_count(n):
    total = 0.0
    count = 0
    for a in prange(1, n // 2 + 1):  # ty: ignore[not-iterable]
        sub = 0.0
        cnt = 0
        for b in range(a, n - a + 1):
            for c in range(b, a + b):
                s = (a + b + c) / 2.0
                sa, sb, sc = s - a, s - b, s - c
                r2 = sa * sb * sc / s
                sin_ha = np.sqrt(sb * sc / (b * c))
                sin_hb = np.sqrt(sa * sc / (a * c))
                ka = (1.0 - sin_ha) / (1.0 + sin_ha)
                kb = (1.0 - sin_hb) / (1.0 + sin_hb)
                k3 = max(kb, ka * ka)
                sub += r2 * (1.0 + ka * ka + k3 * k3)
                cnt += 1
        total += sub
        count += cnt
    return np.pi * total, count


def S(n):
    total, count = total_and_count(n)
    return total / count


if __name__ == "__main__":
    assert round(S(2), 5) == 0.31998
    assert round(S(5), 5) == 1.25899
    print(f"{S(1803):.5f}")  # 110242.87794
