def _diagonal(w: int, h: int) -> int:
    # Tilted rectangles use "/" lines c = x-y and "\" lines d = x+y. A rectangle
    # of spans dc, dd in (c,d) fits when, with s = c1+d1 and t = d1-c1 (equal
    # parity), s in [0, 2w-dc-dd] and t in [dc, 2h-dd]. Count same-parity (s,t).
    total = 0
    for dc in range(1, 2 * w):
        for dd in range(1, 2 * h):
            s_hi = 2 * w - dc - dd
            if s_hi < 0:
                break
            t_hi = 2 * h - dd
            if t_hi < dc:
                continue
            se = s_hi // 2 + 1
            so = (s_hi + 1) - se
            te = t_hi // 2 - (dc - 1) // 2
            to = (t_hi - dc + 1) - te
            total += se * te + so * to
    return total


def solve(m_max: int = 47, n_max: int = 43) -> int:
    total = 0
    for m in range(1, m_max + 1):
        for n in range(1, n_max + 1):
            axis = (m * (m + 1) // 2) * (n * (n + 1) // 2)
            total += axis + _diagonal(m, n)
    return total


if __name__ == "__main__":
    print(solve())  # 846910284
