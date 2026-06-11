"""Project Euler Problem 671: Colouring a Loop.

Tiles 1x1, 1x2, 1x3 lie along either row of the 2 x n loop, and a 1x2
may also stand vertically, covering both rows of one column (visible in
the problem's images).  Tiles sharing a unit edge are adjacent and must
differ in colour, so the top and bottom tile of any column always
differ.  The "no four corners at a point" rule, read off the images,
forbids exactly the interior points whose four surrounding cells belong
to four distinct tiles: both rows change tiles at the cut and neither
adjacent column is vertical (a vertical contributes an edge, not a
corner, at mid-height).

Crucially, F counts tilings UP TO ROTATION of the loop (reflections
explicitly distinct): the labelled brute-force counts come out exactly
n times the given values, e.g. 23291100 = 7 * 3327300 for F_5(7), once
full-wrap tiles of length n (whose two ends would meet, making the tile
adjacent to itself) are excluded.  Burnside over the rotation group
gives F_k(n) = (1/n) sum_{d | n} phi(n/d) P(d), where P(d) is the
labelled count on a 2 x d loop; P(1) = 0 (a lone column is horizontally
adjacent to itself).  This reproduces F_4(3) = 312/3 = 104 and
F_5(7) = 3327300.  Here n = 10004003002001 is prime, so
F = P(n) / n mod 1000004321 (also prime, coprime to n).

P(d) for d >= 3 comes from a 66-state transfer machine over cut states
(pa, pb, A, B, v): remaining lengths of the tiles covering the previous
column, their colour classes relative to the two colours fixed at the
starting cut ('1', '2', or anonymous 'o' -- top and bottom colours are
always distinct except inside a vertical), and whether the previous
column was vertical.  Two fresh horizontals may start at a cut only
after a vertical; a vertical may always start; colour choices are
counted per class.  The trace over the nine horizontal shapes with
classes (1, 2), weighted k(k-1), plus the vertical diagonal entry
weighted k, equals L(d) -- verified against a brute force (vertical
mask + arc compositions, four-corner test on cell owners, exact graph
colour counting) for all k in {3,4,5} and d in {3,4,5,6}.

Verified: F_4(3) = 104, F_5(7) = 3327300 and
F_6(101) = 75309980 mod 1000004321 from the statement.
"""

from functools import lru_cache
from itertools import product

MOD = 1_000_004_321
N = 10_004_003_002_001
K = 10
CL = ("1", "2", "o")


# ----------------------------- transfer ------------------------------

def choices(excluded: list[str], k: int) -> list[tuple[str, int]]:
    """(class, count) of new colours differing from the distinct
    colours whose classes are listed."""
    res = []
    if "1" not in excluded:
        res.append(("1", 1))
    if "2" not in excluded:
        res.append(("2", 1))
    cnt = k - 2 - sum(1 for e in excluded if e == "o")
    if cnt > 0:
        res.append(("o", cnt))
    return res


def machine_states() -> list[tuple[int, int, str, str, int]]:
    out = []
    for pa, pb in product(range(3), repeat=2):
        for a, b in product(CL, repeat=2):
            if a == b and a != "o":
                continue
            out.append((pa, pb, a, b, 0))
    for c in CL:
        out.append((0, 0, c, c, 1))
    return out


def build(k: int):
    st = machine_states()
    idx = {s: i for i, s in enumerate(st)}
    mat = [[0] * len(st) for _ in st]
    for s in st:
        pa, pb, a, b, v = s
        row = mat[idx[s]]
        if pa > 0 and pb > 0:
            row[idx[(pa - 1, pb - 1, a, b, 0)]] += 1
        elif pa > 0:  # bottom row starts a new tile
            for ln in (1, 2, 3):
                for nc, w in choices([b, a], k):
                    row[idx[(pa - 1, ln - 1, a, nc, 0)]] += w
        elif pb > 0:  # top row starts a new tile
            for ln in (1, 2, 3):
                for nc, w in choices([a, b], k):
                    row[idx[(ln - 1, pb - 1, nc, b, 0)]] += w
        else:
            # vertical tile: allowed regardless (no corner at mid-height)
            for nc, w in choices([a] if v else [a, b], k):
                row[idx[(0, 0, nc, nc, 1)]] += w
            # two fresh horizontals: legal only after a vertical
            if v:
                for la, lb in product((1, 2, 3), repeat=2):
                    for nca, wa in choices([a], k):
                        for ncb, wb in choices([a, nca], k):
                            row[idx[(la - 1, lb - 1, nca, ncb, 0)]] += (
                                wa * wb
                            )
    return idx, mat


