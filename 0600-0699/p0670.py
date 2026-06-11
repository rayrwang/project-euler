"""Project Euler Problem 670: Colouring a Strip.

The rectangular sibling of Problem 671: tile a 2 x n strip with 1x1,
1x2, 1x3 tiles lying along either row plus the vertical 1x2 spanning
both rows of a column, in four colours, such that edge-adjacent tiles
differ and no interior point has the corners of four distinct tiles
(both rows changing tiles at a cut is illegal unless one of the two
adjacent columns is a vertical tile, which presents an edge rather than
a corner at mid-height).

Column-by-column transfer.  A state after a column records
(pa, pb, ca, cb, v): the remaining lengths (0..2) of the tiles covering
that column in each row, their colours -- when a tile has ended its
colour is kept as the predecessor for the next tile in that row -- and
whether the column was a vertical tile.  The top and bottom colours of
a column always differ except inside a vertical, so 112 states suffice
for k = 4.  Transitions: continuing tiles decrement; a row whose tile
ended starts a new horizontal coloured differently from its predecessor
and from the other row's current tile; when both rows need tiles, a
vertical (differing from both predecessors, or from the single vertical
predecessor) is always allowed, while two fresh horizontals are allowed
only following a vertical column.  The initial vector enumerates the
unconstrained first column; acceptance requires both tiles to end at
the right edge.  F(n) follows from one vector times T^(n-1) with fast
exponentiation mod 1000004321.

Verified: transfer equals an independent brute force (vertical masks,
arc compositions, four-corner test on cell owners, exact colour
counting) for n = 1..5, including the given F(2) = 120 and
F(5) = 45876, plus F(100) = 53275818 mod 1000004321.
"""

from functools import lru_cache
from itertools import product

MOD = 1_000_004_321
K = 4
N = 10**16


@lru_cache(maxsize=None)
def comps(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    out = []
    for p in (1, 2, 3):
        if p <= total:
            out.extend((p, *c) for c in comps(total - p))
    return tuple(out)


def row_fill_strip(n: int, vcols: list[int]):
    segs, prev = [], 0
    for c in vcols:
        segs.append((prev, c - prev))
        prev = c + 1
    segs.append((prev, n - prev))
    per = []
    for s, ln in segs:
        opts = []
        for comp in comps(ln):
            tiles, pos = [], s
            for p in comp:
                tiles.append((pos, p))
                pos += p
            opts.append(tiles)
        per.append(opts)
    return [
        [t for seg in combo for t in seg] for combo in product(*per)
    ]


def brute_f(n: int, k: int = K) -> int:
    total = 0
    for vmask in range(1 << n):
        vcols = [c for c in range(n) if vmask >> c & 1]
        fills = row_fill_strip(n, vcols)
        for tt in fills:
            for bb in fills:
                ot: dict[int, int] = {}
                ob: dict[int, int] = {}
                tid = 0
                for c in vcols:
                    ot[c] = ob[c] = tid
                    tid += 1
                for s, ln in tt:
                    for j in range(ln):
                        ot[s + j] = tid
                    tid += 1
                for s, ln in bb:
                    for j in range(ln):
                        ob[s + j] = tid
                    tid += 1
                if any(
                    len({ot[c - 1], ot[c], ob[c - 1], ob[c]}) == 4
                    for c in range(1, n)
                ):
                    continue
                adj = [set() for _ in range(tid)]
                for c in range(n):
                    if c + 1 < n:
                        for own in (ot, ob):
                            x, y = own[c], own[c + 1]
                            if x != y:
                                adj[x].add(y)
                                adj[y].add(x)
                    x, y = ot[c], ob[c]
                    if x != y:
                        adj[x].add(y)
                        adj[y].add(x)
                cnt = 0
                colors = [0] * tid

                def rec(i):
                    nonlocal cnt
                    if i == tid:
                        cnt += 1
                        return
                    for col in range(1, k + 1):
                        if all(colors[j] != col for j in adj[i]
                               if j < i):
                            colors[i] = col
                            rec(i + 1)
                    colors[i] = 0

                rec(0)
                total += cnt
    return total


def machine(k: int):
    st = []
    for pa, pb in product(range(3), repeat=2):
        for ca, cb in product(range(k), repeat=2):
            if ca != cb:
                st.append((pa, pb, ca, cb, 0))
    for c in range(k):
        st.append((0, 0, c, c, 1))
    idx = {s: i for i, s in enumerate(st)}
    mat = [[0] * len(st) for _ in st]
    for s in st:
        pa, pb, ca, cb, v = s
        row = mat[idx[s]]
        if pa > 0 and pb > 0:
            row[idx[(pa - 1, pb - 1, ca, cb, 0)]] += 1
        elif pa > 0:
            for ln in (1, 2, 3):
                for nc in range(k):
                    if nc not in (ca, cb):
                        row[idx[(pa - 1, ln - 1, ca, nc, 0)]] += 1
        elif pb > 0:
            for ln in (1, 2, 3):
                for nc in range(k):
                    if nc not in (ca, cb):
                        row[idx[(ln - 1, pb - 1, nc, cb, 0)]] += 1
        else:
            excl = {ca} if v else {ca, cb}
            for nc in range(k):
                if nc not in excl:
                    row[idx[(0, 0, nc, nc, 1)]] += 1
            if v:
                for la, lb in product((1, 2, 3), repeat=2):
                    for nca in range(k):
                        if nca == ca:
                            continue
                        for ncb in range(k):
                            if ncb not in (ca, nca):
                                row[idx[(la - 1, lb - 1, nca, ncb, 0)]] += 1
    return st, idx, mat


def transfer_f(n: int, k: int = K, mod: int = MOD) -> int:
    st, idx, base = machine(k)
    m = len(st)
    vec = [0] * m
    for c in range(k):
        vec[idx[(0, 0, c, c, 1)]] += 1
    for la, lb in product((1, 2, 3), repeat=2):
        for ca, cb in product(range(k), repeat=2):
            if ca != cb:
                vec[idx[(la - 1, lb - 1, ca, cb, 0)]] += 1

    def vmul(v, mat):
        out = [0] * m
        for i, a in enumerate(v):
            if a:
                ri = mat[i]
                for j in range(m):
                    if ri[j]:
                        out[j] = (out[j] + a * ri[j]) % mod
        return out

    def mmul(x, y):
        out = [[0] * m for _ in range(m)]
        for i in range(m):
            xi, oi = x[i], out[i]
            for t in range(m):
                a = xi[t]
                if a:
                    yt = y[t]
                    for j in range(m):
                        if yt[j]:
                            oi[j] = (oi[j] + a * yt[j]) % mod
        return out

    e = n - 1
    while e:
        if e & 1:
            vec = vmul(vec, base)
        e >>= 1
        if e:
            base = mmul(base, base)
    return sum(vec[idx[s]] for s in st if s[0] == 0 and s[1] == 0) % mod


if __name__ == "__main__":
    big = 10**15
    for n in range(1, 6):
        assert brute_f(n) == transfer_f(n, mod=big), n
    assert brute_f(2) == 120
    assert brute_f(5) == 45876
    assert transfer_f(100) == 53275818
    print(transfer_f(N))  # 551055065
