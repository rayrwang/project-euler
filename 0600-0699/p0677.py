"""Project Euler Problem 677: Coloured Graphs.

Count unlabeled trees with nodes colored red/blue/yellow, degree caps 4
for red and 3 for blue and yellow, and no yellow-yellow edge.

Planted generating functions (root hanging from an edge, so one slot is
used upward): with F = f_R + f_B + f_Y and F_Y = f_R + f_B (yellow cannot
have yellow children),

    f_R = x M_3(F),   f_B = x M_2(F),   f_Y = x M_2(F_Y),

where M_k is the multiset-of-size-<=-k operator from the cycle index of
the symmetric groups, e.g. M_2(F) = 1 + F + (F^2 + F(x^2)) / 2.  These
implicit equations are solved degree by degree, each step extending the
running convolutions F^2, F^3, F F(x^2), and the F_Y analogues by one
coefficient.

Vertex-rooted trees use the full caps, g_R = x M_4(F), g_B = x M_3(F),
g_Y = x M_3(F_Y).  By the dissimilarity theorem (vertex orbits minus
edge orbits plus [tree has a symmetry edge] equals 1 for every tree),

    g(n) = [x^n] ( g_R + g_B + g_Y - f_R f_B - f_R f_Y - f_B f_Y
                   - (f_R^2 - f_R(x^2)) / 2 - (f_B^2 - f_B(x^2)) / 2 ),

the edge-rooted classes being unordered compatible pairs of planted
trees (no Y-Y), and symmetry edges existing only for R-R and B-B.

Verified: g(2) = 5, g(3) = 15, g(4) = 57, g(10) = 710249 and
g(100) = 919747298 mod 10^9 + 7 from the statement -- five anchors
spanning the small cases and a large modular value.
"""

import numba
import numpy as np

N = 10**4
MOD = 1_000_000_007
INV2 = pow(2, MOD - 2, MOD)
INV6 = pow(6, MOD - 2, MOD)
INV24 = pow(24, MOD - 2, MOD)


