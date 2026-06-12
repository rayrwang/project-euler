import math

import numba
import numpy as np

# s(n) = sum_{i<=n} b(i) with b the Rudin-Shapiro sequence.  The visit
# counts C_L(v) = #{i < 2^L : s(i) = v} obey a self-similar recursion: for
# i = 2^(L-1) + r the leading one flips the sign of b exactly while r keeps
# its top bit set, so the running sum over the top half equals S1 + s(r) on
# the bottom quarter and S1 + 2 S2 - s(r) on the top quarter, where
# S_j = s(2^(L-j) - 1) = 2^ceil((L-j)/2).  Hence
#   C_L(v) = C_(L-1)(v) + C_(L-2)(v - S1) + C_(L-1)(u) - C_(L-2)(u)
# with u = S1 + 2 S2 - v, memoised over (L, v), cut off with the classical
# bounds 1 <= s(i) <= sqrt(6 i), and grounded in direct tables for L <= 16.
#
# Splitting [0, m] into aligned binary blocks [B, B + 2^j) (bit j of B is
# zero, so no 11-pair straddles the boundary) gives s(B + q) =
# s(B - 1) + b(B) s(q), so each block contributes one C_j query, and
# g(t, c) is a binary search over m.

BASE_L = 16
KEY = np.int64(1) << 45
# vcap[L] = floor(sqrt(6 * 2^L)), precomputed in plain Python to avoid
# int64 overflow of 6 << L inside the jitted code
VCAP = np.array([math.isqrt(6 << ell) for ell in range(64)], dtype=np.int64)

@numba.jit(cache=True)
def base_tables():
    n = 1 << BASE_L
    s = np.empty(n, dtype=np.int64)
    acc = 0
    for i in range(n):
        pairs = i & (i >> 1)
        bit = 0
        while pairs:
            bit ^= pairs & 1
            pairs >>= 1
        acc += 1 - 2 * bit
        s[i] = acc
    vmax = 700
    base = np.zeros((BASE_L + 1, vmax + 1), dtype=np.int64)
    for length in range(BASE_L + 1):
        for i in range(1 << length):
            base[length, s[i]] += 1
    return base

@numba.jit(cache=True)
def visits(length, v, base, memo):
    # number of i < 2^length with s(i) = v
    if v < 1 or v > VCAP[length]:
        return 0
    if length <= BASE_L:
        if v >= base.shape[1]:
            return 0
        return base[length, v]
    key = length * KEY + v
    if key in memo:
        return memo[key]
    s1 = 1 << ((length - 1 + 1) >> 1)
    s2 = 1 << ((length - 2 + 1) >> 1)
    u = s1 + 2 * s2 - v
    r = (
        visits(length - 1, v, base, memo)
        + visits(length - 2, v - s1, base, memo)
        + visits(length - 1, u, base, memo)
        - visits(length - 2, u, base, memo)
    )
    memo[key] = r
    return r

@numba.jit(cache=True)
def count_up_to(t, m, base, memo):
    # occurrences of t among s(0), ..., s(m)
    x = m + 1
    total = 0
    pref = 0  # s(B - 1) for the running block start B
    flips = 0  # parity of the number of 11-pairs in B
    prev = -2  # position of the lowest set bit of B so far
    for j in range(62, -1, -1):
        if not (x >> j) & 1:
            continue
        sign = 1 - 2 * (flips & 1)
        val = sign * (t - pref)
        total += visits(j, val, base, memo)
        pref += sign << ((j + 1) >> 1)
        if prev == j + 1:
            flips ^= 1
        prev = j
    return total

@numba.jit(cache=True)
def g(t, c, base, memo):
    lo = 0
    hi = np.int64(1) << 62
    while lo < hi:
        mid = (lo + hi) >> 1
        if count_up_to(t, mid, base, memo) >= c:
            hi = mid
        else:
            lo = mid + 1
    return lo

@numba.jit(cache=True)
def total(base):
    memo = {np.int64(0): np.int64(0)}
    assert g(3, 3, base, memo) == 6
    assert g(4, 2, base, memo) == 7
    assert g(54321, 12345, base, memo) == 1220847710
    f2, f1 = 1, 1  # F(0), F(1)
    res = 0
    for _ in range(2, 46):
        f2, f1 = f1, f1 + f2
        res += g(f1, f2, base, memo)
    return res

if __name__ == "__main__":
    print(total(base_tables()))  # 3354706415856332783
