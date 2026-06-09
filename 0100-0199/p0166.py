def _rows_with_sum(s: int, d_max: int) -> list[tuple[int, int, int, int]]:
    out = []
    for a in range(d_max + 1):
        for b in range(d_max + 1):
            for c in range(d_max + 1):
                d = s - a - b - c
                if 0 <= d <= d_max:
                    out.append((a, b, c, d))
    return out


def solve(d_max: int = 9) -> int:
    # 4x4 grids where every row, column and both diagonals share the sum s.
    # Fix rows 0 and 1; columns force row 3 from row 2, so the diagonal and
    # anti-diagonal conditions plus the row-2 sum pin down row 2 up to one
    # free cell, which is counted directly.
    total = 0
    for s in range(4 * d_max + 1):
        rows = _rows_with_sum(s, d_max)
        for a0, a1, a2, a3 in rows:
            for b0, b1, b2, b3 in rows:
                shift_12 = a3 + b3 - a0 - b1  # c2 - c3 (diagonal)
                shift_10 = a0 + b0 - a3 - b2  # c1 - c0 (anti-diagonal)
                rem = s - shift_12 - shift_10
                if rem < 0 or rem & 1:
                    continue
                q = rem // 2  # c0 + c3
                lo0, hi0 = max(0, s - a0 - b0 - d_max), min(d_max, s - a0 - b0)
                lo1, hi1 = max(0, s - a1 - b1 - d_max), min(d_max, s - a1 - b1)
                lo2, hi2 = max(0, s - a2 - b2 - d_max), min(d_max, s - a2 - b2)
                lo3, hi3 = max(0, s - a3 - b3 - d_max), min(d_max, s - a3 - b3)
                for c0 in range(max(lo0, q - hi3), min(hi0, q - lo3) + 1):
                    if lo1 <= c0 + shift_10 <= hi1 and lo2 <= (q - c0) + shift_12 <= hi2:
                        total += 1
    return total


if __name__ == "__main__":
    print(solve())  # 7130034
