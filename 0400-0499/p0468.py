"""Project Euler 468: Smooth Divisors of Binomial Coefficients.

F(n) = sum over B = 1..n and r = 0..n of the largest B-smooth divisor of
C(n, r); find F(11111111) mod 1000000993 (a prime).

For fixed r, let p_1 < p_2 < ... <= n be the primes and
Q_k(r) = prod_{i <= k} p_i^{v_{p_i}(C(n, r))}. As B sweeps 1..n the smooth
part is constant between consecutive primes, so

    sum_B S_B(C(n,r)) = sum_k (p_{k+1} - p_k) Q_k(r),

with p_0 = 1 and p_{K+1} = n + 1. Sweep r upward via
C(n, r+1) = C(n, r) (n - r) / (r + 1): each prime power p^e appearing in the
numerator or denominator multiplies every Q_k with k >= index(p) by p^e or
its modular inverse. A lazy segment tree over the K + 1 prefix products,
storing span_k * Q_k per leaf, supports suffix-multiply in O(log K) and the
per-r answer is just the root sum. Total work is sum of Omega(m) over
m <= n, about 3 * 10^7 prime-power updates, around half a minute in numba.
F(11) = 3132, F(1111) and F(111111) mod 1000000993 are asserted.
"""

import numpy as np
from numba import njit

M = 1000000993
N = 11111111


def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    spf[1] = 1
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf


@njit(cache=True)
def solve(n, spf):
    primes = np.empty(n, np.int64)
    num_primes = 0
    for p in range(2, n + 1):
        if spf[p] == p:
            primes[num_primes] = p
            num_primes += 1
    pidx = np.zeros(n + 1, np.int64)
    for k in range(num_primes):
        pidx[primes[k]] = k + 1  # leaf index of prime k; leaf 0 holds Q_0
    nleaf = num_primes + 1
    size = 1
    while size < nleaf:
        size *= 2
    seg = np.zeros(2 * size, np.int64)
    lazy = np.ones(2 * size, np.int64)
    for k in range(nleaf):
        lo = 1 if k == 0 else primes[k - 1]
        hi = primes[k] if k < num_primes else n + 1
        seg[size + k] = hi - lo  # span_k * Q_k with Q_k = 1 at r = 0
    for v in range(size - 1, 0, -1):
        seg[v] = (seg[2 * v] + seg[2 * v + 1]) % M
    invp = np.empty(num_primes, np.int64)
    for k in range(num_primes):
        b = primes[k] % M
        e = M - 2
        r = 1
        while e:
            if e & 1:
                r = r * b % M
            b = b * b % M
            e >>= 1
        invp[k] = r
    path = np.empty(64, np.int64)

    total = np.int64(0)
    for r in range(n + 1):
        total = (total + seg[1]) % M
        if r == n:
            break
        for sign in range(2):
            m = n - r if sign == 0 else r + 1
            while m > 1:
                p = spf[m]
                e = 0
                while m % p == 0:
                    m //= p
                    e += 1
                k = pidx[p]
                f = primes[k - 1] % M if sign == 0 else invp[k - 1]
                fe = 1
                b = f
                ee = e
                while ee:
                    if ee & 1:
                        fe = fe * b % M
                    b = b * b % M
                    ee >>= 1
                # multiply leaves [k, size) by fe
                node = 1
                lo = 0
                hi = size
                depth = 0
                while True:
                    if k <= lo:
                        seg[node] = seg[node] * fe % M
                        lazy[node] = lazy[node] * fe % M
                        break
                    if lazy[node] != 1:
                        lz = lazy[node]
                        lc, rc = 2 * node, 2 * node + 1
                        seg[lc] = seg[lc] * lz % M
                        lazy[lc] = lazy[lc] * lz % M
                        seg[rc] = seg[rc] * lz % M
                        lazy[rc] = lazy[rc] * lz % M
                        lazy[node] = 1
                    path[depth] = node
                    depth += 1
                    mid = (lo + hi) // 2
                    if k < mid:
                        rc = 2 * node + 1
                        seg[rc] = seg[rc] * fe % M
                        lazy[rc] = lazy[rc] * fe % M
                        node = 2 * node
                        hi = mid
                    else:
                        node = 2 * node + 1
                        lo = mid
                for i in range(depth - 1, -1, -1):
                    v = path[i]
                    seg[v] = (seg[2 * v] + seg[2 * v + 1]) % M
    return total


if __name__ == "__main__":
    assert solve(11, spf_sieve(11)) == 3132
    assert solve(1111, spf_sieve(1111)) == 706036312
    assert solve(111111, spf_sieve(111111)) == 22156169
    print(solve(N, spf_sieve(N)))  # 852950321
