import numpy as np
from numba import njit


@njit(cache=True)
def _count(n_max: int) -> int:
    # Mark, for each form a^2 + k b^2 (k in {1,2,3,7}), a distinct bit at every
    # representable value; count integers carrying all four bits (value 15).
    flags = np.zeros(n_max + 1, dtype=np.uint8)
    ks = (1, 2, 3, 7)
    for ki in range(4):
        k = ks[ki]
        bit = np.uint8(1 << ki)
        b = 1
        while k * b * b + 1 <= n_max:
            kb2 = k * b * b
            a = 1
            while True:
                v = a * a + kb2
                if v > n_max:
                    break
                flags[v] |= bit
                a += 1
            b += 1
    cnt = 0
    for n in range(1, n_max + 1):
        if flags[n] == 15:
            cnt += 1
    return cnt


def solve(n_max: int = 2_000_000_000) -> int:
    return _count(n_max)


if __name__ == "__main__":
    print(solve())  # 11325263
