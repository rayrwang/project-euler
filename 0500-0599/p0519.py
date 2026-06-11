"""Project Euler problem 519: Tricoloured Coin Fountains.

A fountain of n coins has a gapless bottom row and every higher coin
rests on exactly two adjacent coins of the row below.  T(n) sums, over
all fountains with n coins, the number of proper 3-colourings (touching
coins coloured differently).  Find the last nine digits of T(20000).

A fountain is equivalent to column heights (h_1, ..., h_k) with h_k = 1
and h_i <= h_{i+1} + 1, where coin (r, i) rests on (r-1, i) and
(r-1, i+1).  The two supports of an upper coin touch each other, so each
upper colour is forced to the third colour of its supporters, and a
colouring is determined by the bottom row: a first colour (3 ways) plus
differences d_i = c_{i+1} - c_i in {+-1} mod 3.  Propagating differences
along rows via D(r, i) = -(D(r-1, i) + D(r-1, i+1)), an adjacent pair in
row r is properly coloured iff the two differences below are equal (and
then the difference is preserved), so the only constraints are
d_i = d_{i+1} whenever columns i and i+1 both have height >= 2.  Hence

    T(n) = 3 * sum over fountains of 2^(k - 1 - e),

with e the number of adjacent column pairs of height >= 2 each.  A DP
over (coins used, current leftmost height) prepends columns of height
h' <= h + 1 with weight 1 if h', h >= 2 else 2; suffix sums over the
height axis make it O(n * sqrt(n)).

Verified by enumerating all fountains for n <= 12 and counting proper
3-colourings of the coin graph (literally over all 3^n colour vectors
for n <= 9, via the forced bottom-row propagation above for n <= 12,
with the two methods asserted equal where both run), matching the given
f(4) = 3, f(10) = 78, T(4) = 48 and T(10) = 17760.
"""

from itertools import product


def gen_fountains(n: int) -> list[frozenset[tuple[int, int]]]:
    """All fountains with exactly n coins, as sets of (row, slot) cells."""
    results: list[frozenset[tuple[int, int]]] = []

    def above(
        prev: tuple[int, ...], coins: int, cells: list[tuple[int, int]], row: int
    ) -> None:
        results.append(frozenset(cells))
        gaps = [j for j in prev if j + 1 in prev]
        if not gaps or coins >= n:
            return
        for mask in range(1, 1 << len(gaps)):
            sub = [gaps[i] for i in range(len(gaps)) if mask >> i & 1]
            if coins + len(sub) <= n:
                above(
                    tuple(sub),
                    coins + len(sub),
                    cells + [(row, j) for j in sub],
                    row + 1,
                )

    for k in range(1, n + 1):
        above(tuple(range(1, k + 1)), k, [(1, j) for j in range(1, k + 1)], 2)
    return [f for f in results if len(f) == n]


def colourings_graph(cells: frozenset[tuple[int, int]]) -> int:
    """Proper 3-colourings, brute force over all colour vectors."""
    order = sorted(cells)
    idx = {c: i for i, c in enumerate(order)}
    edges = []
    for r, j in order:
        for nb in ((r, j + 1), (r + 1, j), (r + 1, j - 1)):
            if nb in idx:
                edges.append((idx[r, j], idx[nb]))
    return sum(
        all(col[a] != col[b] for a, b in edges)
        for col in product(range(3), repeat=len(order))
    )


def colourings_forced(cells: frozenset[tuple[int, int]]) -> int:
    """Proper 3-colourings via forced upward propagation from row 1."""
    rows: dict[int, list[int]] = {}
    for r, j in cells:
        rows.setdefault(r, []).append(j)
    bottom = sorted(rows[1])
    k = len(bottom)
    count = 0
    for diffs in product((1, 2), repeat=k - 1):
        col = {(1, bottom[0]): 0}
        c = 0
        for j, d in zip(bottom[1:], diffs):
            c = (c + d) % 3
            col[1, j] = c
        ok = True
        for r in sorted(rows):
            if r == 1:
                continue
            for j in sorted(rows[r]):
                a, b = col[r - 1, j], col[r - 1, j + 1]
                if a == b:
                    ok = False
                    break
                col[r, j] = 3 - a - b
                if (r, j - 1) in col and col[r, j - 1] == col[r, j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            count += 1
    return 3 * count


def t_brute(n: int) -> int:
    return sum(colourings_forced(f) for f in gen_fountains(n))


def t_fast(n: int, mod: int = 10**9) -> int:
    """T(n) mod `mod` by the column-height DP with suffix sums."""
    hmax = int((2 * n) ** 0.5) + 2
    dp = [[0] * (hmax + 2) for _ in range(n + 1)]
    dp[1][1] = 1
    for c in range(1, n + 1):
        row = dp[c]
        suf = [0] * (hmax + 3)
        for h in range(hmax, 0, -1):
            suf[h] = (suf[h + 1] + row[h]) % mod
        for hp in range(1, min(hmax, n - c) + 1):
            if hp == 1:
                dp[c + 1][1] = (dp[c + 1][1] + 2 * suf[1]) % mod
            elif hp == 2:
                dp[c + 2][2] = (dp[c + 2][2] + suf[2] + 2 * row[1]) % mod
            else:
                dp[c + hp][hp] = (dp[c + hp][hp] + suf[hp - 1]) % mod
    return 3 * sum(dp[n][1:]) % mod


def main() -> None:
    assert len(gen_fountains(4)) == 3
    assert len(gen_fountains(10)) == 78
    for n in range(1, 10):
        for f in gen_fountains(n):
            assert colourings_graph(f) == colourings_forced(f)
    assert t_brute(4) == 48
    assert t_brute(10) == 17760
    for n in range(1, 13):
        assert t_brute(n) % 10**9 == t_fast(n)
    print(t_fast(20000))  # 804739330


if __name__ == "__main__":
    main()
