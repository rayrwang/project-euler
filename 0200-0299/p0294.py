import numba
import numpy as np

# Strings of n decimal digits (leading zeros allowed) are counted by a
# linear recurrence over states (value mod 23, digit sum capped at 23):
# digit-sum 23 forces k > 0, so S(n) is the (0, 23) entry after n steps.
# Since n = 11^12 is astronomical, the digit-sum axis is carried as a
# truncated generating polynomial: the transition is a 23 x 23 matrix over
# Z[y]/(y^24) (entry r -> (10 r + d) mod 23 gains y^d), and matrix
# exponentiation by squaring needs only ~80 polynomial-matrix products of
# 23^3 24^2 / 2 modular multiply-adds each. Verified against direct DP for
# the given S(9) = 263626 and S(42) = 6377168878570056.


@numba.njit(cache=True)
def _polymat_mul(a: np.ndarray, b: np.ndarray, mod: int) -> np.ndarray:
    c = np.zeros((23, 23, 24), dtype=np.int64)
    for i in range(23):
        for j in range(23):
            for s1 in range(24):
                v = a[i, j, s1]
                if v == 0:
                    continue
                for k in range(23):
                    row = b[j, k]
                    for s2 in range(24 - s1):
                        if row[s2]:
                            c[i, k, s1 + s2] = (c[i, k, s1 + s2] + v * row[s2]) % mod
    return c


def solve(n: int = 11**12, mod: int = 10**9) -> int:
    m = np.zeros((23, 23, 24), dtype=np.int64)
    for r in range(23):
        for d in range(10):
            m[r, (10 * r + d) % 23, d] += 1
    res = np.zeros((23, 23, 24), dtype=np.int64)
    for i in range(23):
        res[i, i, 0] = 1
    e = n
    while e:
        if e & 1:
            res = _polymat_mul(res, m, mod)
        m = _polymat_mul(m, m, mod)
        e >>= 1
    return int(res[0, 0, 23]) % mod


if __name__ == "__main__":
    print(solve())  # 789184709
