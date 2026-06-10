"""Project Euler 922: Young's Game A.

This is a partizan game: Right (moving first, treated as Left in CGT
conventions) moves a token rightwards within its row, Down moves it
downwards within its column, and the loser is the player who cannot
move.  Computing canonical forms with a small combinatorial game theory
engine reveals that the token-at-origin value of every (a, b, k)
staircase is

    G(a, b, k) = (b - a) + *(k - 1),

a number plus a nimber: each step of the frontier contributes one unit
of nim-like interaction, while the surplus of horizontal over vertical
moves contributes the integer b - a.  The formula is verified below by
exact canonical-form computation (domination + reversibility
simplification, and game comparison by the standard <= recursion) for
every staircase of weight at most 6 and a set of larger spot checks.

A sum of such games is Sigma(b_i - a_i) + *(XOR of (k_i - 1)).  The
first player wins iff the total is positive or fuzzy:

    Sigma d_i > 0   or   (Sigma d_i = 0 and XOR j_i != 0),

with d = b - a, j = k - 1.  Counting ordered m-tuples therefore needs
the joint distribution of (d, j) over staircases of weight <= w, raised
to the m-th convolution power: the d-axis is ordinary convolution and
the j-axis is XOR-convolution, diagonalised by a Walsh-Hadamard
transform over j < 64 (j <= 62 for w = 64).  The answer is
A + B0 - B0_xor0 where A counts Sigma d > 0, B0 counts Sigma d = 0 and
B0_xor0 counts Sigma d = 0 with zero XOR.  R(2, 4) = 7 and
R(3, 9) = 314104 are reproduced.
"""

import sys
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache

sys.setrecursionlimit(100000)
P = 10**9 + 7


class Game:
    __slots__ = ("left", "right", "_hash")
    left: tuple
    right: tuple
    _hash: int
    _intern: dict = {}

    def __new__(cls, left, right):
        left = tuple(dict.fromkeys(left))
        right = tuple(dict.fromkeys(right))
        key = (tuple(id(g) for g in left), tuple(id(g) for g in right))
        if key in cls._intern:
            return cls._intern[key]
        self = super().__new__(cls)
        self.left = left
        self.right = right
        self._hash = hash(key)
        cls._intern[key] = self
        return self

    def __hash__(self):
        return self._hash


ZERO = Game((), ())
_le_cache: dict = {}


def le(g: Game, h: Game) -> bool:
    key = (id(g), id(h))
    if key in _le_cache:
        return _le_cache[key]
    res = all(not le(h, gl) for gl in g.left) and all(
        not le(hr, g) for hr in h.right)
    _le_cache[key] = res
    return res


def eq(g: Game, h: Game) -> bool:
    return le(g, h) and le(h, g)


_canon_cache: dict = {}


def canonical(g: Game) -> Game:
    if id(g) in _canon_cache:
        return _canon_cache[id(g)]
    left = [canonical(x) for x in g.left]
    right = [canonical(x) for x in g.right]
    changed = True
    while changed:
        changed = False
        left = _undominated(left, True)
        right = _undominated(right, False)
        left, c1 = _bypass(left, g, True)
        right, c2 = _bypass(right, g, False)
        if c1 or c2:
            left = [canonical(x) for x in left]
            right = [canonical(x) for x in right]
            changed = True
    res = Game(left, right)
    _canon_cache[id(g)] = res
    _canon_cache[id(res)] = res
    return res


def _undominated(opts, is_left):
    out = []
    for i, x in enumerate(opts):
        dom = False
        for j, y in enumerate(opts):
            if i == j:
                continue
            better = le(x, y) if is_left else le(y, x)
            if better and (not (le(y, x) if is_left else le(x, y)) or j < i):
                dom = True
                break
        if not dom:
            out.append(x)
    return out


def _bypass(opts, g, is_left):
    changed = False
    out = []
    for o in opts:
        rev = None
        if is_left:
            for orr in o.right:
                if le(orr, g):
                    rev = orr.left
                    break
        else:
            for ol in o.left:
                if le(g, ol):
                    rev = ol.right
                    break
        if rev is not None:
            out.extend(rev)
            changed = True
        else:
            out.append(o)
    return out, changed


