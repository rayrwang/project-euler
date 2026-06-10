"""Project Euler 275: Balanced Sculptures."""

# A balanced sculpture is a polyomino of n blocks in y >= 1 plus the plinth
# at the origin; connectivity forces (0, 1) to be a block, the blocks'
# torque sum x must vanish, and mirror images coincide. The answer is
# (A + S) / 2 with A the count taking reflections as distinct and S the
# symmetric count. Connectivity also bounds the lateral reach: cells out to
# column X need a cell in every column 1..X (torque >= X(X+1)/2), which the
# remaining cells on the left can no longer cancel beyond X = 8 for n = 18.
#
# A is computed by a broken-profile transfer-matrix DP over columns
# x = -R..R and rows 1..n: the boundary state is the connectivity partition
# of the profile (canonically relabelled, 4 bits per row), plus the number
# of cells used. The torque dimension is not part of the hash key - each
# (profile, cells) entry stores a vector over the feasible torque window
# [max(-rem R, -cells R), min(-rem x, 0 if x <= 0)] (rem = n - cells), so
# transitions are vector adds instead of per-torque hashing. States are
# killed when a boundary component vanishes prematurely (the polyomino
# would disconnect; if the last component vanishes with all n cells and
# torque 0 it is tallied), when components can no longer merge - future
# cells must at least fill a minimum spanning tree of the row gaps between
# boundary components (connected sets span row intervals) - or when the
# torque window empties. The cell (0, 1) is forced. S uses the same DP on
# the half board x >= 0 with cells at x > 0 counted twice, since a
# symmetric sculpture is connected iff its right half is.
#
# Verified against direct Redelmeier enumeration for orders 6 (A = 27,
# S = 9, 18 sculptures) and 10 (A = 1825, S = 103, 964), and against the
# stated 360505 at order 15 (A = 718474, S = 2536). Order 18:
# A = 30044041, S = 17087. Runtime is dominated by the order-18 A pass
# (about seven minutes; peak around 1.1e8 window elements).

import numba
import numpy as np
from numba.typed import Dict

KEY = numba.types.UniTuple(numba.types.int64, 2)


@numba.njit(cache=True)
def _canon_key(work, h, cells):
    mapping = np.zeros(16, dtype=np.int64)
    nxt = 1
    k1 = np.int64(0)
    k2 = np.int64(0)
    ncomp = 0
    gaps = 0
    last_occ = -1
    for i in range(h):
        v = work[i]
        c = 0
        if v != 0:
            if mapping[v] == 0:
                mapping[v] = nxt
                nxt += 1
                ncomp += 1
            c = mapping[v]
            if last_occ >= 0 and i - last_occ > 1 and work[last_occ] != v:
                gaps += i - last_occ - 1
            last_occ = i
        if i < 16:
            k1 |= c << (4 * i)
        else:
            k2 |= c << (4 * (i - 16))
    k2 |= cells << 8
    # MST lower bound on future cells: edges between consecutive occupied
    # slots with different (canonical) labels, weight = gap size; Kruskal on
    # the line metric. future >= max(MST, ncomp - 1).
    if ncomp <= 1:
        return (k1, k2), 0 if ncomp == 0 else ncomp - 1
    ew = np.empty(h, dtype=np.int64)
    ea = np.empty(h, dtype=np.int64)
    eb = np.empty(h, dtype=np.int64)
    ne = 0
    last_occ = -1
    for i in range(h):
        if work[i] != 0:
            if last_occ >= 0 and work[last_occ] != work[i]:
                ew[ne] = i - last_occ - 1
                ea[ne] = mapping[work[last_occ]]
                eb[ne] = mapping[work[i]]
                ne += 1
            last_occ = i
    # insertion sort edges by weight
    for a in range(1, ne):
        w0, a0, b0 = ew[a], ea[a], eb[a]
        b = a - 1
        while b >= 0 and ew[b] > w0:
            ew[b + 1] = ew[b]
            ea[b + 1] = ea[b]
            eb[b + 1] = eb[b]
            b -= 1
        ew[b + 1] = w0
        ea[b + 1] = a0
        eb[b + 1] = b0
    parent = np.arange(16, dtype=np.int64)
    mst = 0
    joined = 0
    for a in range(ne):
        ra = ea[a]
        while parent[ra] != ra:
            ra = parent[ra]
        rb = eb[a]
        while parent[rb] != rb:
            rb = parent[rb]
        if ra != rb:
            parent[ra] = rb
            mst += ew[a]
            joined += 1
            if joined == ncomp - 1:
                break
    need = mst if mst > ncomp - 1 else ncomp - 1
    return (k1, k2), need


