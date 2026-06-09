import numba
import numpy as np


@numba.njit(cache=True)
def _counts(limit: int) -> int:
    # x,y,z consecutive AP terms => z = 2y - x, and
    # x^2 - y^2 - z^2 = y(4x - 5y). Put k = 4x - 5y, so n = y*k with
    # x = (5y+k)/4, z = (3y-k)/4: need k < 3y and (y+k) % 4 == 0.
    cnt = np.zeros(limit, dtype=np.int32)
    for y in range(1, limit):
        if y >= limit:
            break
        k = 1
        while k < 3 * y:
            n = y * k
            if n >= limit:
                break
            if (y + k) % 4 == 0:
                cnt[n] += 1
            k += 1
    total = 0
    for n in range(1, limit):
        if cnt[n] == 10:
            total += 1
    return total


def solve(limit: int = 1_000_000) -> int:
    return int(_counts(limit))


if __name__ == "__main__":
    print(solve())  # 4989
