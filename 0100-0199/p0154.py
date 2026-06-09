import numba
import numpy as np


def _valuation_factorials(n: int, p: int) -> np.ndarray:
    # f[m] = v_p(m!) via cumulative p-adic valuations of 1..m.
    f = np.zeros(n + 1, dtype=np.int64)
    for m in range(1, n + 1):
        v = 0
        x = m
        while x % p == 0:
            x //= p
            v += 1
        f[m] = f[m - 1] + v
    return f


@numba.njit(cache=True)
def _count(n: int, f2: np.ndarray, f5: np.ndarray, v2n: int, v5n: int) -> int:
    # v_p(n!/(i!j!k!)) = v_p(n!) - v_p(i!) - v_p(j!) - v_p(k!). Need >=12 for
    # p=2 and p=5. Count i<=j<=k with i+j+k=n, weighting by permutations.
    total = 0
    for i in range(n // 3 + 1):
        f2i = f2[i]
        f5i = f5[i]
        jmax = (n - i) // 2
        for j in range(i, jmax + 1):
            k = n - i - j
            if v2n - f2i - f2[j] - f2[k] < 12:
                continue
            if v5n - f5i - f5[j] - f5[k] < 12:
                continue
            if i == j and j == k:
                total += 1
            elif i == j or j == k or i == k:
                total += 3
            else:
                total += 6
    return total


def solve(n: int = 200000) -> int:
    f2 = _valuation_factorials(n, 2)
    f5 = _valuation_factorials(n, 5)
    return int(_count(n, f2, f5, int(f2[n]), int(f5[n])))


if __name__ == "__main__":
    print(solve())  # 479742450