@numba.njit(cache=True)
def _unpack_key(key, work, h):
    k1, k2 = key
    for i in range(h):
        if i < 16:
            work[i] = (k1 >> (4 * i)) & 15
        else:
            work[i] = (k2 >> (4 * (i - 16))) & 15
    return (k2 >> 8) & 255


@numba.njit(cache=True)
def _run_A(n, R, bufcap, rowcap):
    h = n
    bufA = np.zeros(bufcap, dtype=np.int64)
    bufB = np.zeros(bufcap, dtype=np.int64)
    offsA = np.zeros(rowcap, dtype=np.int64)
    offsB = np.zeros(rowcap, dtype=np.int64)
    losA = np.zeros(rowcap, dtype=np.int64)
    losB = np.zeros(rowcap, dtype=np.int64)
    widsA = np.zeros(rowcap, dtype=np.int64)
    widsB = np.zeros(rowcap, dtype=np.int64)
    keys = Dict.empty(KEY, numba.types.int64)
    work = np.zeros(h, dtype=np.int64)
    work2 = np.zeros(h, dtype=np.int64)
    use_a = True
    # initial: empty profile, cells 0, torque 0 stored within full window at x=-R
    lo0 = -n * R
    hi0 = n * R
    k0, _ = _canon_key(work, h, 0)
    keys[k0] = 0
    offsA[0] = 0
    losA[0] = lo0
    widsA[0] = hi0 - lo0 + 1
    for t in range(hi0 - lo0 + 1):
        bufA[t] = 0
    bufA[0 - lo0] = 1
    total = 0
    peak_elems = 0
    peak_rows = 0
    for x in range(-R, R + 2):
        for yi in range(h):
            force_cell = x == 0 and yi == 0
            if use_a:
                buf, offs, los, wids = bufA, offsA, losA, widsA
                nbuf, noffs, nlos, nwids = bufB, offsB, losB, widsB
            else:
                buf, offs, los, wids = bufB, offsB, losB, widsB
                nbuf, noffs, nlos, nwids = bufA, offsA, losA, widsA
            nkeys = Dict.empty(KEY, numba.types.int64)
            nn = 0
            nused = 0
            for key in keys:
                row = keys[key]
                cells = _unpack_key(key, work, h)
                o, lo, wd = offs[row], los[row], wids[row]
                rem = n - cells
                # feasible (can still reach 0) intersect achieved bounds
                flo = max(-rem * R, -cells * R)
                fhi = -rem * x
                if x <= 0 and fhi > 0:
                    fhi = 0
                left = work[yi]
                below = work[yi - 1] if yi > 0 else 0
                # SKIP
                if not force_cell:
                    old = work[yi]
                    work[yi] = 0
                    if old != 0:
                        present = False
                        for i in range(h):
                            if work[i] == old:
                                present = True
                                break
                        if not present:
                            others = False
                            for i in range(h):
                                if work[i] != 0:
                                    others = True
                                    break
                            if cells == n and not others:
                                if lo <= 0 < lo + wd:
                                    total += buf[o - lo]
                        else:
                            if fhi >= flo:
                                k, nc = _canon_key(work, h, cells)
                                if nc <= rem:
                                    a = max(lo, flo)
                                    b = min(lo + wd - 1, fhi)
                                    if a <= b:
                                        if k in nkeys:
                                            r2 = nkeys[k]
                                        else:
                                            if nused + (fhi - flo + 1) > len(
                                                nbuf
                                            ) or nn + 1 > len(noffs):
                                                return -1, nused, nn
                                            r2 = nn
                                            nkeys[k] = nn
                                            noffs[nn] = nused
                                            nlos[nn] = flo
                                            nwids[nn] = fhi - flo + 1
                                            for t in range(fhi - flo + 1):
                                                nbuf[nused + t] = 0
                                            nused += fhi - flo + 1
                                            nn += 1
                                        o2 = noffs[r2]
                                        l2 = nlos[r2]
                                        for t in range(a, b + 1):
                                            nbuf[o2 + t - l2] += buf[o + t - lo]
                    else:
                        if fhi >= flo:
                            k, nc = _canon_key(work, h, cells)
                            a = max(lo, flo)
                            b = min(lo + wd - 1, fhi)
                            if a <= b:
                                if k in nkeys:
                                    r2 = nkeys[k]
                                else:
                                    if nused + (fhi - flo + 1) > len(
                                        nbuf
                                    ) or nn + 1 > len(noffs):
                                        return -1, nused, nn
                                    r2 = nn
                                    nkeys[k] = nn
                                    noffs[nn] = nused
                                    nlos[nn] = flo
                                    nwids[nn] = fhi - flo + 1
                                    for t in range(fhi - flo + 1):
                                        nbuf[nused + t] = 0
                                    nused += fhi - flo + 1
                                    nn += 1
                                o2 = noffs[r2]
                                l2 = nlos[r2]
                                for t in range(a, b + 1):
                                    nbuf[o2 + t - l2] += buf[o + t - lo]
                    work[yi] = old
                # PLACE
                if cells < n and x <= R:
                    rem2 = n - cells - 1
                    flo2 = max(-rem2 * R, -(cells + 1) * R)
                    fhi2 = -rem2 * x
                    if x <= 0 and fhi2 > 0:
                        fhi2 = 0
                    if fhi2 >= flo2:
                        for i in range(h):
                            work2[i] = work[i]
                        if left != 0 and below != 0 and left != below:
                            m = left if left < below else below
                            big = left if left > below else below
                            for i in range(h):
                                if work2[i] == big:
                                    work2[i] = m
                            work2[yi] = m
                        elif left != 0 or below != 0:
                            work2[yi] = left if left != 0 else below
                        else:
                            mx = 0
                            for i in range(h):
                                if work2[i] > mx:
                                    mx = work2[i]
                            work2[yi] = mx + 1
                        k, nc = _canon_key(work2, h, cells + 1)
                        if nc <= rem2:
                            a = max(lo + x, flo2)
                            b = min(lo + wd - 1 + x, fhi2)
                            if a <= b:
                                if k in nkeys:
                                    r2 = nkeys[k]
                                else:
                                    if nused + (fhi2 - flo2 + 1) > len(
                                        nbuf
                                    ) or nn + 1 > len(noffs):
                                        return -1, nused, nn
                                    r2 = nn
                                    nkeys[k] = nn
                                    noffs[nn] = nused
                                    nlos[nn] = flo2
                                    nwids[nn] = fhi2 - flo2 + 1
                                    for t in range(fhi2 - flo2 + 1):
                                        nbuf[nused + t] = 0
                                    nused += fhi2 - flo2 + 1
                                    nn += 1
                                o2 = noffs[r2]
                                l2 = nlos[r2]
                                for t in range(a, b + 1):
                                    nbuf[o2 + t - l2] += buf[o + t - x - lo]
            keys = nkeys
            use_a = not use_a
            if nused > peak_elems:
                peak_elems = nused
            if nn > peak_rows:
                peak_rows = nn
    return total, peak_elems, peak_rows


