import numba
import numpy as np

MOD = 1000000033

@numba.jit(cache=True)
def rigid_sum(n_max: int, mod: int) -> int:
    """S(N) = sum of R(m, n) for 1 <= m, n <= N, mod `mod`.

    By the Bolker-Crapo theorem, a braced m x n grid is rigid exactly when
    the bipartite 'brace graph' — m row vertices, n column vertices, an
    edge per braced cell — is connected. Each cell is independently braced
    or not, so R(m, n) counts the connected spanning subgraphs of K_{m,n}.

    Recurrence by extracting the component of a fixed row vertex (i rows
    including it, j columns; everything else arbitrary):
      2^{mn} = sum_{i,j} C(i, j) binom(m-1, i-1) binom(n, j) 2^{(m-i)(n-j)},
    solved for C(m, n) = R(m, n); C(1, 0) = 1 covers the isolated-vertex
    component and C(i >= 2, 0) = 0.
    """
    # Pascal's triangle mod p (no primality assumptions needed)
    ch = np.zeros((n_max + 1, n_max + 1), dtype=np.int64)
    for i in range(n_max + 1):
        ch[i][0] = 1
        for j in range(1, i + 1):
            ch[i][j] = (ch[i - 1][j - 1] + ch[i - 1][j]) % mod
    pw2 = np.empty(n_max * n_max + 1, dtype=np.int64)
    pw2[0] = 1
    for i in range(1, n_max * n_max + 1):
        pw2[i] = pw2[i - 1] * 2 % mod
    c = np.zeros((n_max + 1, n_max + 1), dtype=np.int64)
    c[1][0] = 1
    total = 0
    for m in range(1, n_max + 1):
        for n in range(1, n_max + 1):
            acc = 0
            for i in range(1, m + 1):
                for j in range(0, n + 1):
                    if i == m and j == n:
                        continue
                    if c[i][j] == 0:
                        continue
                    acc = (acc + c[i][j] * ch[m - 1][i - 1] % mod
                           * ch[n][j] % mod * pw2[(m - i) * (n - j)]) % mod
            c[m][n] = (pw2[m * n] - acc) % mod
            total = (total + c[m][n]) % mod
    return total % mod

def brute_r(m: int, n: int) -> int:
    """Direct count of connected spanning subgraphs of K_{m,n}."""
    edges = [(i, m + j) for i in range(m) for j in range(n)]
    count = 0
    for mask in range(1 << len(edges)):
        parent = list(range(m + n))

        def find(a: int) -> int:
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        comp = m + n
        for k, (a, b) in enumerate(edges):
            if mask >> k & 1:
                ra, rb = find(a), find(b)
                if ra != rb:
                    parent[ra] = rb
                    comp -= 1
        if comp == 1:
            count += 1
    return count

if __name__ == "__main__":
    assert brute_r(2, 3) == 19  # given R(2,3)
    # check table values against brute force and the given S(5)
    assert rigid_sum(1, MOD) == brute_r(1, 1) == 1
    s3 = sum(brute_r(i, j) for i in range(1, 4) for j in range(1, 4))
    assert rigid_sum(3, MOD) == s3 % MOD
    assert rigid_sum(5, MOD) == 25021721  # given S(5)
    print(rigid_sum(100, MOD))  # 863253606
