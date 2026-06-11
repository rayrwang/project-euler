import numba
import numpy as np

# Binary partitions satisfy b(2n + 1) = b(2n) = b(2n - 1) + b(n), whence the
# classical b(2n) = sum_(j <= n) b(j): the even parts of a partition of 2n
# halve to a partition of some j and the 2(n - j) ones are forced.  Iterating
# the summation operator, S_0 = b and S_r(n) = sum_(j <= n) S_(r-1)(j), the
# family is closed under halving the argument:
#     S_r(2n + 1) = sum_(m <= n) [S_(r-1)(2m) + S_(r-1)(2m + 1)],
#     S_r(2n)     = S_r(2n + 1) - S_(r-1)(2n + 1),
# so if the rows A_r, B_r express S_r(2n), S_r(2n + 1) as combinations of
# the S_j(n), then B_r = shift(A_(r-1) + B_(r-1)) and A_r = B_r - B_(r-1),
# with A_0 = B_0 = e_1.  Processing the binary digits of N most significant
# first therefore needs one extra summation level per digit: a vector of
# bitlength(N) + 2 components, starting from S_r(1) = r + 1, multiplied by
# one of two banded matrices per digit, gives b(N) in O(bits^3) word ops.

MOD = 10**9 + 7


@numba.njit(cache=True)
def direct_table(limit: int, mod: int) -> np.ndarray:
    b = np.empty(limit + 1, dtype=np.int64)
    b[0] = 1
    if limit >= 1:
        b[1] = 1
    for n in range(2, limit + 1):
        b[n] = b[n - 1] if n % 2 else (b[n - 1] + b[n // 2]) % mod
    return b


def build_matrices(k: int, mod: int):
    m0 = np.zeros((k, k), dtype=np.int64)
    m1 = np.zeros((k, k), dtype=np.int64)
    m0[0, 1] = m1[0, 1] = 1
    for r in range(1, k):
        s = (m0[r - 1] + m1[r - 1]) % mod
        m1[r, 1:] = s[:-1]
        m0[r] = (m1[r] - m1[r - 1]) % mod
    lo0 = np.array([int(np.argmax(m0[r] != 0)) for r in range(k)], dtype=np.int64)
    lo1 = np.array([int(np.argmax(m1[r] != 0)) for r in range(k)], dtype=np.int64)
    return m0, m1, lo0, lo1


@numba.njit(cache=True)
def run_bits(m0, m1, lo0, lo1, bits, w, mod):
    k = w.shape[0]
    out = np.empty(k, dtype=np.int64)
    cap = np.int64(1) << 62
    for b in bits:
        m, lo = (m1, lo1) if b else (m0, lo0)
        for r in range(k):
            acc = np.int64(0)
            hi = min(r + 2, k)
            for j in range(lo[r], hi):
                acc += m[r, j] * w[j]
                if acc >= cap:
                    acc %= mod
            out[r] = acc % mod
        w, out = out, w
    return w


def binary_partitions(n: int, mod: int) -> int:
    k = n.bit_length() + 2
    m0, m1, lo0, lo1 = build_matrices(k, mod)
    bits = np.array([int(c) for c in bin(n)[3:]], dtype=np.int64)
    w = np.arange(1, k + 1, dtype=np.int64) % mod  # S_r(1) = r + 1
    w = run_bits(m0, m1, lo0, lo1, bits, w, mod)
    return int(w[0])


if __name__ == "__main__":
    table = direct_table(7**7, MOD)
    assert table[7] == 6  # given p(7) = 6
    assert table[7**7] == 144548435  # given p(7^7) mod 1e9+7
    assert all(binary_partitions(n, MOD) == table[n] for n in range(1, 400))
    assert binary_partitions(7**7, MOD) == 144548435
    print(binary_partitions(7**777, MOD))  # 820442179
