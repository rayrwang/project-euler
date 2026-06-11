"""Project Euler 950: Pirate Treasure.

Game analysis. A voter compares acceptance (coins offered now) with the
continuation where the proposer walks: c' + p(1 + w') with (c', w') the
voter's coins and future walks in the (m-1)-pirate subgame. Since p is
irrational and coins are integers, the comparison is never a tie, so the
equilibrium is unique where it matters. Pirates doomed in the subgame have
continuation -infinity and vote yes for free; an alive voter is bought for
exactly c' + floor(p (1 + w')) + 1 coins. The proposer votes for himself
and needs ceil(m/2) - 1 further votes, taking frees first and then the
cheapest alive voters; he survives iff the minimum total is at most C.

Consequently only the "successful" levels matter. After a success at level
s every pirate is alive with a known multiset of coins (proposer keeps
C - paid, bought voters hold their price, everyone else 0). For n above s
the proposers walk until the next success: at level n = s + g there are
g - 1 free votes, q = ceil((s - g)/2) paid votes are needed, every alive
voter's price carries the same uplift u = floor(g / sqrt(D)) + 1, and the
cheapest q cost S(q) + q u, with S(q) the sum of the q smallest coins.
The next success is the minimal such g with S(q) + q u <= C; it exists
since q = 0 at g = s. For n in [s, s'-1] the most senior survivor is the
proposer of level s, so c(n) + w(n) = keep + (n - s) sums in closed form
per block. The multiset has only a handful of distinct values, and the
number of successes up to 10^16 is about 2C + O(log) (gaps eventually
double), so the whole simulation is tiny. floor(x / sqrt(D)) is computed
exactly as isqrt(x^2 // D).

Verified against a full O(n^2) game simulation for many (N, C, D) and the
given T(30,3,1/sqrt 3) = 190, T(50,3,1/sqrt 31) = 385,
T(10^3,101,1/sqrt 101) = 142427.
"""

from math import isqrt

N = 10**16
MOD = 10**9


def fsqrt_div(x: int, d: int) -> int:
    """floor(x / sqrt(d)) exactly, for integer x >= 0."""
    return isqrt(x * x // d)


def t_sum(n_max: int, c_coins: int, d: int) -> int:
    """T(n_max, c_coins, 1/sqrt(d))."""
    total = 0
    s = 1
    keep = c_coins
    groups: list[tuple[int, int]] = [(c_coins, 1)]  # sorted (value, count)

    while s <= n_max:
        pc = [0]
        ps = [0]
        for v, cn in groups:
            pc.append(pc[-1] + cn)
            ps.append(ps[-1] + v * cn)

        def s_of_q(q: int, pc: list[int] = pc, ps: list[int] = ps) -> int:
            lo, hi = 0, len(pc) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if pc[mid] >= q:
                    hi = mid
                else:
                    lo = mid + 1
            return ps[lo - 1] + (q - pc[lo - 1]) * groups[lo - 1][0]

        def sigma(g: int) -> int:
            q = max((s - g + 1) // 2, 0)
            if q == 0:
                return 0
            return s_of_q(q) + q * (fsqrt_div(g, d) + 1)

        g_found = -1
        if s <= 4 * c_coins + 64:
            g = 1
            while True:
                if sigma(g) <= c_coins:
                    g_found = g
                    break
                g += 1
        else:
            q = min(c_coins, s // 2)  # q <= ceil((s-1)/2) and q * 1 <= C
            while True:
                if q <= 0:
                    g_found = s
                    break
                g1 = s - 2 * q
                if g1 < 1:
                    q -= 1
                    continue
                u1 = fsqrt_div(g1, d) + 1
                sq = s_of_q(q)
                if sq + q * u1 <= c_coins:
                    g_found = g1
                    break
                u2 = fsqrt_div(g1 + 1, d) + 1
                if sq + q * u2 <= c_coins:
                    g_found = g1 + 1
                    break
                # all smaller q have larger g hence price uplift >= u2
                q = min(q - 1, c_coins // u2)
        g = g_found
        n = s + g
        hi = min(n - 1, n_max)
        ln = hi - s + 1
        total += ln * keep + ln * (ln - 1) // 2
        if n > n_max:
            break
        q = max((s - g + 1) // 2, 0)
        u = fsqrt_div(g, d) + 1
        pay = s_of_q(q) + q * u if q > 0 else 0
        keep = c_coins - pay
        new: dict[int, int] = {0: n - 1 - q}
        rem = q
        for v, cn in groups:
            if rem <= 0:
                break
            take = min(cn, rem)
            rem -= take
            new[v + u] = new.get(v + u, 0) + take
        new[keep] = new.get(keep, 0) + 1
        groups = sorted((v, cn) for v, cn in new.items() if cn > 0)
        s = n
    return total


def solve() -> int:
    assert t_sum(30, 3, 3) == 190
    assert t_sum(50, 3, 31) == 385
    assert t_sum(1000, 101, 101) == 142427
    grand = 0
    for k in range(1, 7):
        c_coins = 10**k + 1
        grand += t_sum(N, c_coins, c_coins)
    return grand % MOD


if __name__ == "__main__":
    print(solve())  # 429162542
