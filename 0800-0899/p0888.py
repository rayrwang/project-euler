from itertools import combinations_with_replacement
from math import comb

import numba
import numpy as np

# Single piles form an octal-style take-and-break game: remove 1, 2, 4 or 9
# stones, or split a pile in two, so g(n) is the mex of the g(n - k) and all
# g(a) xor g(n - a).  The sequence is eventually periodic with preperiod 322
# and period 11060, which the Guy-Smith theorem makes rigorous: with largest
# take t = 9, checking g(n + p) = g(n) for i0 <= n <= 2 i0 + 2p + t suffices,
# because any split of a larger n has its big part inside the verified zone.
#
# A multiset of piles is losing iff its Grundy values xor to zero, and since
# v xor v = 0 only the parity of each value's multiplicity matters.  With
# c_v = #{n <= N : g(n) = v} (values fit in 4 bits; 9 never occurs), the
# characters of GF(2)^4 give
#   S(N, m) = 1/16 sum_s [x^m] (1 - x)^(-P_s) (1 + x)^(-Q_s),
# where P_s sums the c_v with <s, v> even and Q_s = N - P_s, each coefficient
# being a length-m alternating convolution of rising binomials.

MOD = 912491249
PREPERIOD = 322
PERIOD = 11060
TAKES = (1, 2, 4, 9)


@numba.njit(cache=True)
def grundy_table(nmax: int) -> np.ndarray:
    g = np.zeros(nmax + 1, dtype=np.int64)
    for n in range(1, nmax + 1):
        seen = np.zeros(64, dtype=np.uint8)
        for k in (1, 2, 4, 9):
            if n >= k:
                seen[g[n - k]] = 1
        for a in range(1, n // 2 + 1):
            seen[g[a] ^ g[n - a]] = 1
        m = 0
        while seen[m]:
            m += 1
        g[n] = m
    return g


def value_counts(g: np.ndarray, n: int) -> list[int]:
    if n < PREPERIOD + PERIOD:
        return [int(x) for x in np.bincount(g[1 : n + 1], minlength=16)]
    pre = np.bincount(g[1:PREPERIOD], minlength=16)
    per = np.bincount(g[PREPERIOD : PREPERIOD + PERIOD], minlength=16)
    full, rem = divmod(n - (PREPERIOD - 1), PERIOD)
    part = np.bincount(g[PREPERIOD : PREPERIOD + rem], minlength=16)
    c = [int(pre[v] + full * per[v] + part[v]) for v in range(16)]
    assert sum(c) == n
    return c


def s_exact(g: np.ndarray, n: int, m: int) -> int:
    """Character sum with exact integers (for the given test values)."""

    def mc(c: int, j: int) -> int:
        return comb(c + j - 1, j) if c > 0 else int(j == 0)

    c = [int(x) for x in np.bincount(g[1 : n + 1], minlength=16)]
    total = 0
    for s in range(16):
        p = sum(c[v] for v in range(16) if (s & v).bit_count() % 2 == 0)
        q = n - p
        total += sum((-1) ** j * mc(q, j) * mc(p, m - j) for j in range(m + 1))
    assert total % 16 == 0
    return total // 16


def s_brute(g: np.ndarray, n: int, m: int) -> int:
    count = 0
    for combo in combinations_with_replacement(range(1, n + 1), m):
        x = 0
        for pile in combo:
            x ^= int(g[pile])
        count += x == 0
    return count


def s_mod(c: list[int], n: int, m: int, mod: int) -> int:
    inv = [0, 1]
    for i in range(2, m + 1):
        inv.append((mod - (mod // i) * inv[mod % i] % mod) % mod)
    total = 0
    for s in range(16):
        p = sum(c[v] for v in range(16) if (s & v).bit_count() % 2 == 0)
        q = n - p
        u = [1] * (m + 1)  # binom(q + j - 1, j), zero for q = 0, j > 0
        w = [1] * (m + 1)  # binom(p + i - 1, i)
        for j in range(1, m + 1):
            u[j] = u[j - 1] * ((q + j - 1) % mod) % mod * inv[j] % mod
            w[j] = w[j - 1] * ((p + j - 1) % mod) % mod * inv[j] % mod
        term = sum((mod - u[j] if j % 2 else u[j]) * w[m - j] for j in range(m + 1))
        total = (total + term) % mod
    return total * pow(16, -1, mod) % mod


if __name__ == "__main__":
    g = grundy_table(2 * PREPERIOD + 3 * PERIOD + 9 + 10)
    # Guy-Smith window: periodicity verified here implies it for all n
    assert all(
        g[n + PERIOD] == g[n]
        for n in range(PREPERIOD, 2 * PREPERIOD + 2 * PERIOD + 9 + 1)
    )
    assert int(g.max()) < 16

    assert s_brute(g, 12, 4) == s_exact(g, 12, 4) == 204  # given
    for n, m in [(7, 3), (15, 5), (20, 3), (9, 6)]:
        assert s_brute(g, n, m) == s_exact(g, n, m)
    assert s_exact(g, 124, 9) == 2259208528408  # given
    assert s_mod(value_counts(g, 124), 124, 9, MOD) == 2259208528408 % MOD
    direct = [int(x) for x in np.bincount(g[1:30001], minlength=16)]
    assert value_counts(g, 30000) == direct

    print(s_mod(value_counts(g, 12491249), 12491249, 1249, MOD))  # 227429102
