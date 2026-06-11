"""Project Euler Problem 979: Hyperbolic Frog.

The hyperbolic plane is tiled by heptagons, three meeting at every vertex
(the {7,3} tiling).  A frog starts on one heptagon and at each step jumps
to one of the seven adjacent tiles.  ``F(n)`` counts the paths that return
to the starting tile after ``n`` steps; ``F(4) = 119``.  Find ``F(20)``.

The adjacency graph of the heptagons is the vertex graph of the dual
{3,7} tiling: 7-regular, vertex-transitive, and planar-hyperbolic.  It can
be built exactly in concentric layers around the root.  Layer 1 is a
7-cycle of the root's neighbours.  Thereafter every layer is a cycle, and
a layer vertex with ``p`` parents in the previous layer (``p`` is 1 or 2)
has ``5 - p`` child edges, because its degree decomposes as two cycle
neighbours + ``p`` parents + children.  Consecutive parents share one
child (the apex of the triangle over their common cycle edge), so shared
children have ``p = 2`` and the interior ones ``p = 1``.  This is the
standard combinatorial growth of {3,q} triangulations; every completed
vertex ends with degree exactly 7, which the construction asserts.

A closed walk of length 20 never leaves the ball of radius 10 (a vertex of
layer 11 would need at least 22 steps to visit and return), so building 11
layers (about 2 * 10^5 vertices, layer growth ratio (3 + sqrt 5)/2)
suffices.  ``F(20)`` is then the root entry of ``A^20 e_root``, computed
with twenty sparse matrix-vector products in exact integer arithmetic.
The graph reproduces ``F(2) = 7`` (degree), ``F(3) = 14`` (the root lies
in seven triangles, each giving two oriented closed walks) and the given
``F(4) = 119``.
"""

from __future__ import annotations


def build_37_graph(layers: int) -> list[list[int]]:
    """Adjacency lists of the {3,7} tiling graph out to the given layer."""
    adj: list[list[int]] = [[]]

    def add_edge(u: int, v: int) -> None:
        adj[u].append(v)
        adj[v].append(u)

    def new_vertex() -> int:
        adj.append([])
        return len(adj) - 1

    root = 0
    cur = [new_vertex() for _ in range(7)]
    for v in cur:
        add_edge(root, v)
    for i in range(7):
        add_edge(cur[i], cur[(i + 1) % 7])
    parents = dict.fromkeys(cur, 1)

    for _ in range(layers - 1):
        nxt: list[int] = []
        shared_first = -1
        prev_last = -1
        for idx, v in enumerate(cur):
            c = 5 - parents[v]
            if idx == 0:
                s = new_vertex()
                parents[s] = 2
                shared_first = s
                nxt.append(s)
                add_edge(v, s)
            else:
                add_edge(v, prev_last)
            for _ in range(c - 2):
                m = new_vertex()
                parents[m] = 1
                nxt.append(m)
                add_edge(v, m)
            if idx < len(cur) - 1:
                t = new_vertex()
                parents[t] = 2
                nxt.append(t)
                add_edge(v, t)
                prev_last = t
            else:
                add_edge(v, shared_first)
        for i in range(len(nxt)):
            add_edge(nxt[i], nxt[(i + 1) % len(nxt)])
        # all vertices of the now-interior layer must have degree exactly 7
        for v in cur:
            assert len(adj[v]) == 7, "degree invariant"
        cur = nxt
    return adj


def closed_walks(adj: list[list[int]], n: int) -> int:
    """Number of closed walks of length n from vertex 0."""
    cnt = [0] * len(adj)
    cnt[0] = 1
    for _ in range(n):
        nc = [0] * len(adj)
        for u, c in enumerate(cnt):
            if c:
                for w in adj[u]:
                    nc[w] += c
        cnt = nc
    return cnt[0]


if __name__ == "__main__":
    adj = build_37_graph(11)
    assert closed_walks(adj, 2) == 7, "F(2) = degree"
    assert closed_walks(adj, 3) == 14, "F(3) = two walks per incident triangle"
    assert closed_walks(adj, 4) == 119, "given checkpoint F(4)"
    print(closed_walks(adj, 20))  # 189306828278449
