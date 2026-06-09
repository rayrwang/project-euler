import numba
import numpy as np

from funcs import gcd

@numba.jit(cache=True)
def count_square_interior(m: int) -> int:
    """Count quadrilaterals A(a,0) B(0,b) C(-c,0) D(0,-d), 1<=a,b,c,d<=m,
    whose strictly interior lattice-point count is a perfect square.

    Pick's theorem on the axis-aligned kite gives
        Area = (a+c)(b+d) / 2,
        boundary points = gcd(a,b) + gcd(b,c) + gcd(c,d) + gcd(d,a),
        interior I = Area - boundary/2 + 1.
    """
    g = np.empty((m + 1, m + 1), dtype=np.int64)
    for i in range(m + 1):
        for j in range(m + 1):
            g[i, j] = gcd(i, j)

    max_i = (2 * m) * (2 * m) // 2 + 1
    is_sq = np.zeros(max_i + 1, dtype=np.bool_)
    k = 0
    while k * k <= max_i:
        is_sq[k * k] = True
        k += 1

    count = 0
    for a in range(1, m + 1):
        for b in range(1, m + 1):
            gab = g[a, b]
            for c in range(1, m + 1):
                ac = a + c
                gbc = g[b, c]
                for d in range(1, m + 1):
                    interior = (ac * (b + d) - (gab + gbc + g[c, d] + g[d, a])) // 2 + 1
                    if is_sq[interior]:
                        count += 1
    return count

if __name__ == "__main__":
    assert count_square_interior(4) == 42
    print(count_square_interior(100))  # 694687
