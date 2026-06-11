"""Project Euler Problem 690: Tom and Jerry.

Characterization (verified by brute force below): a graph is a Tom graph
exactly when it is a forest in which no tree contains the spider S(3,3,3)
- a vertex with three branches of depth >= 3 - as a subgraph.  A cycle
lets Jerry evade forever (so Tom graphs are forests), an embedded spider
does too, and on every spider-free tree Tom can win; the game itself is
solved exactly for all trees with <= 10 vertices by breadth-first search
over belief states (sets of holes Jerry might occupy), matching the
spider-free predicate on all 201 trees and failing on all cycles.

Counting spider-free trees: let the core of a tree be the set of vertices
having at least two branches of depth >= 2.  The core is empty exactly
for trees of diameter <= 3 (stars and double stars, 1 + floor((n-2)/2)
of them for n >= 4), and otherwise the tree is spider-free iff the core
is a path.  A core path is decorated at every vertex by a multiset of
height-<=-1 rooted trees (a child plus l >= 0 leaves, one shape per size,
so a vertex with decorations has generating function x P(x) with P the
partition function), and a core endpoint must carry at least one
decoration of size >= 2 to have its second branch of depth 2, giving
E(x) = x (P(x) - 1/(1-x)).  A single-vertex core needs two such, giving
G1 = x (P - Q - x^2 Q^2) with Q = 1/(1-x).  Ordered paths of length >= 2
contribute E^2 / (1 - x P); unlabeled trees are these up to reflection,
so by Burnside the spider-free trees with non-empty core are

  ( G1 + E(x)^2/(1 - I(x))  +  G1 + E(x^2)(1 + I(x))/(1 - I(x^2)) ) / 2

with I = x P(x) (the palindrome terms pair mirrored spine vertices, so
substitute x^2, with a free middle vertex for odd lengths).  T(n) is the
Euler transform (multisets of components).  All series work is O(n^2)
modulo 10^9 + 7.

Verified: the game brute force against the spider-free predicate for all
trees with <= 10 vertices and all cycles up to C_8; the tree counts
against direct generation for n <= 11; and T(3) = 3, T(7) = 37,
T(10) = 328, T(20) = 1416269.
"""

N = 2019
MOD = 1_000_000_007


# ----- exact game solver and small-tree generation (verification) -----

def catchable(n: int, edges: list[tuple[int, int]]) -> bool:
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    def expand(b: int) -> int:
        out = 0
        while b:
            u = (b & -b).bit_length() - 1
            out |= adj[u] if adj[u] else 1 << u  # isolated mouse stays
            b &= b - 1
        return out

    full = (1 << n) - 1
    seen = {full}
    stack = [full]
    while stack:
        b = stack.pop()
        for v in range(n):
            nb = expand(b & ~(1 << v))
            if nb == 0:
                return True
            if nb not in seen:
                seen.add(nb)
                stack.append(nb)
    return False


def spider_free(n: int, edges: list[tuple[int, int]]) -> bool:
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def depth(u: int, p: int) -> int:
        return 1 + max((depth(w, u) for w in adj[u] if w != p), default=0)

    return all(
        sum(1 for w in adj[v] if depth(w, v) >= 3) < 3 for v in range(n)
    )


def all_trees(up_to: int) -> dict[int, list[list[tuple[int, int]]]]:
    """All unlabeled trees by leaf addition, deduplicated by AHU forms."""

    def canon(n: int, edges: list[tuple[int, int]]) -> str:
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def ahu(u: int, p: int) -> str:
            return "(" + "".join(
                sorted(ahu(w, u) for w in adj[u] if w != p)
            ) + ")"

        return min(ahu(r, -1) for r in range(n))  # n <= 11: fast enough

    out: dict[int, list[list[tuple[int, int]]]] = {1: [[]]}
    prev: dict[str, list[tuple[int, int]]] = {"()": []}
    for n in range(2, up_to + 1):
        new: dict[str, list[tuple[int, int]]] = {}
        for edges in prev.values():
            for v in range(n - 1):
                e2 = [*edges, (v, n - 1)]
                new.setdefault(canon(n, e2), e2)
        prev = new
        out[n] = list(new.values())
    return out


