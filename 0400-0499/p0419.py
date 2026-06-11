MOD = 2**30

def evolve(s: str) -> str:
    out = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(str(j - i))
        out.append(s[i])
        i = j
    return "".join(out)

def splits_cleanly(left: str, right: str, depth: int = 15) -> bool:
    """True if `left + right` evolves as the independent concatenation
    of its parts for `depth` steps (a Conway split)."""
    whole = left + right
    for _ in range(depth):
        left, right, whole = evolve(left), evolve(right), evolve(whole)
        if left + right != whole:
            return False
    return True

def decompose(s: str) -> list[str]:
    """Split into irreducible chunks, greedily taking the leftmost
    valid split point."""
    chunks = []
    while s:
        for i in range(1, len(s)):
            if s[i] != s[i - 1] and splits_cleanly(s[:i], s[i:]):
                chunks.append(s[:i])
                s = s[i:]
                break
        else:
            chunks.append(s)
            s = ""
    return chunks

def build_elements() -> tuple[list[str], list[list[int]]]:
    """All irreducible chunks reachable from '1' (Conway's elements plus
    a few early transients) and the decay matrix D[i][j] = how many
    copies of element j appear in one evolution step of element i."""
    elements: dict[str, int] = {"1": 0}
    order = ["1"]
    decays: list[list[str] | None] = [None]
    frontier = ["1"]
    while frontier:
        nxt = []
        for e in frontier:
            parts = decompose(evolve(e))
            decays[elements[e]] = parts
            for p in parts:
                if p not in elements:
                    elements[p] = len(order)
                    order.append(p)
                    decays.append(None)
                    nxt.append(p)
        frontier = nxt
    k = len(order)
    mat = [[0] * k for _ in range(k)]
    for i in range(k):
        parts = decays[i]
        assert parts is not None
        for p in parts:
            mat[i][elements[p]] += 1
    return order, mat

def mat_mul(a, b, mod):
    n = len(a)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        ai = a[i]
        oi = out[i]
        for kk in range(n):
            v = ai[kk]
            if v:
                bk = b[kk]
                for j in range(n):
                    oi[j] = (oi[j] + v * bk[j]) % mod
    return out

def digit_counts(n: int) -> tuple[int, int, int]:
    """(#1s, #2s, #3s) of the n'th look-and-say term, mod 2^30."""
    order, mat = build_elements()
    k = len(order)
    vec = [0] * k
    vec[0] = 1  # term 1 is the string "1"
    e = n - 1
    while e:
        if e & 1:
            vec = [sum(vec[i] * mat[i][j] for i in range(k)) % MOD
                   for j in range(k)]
        mat = mat_mul(mat, mat, MOD)
        e >>= 1
    a = b = c = 0
    for i, s in enumerate(order):
        a = (a + vec[i] * s.count("1")) % MOD
        b = (b + vec[i] * s.count("2")) % MOD
        c = (c + vec[i] * s.count("3")) % MOD
    return a, b, c

if __name__ == "__main__":
    # direct simulation cross-check, including the given n = 40
    s = "1"
    for n in range(1, 49):
        if n in (1, 2, 7, 18, 30, 40, 48):
            assert digit_counts(n) == (s.count("1"), s.count("2"),
                                       s.count("3")), n
        s = evolve(s)
    assert digit_counts(40) == (31254, 20259, 11625)  # given
    a, b, c = digit_counts(10**12)
    print(f"{a},{b},{c}")  # 998567458,1046245404,43363922
