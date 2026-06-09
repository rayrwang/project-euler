def build_edges(n: int) -> set[frozenset[tuple[int, int]]]:
    """Edge set of the Sierpinski graph S_n on triangular lattice points."""
    if n == 1:
        a, b, c = (0, 0), (1, 0), (0, 1)
        return {frozenset((a, b)), frozenset((b, c)), frozenset((a, c))}
    s = 2 ** (n - 2)
    sub = build_edges(n - 1)
    edges = set()
    for ox, oy in ((0, 0), (s, 0), (0, s)):
        for e in sub:
            u, v = tuple(e)
            edges.add(
                frozenset(((u[0] + ox, u[1] + oy), (v[0] + ox, v[1] + oy)))
            )
    return edges


def count_hamiltonian_cycles(n: int) -> int:
    """Count Hamiltonian cycles of S_n by pruned backtracking.

    Starting at a degree-2 corner with the first edge fixed counts every
    cycle exactly once. The prune: an unvisited vertex whose available
    connections (unvisited neighbours, plus the path head if adjacent,
    plus the start if adjacent) drop below two can never be both entered
    and left, so the branch is dead. Only vertices adjacent to the old or
    new head can have lost availability, so the check is local.
    """
    edges = build_edges(n)
    verts = sorted({v for e in edges for v in e})
    idx = {v: i for i, v in enumerate(verts)}
    total = len(verts)
    adj: list[list[int]] = [[] for _ in range(total)]
    for e in edges:
        u, v = tuple(e)
        adj[idx[u]].append(idx[v])
        adj[idx[v]].append(idx[u])
    adj_set = [set(a) for a in adj]
    start = idx[(0, 0)]
    start_adj = adj_set[start]
    visited = [False] * total
    cnt = [len(a) for a in adj]  # unvisited-neighbour counts
    count = 0

    def dfs(u: int, depth: int) -> None:
        nonlocal count
        if depth == total:
            count += u in start_adj
            return
        for w in adj[u]:
            if visited[w]:
                continue
            visited[w] = True
            for x in adj[w]:
                cnt[x] -= 1
            ok = True
            for x in adj[w]:  # lost a free neighbour, gained the new head
                if not visited[x] and cnt[x] + (x in start_adj) < 1:
                    ok = False
                    break
            if ok:
                for x in adj[u]:  # lost the old head
                    if (
                        not visited[x]
                        and x not in adj_set[w]
                        and cnt[x] + (x in start_adj) < 2
                    ):
                        ok = False
                        break
            if ok:
                dfs(w, depth + 1)
            for x in adj[w]:
                cnt[x] += 1
            visited[w] = False

    for v in (start, adj[start][0]):
        visited[v] = True
        for x in adj[v]:
            cnt[x] -= 1
    dfs(adj[start][0], 2)
    return count


def totient(m: int) -> int:
    result = m
    p = 2
    while p * p <= m:
        if m % p == 0:
            result -= result // p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        result -= result // m
    return result


# C(n) = 8 * 12^t(n) with t(n) = (3^(n-2) - 3) / 2, verified by brute force
# at n = 3, 4, by the given C(5), and by both C(10000) residues below.
# x_0 = 10000 and x_{k+1} = C(x_k); every x_k for k >= 1 (and every
# exponent fed to the lift) is astronomically larger than log2 of any
# modulus involved, which is exactly the condition for the generalised
# Euler lift b^E = b^(E mod phi(m) + phi(m)) (mod m), valid for any base.


def c_mod(level: int, m: int) -> int:
    """x_level mod m."""
    if m == 1:
        return 0
    if level == 0:
        return 10000 % m
    phi = totient(m)
    t = t_mod(level - 1, phi)
    return 8 * pow(12, t + phi, m) % m


def t_mod(level: int, m: int) -> int:
    """t(x_level) = (3^(x_level - 2) - 3) / 2 mod m."""
    if m == 1:
        return 0
    m2 = 2 * m  # work mod 2m so the halving is exact
    if level == 0:
        a = pow(3, 10000 - 2, m2)
    else:
        phi = totient(m2)
        e = (c_mod(level, phi) - 2) % phi
        a = pow(3, e + phi, m2)
    return (a - 3) % m2 // 2 % m


if __name__ == "__main__":
    assert count_hamiltonian_cycles(3) == 8
    assert count_hamiltonian_cycles(4) == 8 * 12**3  # t(4) = 3
    assert 8 * 12 ** ((3**3 - 3) // 2) == 71328803586048  # given C(5)
    assert c_mod(1, 10**8) == 37652224  # given C(10000) mod 10^8
    assert c_mod(1, 13**8) == 617720485  # given C(10000) mod 13^8
    print(c_mod(3, 13**8))  # 324681947
