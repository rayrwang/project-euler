from math import isqrt

import numpy as np
from numba import njit


@njit(cache=True)
def _block(lo: int, hi: int, ymax: int) -> int:
    """Sum of C(r(V), 3) for V in [lo, hi), where r(V) counts pairs x >= y >= 1 with x^2+y^2 = V."""
    counts = np.zeros(hi - lo, dtype=np.int8)
    for y in range(1, ymax + 1):
        y2 = y * y
        if y2 + y2 >= hi:  # smallest V for this y is 2y^2
            break
        x = y
        if lo - y2 > y2:
            x = int(np.sqrt(lo - y2))
            if x < y:
                x = y
        while x * x + y2 < lo:
            x += 1
        while x * x + y2 < hi:
            counts[x * x + y2 - lo] += 1
            x += 1
    total = 0
    for i in range(hi - lo):
        r = counts[i]
        if r >= 3:
            total += r * (r - 1) * (r - 2) // 6
    return total


def solve(n: int = 10**10, block: int = 50_000_000) -> int:
    """Number of biclinic integral quadrilaterals with AB^2+BC^2+CD^2+AD^2 <= n.

    With O the midpoint of BD and AO = CO = a, BO = DO = d, the median (parallelogram) law gives
    AB^2+AD^2 = BC^2+CD^2 = 2(a^2+d^2), so the side-square sum is 4(a^2+d^2) <= n. Placing O at the
    origin with B, D on the x-axis, a side pair (p, q) of A corresponds to a representation
    p^2+q^2 = 2(a^2+d^2); halving via (p,q) = (u-w, u+w) turns these into representations
    u^2+w^2 = a^2+d^2. So a quadrilateral is three distinct representations of a common
    V = a^2+d^2 = x^2+y^2: the one with the smallest x-y plays (d, a) (the always-present, here
    excluded, degenerate split), and the other two give the nested side pairs. Each rep has a
    distinct x-y, so the count for a given V is exactly C(r(V), 3) with r(V) the number of
    representations x >= y >= 1. Summing C(r(V), 3) for V <= n/4, done in memory-bounded blocks,
    gives B. The checks B(10^4) = 49 and B(10^6) = 38239 confirm the formula."""
    limit = n // 4
    total = 0
    lo = 2
    while lo <= limit:
        hi = min(lo + block, limit + 1)
        total += _block(lo, hi, isqrt(hi) + 1)
        lo = hi
    return total


if __name__ == "__main__":
    assert solve(10_000, block=3_000) == 49
    assert solve(1_000_000, block=300_000) == 38239
    print(solve())  # 2466018557