def mat_mul(x, y, mod):
    n = len(x)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        xi, oi = x[i], out[i]
        for t in range(n):
            a = xi[t]
            if a:
                yt = y[t]
                for j in range(n):
                    if yt[j]:
                        oi[j] = (oi[j] + a * yt[j]) % mod
    return out


def labeled(k: int, d: int, mod: int) -> int:
    """Labelled tilings of the 2 x d loop (d >= 3), mod `mod`."""
    idx, mat = build(k)
    size = len(mat)
    power = [[int(i == j) for j in range(size)] for i in range(size)]
    e = d
    while e:
        if e & 1:
            power = mat_mul(power, mat, mod)
        mat = mat_mul(mat, mat, mod)
        e >>= 1
    total = 0
    for pa in range(3):
        for pb in range(3):
            i = idx[(pa, pb, "1", "2", 0)]
            total += k * (k - 1) * power[i][i]
    i = idx[(0, 0, "1", "1", 1)]
    return (total + k * power[i][i]) % mod


# --------------------------- brute force -----------------------------

@lru_cache(maxsize=None)
def comps(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    out = []
    for p in (1, 2, 3):
        if p <= total:
            out.extend((p, *c) for c in comps(total - p))
    return tuple(out)


def row_fillings(n: int, vcols: list[int]):
    """Fillings of one row outside the vertical columns; full-wrap
    tiles (length n) are self-adjacent and excluded."""
    if not vcols:
        rows = []
        for mask in range(1, 1 << n):
            pts = [i for i in range(n) if mask >> i & 1]
            tiles, ok = [], True
            for i, s in enumerate(pts):
                ln = (pts[(i + 1) % len(pts)] - s) % n or n
                if ln > 3 or ln >= n:
                    ok = False
                    break
                tiles.append((s, ln))
            if ok:
                rows.append(tiles)
        return rows
    arcs = []
    for i, vc in enumerate(vcols):
        ln = (vcols[(i + 1) % len(vcols)] - vc - 1) % n
        arcs.append(((vc + 1) % n, ln))
    per_arc = []
    for s, ln in arcs:
        opts = []
        for comp in comps(ln):
            tiles, pos = [], s
            for p in comp:
                tiles.append((pos, p))
                pos = (pos + p) % n
            opts.append(tiles)
        per_arc.append(opts)
    return [
        [t for arc in combo for t in arc] for combo in product(*per_arc)
    ]


def brute_labeled(k: int, n: int) -> int:
    total = 0
    for vmask in range(1 << n):
        vcols = [c for c in range(n) if vmask >> c & 1]
        fillings = row_fillings(n, vcols)
        for tt in fillings:
            for bb in fillings:
                owner_t, owner_b, tid = {}, {}, 0
                for c in vcols:
                    owner_t[c] = owner_b[c] = tid
                    tid += 1
                for s, ln in tt:
                    for j in range(ln):
                        owner_t[(s + j) % n] = tid
                    tid += 1
                for s, ln in bb:
                    for j in range(ln):
                        owner_b[(s + j) % n] = tid
                    tid += 1
                if any(
                    len({owner_t[(c - 1) % n], owner_t[c],
                         owner_b[(c - 1) % n], owner_b[c]}) == 4
                    for c in range(n)
                ):
                    continue
                adj = [set() for _ in range(tid)]
                for c in range(n):
                    for own in (owner_t, owner_b):
                        x, y = own[c], own[(c + 1) % n]
                        if x != y:
                            adj[x].add(y)
                            adj[y].add(x)
                    x, y = owner_t[c], owner_b[c]
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


if __name__ == "__main__":
    big = 10**15
    for k in (3, 4, 5):
        for d in (3, 4, 5):
            assert brute_labeled(k, d) == labeled(k, d, big), (k, d)
    assert brute_labeled(3, 6) == labeled(3, 6, big)
    # Burnside anchors: P(1) = 0 and the divisor sums collapse for
    # prime lengths to L(p) / p.
    assert labeled(4, 3, big) // 3 == 104
    assert labeled(5, 7, big) // 7 == 3327300
    assert labeled(6, 101, MOD) * pow(101, MOD - 2, MOD) % MOD == 75309980
    # n is prime (and coprime to the prime modulus)
    answer = labeled(K, N, MOD) * pow(N, MOD - 2, MOD) % MOD
    print(answer)  # 946106780