@numba.jit(nogil=True)
def planted(n: int, mod: int, inv2: int, inv6: int):
    """f_R, f_B, f_Y plus the running convolutions of F and F_Y."""
    f_r = np.zeros(n + 1, dtype=np.int64)
    f_b = np.zeros(n + 1, dtype=np.int64)
    f_y = np.zeros(n + 1, dtype=np.int64)
    big = np.zeros(n + 1, dtype=np.int64)     # F
    big_y = np.zeros(n + 1, dtype=np.int64)   # F_Y
    f2 = np.zeros(n + 1, dtype=np.int64)      # F^2
    f3 = np.zeros(n + 1, dtype=np.int64)      # F^3
    ff2 = np.zeros(n + 1, dtype=np.int64)     # F * F(x^2)
    y2 = np.zeros(n + 1, dtype=np.int64)      # F_Y^2
    y3 = np.zeros(n + 1, dtype=np.int64)      # F_Y^3
    yy2 = np.zeros(n + 1, dtype=np.int64)     # F_Y * F_Y(x^2)
    for deg in range(1, n + 1):
        m = deg - 1
        s = 0
        for i in range(m + 1):
            s += big[i] * big[m - i] % mod
        f2[m] = s % mod
        s = 0
        for i in range(m + 1):
            s += f2[i] * big[m - i] % mod
        f3[m] = s % mod
        s = 0
        for j in range(m // 2 + 1):
            s += big[j] * big[m - 2 * j] % mod
        ff2[m] = s % mod
        s = 0
        for i in range(m + 1):
            s += big_y[i] * big_y[m - i] % mod
        y2[m] = s % mod
        s = 0
        for i in range(m + 1):
            s += y2[i] * big_y[m - i] % mod
        y3[m] = s % mod
        s = 0
        for j in range(m // 2 + 1):
            s += big_y[j] * big_y[m - 2 * j] % mod
        yy2[m] = s % mod

        sq = big[m // 2] if m % 2 == 0 else 0
        sq_y = big_y[m // 2] if m % 2 == 0 else 0
        cube = big[m // 3] if m % 3 == 0 else 0
        m2 = ((1 if m == 0 else 0) + big[m] + (f2[m] + sq) * inv2) % mod
        m3 = (m2 + (f3[m] + 3 * ff2[m] + 2 * cube) * inv6) % mod
        m2y = ((1 if m == 0 else 0) + big_y[m]
               + (y2[m] + sq_y) * inv2) % mod
        f_r[deg] = m3
        f_b[deg] = m2
        f_y[deg] = m2y
        big[deg] = (m3 + m2 + m2y) % mod
        big_y[deg] = (m3 + m2) % mod
    return f_r, f_b, f_y, big, big_y, f2, f3, ff2, y2, y3, yy2


@numba.jit(nogil=True)
def conv(a: np.ndarray, b: np.ndarray, n: int, mod: int) -> np.ndarray:
    out = np.zeros(n + 1, dtype=np.int64)
    for i in range(n + 1):
        if a[i] == 0:
            continue
        ai = a[i]
        for j in range(n + 1 - i):
            out[i + j] = (out[i + j] + ai * b[j]) % mod
    return out


@numba.jit(nogil=True)
def conv_stretch(a: np.ndarray, b: np.ndarray, k: int, n: int,
                 mod: int) -> np.ndarray:
    """a(x) * b(x^k) truncated to degree n."""
    out = np.zeros(n + 1, dtype=np.int64)
    for j in range(n // k + 1):
        bj = b[j]
        if bj == 0:
            continue
        for i in range(n + 1 - k * j):
            out[i + k * j] = (out[i + k * j] + a[i] * bj) % mod
    return out


def g_series(n: int) -> np.ndarray:
    f_r, f_b, f_y, big, big_y, f2, f3, ff2, y2, y3, yy2 = planted(
        n, MOD, INV2, INV6
    )

    def shift(arr: np.ndarray) -> np.ndarray:
        out = np.zeros(n + 1, dtype=np.int64)
        out[1:] = arr[:-1]
        return out

    def stretch(arr: np.ndarray, k: int) -> np.ndarray:
        out = np.zeros(n + 1, dtype=np.int64)
        out[:: k][: len(arr[: n // k + 1])] = arr[: n // k + 1]
        return out

    def m3_of(b_arr, b2, b3, bb2):
        sq = stretch(b_arr, 2)
        cube = stretch(b_arr, 3)
        one = np.zeros(n + 1, dtype=np.int64)
        one[0] = 1
        m2 = (one + b_arr + (b2 + sq) * INV2) % MOD
        return (m2 + (b3 + 3 * bb2 + 2 * cube) * INV6) % MOD

    g_b = shift(m3_of(big, f2, f3, ff2))
    g_y = shift(m3_of(big_y, y2, y3, yy2))
    # M4 extra term for red roots
    f4 = conv(f2, f2, n, MOD)
    f2_f2x = conv_stretch(f2, big, 2, n, MOD)  # F^2 * F(x^2) ... see below
    # careful: F^2 * F(x^2): conv_stretch(a=F^2, b=F, k=2)
    sq2 = stretch(f2, 2)  # (F(x^2))^2 = (F^2)(x^2)
    f_f3x = conv_stretch(big, big, 3, n, MOD)  # F * F(x^3)
    f4x = stretch(big, 4)
    extra = (f4 + 6 * f2_f2x + 3 * sq2 + 8 * f_f3x + 6 * f4x) % MOD
    g_r = shift((m3_of(big, f2, f3, ff2) + extra * INV24) % MOD)

    pairs = (
        conv(f_r, f_b, n, MOD) + conv(f_r, f_y, n, MOD)
        + conv(f_b, f_y, n, MOD)
        + (conv(f_r, f_r, n, MOD) - stretch(f_r, 2)) * INV2
        + (conv(f_b, f_b, n, MOD) - stretch(f_b, 2)) * INV2
    ) % MOD
    return (g_r + g_b + g_y - pairs) % MOD


if __name__ == "__main__":
    series = g_series(110)
    assert series[2] == 5 and series[3] == 15 and series[4] == 57
    assert series[10] == 710249
    assert series[100] == 919747298
    full = g_series(N)
    assert (full[:111] == series).all()
    print(int(full[N]))  # 984183023
