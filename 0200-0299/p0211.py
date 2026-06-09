import numpy as np
from numba import njit


@njit(cache=True)
def _sigma2_sieve(n: int) -> np.ndarray:
    # sigma2[k] = sum of squares of divisors of k, via a divisor sieve.
    sig = np.ones(n, dtype=np.int64)
    for d in range(2, n):
        dd = d * d
        for m in range(d, n, d):
            sig[m] += dd
    return sig


def solve(limit: int = 64_000_000) -> int:
    sig = _sigma2_sieve(limit)
    vals = sig[1:limit]
    root = np.sqrt(vals.astype(np.float64)).astype(np.int64)
    mask = np.zeros(len(vals), dtype=bool)
    for off in (-2, -1, 0, 1, 2):
        rr = root + off
        mask |= rr * rr == vals
    idx = np.nonzero(mask)[0] + 1
    return int(idx.sum(dtype=np.int64))


if __name__ == "__main__":
    print(solve())  # 1922364685
