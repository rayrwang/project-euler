import sys
from functools import lru_cache

sys.setrecursionlimit(300000)

MOD = 10**18

def fib_game_winning_moves(k: int, mod: int) -> int:
    """f(k): winning first moves on the Fibonacci tree T(k), mod `mod`.

    A move removes a node with its subtree; whoever is forced to take the
    overall root loses, which is normal play on the non-root nodes. For a
    removable subtree the Grundy value satisfies G = 1 + xor of children
    (mex over removing the subtree's own root, giving 0, and the moves
    inside the children), so G(j) = 1 + (G(j-1) ^ G(j-2)) with G(0) = 0,
    G(1) = 1, and the whole position has value G(k-1) ^ G(k-2).

    A first move inside the T(k-1) child wins iff it moves that child's
    value to G(k-2), and symmetrically, so f(k) = cnt(k-1, G(k-2)) +
    cnt(k-2, G(k-1)) where cnt(j, t) counts nodes of T(j) whose removal
    sets its value to t: removing T(j) itself is the unique move to 0
    (interior moves give 1 + xor >= 1), and for t >= 1 the move sits in
    one of the two children with the target xor-adjusted:
        cnt(j, t) = cnt(j-1, (t-1) ^ G(j-2)) + cnt(j-2, (t-1) ^ G(j-1)).
    The reachable (j, t) states stay sparse (about 1.7 * 10^7 at
    k = 10^4), and counts only ever add, so reducing mod 10^18 is safe.
    """
    g = {0: 0, 1: 1}
    for j in range(2, k + 1):
        g[j] = 1 + (g[j - 1] ^ g[j - 2])
    memo: dict[tuple[int, int], int] = {}

    def cnt(j: int, t: int) -> int:
        if j == 0:
            return 0
        if t == 0:
            return 1
        if j == 1:
            return 0
        key = (j, t)
        if key in memo:
            return memo[key]
        r = (cnt(j - 1, (t - 1) ^ g[j - 2])
             + cnt(j - 2, (t - 1) ^ g[j - 1])) % mod
        memo[key] = r
        return r

    if k == 1:
        return 0  # only the root exists: no winning first move
    return (cnt(k - 1, g[k - 2]) + cnt(k - 2, g[k - 1])) % mod

def fib_tree(k: int):
    if k == 0:
        return None
    if k == 1:
        return ()
    return tuple(t for t in (fib_tree(k - 1), fib_tree(k - 2))
                 if t is not None)

def canon(tree):
    return tuple(sorted(canon(c) for c in tree))

def prunes(tree):
    """Each yielded result is the removal of exactly one node's subtree;
    None means the whole tree was removed."""
    yield None
    for i, c in enumerate(tree):
        for r in prunes(c):
            if r is None:
                yield tree[:i] + tree[i + 1:]
            else:
                yield tree[:i] + (r,) + tree[i + 1:]

@lru_cache(maxsize=None)
def wins(forest) -> bool:
    for i, t in enumerate(forest):
        for r in prunes(t):
            rest = forest[:i] + forest[i + 1:] if r is None else \
                forest[:i] + (r,) + forest[i + 1:]
            if not wins(tuple(sorted(canon(x) for x in rest))):
                return True
    return False

def brute(k: int) -> int:
    children = fib_tree(k)
    count = 0
    for i, t in enumerate(children):
        for r in prunes(t):
            rest = [canon(children[j]) for j in range(len(children))
                    if j != i]
            if r is not None:
                rest.append(canon(r))
            if not wins(tuple(sorted(rest))):
                count += 1
    return count

if __name__ == "__main__":
    for kk in range(2, 8):
        assert fib_game_winning_moves(kk, MOD) == brute(kk), kk
    assert fib_game_winning_moves(5, MOD) == 1  # given
    assert fib_game_winning_moves(10, MOD) == 17  # given
    print(fib_game_winning_moves(10000, MOD))  # 438505383468410633
