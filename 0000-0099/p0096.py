def solve_grid(grid):
    """Backtracking solver using bitmask constraints and a minimum-remaining-values
    heuristic (always fill the empty cell with the fewest candidates first)."""
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    for i in range(81):
        v = grid[i]
        if v:
            r, c = divmod(i, 9)
            bit = 1 << v
            rows[r] |= bit
            cols[c] |= bit
            boxes[(r // 3) * 3 + c // 3] |= bit

    def backtrack():
        best, best_cands, best_count = -1, [], 10
        for i in range(81):
            if grid[i] == 0:
                r, c = divmod(i, 9)
                used = rows[r] | cols[c] | boxes[(r // 3) * 3 + c // 3]
                cands = [v for v in range(1, 10) if not (used >> v) & 1]
                if len(cands) < best_count:
                    best, best_cands, best_count = i, cands, len(cands)
                    if best_count <= 1:
                        break
        if best == -1:
            return True               # no empty cells: solved
        r, c = divmod(best, 9)
        b = (r // 3) * 3 + c // 3
        for v in best_cands:
            bit = 1 << v
            grid[best] = v
            rows[r] |= bit
            cols[c] |= bit
            boxes[b] |= bit
            if backtrack():
                return True
            grid[best] = 0
            rows[r] &= ~bit
            cols[c] &= ~bit
            boxes[b] &= ~bit
        return False

    backtrack()
    return grid

if __name__ == "__main__":
    with open("assets/0096_sudoku.txt") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    total = 0
    i = 0
    while i < len(lines):
        if lines[i].startswith("Grid"):
            grid = [int(ch) for r in range(1, 10) for ch in lines[i + r]]
            solve_grid(grid)
            total += grid[0] * 100 + grid[1] * 10 + grid[2]
            i += 10
        else:
            i += 1
    print(total)  # 24702
