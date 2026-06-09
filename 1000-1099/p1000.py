"""Project Euler 1000.

The landmark problem bundles three sub-problems whose answers seed a tribonacci
product sequence; the final answer is M(1000) mod p with p = 10**9 + 7.

Sub-problem I(n) -- Max And. Splitting 1..n into A, B and summing a AND b over
a in A, b in B is exactly weighted max-cut on the complete graph with edge
weight (i AND j). Decomposing by bit k (value 2**k) and writing s_i = +-1 for
the side of i, the cut value is
    (1/4) * sum_k 2**k (c_k**2 - d_k**2),   d_k = sum_{i has bit k} s_i,
where c_k counts 1..n having bit k. The first term is fixed, so we minimise
sum_k 2**k d_k**2. Each d_k has parity c_k, so its least square is (c_k mod 2);
that joint minimum is attainable (verified by brute force for every n <= 12),
giving I(n) = (1/4)[sum_k 2**k c_k**2 - sum_k 2**k (c_k mod 2)].

Sub-problem X(N) -- Max Xor Sum. With edge weight [x, y] = x**2 XOR y**2, a valid
sequence is a walk whose consecutive edge weights strictly increase; we maximise
their sum. Sort edges by weight and sweep upward keeping f[v] = best walk sum
ending at vertex v using strictly lighter edges; an edge (u, v, w) offers
f[u] + w to v and f[v] + w to u. Equal-weight edges are applied as a batch so
none chains onto another (the inequality is strict). The answer is max f.

Sub-problem C(N) -- Unreachable Nim. Every P-position (nim-value 0) is the
target of a winning move, hence reachable; the empty walk argument shows a
status is unreachable iff it is an N-position with no P-position predecessor.
Increasing pile a to b XOR c (etc.) is the only way to land on a P-position, so
(a, b, c) is unreachable exactly when a^b^c != 0 and b^c <= a and a^c <= b and
a^b <= c. Equality forces nim-value 0, so this is the strict, symmetric system
    a^b < c,  b^c < a,  c^a < b,
counted over [0, N)^3 by a digit DP (matches the given C(10) = 123).

Meta. M(k) = M(k-1) M(k-2) M(k-3) makes M(k) = I^e0 X^e1 C^e2 with tribonacci
exponents; reduce the exponents mod (p - 1) by Fermat and combine. The check
M(4) = I * X**2 * C**2 reproduces the given 457587170.
"""
from functools import lru_cache

P = 10**9 + 7

def max_and(n):
    """I(n): maximum cut value sum_{a in A, b in B} (a AND b)."""
    const4 = lb4 = 0
    k = 0
    while (1 << k) <= n:
        period = 1 << (k + 1)
        c = (n + 1) // period * (1 << k) + max(0, (n + 1) % period - (1 << k))
        const4 += (1 << k) * c * c
        lb4 += (1 << k) * (c & 1)
        k += 1
    return (const4 - lb4) // 4

def max_xor_sum(n):
    """X(n): largest sum over a strictly-increasing-weight walk."""
    edges = []
    for a in range(1, n + 1):
        a2 = a * a
        for b in range(a + 1, n + 1):
            edges.append((a2 ^ (b * b), a, b))
    edges.sort()
    f = [0] * (n + 1)
    i, m = 0, len(edges)
    while i < m:
        j, w = i, edges[i][0]
        while j < m and edges[j][0] == w:
            j += 1
        updates = []
        for t in range(i, j):
            _, u, v = edges[t]
            updates.append((v, f[u] + w))
            updates.append((u, f[v] + w))
        for vert, val in updates:
            if val > f[vert]:
                f[vert] = val
        i = j
    return max(f)

def unreachable_nim(n):
    """C(n): triples in [0, n)^3 with a^b < c, b^c < a, c^a < b."""
    hi = n - 1
    nbits = max(1, hi.bit_length())

    @lru_cache(maxsize=None)
    def rec(pos, ta, tb, tc, c1, c2, c3):
        if pos < 0:
            return 1 if c1 == 1 and c2 == 1 and c3 == 1 else 0
        nb = (hi >> pos) & 1
        total = 0
        for da in range(((nb if ta else 1)) + 1):
            nta = ta and da == nb
            for db in range(((nb if tb else 1)) + 1):
                ntb = tb and db == nb
                for dc in range(((nb if tc else 1)) + 1):
                    ntc = tc and dc == nb
                    # compare left^right bit pairs: a^b vs c, b^c vs a, c^a vs b
                    n1 = c1 or (1 if (da ^ db) < dc else 2 if (da ^ db) > dc else 0)
                    n2 = c2 or (1 if (db ^ dc) < da else 2 if (db ^ dc) > da else 0)
                    n3 = c3 or (1 if (dc ^ da) < db else 2 if (dc ^ da) > db else 0)
                    total += rec(pos - 1, nta, ntb, ntc, n1, n2, n3)
        return total

    res = rec(nbits - 1, True, True, True, 0, 0, 0)
    rec.cache_clear()
    return res

def meta(k, m0, m1, m2):
    """M(k) mod P from M(0)=m0, M(1)=m1, M(2)=m2 and the product recurrence."""
    exps = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    if k <= 2:
        e = exps[k]
    else:
        a, b, c = exps
        for _ in range(3, k + 1):
            a, b, c = b, c, tuple((a[i] + b[i] + c[i]) % (P - 1) for i in range(3))
        e = c
    return (pow(m0 % P, e[0], P) * pow(m1 % P, e[1], P) * pow(m2 % P, e[2], P)) % P

if __name__ == "__main__":
    i_val = max_and(1000)
    x_val = max_xor_sum(1000)
    c_val = unreachable_nim(1000)
    assert meta(4, i_val, x_val, c_val) == 457587170, "M(4) check failed"
    print(meta(1000, i_val, x_val, c_val))  # 891213201