@numba.njit(cache=True)
def _sym_pack(work, h, cells, tor, started, placed_col):
    mapping = np.zeros(16, dtype=np.int64)
    nxt = 1
    k1 = np.int64(0)
    k2 = np.int64(0)
    for i in range(h):
        v = work[i]
        c = 0
        if v != 0:
            if mapping[v] == 0:
                mapping[v] = nxt
                nxt += 1
            c = mapping[v]
        if i < 16:
            k1 |= c << (4 * i)
        else:
            k2 |= c << (4 * (i - 16))
    k2 |= cells << 8
    k2 |= (tor + 512) << 16
    k2 |= started << 27
    k2 |= placed_col << 28
    return (k1, k2)


@numba.njit(cache=True)
def _sym_unpack(key, work, h):
    k1, k2 = key
    for i in range(h):
        if i < 16:
            work[i] = (k1 >> (4 * i)) & 15
        else:
            work[i] = (k2 >> (4 * (i - 16))) & 15
    cells = (k2 >> 8) & 255
    tor = ((k2 >> 16) & 2047) - 512
    started = (k2 >> 27) & 1
    placed_col = (k2 >> 28) & 1
    return cells, tor, started, placed_col


@numba.njit(cache=True)
def _run_sym(n, R, sym):
    # sym=0: count A over x in [-R, R] with torque == 0, cell (0, row0) forced.
    # sym=1: count S over x in [0, R], weights 2 for x > 0, no torque.
    h = n
    states = Dict.empty(KEY, numba.types.int64)
    work = np.zeros(h, dtype=np.int64)
    states[_sym_pack(work, h, 0, 0, 0, 0)] = 1
    total = 0
    x0 = 0 if sym == 1 else -R
    maxstates = 0
    for x in range(x0, R + 2):
        wgt = 1
        if sym == 1 and x > 0:
            wgt = 2
        # column-start: torque feasibility prune (A only), reset placed_col
        pruned = Dict.empty(KEY, numba.types.int64)
        for key in states:
            cells, tor, started, _pc = _sym_unpack(key, work, h)
            if sym == 0:
                rem = n - cells
                if tor + rem * x > 0 or tor + rem * R < 0:
                    continue
            k = _sym_pack(work, h, cells, tor, started, 0)
            if k in pruned:
                pruned[k] += states[key]
            else:
                pruned[k] = states[key]
        states = pruned
        for yi in range(h):
            new = Dict.empty(KEY, numba.types.int64)
            force_cell = x == 0 and yi == 0
            for key in states:
                w = states[key]
                cells, tor, started, pc = _sym_unpack(key, work, h)
                left = work[yi]
                below = work[yi - 1] if yi > 0 else 0
                # skip option (not allowed at the forced cell (0, row0))
                if not force_cell:
                    old = work[yi]
                    work[yi] = 0
                    if old != 0:
                        present = False
                        for i in range(h):
                            if work[i] == old:
                                present = True
                                break
                        if not present:
                            others = False
                            for i in range(h):
                                if work[i] != 0:
                                    others = True
                                    break
                            if cells == n and not others and tor == 0:
                                total += w
                        else:
                            k = _sym_pack(work, h, cells, tor, started, pc)
                            if k in new:
                                new[k] += w
                            else:
                                new[k] = w
                    else:
                        k = _sym_pack(work, h, cells, tor, started, pc)
                        if k in new:
                            new[k] += w
                        else:
                            new[k] = w
                    work[yi] = old
                # place option
                if cells + wgt <= n and x <= R:
                    save = work[yi]
                    if left != 0 and below != 0 and left != below:
                        m = left if left < below else below
                        big = left if left > below else below
                        for i in range(h):
                            if work[i] == big:
                                work[i] = m
                        work[yi] = m
                        nk = _sym_pack(
                            work, h, cells + wgt, tor + (x if sym == 0 else 0), 1, 1
                        )
                        _sym_unpack(key, work, h)
                    else:
                        if left != 0 or below != 0:
                            work[yi] = left if left != 0 else below
                        else:
                            mx = 0
                            for i in range(h):
                                if work[i] > mx:
                                    mx = work[i]
                            work[yi] = mx + 1
                        nk = _sym_pack(
                            work, h, cells + wgt, tor + (x if sym == 0 else 0), 1, 1
                        )
                        work[yi] = save
                    if nk in new:
                        new[nk] += w
                    else:
                        new[nk] = w
            states = new
            if len(states) > maxstates:
                maxstates = len(states)
        # column-end: interval property: started states must place every column
        # until complete (boundary empties only at completion)
        flt = Dict.empty(KEY, numba.types.int64)
        for key in states:
            cells, tor, started, pc = _sym_unpack(key, work, h)
            if started == 1 and pc == 0:
                anylab = False
                for i in range(h):
                    if work[i] != 0:
                        anylab = True
                        break
                if anylab or cells < n:
                    continue
            flt[key] = states[key]
        states = flt
    return total, maxstates


def _max_left(c: int) -> int:
    return max(L * (L + 1) // 2 + (c - L) * L for L in range(c + 1))


def _r_bound(n: int) -> int:
    r = 0
    while (r + 1) * (r + 2) // 2 <= _max_left(n - (r + 1) - 1):
        r += 1
    return r


def solve(n: int = 18) -> int:
    r = _r_bound(n)
    a, _pe, _pr = _run_A(n, r, 130_000_000, 4_000_000)
    assert a >= 0, "buffer overflow"
    s, _ = _run_sym(n, r, 1)
    assert (a + s) % 2 == 0
    return (a + s) // 2


if __name__ == "__main__":
    print(solve())  # 15030564
