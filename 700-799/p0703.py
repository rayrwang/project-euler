from collections import deque

MOD = 1_001_001_011
N = 20

def solve(n):
    """T satisfies T(x) AND T(f(x)) = false for all x exactly when the chosen
    set {x : T(x) = true} is independent in the functional graph of f (edges
    x - f(x)). So S(n) counts independent sets in that graph on 2^n vertices.

    Each weakly connected component is a single cycle with in-trees attached.
    Peel the trees leaf-first, folding each node into its image f(v) with
        dp0[parent] *= dp0[v] + dp1[v],   dp1[parent] *= dp0[v]
    (dp0/dp1 = ways with v unselected / selected). Whatever survives the peeling
    are the cycle nodes, already carrying their trees' contributions; each cycle
    is then counted by the trace of a product of 2x2 transfer matrices
        M_v = [[A_v, B_v], [A_v, 0]],  A_v = dp0[v], B_v = dp1[v],
    and the answer is the product over cycles. No division is needed.
    """
    mask = (1 << n) - 1
    size = 1 << n
    f = [0] * size
    for x in range(size):
        b1 = (x >> (n - 1)) & 1
        b2 = (x >> (n - 2)) & 1
        b3 = (x >> (n - 3)) & 1
        f[x] = ((x << 1) & mask) | (b1 & (b2 ^ b3))

    indeg = [0] * size
    for x in range(size):
        indeg[f[x]] += 1
    dp0 = [1] * size
    dp1 = [1] * size
    q = deque(i for i in range(size) if indeg[i] == 0)
    alive = bytearray([1]) * size
    while q:
        v = q.popleft()
        alive[v] = 0
        p = f[v]
        dp0[p] = dp0[p] * ((dp0[v] + dp1[v]) % MOD) % MOD
        dp1[p] = dp1[p] * dp0[v] % MOD
        indeg[p] -= 1
        if indeg[p] == 0:
            q.append(p)

    res = 1
    visited = bytearray(size)
    for s in range(size):
        if not alive[s] or visited[s]:
            continue
        cyc = []
        v = s
        while not visited[v]:
            visited[v] = 1
            cyc.append(v)
            v = f[v]
        m00, m01, m10, m11 = 1, 0, 0, 1  # identity matrix
        for v in cyc:
            a, b = dp0[v], dp1[v]
            n00 = (m00 * a + m01 * a) % MOD
            n01 = m00 * b % MOD
            n10 = (m10 * a + m11 * a) % MOD
            n11 = m10 * b % MOD
            m00, m01, m10, m11 = n00, n01, n10, n11
        res = res * ((m00 + m11) % MOD) % MOD
    return res

if __name__ == "__main__":
    print(solve(N))  # 843437991
