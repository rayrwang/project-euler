import numba
import numpy as np


@numba.njit(cache=True)
def _mdrs_sum(limit: int) -> int:
    # mdrs(n) = max over factorisations into factors > 1 of the sum of digital
    # roots. dr(n) = 1 + (n-1) % 9. Process n increasingly: every split n = a*b
    # has a, b < n already finalised, so mdrs(n) = max(dr(n), max_a mdrs(a)+mdrs(n/a)).
    mdrs = np.empty(limit, dtype=np.int64)
    mdrs[0] = 0
    if limit > 1:
        mdrs[1] = 0
    total = 0
    for n in range(2, limit):
        best = 1 + (n - 1) % 9  # dr(n)
        a = 2
        while a * a <= n:
            if n % a == 0:
                cand = mdrs[a] + mdrs[n // a]
                if cand > best:
                    best = cand
            a += 1
        mdrs[n] = best
        total += best
    return total


def solve(limit: int = 1_000_000) -> int:
    return int(_mdrs_sum(limit))


if __name__ == "__main__":
    print(solve())  # 14489159
