import numba
import numpy as np


@numba.njit(cache=True)
def _count_singletons(limit: int) -> int:
    # Same reduction as Problem 135: solutions of x^2-y^2-z^2=n (AP terms)
    # correspond to pairs n=y*k with k<3y and (y+k)%4==0. Tally each n,
    # saturating at 2 (we only need 0/1/many), then count tallies equal to 1.
    cnt = np.zeros(limit, dtype=np.int8)
    for y in range(1, limit):
        if y >= limit:
            break
        k = 1
        while k < 3 * y:
            n = y * k
            if n >= limit:
                break
            if (y + k) % 4 == 0 and cnt[n] < 2:
                cnt[n] += 1
            k += 1
    total = 0
    for n in range(1, limit):
        if cnt[n] == 1:
            total += 1
    return total


def solve(limit: int = 50_000_000) -> int:
    return int(_count_singletons(limit))


if __name__ == "__main__":
    print(solve())  # 2544559
