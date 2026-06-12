"""Problem 424: Kakuro.

Each puzzle encrypts its clue sums with a letter-to-digit bijection
(A-J onto 0-9). The solver runs a DFS over letter assignments, ordered
by how many clue specs each letter touches, pruning with run-sum
bounds (a run of length L sums to between L(L+1)/2 and L(19-L)/2,
tens letters are 1-4, letters on prefilled cells are nonzero). Each
complete assignment fixes all clue values and the grid is then solved
by constraint propagation over precomputed digit-subset tables (per
run: the union of compatible subsets prunes cell candidates to a
fixpoint) with a small backtracking search on top. The per-puzzle
answer is the digit string of A..J; a missing tenth letter takes the
leftover digit.
"""

from functools import lru_cache
from itertools import combinations

@lru_cache(maxsize=None)
def combos(length: int, total: int) -> tuple[int, ...]:
    """Bitmasks (bit d = digit d) of `length` distinct digits 1-9
    summing to `total`."""
    out = []
    for sub in combinations(range(1, 10), length):
        if sum(sub) == total:
            m = 0
            for d in sub:
                m |= 1 << d
            out.append(m)
    return tuple(out)

def split_top_level(line: str) -> list[str]:
    parts = []
    depth = 0
    cur = []
    for ch in line:
        if ch == "," and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            cur.append(ch)
    parts.append("".join(cur))
    return parts

def parse_puzzle(line: str):
    toks = split_top_level(line.strip())
    g = int(toks[0])
    cells = toks[1:]
    assert len(cells) == g * g
    grid = [cells[r * g:(r + 1) * g] for r in range(g)]
    white = {}          # (r, c) -> white-cell index
    prefill = {}        # cell index -> letter
    clues = []          # (letters, list of cell indices)
    for r in range(g):
        for c in range(g):
            t = grid[r][c]
            if t == "O" or (len(t) == 1 and "A" <= t <= "J"):
                white[(r, c)] = len(white)
                if t != "O":
                    prefill[white[(r, c)]] = t
    for r in range(g):
        for c in range(g):
            t = grid[r][c]
            if not t.startswith("("):
                continue
            for spec in t[1:-1].split(","):
                kind, letters = spec[0], spec[1:]
                run = []
                dr, dc = (0, 1) if kind == "h" else (1, 0)
                rr, cc = r + dr, c + dc
                while 0 <= rr < g and 0 <= cc < g and (rr, cc) in white:
                    run.append(white[(rr, cc)])
                    rr += dr
                    cc += dc
                clues.append((letters, run))
    return len(white), prefill, clues

def solve_grid(ncells: int, fixed: dict[int, int], runs) -> bool:
    """runs: list of (sum_value, cells). True iff solvable."""
    cand = [0b1111111110] * ncells
    for c, d in fixed.items():
        cand[c] = 1 << d
    def propagate(cand) -> bool:
        changed = True
        while changed:
            changed = False
            for s, cells in runs:
                length = len(cells)
                if not (length * (length + 1) // 2 <= s
                        <= length * (19 - length) // 2):
                    return False
                union_new = [0] * length
                assigned = 0
                for i, c in enumerate(cells):
                    if cand[c].bit_count() == 1:
                        assigned |= cand[c]
                for m in combos(length, s):
                    if assigned & ~m:
                        continue
                    ok = True
                    for c in cells:
                        if not (cand[c] & m):
                            ok = False
                            break
                    if ok:
                        for i, c in enumerate(cells):
                            union_new[i] |= m
                for i, c in enumerate(cells):
                    nc = cand[c] & union_new[i]
                    if nc != cand[c]:
                        if nc == 0:
                            return False
                        cand[c] = nc
                        changed = True
                # distinctness: singletons removed from runmates
                for c in cells:
                    if cand[c].bit_count() == 1:
                        for c2 in cells:
                            if c2 != c and cand[c2] & cand[c]:
                                cand[c2] &= ~cand[c]
                                if cand[c2] == 0:
                                    return False
                                changed = True
        return True
    def dfs(cand) -> bool:
        if not propagate(cand):
            return False
        best = -1
        bestn = 10
        for c in range(ncells):
            n = cand[c].bit_count()
            if 1 < n < bestn:
                best, bestn = c, n
        if best < 0:
            return True
        m = cand[best]
        d = 1
        while m:
            if m & 2:
                nxt = cand[:]
                nxt[best] = 1 << d
                if dfs(nxt):
                    return True
            m >>= 1
            d += 1
        return False
    return dfs(cand)

def solve_puzzle(line: str) -> int:
    ncells, prefill, clues = parse_puzzle(line)
    letters = sorted({ch for sp, _ in clues for ch in sp}
                     | set(prefill.values()))
    freq = {le: 0 for le in letters}
    for sp, _ in clues:
        for ch in sp:
            freq[ch] += 1
    order = sorted(letters, key=lambda x: -freq[x])
    nonzero = set(prefill.values()) | {sp[0] for sp, _ in clues
                                       if len(sp) == 2}
    assign: dict[str, int] = {}
    used = [False] * 10
    def spec_ok(sp: str, run_len: int) -> bool:
        lo = run_len * (run_len + 1) // 2
        hi = run_len * (19 - run_len) // 2
        if len(sp) == 1:
            if sp in assign:
                return lo <= assign[sp] <= hi
            return True
        t, u = sp[0], sp[1]
        tv = assign.get(t)
        uv = assign.get(u)
        if tv is not None and uv is not None:
            return lo <= 10 * tv + uv <= hi
        if tv is not None:
            return 10 * tv + 9 >= lo and 10 * tv <= hi
        return True
    def try_grid() -> bool:
        full = dict(assign)
        missing = [le for le in "ABCDEFGHIJ" if le not in full]
        if missing:
            rem = [d for d in range(10) if not used[d]]
            if len(missing) != 1 or len(rem) != 1:
                return False
            full[missing[0]] = rem[0]
        runs = []
        for sp, cells in clues:
            s = (full[sp[0]] if len(sp) == 1
                 else 10 * full[sp[0]] + full[sp[1]])
            runs.append((s, cells))
        fixed = {c: full[le] for c, le in prefill.items()}
        if any(d == 0 for d in fixed.values()):
            return False
        if solve_grid(ncells, fixed, runs):
            nonlocal answer
            answer = int("".join(str(full[le]) for le in "ABCDEFGHIJ"))
            return True
        return False
    answer = -1
    def dfs(i: int) -> bool:
        if i == len(order):
            return try_grid()
        le = order[i]
        for d in range(10):
            if used[d] or (d == 0 and le in nonzero):
                continue
            assign[le] = d
            used[d] = True
            if all(spec_ok(sp, len(cells)) for sp, cells in clues
                   if le in sp):
                if dfs(i + 1):
                    return True
            del assign[le]
            used[d] = False
        return False
    found = dfs(0)
    assert found
    return answer

if __name__ == "__main__":
    path = "assets/0424_kakuro200.txt"
    lines = [ln for ln in open(path).read().splitlines() if ln.strip()]
    assert len(lines) == 200
    answers = [solve_puzzle(ln) for ln in lines]
    assert answers[0] == 8426039571  # given example
    assert sum(answers[:10]) == 64414157580  # given
    print(sum(answers))  # 1059760019628
