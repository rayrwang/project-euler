import numba
import numpy as np

from funcs import proper_divisor_sum_sieve

@numba.jit(cache=True)
def sum_non_abundant(sds, limit):
    abundant = np.empty(limit + 1, dtype=np.int64)
    n_ab = 0
    for n in range(1, limit + 1):
        if sds[n] > n:
            abundant[n_ab] = n
            n_ab += 1
    can = np.zeros(limit + 1, dtype=np.bool_)
    for i in range(n_ab):
        a = abundant[i]
        for j in range(i, n_ab):
            s = a + abundant[j]
            if s > limit:
                break
            can[s] = True
    total = 0
    for n in range(1, limit + 1):
        if not can[n]:
            total += n
    return total

if __name__ == "__main__":
    # Every integer > 28123 is a sum of two abundant numbers, so that is the cap.
    LIMIT = 28123
    sds = proper_divisor_sum_sieve(LIMIT + 1)
    print(sum_non_abundant(sds, LIMIT))  # 4179871
