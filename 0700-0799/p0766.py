"""
Project Euler Problem 766: Sliding Block Puzzle
https://projecteuler.net/problem=766

Pieces slide one unit up/down/left/right inside a grid; configurations
that place equal-shape (and equal-colour) pieces on the same cells are
identical.  The 4 x 3 example with one green L-tromino, seven red unit
squares and two holes has 208 reachable configurations; count them for
the 6 x 5 puzzle in the problem image.

Reading the image (cell colours and the black piece borders between
same-coloured neighbours) gives the layout

        . R R G r r          R/r red L-trominoes  (corner at top-left)
        . R G G r Y          G/g green L-trominoes (corner at bottom-right)
        m m B B y Y          Y/y yellow vertical 1 x 2 dominoes
        m m B B y g          B   blue 2 x 2 square
        m m C C g g          C   cyan horizontal 1 x 2 domino
                             m   six magenta unit squares, .  two holes

(the capital/lowercase pairs mark the two same-shape copies, which are
interchangeable; red and green L's have different orientations and
colours, so they are never identified with each other).

A breadth-first search over configurations suffices: a configuration is
canonically encoded by the anchor cells of the eight multi-cell pieces
(anchors sorted inside each interchangeable pair) plus the two sorted
hole positions, all packed in 5-bit fields of one 64-bit word -- the unit
squares are whatever cells remain, so they need no encoding at all.
Moves are precomputed per shape as bitboard masks over the 30 cells: a
piece may shift one step when the newly covered cells are currently
holes, and a unit square moves by swapping with an adjacent hole.  An
open-addressing hash set over the packed words makes the whole search a
few seconds of numba; the same routine run on the example layout
reproduces the given 208.
"""

import numpy as np
from numba import njit

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
L_RED = ((0, 0), (0, 1), (1, 0))
L_GREEN = ((0, 1), (1, 0), (1, 1))
V_DOMINO = ((0, 0), (1, 0))
H_DOMINO = ((0, 0), (0, 1))
SQUARE_2 = ((0, 0), (0, 1), (1, 0), (1, 1))


