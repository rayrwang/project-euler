"""Project Euler 963: Ternary Game.

The position is a sum of partizan games, one per number: for a number on
Left's paper, Left may delete a 0 or a 2 from its ternary expansion and
Right may delete a 1 or a 2 (leading zeros evaporate after a deletion --
this convention, as in problem 882, reproduces the given F(5) = 21,
verified below by a direct compound-game solver, whereas forbidding such
moves gives 29). A number on the other paper is the negative of the same
game. The setting (x1, x2 | y1, y2) is fair -- the first mover loses
either way -- exactly when the compound game is a second-player win, i.e.
G(x1) + G(x2) - G(y1) - G(y2) = 0, so fairness only depends on the game
value G(x1) + G(x2), and F(N) = sum over value classes of (number of
unordered pairs in the class)^2.

Single-number values are computed in canonical form with a small CGT
engine (interned games, memoised <=, dominance and reversibility
reduction, memoised sums). For N = 10^5 there are 3072 distinct values.
Each one turns out to be (dyadic number) + (infinitesimal): the left and
right stops agree (asserted), the number part q is the common stop, and
u = G - q is one of only 768 distinct infinitesimals (uptimal-like values
built from *, up, and friends). Sums therefore carry the label
(q1 + q2, canonical id of u1 + u2), needing only ~300k infinitesimal
additions instead of millions of full-value additions.

The pipeline reproduces F(5) = 21 (also checked against the direct
solver) and F(12) = 292 (direct solver), and gives F(10^5) in about a
minute.
"""

import math
import sys

from collections import Counter
from fractions import Fraction
from functools import lru_cache

sys.setrecursionlimit(100000)

N = 10**5

# ---------------------------------------------------------------- engine
_games: dict[tuple, int] = {}
_by_id: list[tuple] = []


def intern(lo: tuple, ro: tuple) -> int:
    key = (tuple(sorted(set(lo))), tuple(sorted(set(ro))))
    if key not in _games:
        _games[key] = len(_by_id)
        _by_id.append(key)
    return _games[key]


ZERO = intern((), ())


@lru_cache(maxsize=None)
def leq(g: int, h: int) -> bool:
    gl, _gr = _by_id[g]
    _hl, hr = _by_id[h]
    for x in gl:
        if leq(h, x):
            return False
    for y in hr:
        if leq(y, g):
            return False
    return True


def canonical(lo: list[int], ro: list[int]) -> int:
    lo, ro = list(set(lo)), list(set(ro))
    changed = True
    while changed:
        changed = False
        keep = []
        for i, x in enumerate(lo):
            if any(
                j != i and leq(x, y) and (not leq(y, x) or j < i)
                for j, y in enumerate(lo)
            ):
                continue
            keep.append(x)
        if len(keep) != len(lo):
            lo, changed = keep, True
        keep = []
        for i, x in enumerate(ro):
            if any(
                j != i and leq(y, x) and (not leq(x, y) or j < i)
                for j, y in enumerate(ro)
            ):
                continue
            keep.append(x)
        if len(keep) != len(ro):
            ro, changed = keep, True
        g = intern(tuple(lo), tuple(ro))
        for x in list(lo):
            rev = next((r for r in _by_id[x][1] if leq(r, g)), None)
            if rev is not None:
                lo.remove(x)
                lo = list(set(lo) | set(_by_id[rev][0]))
                changed = True
                break
        if changed:
            continue
        for y in list(ro):
            rev = next((r for r in _by_id[y][0] if leq(g, r)), None)
            if rev is not None:
                ro.remove(y)
                ro = list(set(ro) | set(_by_id[rev][1]))
                changed = True
                break
    return intern(tuple(lo), tuple(ro))


@lru_cache(maxsize=None)
def neg(g: int) -> int:
    gl, gr = _by_id[g]
    return intern(tuple(neg(x) for x in gr), tuple(neg(x) for x in gl))


@lru_cache(maxsize=None)
def add(g: int, h: int) -> int:
    if g > h:
        g, h = h, g
    gl, gr = _by_id[g]
    hl, hr = _by_id[h]
    lo = [add(x, h) for x in gl] + [add(g, x) for x in hl]
    ro = [add(x, h) for x in gr] + [add(g, x) for x in hr]
    return canonical(lo, ro)


# ----------------------------------------------- single-number values
@lru_cache(maxsize=None)
def value_str(s: str) -> int:
    """Game of ternary string s owned by Left (Left deletes 0/2, Right 1/2)."""
    lo, ro = [], []
    for i, ch in enumerate(s):
        rest = (s[:i] + s[i + 1 :]).lstrip("0")
        v = value_str(rest)
        if ch == "0":
            lo.append(v)
        elif ch == "1":
            ro.append(v)
        else:
            lo.append(v)
            ro.append(v)
    return canonical(lo, ro)