def num_game(fr: Fraction) -> Game:
    if fr == 0:
        return ZERO
    if fr.denominator == 1:
        n = fr.numerator
        if n > 0:
            return canonical(Game([num_game(Fraction(n - 1))], []))
        return canonical(Game([], [num_game(Fraction(n + 1))]))
    return canonical(Game([num_game(fr - Fraction(1, fr.denominator))],
                          [num_game(fr + Fraction(1, fr.denominator))]))


def nim_game(j: int) -> Game:
    games = [ZERO]
    for _ in range(j):
        games.append(canonical(Game(list(games), list(games))))
    return games[j]


def add(g: Game, h: Game) -> Game:
    @lru_cache(maxsize=None)
    def s(x, y):
        left = [s(xl, y) for xl in x.left] + [s(x, yl) for yl in y.left]
        right = [s(xr, y) for xr in x.right] + [s(x, yr) for yr in y.right]
        return Game(left, right)

    return canonical(s(g, h))


def staircase_game(a: int, b: int, k: int) -> Game:
    rows: list[int] = []
    for step in range(k, 0, -1):
        rows += [step * b] * a
    n = len(rows)

    @lru_cache(maxsize=None)
    def colheight(c: int) -> int:
        h = 0
        while h < n and rows[h] > c:
            h += 1
        return h

    @lru_cache(maxsize=None)
    def pos(r: int, c: int) -> Game:
        lops = [pos(r, c2) for c2 in range(c + 1, rows[r])]
        rops = [pos(r2, c) for r2 in range(r + 1, colheight(c))]
        return canonical(Game(lops, rops))

    return pos(0, 0)


def _conv(x: list[int], y: list[int]) -> list[int]:
    out = [0] * (len(x) + len(y) - 1)
    for i, xv in enumerate(x):
        if xv:
            for j, yv in enumerate(y):
                if yv:
                    out[i + j] = (out[i + j] + xv * yv) % P
    return out


def solve(m: int, w: int) -> int:
    nx = 64  # covers j = k - 1 <= w - 2 <= 62
    assert w - 2 < nx
    counts: dict[tuple[int, int], int] = defaultdict(int)
    for a in range(1, w - 1):
        for b in range(1, w - a):
            for k in range(1, w - a - b + 1):
                counts[(b - a, k - 1)] += 1
    size_d = 2 * (w - 1) + 1
    base = [[0] * nx for _ in range(size_d)]
    for (d, j), c in counts.items():
        base[d + (w - 1)][j] += c
    marg = [sum(row) % P for row in base]
    conv = [1]
    for _ in range(m):
        conv = _conv(conv, marg)
    zero_idx = m * (w - 1)
    a_count = sum(conv[zero_idx + 1:]) % P
    b0 = conv[zero_idx]
    h = 1  # Walsh-Hadamard over the nim axis
    while h < nx:
        for i in range(0, nx, 2 * h):
            for t in range(i, i + h):
                for row in base:
                    x, y = row[t], row[t + h]
                    row[t], row[t + h] = (x + y) % P, (x - y) % P
        h *= 2
    tot0 = 0
    for t in range(nx):
        col = [row[t] for row in base]
        c = [1]
        for _ in range(m):
            c = _conv(c, col)
        tot0 = (tot0 + c[zero_idx]) % P
    b0_xor0 = tot0 * pow(nx, P - 2, P) % P
    return (a_count + b0 - b0_xor0) % P


if __name__ == "__main__":
    weight = 6
    for a in range(1, weight - 1):
        for b in range(1, weight - a):
            for k in range(1, weight - a - b + 1):
                g = staircase_game(a, b, k)
                expect = add(num_game(Fraction(b - a)), nim_game(k - 1))
                assert eq(g, expect), (a, b, k)
    for a, b, k in [(2, 4, 3), (4, 2, 2), (2, 2, 6), (1, 2, 7), (3, 1, 5),
                    (3, 5, 2), (4, 4, 2)]:
        g = staircase_game(a, b, k)
        assert eq(g, add(num_game(Fraction(b - a)), nim_game(k - 1))), (a, b, k)
    assert solve(2, 4) == 7
    assert solve(3, 9) == 314104
    print(solve(8, 64))  # 858945298
