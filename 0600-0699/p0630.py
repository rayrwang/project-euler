"""Project Euler Problem 630: Crossed Lines.

Generate the 2500 pseudo-random points and canonicalise the line through
every pair as A x + B y = C with A = y2 - y1, B = x1 - x2, C = A x1 + B y1,
divided by gcd(A, B, C) and sign-fixed so the first nonzero of (A, B) is
positive.  Distinct triples are distinct lines, giving M(L).

Two distinct lines cross exactly when they are not parallel, so

    S(L) = M (M - 1) - sum_d c_d (c_d - 1),

where c_d counts lines in each parallel class d = (A, B) / gcd(A, B),
sign-fixed.  Both the line triple and the direction pair are packed into a
single int64 key, so the 3.1 million pairs reduce to two numpy unique scans.

Checks: M(L_3) = 3 and S(L_3) = 6; M(L_100) = 4948 and S(L_100) = 24477690.
"""

import numba
import numpy as np


def points(n: int) -> tuple[np.ndarray, np.ndarray]:
    s, xs, ys, seen = 290797, [], [], set()
    for _ in range(n):
        s = s * s % 50515093
        x = s % 2000 - 1000
        s = s * s % 50515093
        y = s % 2000 - 1000
        if (x, y) not in seen:
            seen.add((x, y))
            xs.append(x)
            ys.append(y)
    return np.array(xs, dtype=np.int64), np.array(ys, dtype=np.int64)


@numba.jit(cache=True)
def line_keys(xs: np.ndarray, ys: np.ndarray) -> np.ndarray:
    """One packed (A, B, C) key per pair of points."""
    n = len(xs)
    keys = np.empty(n * (n - 1) // 2, dtype=np.int64)
    idx = 0
    for i in range(n):
        for j in range(i + 1, n):
            a = ys[j] - ys[i]
            b = xs[i] - xs[j]
            c = a * xs[i] + b * ys[i]
            g = np.gcd(np.gcd(abs(a), abs(b)), abs(c))
            a, b, c = a // g, b // g, c // g
            if a < 0 or (a == 0 and b < 0):
                a, b, c = -a, -b, -c
            keys[idx] = ((a + 2000) * 4001 + (b + 2000)) * 8000001 + c + 4000000
            idx += 1
    return keys


def M_and_S(xs: np.ndarray, ys: np.ndarray) -> tuple[int, int]:
    lines = np.unique(line_keys(xs, ys))
    directions = lines // 8000001  # the packed (A, B, C) key sans C is (A, B)
    # parallel classes still need (A, B) itself reduced by gcd(A, B):
    a = directions // 4001 - 2000
    b = directions % 4001 - 2000
    g = np.gcd(np.abs(a), np.abs(b))
    a, b = a // g, b // g
    flip = (a < 0) | ((a == 0) & (b < 0))
    a, b = np.where(flip, -a, a), np.where(flip, -b, b)
    _, counts = np.unique(a * 4001 + b, return_counts=True)
    m = len(lines)
    return m, m * (m - 1) - int(np.sum(counts * (counts - 1)))


if __name__ == "__main__":
    xs, ys = points(2500)
    assert (xs[0], ys[0]) == (527, 144) and (xs[1], ys[1]) == (-488, 732)
    assert M_and_S(xs[:3], ys[:3]) == (3, 6)
    assert M_and_S(xs[:100], ys[:100]) == (4948, 24477690)
    print(M_and_S(xs, ys)[1])  # 9669182880384
