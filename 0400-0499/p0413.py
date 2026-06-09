import numpy as np

def one_child_count(d: int) -> int:
    """Number of d-digit one-child numbers: exactly one contiguous
    substring (by value, leading zeros allowed) is divisible by d.

    Scan digits left to right and track the residues mod d of every
    substring ending at the current position: appending digit c maps each
    residue r to 10r + c and adds a fresh single-digit substring c. A
    substring is a 'child' when its residue hits 0 at the moment it is
    completed... but every prefix of the scan completes the substrings
    ending there, so children are counted as classes land on residue 0.

    Two suffixes sharing a residue stay together forever, so only the
    *multiset* of residues matters, and any class of size >= 2 landing on
    0 means two children at once — fatal. Hence counts cap at 2, giving a
    state of d trits plus a child flag (0 or 1; >= 2 dies). The reachable
    state space stays small (about 5 * 10^5 at the worst, d = 19), and
    the whole layer-by-layer DP vectorises over the state table.
    """
    # initial layer: first digit 1..9
    seen: dict[bytes, int] = {}
    rows = []
    cnts = []
    for c in range(1, 10):
        v = np.zeros(d + 1, dtype=np.int8)
        v[c % d] = 1
        v[d] = 1 if c % d == 0 else 0
        key = v.tobytes()
        if key in seen:
            cnts[seen[key]] += 1
        else:
            seen[key] = len(rows)
            rows.append(v)
            cnts.append(1)
    states = np.array(rows)
    counts = np.array(cnts, dtype=np.int64)
    for _ in range(1, d):
        new_states = []
        new_counts = []
        for c in range(10):
            t = np.zeros_like(states)
            for r in range(d):
                t[:, (10 * r + c) % d] += states[:, r]
            landed = t[:, 0].astype(np.int64)  # suffix classes hitting 0
            if c % d == 0:
                landed = landed + 1  # the new single-digit substring c
            t[:, c % d] += 1
            np.minimum(t[:, :d], 2, out=t[:, :d])
            child = states[:, d].astype(np.int64) + landed
            keep = child <= 1
            t = t[keep]
            t[:, d] = child[keep].astype(np.int8)
            new_states.append(t)
            new_counts.append(counts[keep])
        states = np.ascontiguousarray(np.concatenate(new_states))
        counts = np.concatenate(new_counts)
        # merge identical states
        packed = states.view(np.dtype((np.void, states.shape[1])))[:, 0]
        order = np.argsort(packed)
        states = states[order]
        counts = counts[order]
        packed = packed[order]
        fresh = np.empty(len(packed), dtype=bool)
        fresh[0] = True
        fresh[1:] = packed[1:] != packed[:-1]
        starts = np.flatnonzero(fresh)
        counts = np.add.reduceat(counts, starts)
        states = states[starts]
    return int(counts[states[:, d] == 1].sum())

def brute(d: int) -> int:
    total = 0
    for n in range(10 ** (d - 1), 10**d):
        s = str(n)
        children = sum(1 for i in range(d) for j in range(i + 1, d + 1)
                       if int(s[i:j]) % d == 0)
        if children == 1:
            total += 1
    return total

if __name__ == "__main__":
    for d in (2, 3, 4):
        assert one_child_count(d) == brute(d)
    assert sum(one_child_count(d) for d in (1, 2, 3)) == 389  # F(10^3)
    assert sum(one_child_count(d) for d in range(1, 8)) == 277674  # F(10^7)
    print(sum(one_child_count(d) for d in range(1, 20)))  # 3079418648040719
