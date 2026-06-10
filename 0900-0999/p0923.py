"""Project Euler 923: Young's Game B.

Like Problem 922 but moves are a single square.  Computing canonical
forms with a CGT engine reveals a periodic closed form: writing
r = (k b) mod (a + b),

    G(a, b, k) = the number r - a            if r != 0,
                 the switch {b - 1 | 1 - a}  if r == 0,

the switch case occurring exactly when (a + b)/gcd(a, b) divides k (and
degenerating to * for a = b = 1).  The formula is verified below by
exact canonical-form computation for every staircase of weight <= 10
and higher-weight spot checks.

A sum of numbers and switches is resolved by the classical rule for
sums of switches: each player moves in a hottest switch, so with
switches sorted by temperature t_1 >= t_2 >= ... (t = (a+b-2)/2, mean
mu = (b-a)/2) the final score for the first player is

    V = sum(numbers) + sum(mu_i) + t_1 - t_2 + t_3 - ...,

after which the player on move at the integer V loses iff V = 0.  Hence
Right (first player) wins iff V > 0, or V = 0 with an odd number of
switch components.  This outcome rule is verified against the engine on
all small sums from a value zoo.

Counting ordered m-tuples: process switch classes (a + b, b - a) in
decreasing temperature; equal temperatures commute in the alternating
sum, and a block of mm equal-temperature switches added after s
switches contributes 2t * (+-1 if mm odd else 0) by parity of s.  A DP
over (slots filled, switch parity, 2V) with binomial slot choices and
class-count powers counts everything; number classes join afterwards
with no rank interaction.  S(2, 4) = 7 and S(3, 9) = 315319 are
reproduced.
"""

import sys
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, gcd

import numpy as np

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


def switch_game(x: int, y: int) -> Game:
    return canonical(Game([num_game(Fraction(x))], [num_game(Fraction(y))]))


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
        lops = [pos(r, c + 1)] if c + 1 < rows[r] else []
        rops = [pos(r + 1, c)] if r + 1 < colheight(c) else []
        return canonical(Game(lops, rops))

    return pos(0, 0)


def value_of(a: int, b: int, k: int):
    r = (k * b) % (a + b)
    if r:
        return ("num", r - a)
    return ("sw", b - 1, 1 - a)


def _outcome_formula(comps) -> bool:
    nums = sum(c[1] for c in comps if c[0] == "num")
    sws = sorted((((c[1] + c[2]), (c[1] - c[2])) for c in comps
                  if c[0] == "sw"), key=lambda mt: -mt[1])
    v2 = 2 * nums
    for i, (mu2, t2) in enumerate(sws):
        v2 += mu2 + (t2 if i % 2 == 0 else -t2)
    return v2 > 0 or (v2 == 0 and len(sws) % 2 == 1)


def solve(m: int, w: int) -> int:
    num_counts: dict[int, int] = defaultdict(int)
    sw_counts: dict[tuple[int, int], int] = defaultdict(int)
    for a in range(1, w - 1):
        for b in range(1, w - a):
            period = (a + b) // gcd(a, b)
            kmax = w - a - b
            for k in range(1, kmax + 1):
                r = (k * b) % (a + b)
                if r:
                    num_counts[r - a] += 1
            sw_counts[(a + b, b - a)] += kmax // period
    off = m * 2 * w
    size = 2 * off + 1
    dp = np.zeros((m + 1, 2, size), dtype=np.int64)
    dp[0, 0, off] = 1

    def apply_class(dp, cnt, shift_of, par_flip):
        new = dp.copy()
        pow_n = 1
        for mm in range(1, m + 1):
            pow_n = pow_n * cnt % P
            for k in range(0, m - mm + 1):
                coef = comb(m - k, mm) % P * pow_n % P
                for par in (0, 1):
                    src = dp[k, par]
                    if not src.any():
                        continue
                    shift = shift_of(mm, par)
                    npar = par ^ (mm & 1) if par_flip else par
                    if shift >= 0:
                        new[k + mm, npar, shift:] = (
                            new[k + mm, npar, shift:]
                            + src[:size - shift] * coef) % P
                    else:
                        new[k + mm, npar, :shift] = (
                            new[k + mm, npar, :shift]
                            + src[-shift:] * coef) % P
        return new

    for (ab, bma), cnt in sorted(sw_counts.items(), key=lambda x: -x[0][0]):
        if not cnt:
            continue
        t2 = ab - 2

        def sh(mm, par, mu2=bma, t2=t2):
            da = 0 if mm % 2 == 0 else (t2 if par == 0 else -t2)
            return mm * mu2 + da

        dp = apply_class(dp, cnt, sh, True)
    for v, cnt in num_counts.items():
        if not cnt:
            continue
        dp = apply_class(dp, cnt, lambda mm, par, v=v: mm * 2 * v, False)
    win = int(dp[m, :, off + 1:].sum() % P)
    return (win + int(dp[m, 1, off])) % P


if __name__ == "__main__":
    import itertools

    weight = 10
    for a in range(1, weight - 1):
        for b in range(1, weight - a):
            for k in range(1, weight - a - b + 1):
                v = value_of(a, b, k)
                expect = (num_game(Fraction(v[1])) if v[0] == "num"
                          else switch_game(v[1], v[2]))
                assert eq(staircase_game(a, b, k), expect), (a, b, k)
    for a, b, k in [(2, 3, 8), (4, 5, 9), (3, 7, 8), (5, 2, 12), (2, 8, 9)]:
        v = value_of(a, b, k)
        expect = (num_game(Fraction(v[1])) if v[0] == "num"
                  else switch_game(v[1], v[2]))
        assert eq(staircase_game(a, b, k), expect), (a, b, k)
    zoo = [("num", v, 0) for v in (-2, -1, 0, 1, 2)] + [
        ("sw", 0, 0), ("sw", 1, 0), ("sw", 0, -1), ("sw", 1, -1),
        ("sw", 2, 0), ("sw", 2, -1), ("sw", 2, -2)]
    for r in (1, 2, 3):
        for comps in itertools.combinations_with_replacement(zoo, r):
            g = ZERO
            for c in comps:
                cg = (num_game(Fraction(c[1])) if c[0] == "num"
                      else switch_game(c[1], c[2]))
                g = add(g, cg)
            assert _outcome_formula(comps) == (not le(g, ZERO)), comps
    assert solve(2, 4) == 7
    assert solve(3, 9) == 315319
    print(solve(8, 64))  # 740759929
