"""Project Euler Problem 693: Finite Sequence Generator.

l(x, y) is the length of the sequence a_x = y, a_{z+1} = a_z^2 mod z,
stopping at 0 or 1; g(x) = max over y < x; f(n) = max over x <= n of g(x).

g(x) for a single x: simulate all starting values y at once.  The set of
values alive at index z evolves as A_{z+1} = {a^2 mod z : a in A_z} minus
{0, 1}, and g(x) is the number of terms generated when the last value dies.
The first image (squares mod x of y = 2..x-1) is built with the symmetry
y^2 = (x - y)^2 mod x.  Images of a function only shrink, and squaring is
at least 2-to-1 on most of the range, so the set collapses geometrically;
once it is a singleton the chain is followed directly.  Deduplication uses
an epoch-stamped marker array while the set is large and a quadratic scan
once it is tiny.

f(n) by branch and bound: dropping the first r - x terms of a sequence
starting at x leaves a valid sequence starting at r, so

    g(x) <= g(r) + (r - x)   for r >= x,

hence max over [l, r] of g is at most g(r) + (r - l).  Seed a coarse grid,
keep intervals in a max-heap keyed by this upper bound, and repeatedly
bisect the most promising interval, pruning any whose bound cannot beat the
best g found.  Every pruned interval provably contains no better x, so the
search is exact while evaluating g at only a few hundred points.

Verified: l(5, 3) = 29, g(5) = 29, f(100) = 145, f(10000) = 8824, and g
against per-y brute force for all x <= 400.
"""

import heapq

import numba
import numpy as np


def chain_len(x: int, y: int) -> int:
    a, z, n = y, x, 1
    while a > 1:
        a = a * a % z
        z += 1
        n += 1
    return n


@numba.jit(cache=True)
def g(x: int) -> int:
    """Longest chain over all starts y < x, via the merged active set."""
    if x <= 2:
        return 1 if x == 2 else 0

    mark = np.zeros(x + 4100, dtype=np.int32)
    cur = np.empty(x // 2 + 2, dtype=np.int64)
    nxt = np.empty(x // 2 + 2, dtype=np.int64)

    # First transition: squares of y = 2..x-1 modulo x, deduplicated.
    # y and x - y square to the same value, and y = x - 1 squares to 1.
    epoch = 1
    cnt = 0
    for y in range(2, x // 2 + 1):
        v = y * y % x
        if v > 1 and mark[v] != epoch:
            mark[v] = epoch
            cur[cnt] = v
            cnt += 1
    length = 2  # terms at indices x and x + 1 exist for any y >= 2
    mod = x + 1

    while cnt > 1:
        ncnt = 0
        if cnt > 64 and mod - x < 4000:  # marker valid while values < len
            epoch += 1
            for i in range(cnt):
                v = cur[i] * cur[i] % mod
                if v > 1 and mark[v] != epoch:
                    mark[v] = epoch
                    nxt[ncnt] = v
                    ncnt += 1
        else:
            for i in range(cnt):
                v = cur[i] * cur[i] % mod
                if v > 1:
                    dup = False
                    for j in range(ncnt):
                        if nxt[j] == v:
                            dup = True
                            break
                    if not dup:
                        nxt[ncnt] = v
                        ncnt += 1
        cur, nxt = nxt, cur
        cnt = ncnt
        mod += 1
        if cnt == 0:
            return length + 1
        length += 1

    if cnt == 0:  # all of y = 2..x-1 squared to 0 or 1
        return length

    v = cur[0]
    while v > 1:
        v = v * v % mod
        mod += 1
        length += 1
    return length


def f(n: int, grid_points: int = 64) -> int:
    """Exact branch and bound on g(x) <= g(r) + (r - x)."""
    if n < 2:
        return 0
    cache: dict[int, int] = {}

    def cached_g(x: int) -> int:
        if x not in cache:
            cache[x] = int(g(x))
        return cache[x]

    step = max(1, (n - 2) // grid_points)
    points = list(range(2, n + 1, step))
    if points[-1] != n:
        points.append(n)
    best = max(cached_g(x) for x in points)

    heap = []
    for left, right in zip(points, points[1:]):
        bound = cached_g(right) + (right - left)
        if bound > best:
            heapq.heappush(heap, (-bound, left, right))

    while heap and -heap[0][0] > best:
        _, left, right = heapq.heappop(heap)
        if right - left <= 1:
            continue
        mid = (left + right) // 2
        best = max(best, cached_g(mid))
        for lo, hi in ((left, mid), (mid, right)):
            if hi - lo > 1:
                bound = cached_g(hi) + (hi - lo)
                if bound > best:
                    heapq.heappush(heap, (-bound, lo, hi))
    return best


if __name__ == "__main__":
    assert chain_len(5, 3) == 29
    assert int(g(5)) == 29
    assert all(
        int(g(x)) == max(chain_len(x, y) for y in range(1, x))
        for x in range(2, 401)
    )
    assert f(100) == 145
    assert f(10**4) == 8824
    print(f(3 * 10**6))  # 699161
