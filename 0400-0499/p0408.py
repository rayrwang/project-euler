import numba
import numpy as np

MOD = 10**9 + 7

@numba.jit(cache=True)
def admissible_paths(n: int, mod: int) -> int:
    """P(n): lattice paths (0,0) -> (n,n) with north/east unit steps that
    avoid every point (x, y) with x, y and x + y all positive perfect
    squares.

    Such a point is (a^2, b^2) with a^2 + b^2 = c^2 — a Pythagorean leg
    pair — so only a few thousand bad points exist below 10^7, not the
    ~10^7 that x, y squares alone would give. The classic
    first-bad-point inclusion-exclusion then applies: with bad points
    sorted, f[i] = paths to bad point i avoiding all earlier ones,
    f[i] = C(x_i + y_i, x_i) - sum_{j dominated by i} f[j] C(dx + dy, dx),
    and P(n) = C(2n, n) - sum_i f[i] C((n - x_i) + (n - y_i), n - x_i).
    """
    # factorials and inverse factorials up to 2n
    size = 2 * n + 1
    fact = np.empty(size, dtype=np.int64)
    inv_fact = np.empty(size, dtype=np.int64)
    fact[0] = 1
    for i in range(1, size):
        fact[i] = fact[i - 1] * i % mod
    # Fermat inverse of fact[size-1], then walk back
    inv = 1
    b = fact[size - 1]
    e = mod - 2
    while e > 0:
        if e & 1:
            inv = inv * b % mod
        b = b * b % mod
        e >>= 1
    inv_fact[size - 1] = inv
    for i in range(size - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod

    # bad points: (a^2, b^2) with a^2 + b^2 a perfect square, inside the grid
    m = int(n**0.5)
    while (m + 1) * (m + 1) <= n:
        m += 1
    while m * m > n:
        m -= 1
    xs = np.empty(64 * m, dtype=np.int64)
    ys = np.empty(64 * m, dtype=np.int64)
    k = 0
    for a in range(1, m + 1):
        for bb in range(1, m + 1):
            s = a * a + bb * bb
            r = int(s**0.5)
            while r * r > s:
                r -= 1
            while (r + 1) * (r + 1) <= s:
                r += 1
            if r * r == s:
                xs[k] = a * a
                ys[k] = bb * bb
                k += 1
    # sort lexicographically by (x, y)
    order = np.argsort(xs[:k] * (n + 1) + ys[:k])
    px = xs[order]
    py = ys[order]

    f = np.empty(k, dtype=np.int64)
    for i in range(k):
        paths = fact[px[i] + py[i]] * inv_fact[px[i]] % mod * inv_fact[py[i]] % mod
        for j in range(i):
            if py[j] <= py[i]:  # px[j] <= px[i] from the sort order
                dx = px[i] - px[j]
                dy = py[i] - py[j]
                c = fact[dx + dy] * inv_fact[dx] % mod * inv_fact[dy] % mod
                paths = (paths - f[j] * c) % mod
        f[i] = paths
    total = fact[2 * n] * inv_fact[n] % mod * inv_fact[n] % mod
    for i in range(k):
        dx = n - px[i]
        dy = n - py[i]
        c = fact[dx + dy] * inv_fact[dx] % mod * inv_fact[dy] % mod
        total = (total - f[i] * c) % mod
    return total % mod

def brute(n: int) -> int:
    import math
    bad = set()
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a * a > n or b * b > n:
                continue
            c = math.isqrt(a * a + b * b)
            if c * c == a * a + b * b:
                bad.add((a * a, b * b))
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    grid[0][0] = 1
    for x in range(n + 1):
        for y in range(n + 1):
            if (x, y) in bad and (x, y) != (n, n):
                grid[x][y] = 0
                continue
            if x:
                grid[x][y] += grid[x - 1][y]
            if y:
                grid[x][y] += grid[x][y - 1]
    return grid[n][n]

if __name__ == "__main__":
    assert admissible_paths(5, MOD) == brute(5) == 252
    assert admissible_paths(16, MOD) == brute(16) % MOD == 596994440 % MOD
    assert admissible_paths(60, MOD) == brute(60) % MOD
    assert admissible_paths(1000, MOD) == 341920854  # given
    print(admissible_paths(10**7, MOD))  # 299742733
