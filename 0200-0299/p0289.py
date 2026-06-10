"""Project Euler 289: Eulerian Cycles."""

# Each circle C(x, y) passes through the four corners of a unit square, so
# neighbouring circles cross at lattice points: a point on k squares lies on
# k circles and has 2k arc-ends. A non-crossing Eulerian cycle chooses, at
# every lattice point, a non-crossing perfect matching of its arc-ends in
# their true cyclic order (Catalan(k) options - the order, with the two
# tangent directions per circle split by curvature, is computed numerically
# by sampling each quarter-arc near its endpoints), such that the resulting
# closed curves form exactly one component. For a single cycle the loop
# closure is necessarily the very last connection made in any processing
# order (a curve closed early could never absorb later arcs), so a sweep
# may forbid closures everywhere except the final vertex.
#
# Sweeping circle-rows, the cut between rows is crossed only by the 2m side
# arcs (the tops of a row peak below the next cut), so the state is a
# non-crossing link pattern over at most ~14 dangling strands - a few
# hundred states. Each lattice vertex consumes a contiguous block of
# frontier strands (asserted) and emits new ones at geometrically correct
# staircase positions; local matchings update the pattern by path-following
# through pattern edges and local pairs. Verified against the given
# L(1,2) = 2, L(2,2) = 37, L(3,3) = 104290.

from math import atan2, pi, sqrt, cos, sin
from functools import lru_cache

R = sqrt(0.5)


def build(m, n):
    # arcs: (i, j, kind) kind in B,R,T,L; endpoints lattice
    aid = 0
    arc_ids = {}
    for i in range(m):
        for j in range(n):
            for kind in "BRTL":
                arc_ids[(i, j, kind)] = aid
                aid += 1
    # vertex incident ends: vertex (x,y) -> list of (angle, arc_id, which_end)
    incid = {}
    for x in range(m + 1):
        for y in range(n + 1):
            ends = []
            # squares adjacent: (x-1..x, y-1..y)
            for si in (x - 1, x):
                for sj in (y - 1, y):
                    if not (0 <= si < m and 0 <= sj < n):
                        continue
                    cx, cy = si + 0.5, sj + 0.5
                    # corner angles from center: which corner is (x,y)?
                    a0 = atan2(y - cy, x - cx)
                    # arcs incident at this corner: the two arcs adjacent to corner
                    # corners: BL(225d): arcs B,L ; BR(315): B,R ; TR(45): T,R ; TL(135): T,L
                    deg = (a0 * 180 / pi) % 360
                    if abs(deg - 225) < 1:
                        ks = "BL"
                    elif abs(deg - 315) < 1:
                        ks = "BR"
                    elif abs(deg - 45) < 1:
                        ks = "TR"
                    else:
                        ks = "TL"
                    for k in ks:
                        # sample slightly along the arc from this corner:
                        # arc k spans corner angles: B:225->315, R:315->45, T:45->135, L:135->225
                        spans = {
                            "B": (225, 315),
                            "R": (315, 45),
                            "T": (45, 135),
                            "L": (135, 225),
                        }
                        s0, s1 = spans[k]
                        # move from corner angle deg into the arc interior
                        d0 = (deg - s0) % 360
                        delta = 0.05  # degrees
                        if d0 < 1:
                            t = deg + delta  # at start, move ccw
                        else:
                            t = deg - delta  # at end, move cw
                        tr = t * pi / 180
                        px, py = cx + R * cos(tr), cy + R * sin(tr)
                        ang = atan2(py - y, px - x) % (2 * pi)
                        ends.append((ang, arc_ids[(si, sj, k)]))
            ends.sort()
            incid[(x, y)] = ends
    return arc_ids, incid


@lru_cache(maxsize=None)
def ncross_matchings(d2):
    # non-crossing perfect matchings of positions 0..d2-1 in cyclic (here linear-cyclic) order
    if d2 == 0:
        return [()]
    res = []
    # match position 0 with odd-distance partner
    for k in range(1, d2, 2):
        inner = ncross_matchings_lin(tuple(range(1, k)))
        outer = ncross_matchings_lin(tuple(range(k + 1, d2)))
        for a in inner:
            for b in outer:
                res.append(((0, k),) + a + b)
    return res


