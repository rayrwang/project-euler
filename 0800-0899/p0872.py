def f(n: int, k: int) -> int:
    """Sum of node numbers on the path from the root of T_n to node k.

    Claim: in T_n the parent of node k < n is k + h(n - k), where h(d) is
    the highest power of two not exceeding d.  Proof by induction on n.
    Given the claim for T_{n-1}, the largest child of a node m is the
    largest k with k + h(n - 1 - k) = m, which forces n - 1 - k to be just
    below a power of two; starting from the root this makes the greatest
    path exactly n - 1, n - 2, n - 4, n - 8, ...  These nodes become the
    children of n, and indeed k + h(n - k) = n exactly when n - k is a
    power of two.  Every other node keeps its parent, and h(n - k) =
    h(n - 1 - k) whenever n - k is not a power of two, so the claim holds
    for T_n.

    Walking down from n therefore subtracts the binary bits of d = n - k
    in increasing order; we just accumulate the partial sums.
    """
    d = n - k
    s = m = n
    bit = 1
    while d:
        if d & bit:
            m -= bit
            s += m
            d ^= bit
        bit <<= 1
    return s


def _brute_check(max_n: int) -> None:
    """Build the trees explicitly and compare every path sum with f."""
    children: dict[int, list[int]] = {1: []}
    parent: dict[int, int] = {}
    for n in range(2, max_n + 1):
        path = [n - 1]
        while children[path[-1]]:
            path.append(max(children[path[-1]]))
        children[n] = path
        for node in path:
            parent[node] = n
        for i in range(1, len(path)):
            children[path[i - 1]].remove(path[i])
        for k in range(1, n + 1):
            s, m = 0, k
            while True:
                s += m
                if m == n:
                    break
                m = parent[m]
            assert s == f(n, k), (n, k)


if __name__ == "__main__":
    assert f(6, 1) == 12
    assert f(10, 3) == 29
    _brute_check(150)
    print(f(10**17, 9**17))  # 2903144925319290239
