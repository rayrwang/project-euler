import numba
import numpy as np


@numba.jit(cache=True)
def max_matching(f: np.ndarray) -> int:
    """Maximum matching of the functional graph x -> f[x].

    A drifting subset A (|A u f(A)| = 2|A|) is exactly a set of vertices
    on which f is injective with image disjoint from A, i.e. a set of
    pairwise vertex-disjoint edges (a, f(a)) -- a matching.  Each
    component is a cycle with trees attached, so a leaf-first greedy on
    the tree parts (peeling in-degree-zero vertices) is optimal, and each
    cycle then contributes floor(run / 2) for every maximal arc of
    still-unmatched vertices (or floor(L / 2) for an untouched cycle;
    fixed points are loops and contribute nothing).
    """
    n = len(f)
    indeg = np.zeros(n, dtype=np.int64)
    for x in range(n):
        indeg[f[x]] += 1
    queue = np.empty(n, dtype=np.int64)
    head = tail = 0
    for x in range(n):
        if indeg[x] == 0:
            queue[tail] = x
            tail += 1
    matched = np.zeros(n, dtype=np.bool_)
    peeled = np.zeros(n, dtype=np.bool_)
    count = 0
    while head < tail:
        x = queue[head]
        head += 1
        peeled[x] = True
        y = f[x]
        if not matched[x] and not matched[y] and y != x:
            matched[x] = True
            matched[y] = True
            count += 1
        indeg[y] -= 1
        if indeg[y] == 0:
            queue[tail] = y
            tail += 1
    # remaining vertices (not peeled) lie on cycles
    seen = np.zeros(n, dtype=np.bool_)
    for s in range(n):
        if peeled[s] or seen[s]:
            continue
        # find a matched vertex on this cycle, if any
        start = -1
        x = s
        while True:
            seen[x] = True
            if matched[x] and start < 0:
                start = x
            x = f[x]
            if x == s:
                break
        if start < 0:  # whole cycle unmatched
            length = 1
            x = f[s]
            while x != s:
                length += 1
                x = f[x]
            count += length // 2
        else:  # sum floor(run/2) over unmatched arcs between matched ones
            run = 0
            x = f[start]
            while x != start:
                if matched[x]:
                    count += run // 2
                    run = 0
                else:
                    run += 1
                x = f[x]
            count += run // 2
    return count


def d_of(n: int) -> int:
    x = np.arange(n, dtype=np.int64)
    return int(max_matching((x * x % n * x + x + 1) % n))


def _d_brute(f: list[int]) -> int:
    n = len(f)
    best = 0
    for mask in range(1 << n):
        a = [x for x in range(n) if (mask >> x) & 1]
        if len(set(a) | {f[x] for x in a}) == 2 * len(a):
            best = max(best, len(a))
    return best


if __name__ == "__main__":
    import random

    rng = random.Random(871)
    for _ in range(200):
        n = rng.randint(1, 12)
        f = [rng.randrange(n) for _ in range(n)]
        assert max_matching(np.array(f, dtype=np.int64)) == _d_brute(f)
    assert d_of(5) == 1  # given
    assert d_of(10) == 3  # given
    print(sum(d_of(10**5 + i) for i in range(1, 101)))  # 2848790
