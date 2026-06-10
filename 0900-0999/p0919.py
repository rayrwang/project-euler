"""Project Euler 919: Fortunate Triangles.

Every vertex is at distance R (the circumradius) from the circumcentre,
and at distance 2R|cos theta| from the orthocentre, where theta is the
angle at that vertex.  So a triangle is fortunate iff some angle has
cos theta = +-1/4; by the law of cosines, with z the side opposite that
angle, 2(x^2 + y^2 - z^2) = +- x y, i.e.

    2x^2 + eps x y + 2y^2 = 2z^2,        eps = +-1.

(Check (6,7,8): cos of the angle opposite 8 is 21/84 = 1/4.)  Each
equation is a conic through (x:y:z) = (1:0:1); the chord through it
with slope -p/q parametrises all rational points:

    (x, y, z) ~ (2(p^2 - q^2),  p(4q - eps p),  2p^2 - eps p q + 2q^2),

with gcd(p, q) = 1, q < p, and additionally 4q > p when eps = +1 for
positivity.  The parametrised perimeter is (4 - eps) p (p + q) and the
content gcd of the triple always divides 30, so enumerating
(4 - eps) p (p + q) <= 30 P captures every primitive fortunate triangle
of perimeter at most P.  Primitives from the two families are merged
and deduplicated (a triangle can be fortunate at several vertices),
and each contributes per * K(K + 1)/2 with K = floor(P / per).  The
parametrisation was checked to reproduce the exact brute-force
primitive sets, and S(P) agrees with brute force for P <= 1000,
including the given S(10) = 24 and S(100) = 3331.
"""

import numba
import numpy as np


@numba.njit(cache=True)
def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _gen_prims(perim_max, eps):
    cap = 30 * perim_max
    out = []
    p = 1
    while (4 - eps) * p * (p + 1) <= cap:
        qlo = p // 4 + 1 if eps == 1 else 1
        for q in range(qlo, p):
            if (4 - eps) * p * (p + q) > cap:
                break
            if _gcd(p, q) != 1:
                continue
            x = 2 * (p * p - q * q)
            y = p * (4 * q - eps * p)
            z = 2 * p * p - eps * p * q + 2 * q * q
            if x <= 0 or y <= 0:
                continue
            g = _gcd(_gcd(x, y), z)
            x //= g
            y //= g
            z //= g
            if x + y + z <= perim_max:
                a, b, c = x, y, z
                if a > b:
                    a, b = b, a
                if b > c:
                    b, c = c, b
                if a > b:
                    a, b = b, a
                out.append((a, b, c))
        p += 1
    res = np.empty((len(out), 3), dtype=np.int64)
    for i, t in enumerate(out):
        res[i, 0] = t[0]
        res[i, 1] = t[1]
        res[i, 2] = t[2]
    return res


def solve(perim_max: int) -> int:
    arr = np.vstack([_gen_prims(perim_max, 1), _gen_prims(perim_max, -1)])
    order = np.lexsort((arr[:, 2], arr[:, 1], arr[:, 0]))
    arr = arr[order]
    keep = np.ones(len(arr), dtype=bool)
    keep[1:] = (arr[1:] != arr[:-1]).any(axis=1)
    arr = arr[keep]
    per = arr.sum(axis=1)
    k = perim_max // per
    return int((per * (k * (k + 1) // 2)).sum())


def _is_fortunate(a: int, b: int, c: int) -> bool:
    for x, y, z in ((a, b, c), (a, c, b), (b, c, a)):
        d = 2 * (x * x + y * y - z * z)
        if d == x * y or d == -x * y:
            return True
    return False


def brute(perim_max: int) -> int:
    tot = 0
    for a in range(1, perim_max // 3 + 1):
        for b in range(a, (perim_max - a) // 2 + 1):
            for c in range(b, perim_max - a - b + 1):
                if c < a + b and _is_fortunate(a, b, c):
                    tot += a + b + c
    return tot


if __name__ == "__main__":
    assert brute(10) == 24 and brute(100) == 3331  # givens
    for p in (10, 100, 400, 1000):
        assert solve(p) == brute(p), p
    print(solve(10**7))  # 134222859969633
