import sys

def feasible(a, b, m):
    """Can a = b be reached in exactly m more moves? Over a remaining move
    word with r moves of type r and s = m - r of type s, the final values are
        a * 2^s + A,  A = sum g_t 2^t  (g_t >= 0, sum g_t = r, t <= s),
        b * 2^r + B,  B analogous,
    so A ranges over [r, r 2^s] (just {0} if r = 0) and similarly B. Equality
    is possible only if the two intervals overlap for some split."""
    for r in range(m + 1):
        s = m - r
        amin = (a << s) + (r if r else 0)
        amax = (a << s) + ((r << s) if r else 0)
        bmin = (b << r) + (s if s else 0)
        bmax = (b << r) + ((s << r) if s else 0)
        if amin <= bmax and bmin <= amax:
            return True
    return False

def dfs(a, b, m, out):
    if m == 0:
        if a == b:
            out.append(a)
        return
    if a == b or not feasible(a, b, m):
        return
    dfs(a + 1, 2 * b, m - 1, out)
    dfs(2 * a, b + 1, m - 1, out)

def smallest_path(a, b, parity):
    """Final value of the shortest path to equality for (a, b) whose length
    n has the given parity. Iterative deepening over the move count
    M = n - 1; intermediate equalities terminate a branch (such a prefix is
    itself a shorter path and would have been found at a smaller M of the
    right parity, or is of the wrong parity and useless).

    The interval prune is extremely strong: writing the final values as
    a 2^s + A vs b 2^r + B, parity of M forces |s - (r + 1)| >= 1 when
    a = 45, b = 90 = 2a, i.e. a factor-2 gap between the leading terms that
    the additive ranges (at most (M/2) 2^(M/2)) cannot bridge until
    M/2 + a >= 2a; every even M < 92 is refuted at the root, and the whole
    M = 96 search visits only a few hundred nodes.
    """
    m = 1 if parity % 2 == 0 else 2
    while True:
        out = []
        dfs(a, b, m, out)
        if out:
            assert len(out) == 1  # the problem promises uniqueness
            return out[0]
        m += 2

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    assert smallest_path(45, 90, 0) == 1476  # length 10, the given example
    print(smallest_path(45, 90, 1))  # 25332747903959376
