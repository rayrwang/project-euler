from math import comb, factorial


def count_xor_zero(total_sum: int, active: int, passive: int, mod: int | None) -> int:
    """Number of vectors of (active + passive) non-negative integers summing to
    total_sum whose *active* entries xor to zero.

    Per binary column the xor-zero requirement means an even number of active
    entries carry a 1; ways[s] counts column patterns with s ones in total.
    Scanning the bits of total_sum from low to high, the only DP state is the
    carry, with a column of s ones legal when (carry + s) matches the target
    bit, after which the carry becomes (carry + s - bit) // 2.
    """
    tot = active + passive
    ways = [0] * (tot + 1)
    for x in range(0, active + 1, 2):  # even count among active gaps
        ca = comb(active, x)
        for y in range(passive + 1):
            ways[x + y] += ca * comb(passive, y)
    if mod is not None:
        ways = [w % mod for w in ways]

    dp = {0: 1}
    for j in range(total_sum.bit_length() + 8):
        bit = (total_sum >> j) & 1
        ndp: dict[int, int] = {}
        for carry, cnt in dp.items():
            for s in range(tot + 1):
                w = ways[s]
                if w == 0:
                    continue
                t = carry + s
                if (t & 1) == bit:
                    nc = (t - bit) >> 1
                    v = cnt * w
                    if mod is not None:
                        v %= mod
                    ndp[nc] = (ndp.get(nc, 0) + v) % mod if mod is not None \
                        else ndp.get(nc, 0) + v
        dp = ndp
    return dp.get(0, 0)


def winning(n: int, c: int, mod: int | None = None) -> int:
    """W(n, c): winning configurations for n squares, c worthless coins and one
    silver dollar (so m = c + 1 coins, here m odd).

    A configuration is m + 1 non-negative gaps summing to N = n - m, times the
    m choices for which coin is the dollar. Losing positions are an xor-zero
    condition on the alternating "active" gaps. L0 (dollar on the 2nd coin)
    counts gap vectors of sum N; L1 (dollar further right) uses sum N+1 with a
    correction removing a vanished leading active gap. The total winning count
    is m*C(n, m) minus L0 + (m-2)*L1.
    """
    m = c + 1
    big = (m + 1) // 2
    small = (m - 1) // 2
    n_gap = n - m

    l0 = count_xor_zero(n_gap, big, big, mod)
    l1 = count_xor_zero(n_gap + 1, big, big, mod) \
        - count_xor_zero(n_gap + 1, small, big, mod)

    num = 1
    for i in range(m):
        num *= n - i
    if mod is None:
        cnm = num // factorial(m)
        return m * cnm - (l0 + (m - 2) * l1)
    cnm = num % mod * pow(factorial(m) % mod, -1, mod) % mod
    return (m * cnm - (l0 + (m - 2) * l1)) % mod


if __name__ == "__main__":
    assert winning(10, 2) == 324
    assert winning(100, 10) == 1514704946113500
    print(winning(1_000_000, 100, mod=1_000_036_000_099))  # 65579304332
