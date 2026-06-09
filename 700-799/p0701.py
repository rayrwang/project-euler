import numba
import numpy as np

def build_transitions(width):
    """Precompute, for every (frontier pattern, next-row mask), how components
    merge, grow, and finish. Patterns are canonical labelings of the frontier
    row (each cell white = -1, else component id 0..3 in left-to-right order).

    Returns numpy tables indexed by pid * 2**width + mask:
        npid           new pattern id
        jcount         number of components in the new frontier
        merge[.,j]     bitmask of old components merged into new component j
        addcnt[.,j]    new black cells joining new component j
        fin            bitmask of old components that finish at this step
    """
    full = (1 << width) - 1

    def transition(labels, mask):
        k = max(labels) + 1 if any(v >= 0 for v in labels) else 0
        parent = list(range(k + width))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for c in range(width):
            if mask & (1 << c):
                node = k + c
                if c > 0 and (mask & (1 << (c - 1))):
                    union(k + c - 1, node)
                if labels[c] >= 0:
                    union(labels[c], node)

        root_cells = {k + c: find(k + c) for c in range(width) if mask & (1 << c)}
        new_labels = [-1] * width
        order = {}
        for c in range(width):
            if mask & (1 << c):
                r = root_cells[k + c]
                if r not in order:
                    order[r] = len(order)
                new_labels[c] = order[r]

        jcount = len(order)
        merge = [0] * 4
        addcnt = [0] * 4
        for c in range(width):
            if mask & (1 << c):
                addcnt[order[root_cells[k + c]]] += 1
        for old in range(k):
            r = find(old)
            if r in order:
                merge[order[r]] |= 1 << old
        used = 0
        for m in merge:
            used |= m
        fin = ((1 << k) - 1) & ~used
        return tuple(new_labels), jcount, merge, addcnt, fin

    # Enumerate reachable canonical patterns via BFS.
    start = (-1,) * width
    pid = {start: 0}
    order_patterns = [start]
    i = 0
    while i < len(order_patterns):
        labels = order_patterns[i]
        i += 1
        for mask in range(full + 1):
            nl = transition(labels, mask)[0]
            if nl not in pid:
                pid[nl] = len(order_patterns)
                order_patterns.append(nl)

    n = len(order_patterns)
    size = n * (full + 1)
    npid = np.zeros(size, dtype=np.int64)
    jcount = np.zeros(size, dtype=np.int64)
    merge = np.zeros((size, 4), dtype=np.int64)
    addcnt = np.zeros((size, 4), dtype=np.int64)
    fin = np.zeros(size, dtype=np.int64)
    for labels, p in pid.items():
        for mask in range(full + 1):
            nl, jc, mg, ad, fm = transition(labels, mask)
            idx = p * (full + 1) + mask
            npid[idx] = pid[nl]
            jcount[idx] = jc
            for j in range(4):
                merge[idx, j] = mg[j]
                addcnt[idx, j] = ad[j]
            fin[idx] = fm
    return n, npid, jcount, merge, addcnt, fin

@numba.jit(cache=True)
def run_dp(height, width, npid, jcount, merge, addcnt, fin):
    """Sum of (largest component size) over all 2**(W*H) colourings.

    State integer packs: pattern id, four 6-bit component sizes, 6-bit running
    max of finished components. Counts are exact int64 (well within range).
    """
    full = (1 << width) - 1
    SBITS = 6
    SMASK = (1 << SBITS) - 1

    states = {np.int64(0): np.int64(1)}  # all-white frontier, sizes 0, max 0
    for _ in range(height):
        new_states = {}
        for state, cnt in states.items():
            runmax = state & SMASK
            scode = (state >> SBITS) & ((1 << (4 * SBITS)) - 1)
            pid = state >> (SBITS + 4 * SBITS)
            s0 = scode & SMASK
            s1 = (scode >> SBITS) & SMASK
            s2 = (scode >> (2 * SBITS)) & SMASK
            s3 = (scode >> (3 * SBITS)) & SMASK
            old = (s0, s1, s2, s3)
            base = pid * (full + 1)
            for mask in range(full + 1):
                idx = base + mask
                nr = runmax
                fm = fin[idx]
                for o in range(4):
                    if (fm >> o) & 1:
                        if old[o] > nr:
                            nr = old[o]
                jc = jcount[idx]
                ncode = np.int64(0)
                biggest_active = np.int64(0)
                for j in range(jc):
                    mg = merge[idx, j]
                    sz = addcnt[idx, j]
                    for o in range(4):
                        if (mg >> o) & 1:
                            sz += old[o]
                    ncode |= sz << (SBITS * j)
                    if sz > biggest_active:
                        biggest_active = sz
                nstate = (npid[idx] << (SBITS + 4 * SBITS)) | (ncode << SBITS) | nr
                if nstate in new_states:
                    new_states[nstate] += cnt
                else:
                    new_states[nstate] = cnt
        states = new_states

    total = np.int64(0)
    for state, cnt in states.items():
        runmax = state & SMASK
        scode = (state >> SBITS) & ((1 << (4 * SBITS)) - 1)
        biggest = runmax
        for j in range(4):
            sz = (scode >> (SBITS * j)) & SMASK
            if sz > biggest:
                biggest = sz
        total += biggest * cnt
    return total

def expected_max_area(width, height):
    n, npid, jcount, merge, addcnt, fin = build_transitions(width)
    total = run_dp(height, width, npid, jcount, merge, addcnt, fin)
    return total / (1 << (width * height))

if __name__ == "__main__":
    print(f"{expected_max_area(7, 7):.8f}")  # 13.51099836
