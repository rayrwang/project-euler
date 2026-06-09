import numba
import numpy as np


@numba.njit(cache=True)
def _sum_hits(n: int, rad: np.ndarray, order: np.ndarray) -> int:
    total = 0
    for a in range(1, n):
        ra = rad[a]
        for idx in range(order.shape[0]):
            b = order[idx]
            rb = rad[b]
            if ra * rb >= n:  # rad(a)rad(b) >= n > c can never be an abc-hit
                break
            if b <= a:
                continue
            c = a + b
            if c >= n:
                continue
            if ra * rb * rad[c] < c:  # rad(abc)=rad(a)rad(b)rad(c) when coprime
                x, y = a, b
                while y:
                    x, y = y, x % y
                if x == 1:  # gcd(a,b)=1 => a,b,c pairwise coprime
                    total += c
    return total


def solve(n: int = 120000) -> int:
    rad = np.ones(n, dtype=np.int64)
    for i in range(2, n):
        if rad[i] == 1:  # i prime
            rad[i::i] *= i
    order = np.argsort(rad, kind="stable").astype(np.int64)
    return int(_sum_hits(n, rad, order))


if __name__ == "__main__":
    print(solve())  # 18407904