def tern(x: int) -> str:
    s = ""
    while x:
        s = str(x % 3) + s
        x //= 3
    return s


# -------------------------------------- number-part / infinitesimal split
@lru_cache(maxsize=None)
def num_value(g: int) -> Fraction | None:
    """Fraction if canonical game g is a number, else None."""
    gl, gr = _by_id[g]
    if g == ZERO:
        return Fraction(0)
    if len(gl) == 1 and not gr:
        v = num_value(gl[0])
        return v + 1 if v is not None and v >= 0 and v == int(v) else None
    if len(gr) == 1 and not gl:
        v = num_value(gr[0])
        return v - 1 if v is not None and v <= 0 and v == int(v) else None
    if len(gl) == 1 and len(gr) == 1:
        a, b = num_value(gl[0]), num_value(gr[0])
        if a is not None and b is not None and a < b:
            if a < 0 < b:
                return Fraction(0)
            if math.floor(a) + 1 < b:
                return Fraction(math.floor(a) + 1 if a >= 0 else math.ceil(b) - 1)
            k = 1
            while True:
                f = Fraction(math.floor(a * (1 << k)) + 1, 1 << k)
                if a < f < b:
                    return f
                k += 1
    return None


@lru_cache(maxsize=None)
def left_stop(g: int) -> Fraction:
    v = num_value(g)
    if v is not None:
        return v
    return max(right_stop(x) for x in _by_id[g][0])


@lru_cache(maxsize=None)
def right_stop(g: int) -> Fraction:
    v = num_value(g)
    if v is not None:
        return v
    return min(left_stop(x) for x in _by_id[g][1])


@lru_cache(maxsize=None)
def num_game(q: Fraction) -> int:
    if q == 0:
        return ZERO
    if q == int(q):
        n = int(q)
        if n > 0:
            return canonical([num_game(Fraction(n - 1))], [])
        return canonical([], [num_game(Fraction(n + 1))])
    d = q.denominator
    return canonical(
        [num_game(Fraction(q.numerator - 1, d))],
        [num_game(Fraction(q.numerator + 1, d))],
    )


def decompose(v: int) -> tuple[Fraction, int]:
    ls, rs = left_stop(v), right_stop(v)
    assert ls == rs
    return ls, add(v, neg(num_game(ls)))


# --------------------------------------------- direct solver (validation)
def _moves(s: str, digit: str) -> list[str]:
    return [(s[:i] + s[i + 1 :]).lstrip("0") for i, ch in enumerate(s) if ch == digit]


@lru_cache(maxsize=None)
def _win(state: tuple) -> bool:
    own, opp = state
    for k, s in enumerate(own):
        for r in _moves(s, "0") + _moves(s, "2"):
            if not _win((opp, tuple(sorted(own[:k] + (r,) + own[k + 1 :])))):
                return True
    for k, s in enumerate(opp):
        for r in _moves(s, "1") + _moves(s, "2"):
            if not _win((tuple(sorted(opp[:k] + (r,) + opp[k + 1 :])), own)):
                return True
    return False


def f_direct(n: int) -> int:
    pairs = [
        tuple(sorted((tern(x1), tern(x2))))
        for x1 in range(1, n + 1)
        for x2 in range(x1, n + 1)
    ]
    return sum(
        1 for pa in pairs for pb in pairs if not _win((pa, pb)) and not _win((pb, pa))
    )


# ------------------------------------------------------------- pipeline
def f_of(n: int) -> int:
    cnt: Counter = Counter()
    for x in range(1, n + 1):
        cnt[value_str(tern(x))] += 1
    classes = [(*decompose(v), c) for v, c in cnt.items()]
    pair_counts: Counter = Counter()
    inf_sum: dict[tuple[int, int], int] = {}
    k = len(classes)
    for i in range(k):
        qi, ui, ci = classes[i]
        for j in range(i, k):
            qj, uj, cj = classes[j]
            key = (ui, uj) if ui <= uj else (uj, ui)
            s = inf_sum.get(key)
            if s is None:
                s = inf_sum[key] = add(ui, uj)
            pair_counts[(qi + qj, s)] += ci * cj if i < j else ci * (ci + 1) // 2
    return sum(c * c for c in pair_counts.values())


def solve() -> int:
    assert f_direct(5) == 21  # confirms the evaporation convention
    assert f_of(5) == 21
    assert f_of(12) == 292 == f_direct(12)
    return f_of(N)


if __name__ == "__main__":
    print(solve())  # 55129975871328418