@lru_cache(maxsize=None)
def ncross_matchings_lin(positions):
    if not positions:
        return [()]
    p = positions[0]
    res = []
    for idx in range(1, len(positions), 2):
        q = positions[idx]
        inner = ncross_matchings_lin(positions[1:idx])
        outer = ncross_matchings_lin(positions[idx + 1 :])
        for a in inner:
            for b in outer:
                res.append(((p, q),) + a + b)
    return res


def L(m, n, mod=None):
    arc_ids, incid = build(m, n)
    # vertex order: by (y, x)
    order = [(x, y) for y in range(n + 1) for x in range(m + 1)]
    # frontier: list of (arc_id) strands in staircase order; state: (tuple frontier partner-pattern) -> count
    # pattern representation: tuple pairing: for frontier of size s, tuple t with t[i] = partner index
    # states dict: key (tuple of arc ids in frontier order? no - frontier contents are SAME for all states at a given step)
    # We maintain frontier list globally (deterministic), states = pattern tuples
    frontier = []  # arc end tokens: (arc_id, end_tag) — use arc_id since each arc dangles at most one end at a time? T arcs: left emitted then consumed... both ends distinct times ✓ arc_id unique in frontier
    states = {(): 1}
    total_vertices = len(order)
    answer = 0
    for vi, (x, y) in enumerate(order):
        ends = incid[(x, y)]
        if not ends:
            continue
        d2 = len(ends)
        # consumed = ends whose arc_id currently in frontier; produced = others
        consumed_pos = {}
        produced = []
        for ang, a in ends:
            if a in frontier:
                consumed_pos[a] = frontier.index(a)
            else:
                produced.append(a)
        cpos = sorted(consumed_pos.values())
        assert cpos == list(range(cpos[0], cpos[0] + len(cpos))) if cpos else True, (
            x,
            y,
            cpos,
        )
        base = cpos[0] if cpos else len(frontier)  # insertion point

        # determine produced order along staircase:
        # next-cut strands: L(x,y) at x-0.207 and R(x-1,y) at x+0.207  (side arcs of row y)
        # micro: T(x, y-1) left end (upper), B(x, y) left end (lower)
        def skey(a):
            # find (i, j, kind)
            for key, idv in arc_ids.items():
                if idv == a:
                    break
            i, j, kind = key
            if kind == "L" and j == y:
                return (0, i - 0.207)
            if kind == "R" and j == y:
                return (0, i + 1.207)
            if kind == "T" and j == y - 1:
                return (1, 0)
            if kind == "B" and j == y:
                return (1, 1)
            raise AssertionError((key, x, y))

        produced.sort(key=skey)
        is_last = (vi == total_vertices - 1) or all(
            len(incid[order[k]]) == 0 for k in range(vi + 1, total_vertices)
        )
        # local pairings: over cyclic positions 0..d2-1 (ends sorted by angle)
        end_arcs = [a for ang, a in ends]
        matchings = ncross_matchings(d2)
        new_states = {}
        for pat, cnt in states.items():
            # pat: tuple partner indices over current frontier
            for matching in matchings:
                # apply: build new pattern
                # work on a copy: map frontier indices; we'll construct connections
                # representation: partner array over frontier
                # produced ends each get a placeholder strand; track links via dict
                # use union through partner-chasing:
                # for each local pair (p, q): ends end_arcs[p], end_arcs[q]
                # consumed end -> frontier slot; produced end -> new slot id 'P k'
                slot_of = {}
                for ang_a in consumed_pos:
                    slot_of[ang_a] = consumed_pos[ang_a]
                # easier: simulate with a generic union of endpoints:
                # nodes: frontier slots (with existing partner info) and produced arcs
                # each local pair connects two nodes (slot or produced)
                # After applying all pairs: compute resulting matching among (un-consumed slots + produced)
                # Build connection graph: each consumed slot is an endpoint that internally connects to partner slot
                # Standard zipper algorithm:

                def node_of(idx):
                    a = end_arcs[idx]
                    if a in slot_of:
                        return ("f", slot_of[a])
                    return ("p", a)

                pairs = [(node_of(p), node_of(q)) for p, q in matching]
                # existing pattern: frontier slot i partners pat[i]
                # We compute the final pairing on nodes = remaining slots + produced
                # Use path-following: each local pair is an edge; each pattern pair is an edge between consumed/unconsumed slots
                # Each remaining endpoint (unconsumed slot or produced arc) has degree<=1 in combined graph; consumed slots have degree 2 (one pattern edge + one local edge)
                adj = {}

                def add_edge(u, v):
                    adj.setdefault(u, []).append(v)
                    adj.setdefault(v, []).append(u)

                for i_s in range(len(pat)):
                    if i_s < pat[i_s]:
                        add_edge(("f", i_s), ("f", pat[i_s]))
                for u, v in pairs:
                    add_edge(u, v)
                # terminals: unconsumed frontier slots + produced arcs: degree 1; consumed slots degree 2
                consumed_set = set(consumed_pos.values())
                terminals = [
                    ("f", i_s) for i_s in range(len(pat)) if i_s not in consumed_set
                ] + [("p", a) for a in produced]
                visited = set()
                final_pairs = []
                bad = False
                for t in terminals:
                    if t in visited:
                        continue
                    # walk
                    prev, cur = None, t
                    while True:
                        visited.add(cur)
                        # handle multigraph: count occurrences
                        # simpler: pick next not equal prev (allowing duplicates handled by removal)
                        nxt = None
                        cnt_prev = 0
                        for w in adj.get(cur, []):
                            if w == prev and cnt_prev == 0:
                                cnt_prev = 1
                                continue
                            nxt = w
                            break
                        if (
                            cur in [x2 for x2 in terminals]
                            and cur != t
                            and prev is not None
                        ):
                            final_pairs.append((t, cur))
                            break
                        if nxt is None:
                            bad = True
                            break
                        prev, cur = cur, nxt
                    if bad:
                        break
                if bad:
                    continue
                # closures: edges among consumed-only cycles: count nodes not visited that have edges
                allnodes = set(adj.keys())
                unvisited = [u for u in allnodes if u not in visited]
                closures = 0
                if unvisited:
                    # they form closed loops
                    closures = 1  # at least one loop closed (count loops)
                    # count properly:
                    uv = set(unvisited)
                    closures = 0
                    while uv:
                        s0 = uv.pop()
                        prev, cur = None, s0
                        while True:
                            nxt = None
                            cnt_prev = 0
                            for w in adj.get(cur, []):
                                if w == prev and cnt_prev == 0:
                                    cnt_prev = 1
                                    continue
                                nxt = w
                                break
                            prev, cur = cur, nxt
                            if cur == s0:
                                break
                            uv.discard(cur)
                        closures += 1
                if closures > 0:
                    # only allowed if final closure: last vertex, frontier empty after, single closure, no terminals left
                    if is_last and closures == 1 and not final_pairs and not terminals:
                        answer = answer + cnt
                    continue
                # build new frontier pattern: new frontier = old minus consumed block, with produced inserted at base
                # mapping old slot index -> new index
                newfront = [a for a in frontier if a not in consumed_pos]
                # insert produced at position base' = number of remaining slots before 'base'
                before = sum(1 for i_s in range(base) if i_s not in consumed_set)
                idx_map = {}
                k2 = 0
                for i_s in range(len(pat)):
                    if i_s in consumed_set:
                        continue
                    pos = k2 if k2 < before else k2 + len(produced)
                    idx_map[("f", i_s)] = pos
                    k2 += 1
                for t2, a in enumerate(produced):
                    idx_map[("p", a)] = before + t2
                size = k2 + len(produced)
                npat = [0] * size
                for u, v in final_pairs:
                    iu, iv = idx_map[u], idx_map[v]
                    npat[iu] = iv
                    npat[iv] = iu
                key = tuple(npat)
                new_states[key] = (new_states.get(key, 0) + cnt) % (mod or (1 << 62))
        # update frontier list
        consumed_set2 = set(consumed_pos.keys())
        newfront = []
        inserted = False
        for i_s, a in enumerate(frontier):
            if a in consumed_set2:
                if not inserted:
                    newfront.extend(produced)
                    inserted = True
                continue
            newfront.append(a)
        if not inserted:
            newfront.extend(produced)
        frontier = newfront
        states = new_states
    return answer


def solve(m: int = 6, n: int = 10, mod: int = 10**10) -> int:
    assert L(1, 2) == 2 and L(2, 2) == 37
    return L(m, n, mod=mod) % mod


if __name__ == "__main__":
    print(solve())  # 6567944538
