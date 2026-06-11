"""Project Euler 846: Magic Bracelets.

Beads display 1, 2, p^k or 2p^k (p an odd prime); adjacent beads must
multiply to x^2 + 1, and a bracelet is a simple cycle of length >= 3
of distinct numbers, counted up to rotation and reflection.

Since x^2 + 1 has all odd prime factors congruent to 1 mod 4 and at
most a single factor of two, and since a product of two beads contains
at most two distinct odd primes, every edge of the compatibility graph
arises from some x < N whose x^2 + 1 is N-smooth with at most two odd
primes.  Factoring x^2 + 1 for all x by sieving with the square roots
of -1 modulo each prime p = 1 mod 4 (a leftover cofactor is a single
prime > N, which can never fit inside a bead <= N) yields the full
edge list directly from the at most handful of bead-shaped divisor
splits per x.

The answer sums, over all simple cycles, the cycle's vertex sum.
Cycles survive in the 2-core and live inside biconnected blocks, which
turn out to be tiny (at most 43 vertices); blocks that are bare edges
contribute nothing, blocks that are bare cycles contribute their
vertex sum once, and the few truly tangled blocks are enumerated by a
rooted depth-first search that fixes the minimum vertex as root and
orients each cycle by requiring the first neighbour to be smaller than
the last, so every bracelet is counted exactly once.  About 1.4
million bracelets exist below 10^6; the code verifies the given
F(20) = 258 and F(10^2) = 538768.
"""

from __future__ import annotations

import itertools
import sys
from collections import defaultdict, deque

import numpy as np


def bead_set(n: int, odd_primes: list[int]) -> set[int]:
    beads = {1, 2}
    for p in odd_primes:
        q = p
        while q <= n:
            beads.add(q)
            if 2 * q <= n:
                beads.add(2 * q)
            q *= p
    return beads


def root_minus_one(p: int) -> int:
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            return pow(a, (p - 1) // 4, p)
    raise AssertionError


def build_edges(n: int) -> set[tuple[int, int]]:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = [int(p) for p in np.nonzero(sieve)[0]]
    beads = bead_set(n, primes[1:])

    x = np.arange(n, dtype=np.int64)
    rem = x * x + 1
    rem[1::2] >>= 1
    factors: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for p in primes:
        if p % 4 != 1:
            continue
        r = root_minus_one(p)
        for s in (r, p - r):
            for xx in range(s, n, p):
                e = 0
                while rem[xx] % p == 0:
                    rem[xx] //= p
                    e += 1
                if e:
                    factors[xx].append((p, e))

    edges: set[tuple[int, int]] = set()

    def add(u: int, v: int) -> None:
        if u != v and u <= n and v <= n and u in beads and v in beads:
            edges.add((min(u, v), max(u, v)))

    for xx in range(1, n):
        if rem[xx] != 1:
            continue  # prime factor above n: cannot fit in any bead
        f = factors[xx]
        two = 2 if xx % 2 == 1 else 1
        if not f:
            add(1, 2)  # x = 1
        elif len(f) == 1:
            p, a = f[0]
            add(1, two * p**a)
            if two == 2:
                add(2, p**a)
            for j in range(1, a):
                add(p**j, two * p ** (a - j))
                if two == 2:
                    add(2 * p**j, p ** (a - j))
        elif len(f) == 2:
            (p, a), (q, b) = f
            if two == 1:
                add(p**a, q**b)
            else:
                add(p**a, 2 * q**b)
                add(2 * p**a, q**b)
    return edges


def biconnected_blocks(adj: dict[int, list[int]]) -> list[list[tuple[int, int]]]:
    disc: dict[int, int] = {}
    low: dict[int, int] = {}
    stack: list[tuple[int, int]] = []
    counter = itertools.count()
    blocks: list[list[tuple[int, int]]] = []
    for s in adj:
        if s in disc:
            continue
        st: list = [(s, None, iter(adj[s]))]
        disc[s] = low[s] = next(counter)
        while st:
            v, parent, it = st[-1]
            advanced = False
            for w in it:
                if w == parent:
                    continue
                if w not in disc:
                    disc[w] = low[w] = next(counter)
                    stack.append((v, w))
                    st.append((w, v, iter(adj[w])))
                    advanced = True
                    break
                if disc[w] < disc[v]:
                    stack.append((v, w))
                    low[v] = min(low[v], disc[w])
            if advanced:
                continue
            st.pop()
            if st:
                u = st[-1][0]
                low[u] = min(low[u], low[v])
                if low[v] >= disc[u]:
                    blk = []
                    while stack:
                        e = stack.pop()
                        blk.append(e)
                        if e == (u, v):
                            break
                    blocks.append(blk)
    return blocks


def cycles_in_block(edges_blk: list[tuple[int, int]]) -> int:
    """Sum of vertex sums over all simple cycles of length >= 3."""
    adj: dict[int, list[int]] = defaultdict(list)
    vs: set[int] = set()
    for a, b in edges_blk:
        adj[a].append(b)
        adj[b].append(a)
        vs.add(a)
        vs.add(b)
    if len(edges_blk) == 1:
        return 0
    if len(edges_blk) == len(vs):
        return sum(vs)
    total = 0
    onpath: set[int] = set()

    def dfs(v: int, root: int, first: int, psum: int, depth: int) -> None:
        nonlocal total
        for w in adj[v]:
            if w == root:
                if depth >= 3 and first < v:
                    total += psum
                continue
            if w < root or w in onpath:
                continue
            onpath.add(w)
            dfs(w, root, first, psum + w, depth + 1)
            onpath.discard(w)

    for root in sorted(vs):
        onpath = {root}
        for w in adj[root]:
            if w > root:
                onpath.add(w)
                dfs(w, root, w, root + w, 2)
                onpath.discard(w)
    return total


def total_potency(n: int) -> int:
    edges = build_edges(n)
    adj: dict[int, set[int]] = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    queue = deque(v for v in adj if len(adj[v]) <= 1)
    while queue:
        v = queue.popleft()
        if v not in adj:
            continue
        for w in list(adj[v]):
            adj[w].discard(v)
            if len(adj[w]) == 1:
                queue.append(w)
        del adj[v]
    core = {v: sorted(ws) for v, ws in adj.items() if ws}
    return sum(cycles_in_block(blk) for blk in biconnected_blocks(core))


def main() -> None:
    sys.setrecursionlimit(100000)
    assert total_potency(20) == 258
    assert total_potency(100) == 538768
    print(total_potency(10**6))  # 9851175623


if __name__ == "__main__":
    main()
