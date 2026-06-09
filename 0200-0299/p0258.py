import numba
import numpy as np

# g_k = g_(k-2000) + g_(k-1999) is a linear recurrence with characteristic
# polynomial x^2000 - x - 1, so g_k = sum_i c_i g_i where
# x^k = sum c_i x^i (mod x^2000 - x - 1, mod 20092010). Since all 2000
# initial terms equal 1, the answer is just the coefficient sum of the
# reduced power. Square-and-multiply on degree-2000 polynomials: schoolbook
# products (coefficients < 2 * 10^7, so 2000-term accumulations stay within
# int64), then the trinomial reduction x^(2000 + j) = x^(j + 1) + x^j.

_MOD = 20_092_010
_D = 2000


@numba.njit(cache=True)
def _mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    c = np.zeros(2 * _D - 1, dtype=np.int64)
    for i in range(_D):
        if a[i] == 0:
            continue
        ai = a[i]
        for j in range(_D):
            c[i + j] += ai * b[j]
        if i % 64 == 63:  # keep far from overflow (sums < 2000 * 4e14)
            for t in range(2 * _D - 1):
                c[t] %= _MOD
    for t in range(2 * _D - 1):
        c[t] %= _MOD
    for j in range(2 * _D - 2, _D - 1, -1):
        if c[j]:
            c[j - 1999] = (c[j - 1999] + c[j]) % _MOD
            c[j - 2000] = (c[j - 2000] + c[j]) % _MOD
            c[j] = 0
    return c[:_D].copy()


def solve(k: int = 10**18) -> int:
    result = np.zeros(_D, dtype=np.int64)
    result[0] = 1  # polynomial 1
    base = np.zeros(_D, dtype=np.int64)
    base[1] = 1  # polynomial x
    e = k
    while e:
        if e & 1:
            result = _mul(result, base)
        e >>= 1
        if e:
            base = _mul(base, base)
    return int(result.sum() % _MOD)


if __name__ == "__main__":
    print(solve())  # 12747994
