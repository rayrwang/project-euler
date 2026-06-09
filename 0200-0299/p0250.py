import numpy as np
from numba import njit

# Only i^i mod 250 matters, so run a subset-sum DP over the 250 residues:
# dp[j] counts subsets with sum = j (mod 250), and each element of residue r
# maps dp -> dp + shift(dp, r) (include it or not). Values are kept modulo
# 10^16; subtract 1 at the end for the empty subset.

_MOD = 10**16


@njit(cache=True)
def _run(residues: np.ndarray) -> int:
    dp = np.zeros(250, dtype=np.uint64)
    dp[0] = 1
    new = np.empty(250, dtype=np.uint64)
    for r in residues:
        for j in range(250):
            new[(j + r) % 250] = (dp[(j + r) % 250] + dp[j]) % _MOD
        dp[:] = new
    return dp[0]


def solve(count: int = 250250, modulus: int = 250) -> int:
    residues = np.array(
        [pow(i, i, modulus) for i in range(1, count + 1)], dtype=np.int64
    )
    return (int(_run(residues)) - 1) % _MOD


if __name__ == "__main__":
    print(solve())  # 1425480602091519
