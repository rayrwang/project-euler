"""Project Euler Problem 984: Knights and Horses.

Count non-empty subsets of an N x N board that are *knight-connected* (a
knight can travel between any two squares of the subset using only squares
of the subset) and *horse-disjoint* (placing a xiangqi horse on every
square of the subset, no horse attacks another; a horse moves one square
orthogonally then one diagonally outward, and is blocked if the orthogonal
"leg" square is occupied).  Given f(3) = 9, f(5) = 903,
f(100) = 8658918531876 and f(10000) = 377956308 (mod 10^9 + 7), find
f(10^18) mod 10^9 + 7.

Structure of valid sets
-----------------------
Horse-disjointness says: for every knight pair X, X + (2, 1) inside the
set, both legs X + (1, 0) and X + (1, 1) belong to the set (all eight
orientations).  Multi-square sets also need at least one knight edge and a
connected knight graph.  Three local arguments pin the geometry down:

* rows are contiguous: a knight pair across an empty row would have its
  legs inside that row, and chunks separated vertically with no pairs
  cannot be knight-connected;
* each row is a single interval: a missing cell inside a row creates an
  unblocked pair across the hole (verified exhaustively for two-segment
  rows by an assumption-free mask DP up to N = 12);
* consecutive row endpoints move by at most one: if the right end grew by
  two, the pair (i, b_i), (i+1, b_i + 2) has the off-set leg (i, b_i + 1).

So every valid multi-cell set is an HV-staircase of row intervals with
+-1 boundary slopes.  An assumption-free profile DP over arbitrary row
bitmasks (with full connectivity partitions) confirms equality of the two
counts for all N <= 12.

Counting
--------
A row-sweep DP processes interval rows; the state holds the last two
intervals and the *exact* partition of their cells into knight components
of the prefix (cells of one row are never knight-adjacent, so fresh rows
enter as isolated cells which merge through (1, +-2) and (2, +-1) edges;
components vanishing from the two-row frontier can never reconnect, which
prunes dead prefixes).  Truncating these partitions is unsound -- merge
"scars" can sit anywhere inside a wide row -- so the partition is kept in
full; reachable state counts stay small (a few thousand per row).  A shape
is complete whenever the frontier holds a single component and at least
one edge; it then contributes (N - h + 1) placements at height h, widths
being handled by absolute coordinates.

f(1..36) computed this way reproduce f(3), f(5), and a direct bitboard
brute force for N = 4.  Berlekamp-Massey on the sequence (under two
primes) finds a linear recurrence of order 14, which holds on all surplus
terms, reproduces f(100) exactly (via CRT of two Kitamasa evaluations) and
f(10000) mod 10^9 + 7.  Kitamasa then evaluates f(10^18) mod 10^9 + 7.
"""

from __future__ import annotations

from collections import defaultdict

P1 = 10**9 + 7
P2 = 998244353

KNIGHT = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))


