from collections import defaultdict

# The six triomino orientations, as cell offsets from the row-major-minimal
# cell (0,0): the straight tromino (2 orientations) and the L tromino (4).
_PIECES = (
    ((0, 0), (0, 1), (0, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 0), (0, 1), (1, 0)),
    ((0, 0), (0, 1), (1, 1)),
    ((0, 0), (1, 0), (1, 1)),
    ((0, 0), (1, 0), (1, -1)),
)


def solve(height: int = 12, width: int = 9) -> int:
    # Broken-profile DP. State = occupancy bitmask of the window of cells
    # [pos, pos + 2*width]. At the first empty cell we must place a piece
    # covering it; otherwise the cell is already filled and we slide on.
    dp: dict[int, int] = defaultdict(int)
    dp[0] = 1
    for pos in range(height * width):
        r, c = divmod(pos, width)
        nxt: dict[int, int] = defaultdict(int)
        for mask, cnt in dp.items():
            if mask & 1:
                nxt[mask >> 1] += cnt
                continue
            for piece in _PIECES:
                bits = 0
                ok = True
                for dr, dc in piece:
                    nc, nr = c + dc, r + dr
                    if nc < 0 or nc >= width or nr >= height:
                        ok = False
                        break
                    delta = dr * width + dc
                    if mask >> delta & 1:
                        ok = False
                        break
                    bits |= 1 << delta
                if ok:
                    nxt[(mask | bits) >> 1] += cnt
        dp = nxt
    return dp.get(0, 0)


if __name__ == "__main__":
    print(solve())  # 20574308184277971
