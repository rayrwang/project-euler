# Cuts are non-crossing chords between the 4N border lattice points, and
# "no more legal cuts" makes every face a triangle with unit border edges -
# so C(N) counts triangulations of the cyclic sequence of border points in
# which collinear triples (three points on one side) are forbidden, since a
# zero-area triangle is not a piece and a chord along a side is not a cut.
# Catalan-style interval DP: T(i, j) triangulates the region cut off by
# chord (i, j), T(i, j) = sum over apexes k of T(i, k) T(k, j) whenever
# (i, k, j) is non-degenerate; collinear spans die automatically (every
# apex degenerate). C(1) = 2 and C(2) = 30 reproduce the statement.


def solve(n: int = 30, mod: int = 10**8) -> int:
    pts: list[tuple[int, int]] = []
    for i in range(n):
        pts.append((i, 0))
    for i in range(n):
        pts.append((n, i))
    for i in range(n):
        pts.append((n - i, n))
    for i in range(n):
        pts.append((0, n - i))
    m = len(pts)

    def nondegenerate(i: int, k: int, j: int) -> bool:
        ax, ay = pts[i]
        bx, by = pts[k]
        cx, cy = pts[j]
        return (bx - ax) * (cy - ay) != (by - ay) * (cx - ax)

    table = [[0] * m for _ in range(m)]
    for i in range(m - 1):
        table[i][i + 1] = 1
    for span in range(2, m):
        for i in range(0, m - span):
            j = i + span
            s = 0
            for k in range(i + 1, j):
                if table[i][k] and table[k][j] and nondegenerate(i, k, j):
                    s += table[i][k] * table[k][j]
            table[i][j] = s % mod
    return table[0][m - 1]


if __name__ == "__main__":
    print(solve())  # 82282080
