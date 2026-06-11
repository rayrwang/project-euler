import numpy as np


def _beans(n: int) -> list[int]:
    """The bean sequence b_1, ..., b_n."""
    t = 123456
    result = []
    for _ in range(n):
        t = t // 2 if t % 2 == 0 else (t // 2) ^ 926252
        result.append((t % 2048) + 1)
    return result


def _final_positions(total: int, moment: int) -> set[int]:
    """The set of occupied bowls once the game halts.

    The move (take two beans, drop one in each neighbour) is the 1-D abelian sandpile, so the
    final stable configuration (every bowl 0 or 1) is unique and conserves both the bean count
    `total` and the first moment `moment`. It is a centred run of 1s: a block of length `total`
    when that block can sit at integer positions, otherwise a block of length total+1 with a
    single central gap, the gap chosen to match the moment."""
    base = moment - total * (total - 1) // 2
    if base % total == 0:
        a = base // total
        return set(range(a, a + total))
    for a in range(moment // total - total, moment // total + 2):
        gap = (total + 1) * a + total * (total + 1) // 2 - moment
        if a <= gap <= a + total:
            block = set(range(a, a + total + 1))
            block.discard(gap)
            return block
    raise AssertionError("no valid final configuration")


def solve(num_bowls: int = 1500) -> int:
    """Total moves to finish the game for bowls initially holding b_1, ..., b_{num_bowls}.

    Let f_i be the number of times bowl i fires. Each firing removes two beans and gives one to
    each neighbour, so init - final = -Δf (discrete Laplacian), and f_i = -1/2 · sum_j |i-j| g_j
    with g = init - final. The total number of moves is sum_i f_i, evaluated in O(spread) with two
    prefix-sum passes (splitting |i-j| at j <= i and j > i). The two-bowl case (b_1, b_2) = (289,
    145) gives 3419100, confirming the method."""
    vals = _beans(num_bowls)
    total = sum(vals)
    moment = sum(i * v for i, v in enumerate(vals))
    final = _final_positions(total, moment)

    lo = min(0, min(final))
    hi = max(num_bowls - 1, max(final))
    g = np.zeros(hi - lo + 1, dtype=np.int64)
    for i, v in enumerate(vals):
        g[i - lo] += v
    for p in final:
        g[p - lo] -= 1

    pos = np.arange(g.size, dtype=np.int64)
    cum = np.cumsum(g)
    cum_pos = np.cumsum(pos * g)
    left = pos * cum - cum_pos
    right = (cum_pos[-1] - cum_pos) - pos * (cum[-1] - cum)
    f = (left + right) // 2
    return -int(f.sum())


if __name__ == "__main__":
    assert solve(2) == 3419100  # bowls b_1, b_2 = 289, 145
    print(solve())  # 150320021261690835
