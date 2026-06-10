from itertools import combinations

import numpy as np

# Between pickup and drop events the ant performs a plain random walk on
# the 25 cells, so the chain decomposes into blocks indexed by
# (bottom-seed mask B, top-filled mask T, carrying c) with
# |B| = 5 - |T| - c. Events - entering a seeded bottom cell while empty, or
# an unfilled top cell while carrying - strictly increase the progress
# (picked + dropped), so the blocks form a DAG. Solving them in reverse
# topological order, each block is a 25-variable linear system
# E(p) = 1 + mean over neighbours q of (E'(q) at the event-updated block,
# or E(q) within the block), with the full-top empty-handed block absorbing
# at 0. The answer is E at the centre in the initial block.


def _neighbors(p: int) -> list[int]:
    r, c = divmod(p, 5)
    out = []
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            out.append(nr * 5 + nc)
    return out


def solve() -> str:
    nbr = [_neighbors(p) for p in range(25)]
    expected: dict[tuple[int, int, int], np.ndarray] = {}

    blocks = []
    for t in range(6):
        for c in (0, 1):
            nb = 5 - t - c
            if nb < 0:
                continue
            for t_cols in combinations(range(5), t):
                t_mask = sum(1 << x for x in t_cols)
                for b_cols in combinations(range(5), nb):
                    b_mask = sum(1 << x for x in b_cols)
                    blocks.append((b_mask, t_mask, c))

    def level(blk: tuple[int, int, int]) -> int:
        b, t, _ = blk
        return (5 - bin(b).count("1")) + bin(t).count("1")

    blocks.sort(key=level, reverse=True)
    for b, t, c in blocks:
        if t == 31 and c == 0:
            expected[(b, t, c)] = np.zeros(25)
            continue
        mat = np.eye(25)
        rhs = np.ones(25)
        for p in range(25):
            w = 1.0 / len(nbr[p])
            for q in nbr[p]:
                r, col = divmod(q, 5)
                if c == 0 and r == 0 and (b >> col) & 1:
                    rhs[p] += w * expected[(b & ~(1 << col), t, 1)][q]
                elif c == 1 and r == 4 and not ((t >> col) & 1):
                    rhs[p] += w * expected[(b, t | (1 << col), 0)][q]
                else:
                    mat[p, q] -= w
        expected[(b, t, c)] = np.linalg.solve(mat, rhs)

    return f"{expected[(31, 0, 0)][12]:.6f}"


if __name__ == "__main__":
    print(solve())  # 430.088247
