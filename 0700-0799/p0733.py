import numba
import numpy as np

MOD = 10**9 + 7

@numba.njit(cache=True)
def solve(n):
    """S(n): sum over all ascending 4-term subsequences of a_1..a_n of the
    sum of their terms, where a_i = 153^i mod 10000019. Answer mod 10^9 + 7.

    Sweep left to right keeping, for each length L = 1..4, Fenwick trees over
    (rank-compressed) values storing the number of ascending L-subsequences
    ending below a given value, and the total of their term-sums. When a_i
    arrives, length-L subsequences ending at a_i are built from length-(L-1)
    ones with smaller last value:
        cnt_L  = cnt_(L-1)(< a_i)
        sum_L  = sum_(L-1)(< a_i) + a_i * cnt_(L-1)(< a_i).
    The answer accumulates sum_4 over all i.
    """
    m = 10_000_019
    a = np.empty(n, dtype=np.int64)
    x = 1
    for i in range(n):
        x = x * 153 % m
        a[i] = x

    # Rank-compress values to 1..k.
    order = np.argsort(a)
    rank = np.empty(n, dtype=np.int64)
    k = 0
    prev = -1
    for idx in order:
        if a[idx] != prev:
            k += 1
            prev = a[idx]
        rank[idx] = k

    cnt = np.zeros((5, k + 1), dtype=np.int64)  # Fenwick trees, levels 1..4
    tot = np.zeros((5, k + 1), dtype=np.int64)

    answer = 0
    for i in range(n):
        r = rank[i]
        v = a[i] % MOD
        # Query strictly-below prefix [1, r-1] for levels 1..3.
        c = np.zeros(4, dtype=np.int64)
        s = np.zeros(4, dtype=np.int64)
        j = r - 1
        while j > 0:
            for lvl in range(1, 4):
                c[lvl] = (c[lvl] + cnt[lvl, j]) % MOD
                s[lvl] = (s[lvl] + tot[lvl, j]) % MOD
            j -= j & (-j)
        # New subsequences ending at a_i, per level.
        new_c = np.zeros(5, dtype=np.int64)
        new_s = np.zeros(5, dtype=np.int64)
        new_c[1] = 1
        new_s[1] = v
        for lvl in range(2, 5):
            new_c[lvl] = c[lvl - 1]
            new_s[lvl] = (s[lvl - 1] + v * c[lvl - 1]) % MOD
        answer = (answer + new_s[4]) % MOD
        j = r
        while j <= k:
            for lvl in range(1, 4):
                cnt[lvl, j] = (cnt[lvl, j] + new_c[lvl]) % MOD
                tot[lvl, j] = (tot[lvl, j] + new_s[lvl]) % MOD
            j += j & (-j)
    return answer

if __name__ == "__main__":
    assert solve(6) == 94513710
    assert solve(100) == 4465488724217 % MOD
    print(solve(10**6))  # 574368578
