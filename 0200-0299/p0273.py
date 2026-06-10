from math import isqrt

import numba
import numpy as np

# Each prime p = 1 (mod 4) splits in Z[i] as pi pibar with pi = x + i y,
# x^2 + y^2 = p. For squarefree N = product of k such primes, the
# representations a^2 + b^2 = N (0 <= a <= b) correspond to the 2^(k-1)
# conjugate-choice classes of prod (pi or pibar) up to units. A DFS over
# the 16 primes below 150 multiplies the canonical pair (a, b) by (x, y)
# in both ways - (|ax - by|, ay + bx) and (|ax + by|, |bx - ay|) - merging
# the two when they coincide (the first prime), and adds min(a, b) at every
# node, summing S(N) over all nonempty subsets at once. Coordinates stay
# below sqrt(prod p) < 10^13, comfortably int64. Verified against direct
# a^2 + b^2 enumeration over all subsets of the first 2, 3 and 4 primes.


@numba.njit(cache=False)
def _dfs(i: int, a: int, b: int, xs: np.ndarray, ys: np.ndarray) -> int:
    total = 0
    for j in range(i, len(xs)):
        x, y = xs[j], ys[j]
        a1, b1 = abs(a * x - b * y), a * y + b * x
        if a1 > b1:
            a1, b1 = b1, a1
        a2, b2 = abs(a * x + b * y), abs(b * x - a * y)
        if a2 > b2:
            a2, b2 = b2, a2
        total += a1 + _dfs(j + 1, a1, b1, xs, ys)
        if (a2, b2) != (a1, b1):
            total += a2 + _dfs(j + 1, a2, b2, xs, ys)
    return total


def solve(limit: int = 150) -> int:
    primes = [
        p for p in range(5, limit, 4) if all(p % q for q in range(2, isqrt(p) + 1))
    ]
    xs = np.empty(len(primes), dtype=np.int64)
    ys = np.empty(len(primes), dtype=np.int64)
    for i, p in enumerate(primes):
        for x in range(1, isqrt(p) + 1):
            y2 = p - x * x
            y = isqrt(y2)
            if y * y == y2:
                xs[i], ys[i] = x, y
                break
    return int(_dfs(0, 0, 1, xs, ys))


if __name__ == "__main__":
    print(solve())  # 2032447591196869022
