from math import gcd, isqrt

import numpy as np

# Up to translation, a convex polygon with no three collinear vertices is
# exactly a multiset of edge vectors with pairwise distinct directions
# summing to zero (sorting by angle reconstructs it); integer edge lengths
# make each vector k (a, b) with a^2 + b^2 a perfect square. Splitting the
# angle-sorted edge cycle at -90 deg (inclusive) and +90 deg gives a right
# chain over directions {dx > 0} union {(0, -1)} and a left chain over
# their negations, so left chains are negated right chains and
#     P(n) = sum_(X, Y, p1 + p2 <= n) R(X, Y, p1) R(X, Y, p2)
#            - 1 (empty + empty) - #(2-gons: single edge with 2 len <= n),
# where R counts right chains by displacement and perimeter, built by a
# take-at-most-one knapsack over each direction's length multiples with
# numpy shifted adds. Verified against the given P(4) = 1, P(30) = 3655,
# P(60) = 891045.


def solve(n: int = 120) -> int:
    dirs = [(0, -1, 1), (1, 0, 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if gcd(a, b) != 1:
                continue
            c = isqrt(a * a + b * b)
            if c * c == a * a + b * b and c <= n:
                dirs.append((a, b, c))
                dirs.append((a, -b, c))
    ny = 2 * n + 1
    r = np.zeros((n + 1, ny, n + 1), dtype=np.int64)
    r[0, n, 0] = 1
    for a, b, c in dirs:
        out = r.copy()
        k = 1
        while k * c <= n:
            ka, kb, kc = k * a, k * b, k * c
            if kb >= 0:
                ys, ys_src = slice(kb, ny), slice(0, ny - kb)
            else:
                ys, ys_src = slice(0, ny + kb), slice(-kb, ny)
            out[ka:, ys, kc:] += r[: n + 1 - ka, ys_src, : n + 1 - kc]
            k += 1
        r = out
    rcum = np.cumsum(r, axis=2)
    total = 0
    for p1 in range(n + 1):
        total += int(np.einsum("xy,xy->", r[:, :, p1], rcum[:, :, n - p1]))
    total -= 1
    for _a, _b, c in dirs:
        k = 1
        while 2 * k * c <= n:
            total -= 1
            k += 1
    return total


if __name__ == "__main__":
    print(solve())  # 3600060866
