"""Project Euler Problem 629: Scatterstone Nim.

A position (a partition of n into piles) is winning iff the XOR of the
piles' Grundy values is nonzero, so f(n, k) = p(n) - Z_k(n) where Z_k
counts the partitions of n with XOR zero.  The single-pile Grundy function
G_k under "split into 2..k non-empty piles" has three regimes:

* k = 2: every move adds exactly one pile, so the game length n - #piles
  is fixed and G_2(m) = (m - 1) mod 2.
* k = 3: no closed form; taken from the exact mex DP below.
* k >= 4: G_k(m) = m - 1.  Inductively any split into j parts has XOR at
  most sum (p_i - 1) = m - j <= m - 2, while the k = 4 moves already
  realise every value 0..m - 2 (verified by the exact DP up to 200);
  larger k only adds moves under the same bound, so the mex stays m - 1.

The exact Grundy DP tracks A[j][r], the set of achievable XOR values over
j-part compositions of r, as a 256-bit Python-int bitmask; appending a part
of size t maps a set through XOR-by-G[t], a bit permutation done level by
level.  mex is the lowest missing bit.  Counting Z is a knapsack over pile
sizes: even multiplicities of size s form an XOR-neutral step-2s closure,
plus an optional odd copy contributing G(s).

g(n) = sum_k f(n, k) = (n-1) p(n) - Z_2(n) - Z_3(n) - (n-3) Z_4(n), exact
in Python ints (p(200) is only about 4 * 10^12), reduced mod 10^9 + 7.
Checks: f(5,2) = 3, f(5,3) = 5, g(7) = 66, g(10) = 291, and the regime
formula against brute per-k tables for every n <= 30.
"""

BITS = 256
LO = [
    sum(
        ((1 << (1 << b)) - 1) << (block << (b + 1))
        for block in range(BITS >> (b + 1))
    )
    for b in range(8)
]


def xor_shift(mask: int, g: int) -> int:
    """Bitmask of {x ^ g : bit x set in mask}."""
    for b in range(8):
        if g >> b & 1:
            s = 1 << b
            mask = ((mask & LO[b]) << s) | ((mask >> s) & LO[b])
    return mask


def grundy_table(k: int, n: int) -> list[int]:
    """G_k(m) for m = 0..n (entries 0 and 1 are 0)."""
    G = [0] * (n + 1)
    A = [[0] * (n + 1) for _ in range(min(k, n) + 1)]  # A[j][r]: XOR set mask
    A[0][0] = 1
    for m in range(1, n + 1):
        achievable = 0
        for j in range(2, min(k, m) + 1):
            A[j][m] = 0
            for t in range(1, m):
                if A[j - 1][m - t]:
                    A[j][m] |= xor_shift(A[j - 1][m - t], G[t])
            achievable |= A[j][m]
        g = 0
        while achievable >> g & 1:
            g += 1
        G[m] = g
        A[1][m] = 1 << g
    return G


def partitions_by_xor(n: int, G: list[int]) -> list[int]:
    """count[x] = partitions of n whose pile-Grundy XOR is x."""
    dp = [[0] * BITS for _ in range(n + 1)]
    dp[0][0] = 1
    for s in range(1, n + 1):
        for m in range(2 * s, n + 1):  # even multiplicities: XOR-neutral
            row, src = dp[m], dp[m - 2 * s]
            for x in range(BITS):
                row[x] += src[x]
        g = G[s]
        for m in range(n, s - 1, -1):  # at most one extra odd copy
            row, src = dp[m], dp[m - s]
            for x in range(BITS):
                row[x] += src[x ^ g]
    return dp[n]


def g(n: int) -> int:
    z2 = partitions_by_xor(n, [(m - 1) % 2 for m in range(n + 1)])
    z3 = partitions_by_xor(n, grundy_table(3, n))
    g4 = grundy_table(4, n)
    assert all(g4[m] == m - 1 for m in range(2, n + 1)), "k>=4 regime"
    z4 = partitions_by_xor(n, [max(0, m - 1) for m in range(n + 1)])
    p = sum(z2)
    assert p == sum(z3) == sum(z4)
    return (n - 1) * p - z2[0] - z3[0] - (n - 3) * z4[0]


def g_brute(n: int) -> int:
    total = 0
    for k in range(2, n + 1):
        z = partitions_by_xor(n, grundy_table(k, n))
        total += sum(z) - z[0]
    return total


if __name__ == "__main__":
    z2_5 = partitions_by_xor(5, [(m - 1) % 2 for m in range(6)])
    z3_5 = partitions_by_xor(5, grundy_table(3, 5))
    assert sum(z2_5) - z2_5[0] == 3  # f(5, 2)
    assert sum(z3_5) - z3_5[0] == 5  # f(5, 3)
    assert g(7) == g_brute(7) == 66
    assert g(10) == g_brute(10) == 291
    assert all(g(n) == g_brute(n) for n in range(4, 31))
    print(g(200) % (10**9 + 7))  # 626616617
