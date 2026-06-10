MOD = 10**9 + 7

def C(H, W):
    """Sum of the number of strongly connected components over all
    2^(H+W) orientations of the H x W grid (rows directed left/right,
    columns up/down), mod 1e9+7.

    Structure (verified exhaustively for all orientations with
    H, W <= 4): every orientation has at most ONE nontrivial SCC, and
    that SCC is exactly the union of the boundaries of all "rectangle
    cycles" -- rectangles i1 < i2, j1 < j2 whose rows/columns are
    directed (type A) top '>', bottom '<', left '^', right 'v', or
    (type B) the mirror image. Hence
        C = 2^(H+W) H W - sum_orient |big SCC| + N1,
    where N1 counts orientations containing at least one cycle.

    A node (i, j) lies on some rectangle boundary iff
    X1(i) Y1(j) or X2(i) Y2(j) or X3(i) Y3(j) or X4(i) Y4(j), with
    X1 = [row i is '>' with some '<' below, or '<' with some '>' above]
    (top/bottom row of a type-A rectangle), Y1 = [some '^' at <= j and
    some 'v' at >= j], X2 = [some '>' at <= i and '<' at >= i],
    Y2 = [col j is '^' with 'v' to its right, or 'v' with '^' to its
    left] (left/right column of type A), and X3, Y3, X4, Y4 the type-B
    mirrors. Rows and columns are independent, so by inclusion-
    exclusion over nonempty subsets S of the four clauses,
    sum_orient |big| splits into products of per-axis sums; each
    per-index count enumerates the 32 atomic states (own direction x
    which directions appear before/after) whose weights are powers
    of two. N1 follows from counting monotone direction sequences:
    orientations free of '>'-above-'<' rows number H + 1, etc.

    Validated against exhaustive enumeration for all H <= 4, W <= 5
    and the given C(3,3), C(3,6), C(10,20).
    """
    pw = [1] * (max(H, W) + 2)
    for k in range(1, len(pw)):
        pw[k] = pw[k - 1] * 2 % MOD

    def side_counts(m):
        """Counts of length-m direction sequences by (has0, has1)."""
        return {
            (0, 0): 1 if m == 0 else 0,
            (1, 0): 1 if m >= 1 else 0,
            (0, 1): 1 if m >= 1 else 0,
            (1, 1): (pw[m] - 2) % MOD if m >= 2 else 0,
        }

    def axis_sums(L, is_row):
        sums = [0] * 16
        for i in range(L):
            above = side_counts(i)
            below = side_counts(L - 1 - i)
            for d in (0, 1):  # rows: 0 = '>', 1 = '<'; cols: 0 = 'v', 1 = '^'
                for (ag, al), wa in above.items():
                    if wa == 0:
                        continue
                    for (bg, bl), wb in below.items():
                        if wb == 0:
                            continue
                        w = wa * wb % MOD
                        if is_row:
                            x1 = (d == 0 and bl == 1) or (d == 1 and ag == 1)
                            x2 = (d == 0 or ag == 1) and (d == 1 or bl == 1)
                            x3 = (d == 1 and bg == 1) or (d == 0 and al == 1)
                            x4 = (d == 1 or al == 1) and (d == 0 or bg == 1)
                            e = (x1, x2, x3, x4)
                        else:
                            y1 = (d == 1 or al == 1) and (d == 0 or bg == 1)
                            y2 = (d == 1 and bg == 1) or (d == 0 and al == 1)
                            y3 = (d == 0 or ag == 1) and (d == 1 or bl == 1)
                            y4 = (d == 0 and bl == 1) or (d == 1 and ag == 1)
                            e = (y1, y2, y3, y4)
                        m = ((1 if e[0] else 0) | (2 if e[1] else 0)
                             | (4 if e[2] else 0) | (8 if e[3] else 0))
                        sub = m
                        while sub:
                            sums[sub] = (sums[sub] + w) % MOD
                            sub = (sub - 1) & m
        return sums

    rs = axis_sums(H, True)
    cs = axis_sums(W, False)
    cover = 0
    for s in range(1, 16):
        sign = -1 if bin(s).count("1") % 2 == 0 else 1
        cover = (cover + sign * rs[s] * cs[s]) % MOD
    total = pw[H] * pw[W] % MOD
    ra = (pw[H] - (H + 1)) % MOD
    ca = (pw[W] - (W + 1)) % MOD
    rab = (pw[H] - 2 * H) % MOD
    cab = (pw[W] - 2 * W) % MOD
    nocycle = (total - 2 * ra * ca + rab * cab) % MOD
    n1 = (total - nocycle) % MOD
    return (total * (H * W % MOD) - cover + n1) % MOD

if __name__ == "__main__":
    assert C(3, 3) == 408
    assert C(3, 6) == 4696
    assert C(10, 20) == 988971143
    print(C(10000, 20000))  # 238948623