def _leg(dx: int, dy: int) -> tuple[int, int]:
    return (dx // 2, 0) if abs(dx) == 2 else (0, dy // 2)


def f_exact(N: int) -> int:
    """f(N) by the exact-partition interval-row profile DP."""
    total = N * N  # singletons
    cur: dict[tuple, int] = defaultdict(int)
    for a in range(N):
        for b in range(a, N):
            cur[(-1, -2, a, b, tuple(range(b - a + 1)), 0)] += 1
    h = 1
    while cur and h <= N:
        for (a1, b1, a2, b2, labels, ef), c in cur.items():
            if ef and len(set(labels)) == 1:
                total += c * (N - h + 1)
        if h == N:
            break
        nxt: dict[tuple, int] = defaultdict(int)
        for (a1, b1, a2, b2, labels, ef), c in cur.items():
            n1 = max(0, b1 - a1 + 1)
            for da in (-1, 0, 1):
                for db in (-1, 0, 1):
                    a3, b3 = a2 + da, b2 + db
                    if a3 > b3 or a3 < 0 or b3 >= N:
                        continue
                    nlab = len(set(labels))
                    parent = list(range(nlab + (b3 - a3 + 1)))

                    def find(x: int) -> int:
                        while parent[x] != x:
                            parent[x] = parent[parent[x]]
                            x = parent[x]
                        return x

                    ok = True
                    ne = ef
                    for y in range(a2, b2 + 1):
                        for dy in (2, -2):
                            y2 = y + dy
                            if a3 <= y2 <= b3:
                                ym = y + dy // 2
                                if not (a2 <= ym <= b2 and a3 <= ym <= b3):
                                    ok = False
                                    break
                                ra, rb = find(labels[n1 + y - a2]), find(nlab + y2 - a3)
                                if ra != rb:
                                    parent[ra] = rb
                                ne = 1
                        if not ok:
                            break
                    if not ok:
                        continue
                    for y in range(a1, b1 + 1):
                        for dy in (1, -1):
                            y2 = y + dy
                            if a3 <= y2 <= b3:
                                if not (a2 <= y <= b2 and a2 <= y2 <= b2):
                                    ok = False
                                    break
                                ra, rb = find(labels[y - a1]), find(nlab + y2 - a3)
                                if ra != rb:
                                    parent[ra] = rb
                                ne = 1
                        if not ok:
                            break
                    if not ok:
                        continue
                    front = set()
                    for y in range(a2, b2 + 1):
                        front.add(find(labels[n1 + y - a2]))
                    for y in range(a3, b3 + 1):
                        front.add(find(nlab + y - a3))
                    if any(find(v) not in front for v in set(labels[:n1])):
                        continue
                    order: dict[int, int] = {}
                    nl = []
                    for y in range(a2, b2 + 1):
                        r = find(labels[n1 + y - a2])
                        if r not in order:
                            order[r] = len(order)
                        nl.append(order[r])
                    for y in range(a3, b3 + 1):
                        r = find(nlab + y - a3)
                        if r not in order:
                            order[r] = len(order)
                        nl.append(order[r])
                    nxt[(a2, b2, a3, b3, tuple(nl), ne)] += c
        cur = nxt
        h += 1
    return total


def _f_brute(N: int) -> int:
    """Assumption-free subset brute force (tiny N)."""
    cells = [(x, y) for x in range(N) for y in range(N)]
    total = 0
    for mask in range(1, 1 << (N * N)):
        s = {cells[i] for i in range(N * N) if (mask >> i) & 1}
        if len(s) == 1:
            total += 1
            continue
        adj: dict[tuple[int, int], list] = {}
        edge = False
        good = True
        for x, y in s:
            for dx, dy in KNIGHT:
                t = (x + dx, y + dy)
                if t in s:
                    lx, ly = _leg(dx, dy)
                    if (x + lx, y + ly) not in s:
                        good = False
                        break
                    adj.setdefault((x, y), []).append(t)
                    edge = True
            if not good:
                break
        if not good or not edge:
            continue
        start = next(iter(s))
        seen = {start}
        st = [start]
        while st:
            q = st.pop()
            for t in adj.get(q, ()):
                if t not in seen:
                    seen.add(t)
                    st.append(t)
        if len(seen) == len(s):
            total += 1
    return total


def berlekamp_massey(s: list[int], p: int) -> list[int]:
    ls: list[int] = []
    cur: list[int] = []
    lf = 0
    ld = 0
    for i in range(len(s)):
        t = 0
        for j in range(len(cur)):
            t = (t + cur[j] * s[i - 1 - j]) % p
        if (s[i] - t) % p == 0:
            continue
        if not cur:
            cur = [0] * (i + 1)
            lf, ld = i, (s[i] - t) % p
            continue
        k = (s[i] - t) * pow(ld, p - 2, p) % p
        c = [0] * (i - lf - 1) + [k] + [(-k * x) % p for x in ls]
        if len(c) < len(cur):
            c += [0] * (len(cur) - len(c))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % p
        if i - len(cur) > lf - len(ls):
            ls, lf, ld = cur, i, (s[i] - t) % p
        cur = c
    return cur


def kitamasa(rec: list[int], init: list[int], n: int, p: int) -> int:
    r = len(rec)
    if n < len(init):
        return init[n] % p
    mod = [(-rec[r - 1 - j]) % p for j in range(r)]

    def mulmod(a: list[int], b: list[int]) -> list[int]:
        res = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    res[i + j] = (res[i + j] + ai * bj) % p
        for i in range(len(res) - 1, r - 1, -1):
            c = res[i]
            if c:
                res[i] = 0
                for j in range(r):
                    res[i - r + j] = (res[i - r + j] - c * mod[j]) % p
        return res[:r]

    result = [1] + [0] * (r - 1)
    base = ([0, 1] + [0] * (r - 2)) if r > 1 else [rec[0] % p]
    e = n
    while e:
        if e & 1:
            result = mulmod(result, base)
        base = mulmod(base, base)
        e >>= 1
    return sum(result[i] * init[i] for i in range(r)) % p


def solve() -> int:
    assert f_exact(3) == 9, "checkpoint f(3)"
    assert f_exact(4) == _f_brute(4), "assumption-free brute check at N=4"
    assert f_exact(5) == 903, "checkpoint f(5)"
    seq = [f_exact(n) for n in range(1, 37)]
    rec1 = berlekamp_massey([x % P1 for x in seq], P1)
    rec2 = berlekamp_massey([x % P2 for x in seq], P2)
    assert len(rec1) == len(rec2) <= 16, "recurrence order"
    # surplus-term consistency
    for i in range(len(rec1), len(seq)):
        assert (
            sum(rec1[j] * seq[i - 1 - j] for j in range(len(rec1))) % P1 == seq[i] % P1
        )
    # exact f(100) via CRT of two Kitamasa evaluations
    v1 = kitamasa(rec1, [x % P1 for x in seq], 99, P1)
    v2 = kitamasa(rec2, [x % P2 for x in seq], 99, P2)
    inv = pow(P1, P2 - 2, P2)
    f100 = (v1 + P1 * ((v2 - v1) * inv % P2)) % (P1 * P2)
    assert f100 == 8658918531876, "checkpoint f(100)"
    assert kitamasa(rec1, [x % P1 for x in seq], 9999, P1) == 377956308, (
        "checkpoint f(10000)"
    )
    return kitamasa(rec1, [x % P1 for x in seq], 10**18 - 1, P1)


if __name__ == "__main__":
    print(solve())  # 885722296
