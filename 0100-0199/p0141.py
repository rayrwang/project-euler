import math

import numba
import numpy as np


@numba.njit(cache=True)
def _isqrt(n: int) -> int:
    r = int(math.sqrt(n))
    while r * r > n:
        r -= 1
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _fill(limit: int, out: np.ndarray) -> int:
    # q,d,r in GP with q the geometric mean: r=a c^2, q=a c e, d=a e^2 (e>c,
    # coprime). Then n = q d + r = a^2 c e^3 + a c^2. Keep the perfect squares.
    cnt = 0
    e = 2
    while e * e * e < limit:
        for c in range(1, e):
            if _gcd(c, e) == 1:
                ce3 = c * e * e * e
                c2 = c * c
                a = 1
                while True:
                    n = a * a * ce3 + a * c2
                    if n >= limit:
                        break
                    r = _isqrt(n)
                    if r * r == n:
                        out[cnt] = n
                        cnt += 1
                    a += 1
        e += 1
    return cnt


def solve(limit: int = 10**12) -> int:
    out = np.zeros(100000, dtype=np.int64)
    cnt = _fill(limit, out)
    return int(sum(set(int(x) for x in out[:cnt])))


if __name__ == "__main__":
    print(solve())  # 878454337159
