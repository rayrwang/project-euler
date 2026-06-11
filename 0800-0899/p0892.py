from collections import defaultdict
from math import comb

import numba
import numpy as np

# The chords of a cutting are non-crossing, so the pieces and chord
# adjacencies form the dual rooted plane tree with n edges (rooting at the
# piece next to a fixed boundary arc makes this the classical bijection,
# Catalan many on each side).  The alternating colouring is the bipartition
# of that tree by depth parity, so d(C) = |#even-depth - #odd-depth|.
#
# Computing the distribution of k = E - O over all rooted plane trees via
# A(x, u) = u / (1 - x A(x, 1/u)) reveals it to be the Narayana numbers:
# trees with n edges and E even-level vertices are counted by N(n, E)
# (even-level vertices are equidistributed with leaves).  Summing
# |2E - n - 1| N(n, E) collapses to closed forms,
#     D(n) = binom(n, n/2)^2 / 2                       for even n,
#     D(n) = (n^2 - 1) binom(n, (n-1)/2)^2 / (2 n^2)   for odd n,
# verified below against the exact tree DP and the given D(3) and D(100).

MOD = 1234567891
N = 10**7


def tree_dp(nmax: int) -> list[int]:
    """Exact D(n) for small n from the plane-tree generating recursion."""
    even = [defaultdict(int) for _ in range(nmax + 1)]
    odd = [defaultdict(int) for _ in range(nmax + 1)]
    even[0][1] = 1
    odd[0][-1] = 1
    for n in range(1, nmax + 1):
        for i in range(n):
            for k1, c1 in odd[i].items():
                for k2, c2 in even[n - 1 - i].items():
                    even[n][k1 + k2] += c1 * c2
            for k1, c1 in even[i].items():
                for k2, c2 in odd[n - 1 - i].items():
                    odd[n][k1 + k2] += c1 * c2
    return [sum(abs(k) * c for k, c in even[n].items()) for n in range(1, nmax + 1)]


def d_exact(n: int) -> int:
    c = n // 2
    if n % 2 == 0:
        return comb(n, c) ** 2 // 2
    return (n - 1) * (n + 1) * comb(n, c) ** 2 // (2 * n * n)


@numba.njit(cache=True)
def total(n_max: int, mod: int) -> int:
    fact = np.empty(n_max + 1, dtype=np.int64)
    inv = np.empty(n_max + 1, dtype=np.int64)
    invfact = np.empty(n_max + 1, dtype=np.int64)
    fact[0] = 1
    for i in range(1, n_max + 1):
        fact[i] = fact[i - 1] * i % mod
    inv[1] = 1
    for i in range(2, n_max + 1):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod
    invfact[0] = 1
    for i in range(1, n_max + 1):
        invfact[i] = invfact[i - 1] * inv[i] % mod
    inv2 = (mod + 1) // 2
    s = 0
    for n in range(1, n_max + 1):
        c = n // 2
        binom = fact[n] * invfact[c] % mod * invfact[n - c] % mod
        d = binom * binom % mod * inv2 % mod
        if n % 2 == 1:
            d = d * (n - 1) % mod * (n + 1) % mod * inv[n] % mod * inv[n] % mod
        s = (s + d) % mod
    return s


if __name__ == "__main__":
    small = tree_dp(12)
    assert small[2] == 4  # given D(3) = 4
    assert all(d_exact(n) == small[n - 1] for n in range(1, 13))
    assert d_exact(100) % MOD == 1172122931  # given
    expected_small = sum(d_exact(n) for n in range(1, 1001)) % MOD
    assert total(1000, MOD) == expected_small
    print(total(N, MOD))  # 469137427
