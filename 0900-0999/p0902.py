"""Project Euler 902: Permutation Powers.

sigma consists of disjoint cycles of lengths 1..m (one per triangular
block), and pi = tau^-1 sigma tau is conjugate to it, so pi has order
L = lcm(1..m), which divides m!.  Hence

    P(m) = (m!/L) * sum_{k=1..L} rank(pi^k).

With the Lehmer code, rank(rho) - 1 = sum_i c_i (n-i)! where
c_i = #{j > i : rho(j) < rho(i)}, so the inner sum becomes a sum over
ordered element pairs.  Writing a = tau(i), b = tau(j) and
w = tau^-1, the condition pi^k(j) < pi^k(i) is w(sigma^k b) < w(sigma^k a).
If a, b live in sigma-cycles of lengths p, q (g = gcd, l = lcm), the pair
of rotation offsets (k mod p, k mod q) sweeps each compatible pair once
per l steps, so the count over k in [1, L] is (L/l) times a count C(d)
depending only on the offset difference d = (alpha - beta) mod g:

    C(d) = #{(u, v): u - v = d (mod g), w(B[v]) < w(A[u])}.

Each ordered cycle pair is handled with two O(pq) double loops (one to
build C, one to accumulate (n - w(a))! * C(d) over pairs with
w(a) < w(b)); same-cycle pairs use the analogous shift table D(delta).
Total work is ~2 n^2 = 5.1e7 simple operations.  All divisions by l are
exact integers, so they are done with modular inverses.  Verified against
direct enumeration for P(2) = 4, P(3) = 780, P(4) = 38810300.
"""

from math import gcd, lcm

import numba
import numpy as np

MOD = 10**9 + 7


@numba.njit(cache=True)
def cross_pair(wa_arr: np.ndarray, wb_arr: np.ndarray, g: int,
               factn: np.ndarray, cbuf: np.ndarray, modulus: int) -> int:
    p, q = len(wa_arr), len(wb_arr)
    cbuf[:] = 0
    for u in range(p):
        wa = wa_arr[u]
        for v in range(q):
            if wb_arr[v] < wa:
                cbuf[(u - v) % g] += 1
    acc = 0
    for a in range(p):
        wa = wa_arr[a]
        fa = factn[wa]
        for b in range(q):
            if wa < wb_arr[b]:
                acc = (acc + fa * cbuf[(a - b) % g]) % modulus
    return acc


@numba.njit(cache=True)
def same_pair(wa_arr: np.ndarray, factn: np.ndarray, dbuf: np.ndarray,
              modulus: int) -> int:
    p = len(wa_arr)
    dbuf[:] = 0
    for d in range(1, p):
        for u in range(p):
            if wa_arr[(u + d) % p] < wa_arr[u]:
                dbuf[d] += 1
    acc = 0
    for a in range(p):
        wa = wa_arr[a]
        fa = factn[wa]
        for b in range(p):
            if a != b and wa < wa_arr[b]:
                acc = (acc + fa * dbuf[(b - a) % p]) % modulus
    return acc


def solve(m: int) -> int:
    n = m * (m + 1) // 2
    tau = [(MOD * i) % n + 1 for i in range(n + 1)]
    tinv = [0] * (n + 1)
    for i in range(1, n + 1):
        tinv[tau[i]] = i

    # sigma-cycles listed in sigma order; store w = tau^-1 of each element
    cycles = []
    for k in range(1, m + 1):
        start = k * (k - 1) // 2 + 1
        cycles.append(
            np.array([tinv[x] for x in range(start, start + k)],
                     dtype=np.int64))

    facts = [1] * (n + 1)
    for i in range(1, n + 1):
        facts[i] = facts[i - 1] * i % MOD
    factn = np.zeros(n + 1, dtype=np.int64)  # factn[w] = (n - w)!
    for w in range(1, n + 1):
        factn[w] = facts[n - w]

    mfact = 1
    for i in range(1, m + 1):
        mfact = mfact * i % MOD

    total = mfact  # the "+1" of each of the m! ranks
    buf = np.zeros(n + 1, dtype=np.int64)
    for ai in range(m):
        wa_arr = cycles[ai]
        p = len(wa_arr)
        acc = same_pair(wa_arr, factn, buf[:p], MOD)
        total = (total + acc * mfact % MOD * pow(p, MOD - 2, MOD)) % MOD
        for bi in range(m):
            if bi == ai:
                continue
            wb_arr = cycles[bi]
            q = len(wb_arr)
            g = gcd(p, q)
            acc = cross_pair(wa_arr, wb_arr, g, factn, buf[:g], MOD)
            inv_l = pow(lcm(p, q), MOD - 2, MOD)
            total = (total + acc * mfact % MOD * inv_l) % MOD
    return total


if __name__ == "__main__":
    assert solve(2) == 4
    assert solve(3) == 780
    assert solve(4) == 38810300
    print(solve(100))  # 343557869