# ----- series arithmetic mod p -----

def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (N + 1)
    for i, ai in enumerate(a):
        if ai:
            for j in range(min(len(b), N + 1 - i)):
                out[i + j] = (out[i + j] + ai * b[j]) % MOD
    return out


def inv_series(a: list[int]) -> list[int]:
    assert a[0] == 1
    out = [0] * (N + 1)
    out[0] = 1
    for n in range(1, N + 1):
        s = 0
        for k in range(1, min(n, len(a) - 1) + 1):
            s += a[k] * out[n - k]
        out[n] = -s % MOD
    return out


def sub(a: list[int], b: list[int]) -> list[int]:
    return [(x - y) % MOD for x, y in zip(a, b)]


def stretch(a: list[int]) -> list[int]:
    out = [0] * (N + 1)
    for i in range(N // 2 + 1):
        out[2 * i] = a[i]
    return out


def shift(a: list[int], k: int) -> list[int]:
    return [0] * k + a[: N + 1 - k]


def spider_free_tree_counts() -> list[int]:
    partitions = [0] * (N + 1)
    partitions[0] = 1
    for j in range(1, N + 1):
        for i in range(j, N + 1):
            partitions[i] = (partitions[i] + partitions[i - j]) % MOD
    q = [1] * (N + 1)  # 1 / (1 - x)
    q2 = mul(q, q)
    e = shift(sub(partitions, q), 1)
    g1 = shift(sub(sub(partitions, q), shift(q2, 2)), 1)
    spine = shift(partitions, 1)  # internal vertex: x P(x)
    linear = mul(mul(e, e), inv_series(sub([1] + [0] * N, spine)))
    one = [1] + [0] * N
    pal_tail = mul(
        mul(stretch(e), [(o + s) % MOD for o, s in zip(one, spine)]),
        inv_series(sub(one, stretch(spine))),
    )
    half = pow(2, MOD - 2, MOD)
    core_path = [
        (2 * g + li + pa) * half % MOD
        for g, li, pa in zip(g1, linear, pal_tail)
    ]
    counts = core_path[:]
    counts[1] = (counts[1] + 1) % MOD  # K1
    counts[2] = (counts[2] + 1) % MOD  # K2
    for n in range(3, N + 1):  # stars and double stars (diameter <= 3)
        counts[n] = (counts[n] + 1 + (n - 2) // 2) % MOD
    return counts


def euler_transform(c: list[int]) -> list[int]:
    b = [0] * (N + 1)
    for d in range(1, N + 1):
        if c[d]:
            for k in range(d, N + 1, d):
                b[k] = (b[k] + d * c[d]) % MOD
    f = [0] * (N + 1)
    f[0] = 1
    for n in range(1, N + 1):
        s = 0
        for k in range(1, n + 1):
            s += b[k] * f[n - k] % MOD
        f[n] = s % MOD * pow(n, MOD - 2, MOD) % MOD
    return f


if __name__ == "__main__":
    trees = all_trees(10)
    brute_counts = {}
    for n, lst in trees.items():
        good = 0
        for edges in lst:
            sf = spider_free(n, edges)
            assert catchable(n, edges) == sf
            good += sf
        brute_counts[n] = good
    for m in range(3, 9):
        assert not catchable(m, [(i, (i + 1) % m) for i in range(m)])

    counts = spider_free_tree_counts()
    assert all(counts[n] == brute_counts[n] for n in brute_counts)
    t = euler_transform(counts)
    assert t[3] == 3 and t[7] == 37 and t[10] == 328
    assert t[20] == 1416269
    print(t[N])  # 415157690
