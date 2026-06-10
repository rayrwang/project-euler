"""Project Euler 939: Partisan Nim.

Each player may remove one stone from an opponent's pile or discard one
of their own piles entirely; taking the last stone wins.  E(N) counts
settings with at most N stones in which A wins regardless of who moves
first.

Rule discovery.  Brute-forcing all positions with <= 16 stones shows
the outcome depends only on summary statistics, and threshold tables
reveal a strikingly clean criterion.  Let X = (stones) - (piles) =
sum over piles of (size - 1) for each side, and let Pi be the total
number of piles on the board.  Then A wins under both move orders iff

    X_A >= X_B + 2,   or   (X_A = X_B + 1  and  Pi is odd).

This was verified against the exact game solver on all 17345 settings
with at most 16 stones.

Counting.  Strip one stone from every pile: a side corresponds to a
partition mu (of X) plus a pile count m >= len(mu) (the surplus piles
are 1-piles), with stones = X + m.  Writing c = X + len(mu) and
H[X][c] = #partitions of X with exactly c - X parts, the surplus
m-choices contribute a triangular weight tri(q) in the leftover budget
q = N - c_A - c_B; for the X_A = X_B + 1 case the parity of m_A + m_B
must be odd, which (given the parities baked into c_A + c_B) restricts
the surplus sum's parity and yields a half-triangle weight u(q, C mod 2).
With T = h * h (h[c] = #{mu : |mu| + len(mu) = c}, an O(N^2) Euler
product and convolution), the diagonal kernels

    S(C)  = sum_X (H[X] * H[X])(C),
    K2(C) = sum_X (H[X+1] * H[X])(C)

are thin (support of H[X] is c in [X+1, 2X], so only X <= N/2
contributes), and the off-by->=2 kernel is K1 = (T - S)/2 - K2.  Then
E(N) = sum_C tri(N-C) K1(C) + u(N-C, C mod 2) K2(C).  Total cost is a
few times 1e9 numba operations, about 10 seconds.

Verified against brute force for E(1)..E(16) including the given
E(4) = 9.
"""

import numpy as np
from numba import njit

MOD = 1234567891


@njit(cache=True)
def _build_g(xmax: int) -> np.ndarray:
    g = np.zeros((xmax + 1, xmax + 1), dtype=np.int64)
    g[0][0] = 1
    for x in range(1, xmax + 1):
        for el in range(1, x + 1):
            v = g[x - 1][el - 1]
            if x - el >= 0:
                v += g[x - el][el]
            g[x][el] = v % MOD
    return g


@njit(cache=True)
def _kernels(n: int, g: np.ndarray):
    h = np.zeros(n + 1, dtype=np.int64)
    h[0] = 1
    for j in range(1, n):
        step = j + 1
        for c in range(step, n + 1):
            h[c] = (h[c] + h[c - step]) % MOD
    t_all = np.zeros(n + 1, dtype=np.int64)
    for a in range(n + 1):
        if h[a] == 0:
            continue
        ha = h[a]
        for b in range(n + 1 - a):
            t_all[a + b] = (t_all[a + b] + ha * h[b]) % MOD
    s_diag = np.zeros(n + 1, dtype=np.int64)
    k2 = np.zeros(n + 1, dtype=np.int64)
    half = n // 2
    for x in range(0, half + 1):
        if x == 0:
            s_diag[0] = (s_diag[0] + 1) % MOD
        else:
            lo = x + 1
            hi = min(2 * x, n)
            for ca in range(lo, hi + 1):
                a = g[x][ca - x]
                if a == 0:
                    continue
                for cb in range(lo, min(hi, n - ca) + 1):
                    b = g[x][cb - x]
                    if b:
                        s_diag[ca + cb] = (s_diag[ca + cb] + a * b) % MOD
        y = x + 1
        if y > n:
            continue
        loa = y + 1
        hia = min(2 * y, n)
        if x == 0:
            for ca in range(loa, hia + 1):
                a = g[y][ca - y]
                if a:
                    k2[ca] = (k2[ca] + a) % MOD
        else:
            lob = x + 1
            hib = min(2 * x, n)
            for ca in range(loa, hia + 1):
                a = g[y][ca - y]
                if a == 0:
                    continue
                for cb in range(lob, min(hib, n - ca) + 1):
                    b = g[x][cb - x]
                    if b:
                        k2[ca + cb] = (k2[ca + cb] + a * b) % MOD
    return t_all, s_diag, k2


def e_count(n: int) -> int:
    g = _build_g(n // 2 + 2)
    t_all, s_diag, k2 = _kernels(n, g)
    inv2 = pow(2, MOD - 2, MOD)
    total = 0
    for c in range(0, n + 1):
        r = (t_all[c] - s_diag[c]) % MOD * inv2 % MOD
        k1 = (r - k2[c]) % MOD
        q = n - c
        tri = (q + 1) * (q + 2) // 2 % MOD
        total = (total + tri * k1) % MOD
        c0 = c % 2
        if q >= c0:
            k = (q - c0) // 2 + 1
            u = (k * (c0 + 1) + k * (k - 1)) % MOD
            total = (total + u * k2[c]) % MOD
    return total % MOD


def solve() -> int:
    assert e_count(4) == 9
    assert [e_count(t) for t in (8, 12, 16)] == [161, 1309, 7607]
    return e_count(5000)


if __name__ == "__main__":
    print(solve())  # 246776732