def build_tables(width, height, shapes):
    """Bitboard masks and one-step anchor moves for each shape."""
    cells = width * height
    ns = len(shapes)
    mask = np.zeros((ns, cells), dtype=np.int64)
    valid = np.zeros((ns, cells), dtype=np.uint8)
    moves = np.full((ns, cells, 4), -1, dtype=np.int64)
    for s, shape in enumerate(shapes):
        for r in range(height):
            for c in range(width):
                covered = [(r + dr, c + dc) for dr, dc in shape]
                if all(0 <= rr < height and 0 <= cc < width for rr, cc in covered):
                    a = r * width + c
                    valid[s, a] = 1
                    m = 0
                    for rr, cc in covered:
                        m |= 1 << (rr * width + cc)
                    mask[s, a] = m
    for s in range(ns):
        for a in range(cells):
            if not valid[s, a]:
                continue
            r, c = divmod(a, width)
            for d, (dr, dc) in enumerate((UP, DOWN, LEFT, RIGHT)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and valid[s, nr * width + nc]:
                    moves[s, a, d] = nr * width + nc
    return mask, moves


@njit(cache=True)
def count_reachable(width, height, mask, moves, ishape, group, start, e0, e1):
    """BFS over configurations; unit squares fill all unencoded cells."""
    cells = width * height
    full = (np.int64(1) << cells) - 1
    n_inst = ishape.shape[0]
    log = 23
    size = 1 << log
    table = np.full(size, -1, dtype=np.int64)
    queue = np.empty(size, dtype=np.int64)

    def pack(anchors, h1, h2):
        # sort anchors within each interchangeable group, then the holes
        srt = anchors.copy()
        for i in range(1, n_inst):
            if group[i] == group[i - 1] and srt[i] < srt[i - 1]:
                srt[i], srt[i - 1] = srt[i - 1], srt[i]
        if h1 > h2:
            h1, h2 = h2, h1
        key = np.int64(0)
        for i in range(n_inst):
            key |= srt[i] << (5 * i)
        key |= h1 << (5 * n_inst)
        key |= h2 << (5 * n_inst + 5)
        return key

    def insert(key):
        h = (key * np.int64(-7046029254386353131)) & (size - 1)
        while True:
            v = table[h]
            if v == key:
                return False
            if v == -1:
                table[h] = key
                return True
            h = (h + 1) & (size - 1)

    anchors = np.empty(n_inst, dtype=np.int64)
    for i in range(n_inst):
        anchors[i] = start[i]
    key = pack(anchors, e0, e1)
    insert(key)
    queue[0] = key
    head, tail = 0, 1
    while head < tail:
        st = queue[head]
        head += 1
        for i in range(n_inst):
            anchors[i] = (st >> (5 * i)) & 31
        h1 = (st >> (5 * n_inst)) & 31
        h2 = (st >> (5 * n_inst + 5)) & 31
        holes = (np.int64(1) << h1) | (np.int64(1) << h2)
        occupied = full & ~holes
        big = np.int64(0)
        for i in range(n_inst):
            big |= mask[ishape[i], anchors[i]]
        # multi-cell pieces
        for i in range(n_inst):
            s = ishape[i]
            cur = anchors[i]
            mo = mask[s, cur]
            for d in range(4):
                na = moves[s, cur, d]
                if na < 0:
                    continue
                mn = mask[s, na]
                if mn & (occupied & ~mo):
                    continue
                new_holes = (holes & ~(mn & ~mo)) | (mo & ~mn)
                p1 = np.int64(-1)
                p2 = np.int64(-1)
                for b in range(cells):
                    if (new_holes >> b) & 1:
                        if p1 < 0:
                            p1 = b
                        else:
                            p2 = b
                            break
                anchors[i] = na
                k = pack(anchors, p1, p2)
                anchors[i] = cur
                if insert(k):
                    queue[tail] = k
                    tail += 1
        # unit squares occupy every remaining cell
        units = full & ~big & ~holes
        for cell in range(cells):
            if not (units >> cell) & 1:
                continue
            r = cell // width
            c = cell % width
            for d in range(4):
                if d == 0:
                    if r == 0:
                        continue
                    t = cell - width
                elif d == 1:
                    if r == height - 1:
                        continue
                    t = cell + width
                elif d == 2:
                    if c == 0:
                        continue
                    t = cell - 1
                else:
                    if c == width - 1:
                        continue
                    t = cell + 1
                if not (holes >> t) & 1:
                    continue
                other = h2 if h1 == t else h1
                k = pack(anchors, np.int64(cell), other)
                if insert(k):
                    queue[tail] = k
                    tail += 1
    return tail


def solve(width, height, shapes, ishape, group, start, holes):
    mask, moves = build_tables(width, height, shapes)
    return count_reachable(
        width,
        height,
        mask,
        moves,
        np.asarray(ishape, dtype=np.int64),
        np.asarray(group, dtype=np.int64),
        np.asarray(start, dtype=np.int64),
        np.int64(holes[0]),
        np.int64(holes[1]),
    )


def main():
    # 4 x 3 example: green L at (0,0); red unit squares fill the rest
    example = solve(4, 3, [L_RED], [0], [0], [0 * 4 + 0], (0 * 4 + 3, 1 * 4 + 3))
    assert example == 208
    # 6 x 5 puzzle (see docstring): red pair, green pair, yellow pair,
    # blue square, cyan domino; magenta unit squares fill the rest
    return solve(
        6,
        5,
        [L_RED, L_GREEN, V_DOMINO, SQUARE_2, H_DOMINO],
        [0, 0, 1, 1, 2, 2, 3, 4],
        [0, 0, 1, 1, 2, 2, 3, 4],
        [
            0 * 6 + 1,
            0 * 6 + 4,
            0 * 6 + 2,
            3 * 6 + 4,
            1 * 6 + 5,
            2 * 6 + 4,
            2 * 6 + 2,
            4 * 6 + 2,
        ],
        (0 * 6 + 0, 1 * 6 + 0),
    )


if __name__ == "__main__":
    print(main())  # 2613742
