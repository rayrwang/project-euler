"""Project Euler Problem 669: The King's Banquet.

With the king breaking the circle, an arrangement is a Hamiltonian path
on knights 1..n with edges between numbers summing to a Fibonacci
number, read from the king's left, which by the left-smaller rule is
the path's smaller endpoint.  n = 99194853094755497 = F(83).

Exhaustive search (unit-propagation over edge choices) for
n = F(8)..F(14) reveals a clean recursion.  Every edge of path(F(m))
sums to F(m-1), F(m) or F(m+1), and path(F(m+1)) is obtained by:
  * inserting the pair (F(m+1) - a, F(m+1) - b) into every edge (a, b)
    with a + b = F(m-1) (the new edges sum to F(m+1), F(m+2), F(m+1));
  * appending F(m+1) after the final element F(m);
  * prepending F(m+1) - first exactly when F(m-1) is even, i.e. when
    m = 1 mod 3, which is forced by parity: the F(m-1) new knights fill
    2 * (number of small edges) + 1 slots otherwise.
The edge-sum word therefore evolves by the substitution S -> MLM,
M -> S, L -> M with an L appended and an M prepended every third level,
where S, M, L mark sums F(m-1), F(m), F(m+1).  This construction
reproduces the search results exactly for n = 34, 55, 89, 144, 233, 377
(including both boundary-ambiguous variants at 55 and 233, where it
selects the member that the unique next level extends).

To read off position P = 10^16 at level 83 without building anything,
the edge word unrolls into O(level) blocks h^j(w) for short words w, so
prefix counts of S come from precomputed count vectors of h^j per
symbol plus an O(j) descent into one block.  An old vertex j sits at
new position prepend + j + 2 * (number of S among the first j - 1 old
edges); binary search inverts this map, classifying P per level as an
old vertex (recurse), a pair member (F(level) minus the neighbour's
value), the prepend, or the appended F(level).

Verified: the descent against the explicit construction for every
position up to level 21, the n = 34 example (3rd chair is knight 30),
and the n = 7 example by direct search.
"""

from functools import lru_cache

K = 83
POS = 10**16
BASE_LEVEL = 8
BASE = [17, 4, 9, 12, 1, 20, 14, 7, 6, 15, 19, 2, 11, 10, 3, 18, 16, 5,
        8, 13, 21]  # the unique path for n = F(8) = 21

FIB = [0, 1, 1]
while len(FIB) <= K + 3:
    FIB.append(FIB[-1] + FIB[-2])

EXPAND = {"S": "MLM", "M": "S", "L": "M"}
MAXPOW = K - BASE_LEVEL + 1
# COUNTS[sym][j] = (S, M, L) counts of h^j(sym)
COUNTS: dict[str, list[tuple[int, int, int]]] = {
    "S": [(1, 0, 0)], "M": [(0, 1, 0)], "L": [(0, 0, 1)]}
for j in range(1, MAXPOW + 1):
    for sym in "SML":
        s = m = ell = 0
        for child in EXPAND[sym]:
            cs, cm, cl = COUNTS[child][j - 1]
            s += cs
            m += cm
            ell += cl
        COUNTS[sym].append((s, m, ell))


def block_len(sym: str, power: int) -> int:
    return sum(COUNTS[sym][power])


def base_word() -> str:
    word = []
    for a, b in zip(BASE, BASE[1:]):
        total = a + b
        word.append({FIB[7]: "S", FIB[8]: "M", FIB[9]: "L"}[total])
    return "".join(word)


SIGMA8 = base_word()


def prepended(step: int) -> bool:
    """Whether the step from level `step` to `step + 1` prepends."""
    return step % 3 == 1


@lru_cache(maxsize=None)
def blocks(level: int) -> tuple[tuple[str, int], ...]:
    """sigma_level as concatenated h^power(word) blocks."""
    out: list[tuple[str, int]] = []
    for j in range(level - 1, BASE_LEVEL - 1, -1):
        if prepended(j):
            out.append(("M", level - 1 - j))
    out.append((SIGMA8, level - BASE_LEVEL))
    for j in range(BASE_LEVEL, level):
        out.append(("L", level - 1 - j))
    return tuple(out)


def descend_s_count(sym: str, power: int, t: int) -> int:
    """Number of S among the first t symbols of h^power(sym)."""
    total = 0
    while t > 0:
        if power == 0:
            return total + (1 if sym == "S" and t >= 1 else 0)
        for child in EXPAND[sym]:
            ln = block_len(child, power - 1)
            if t >= ln:
                total += COUNTS[child][power - 1][0]
                t -= ln
            else:
                sym = child
                power -= 1
                break
        else:
            return total
    return total


def pref_s(level: int, t: int) -> int:
    """Number of S among the first t edge symbols of sigma_level."""
    if level == BASE_LEVEL:
        return SIGMA8[:t].count("S")
    total = 0
    for word, power in blocks(level):
        for sym in word:
            ln = block_len(sym, power)
            if t >= ln:
                total += COUNTS[sym][power][0]
                t -= ln
            else:
                return total + descend_s_count(sym, power, t)
            if t == 0:
                return total
    return total


def value(level: int, pos: int) -> int:
    """The knight in chair `pos` from the king's left, n = F(level)."""
    if level == BASE_LEVEL:
        return BASE[pos - 1]
    m = level - 1
    pre = 1 if prepended(m) else 0
    if pre and pos == 1:
        return FIB[level] - value(m, 1)
    if pos == FIB[level]:
        return FIB[level]

    def new_pos(j: int) -> int:
        return pre + j + 2 * pref_s(m, j - 1)

    lo, hi = 1, FIB[m]
    while lo < hi:  # largest j with new_pos(j) <= pos
        mid = (lo + hi + 1) // 2
        if new_pos(mid) <= pos:
            lo = mid
        else:
            hi = mid - 1
    if new_pos(lo) == pos:
        return value(m, lo)
    if pos - new_pos(lo) == 1:
        return FIB[level] - value(m, lo)
    return FIB[level] - value(m, lo + 1)


def build(level: int) -> list[int]:
    path = BASE[:]
    for m in range(BASE_LEVEL, level):
        nxt_fib = FIB[m + 1]
        small = FIB[m - 1]
        new = [nxt_fib - path[0]] if prepended(m) else []
        for i, v in enumerate(path):
            new.append(v)
            if i + 1 < len(path) and v + path[i + 1] == small:
                new.append(nxt_fib - v)
                new.append(nxt_fib - path[i + 1])
        new.append(nxt_fib)
        path = new
    return path


def brute_n7() -> list[int]:
    fset = {2, 3, 5, 8, 13}
    adj = {a: [b for b in range(1, 8)
               if b != a and a + b in fset] for a in range(1, 8)}
    found = []

    def dfs(path: list[int]) -> None:
        if len(path) == 7:
            found.append(path[:])
            return
        for w in adj[path[-1]]:
            if w not in path:
                dfs([*path, w])

    for s in range(1, 8):
        dfs([s])
    paths = {tuple(p) if p[0] < p[-1] else tuple(reversed(p))
             for p in found}
    assert len(paths) == 1
    return list(next(iter(paths)))


if __name__ == "__main__":
    assert brute_n7() == [4, 1, 7, 6, 2, 3, 5]  # 3rd chair: knight 7
    assert FIB[K] == 99_194_853_094_755_497
    for level in range(9, 22):
        path = build(level)
        fset = {FIB[i] for i in range(2, level + 3)}
        assert sorted(path) == list(range(1, FIB[level] + 1))
        assert all(a + b in fset for a, b in zip(path, path[1:]))
        assert path[0] < path[-1]
        assert all(value(level, i + 1) == v for i, v in enumerate(path))
    assert value(9, 3) == 30  # the n = 34 example
    print(value(K, POS))  # 56342087360542122
