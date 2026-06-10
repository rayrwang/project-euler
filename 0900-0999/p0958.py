"""Project Euler 958: Euclid's Labour.

The subtractive Euclidean algorithm on coprime (n, m) takes
(sum of the partial quotients of n/m) - 1 steps, so f(n) is the m minimizing
the quotient sum, ties broken by smaller m. Writing the continued fraction
n/m = [a_0; a_1, ..., a_r], n is the continuant K(a_0..a_r) and
m = K(a_1..a_r); a coprime pair determines its digit sequence, so the
quotient sum of any pair is one Euclid run.

Search over digit sequences, split at the first prefix continuant
p = K(a_0..a_j) >= T ~ sqrt(n). The prefix matrix [[p, p'], [q, q']]
(p' = K(a_0..a_{j-1}), q = K(a_1..a_j), q' = K(a_1..a_{j-1})) satisfies
n = p u + p' v and m = q u + q' v, where (u, v) is the suffix continuant
pair. Given a prefix, u is fixed modulo p' inside [n/(p+p'), n/p] -- an
interval of width ~ n p'/p^2, so about one candidate -- and v follows.
The DFS over prefixes uses three prunings:
  * budget: F(t+1) u_min must reach n, where t is the remaining digit sum
    (for a fixed quotient sum the continuant is maximized by all ones);
  * branch & bound against the best (sum, m) so far, warm-started by
    scanning m near n/phi (nearly-all-ones expansions);
  * an m-prune: within a subtree m >= q ceil(n/(p + p')), so once the
    optimal sum is locked, subtrees that cannot lower m die -- this is what
    makes the tie-breaking phase cheap.
Each solution m also yields its reversed-CF partner (m^{-1} or n - m^{-1}
mod n) with the same quotient sum, collapsing best-m early.

Verified against an exhaustive IDDFS for dozens of random n up to 3 * 10^6
and against the given f(7) = 2, f(89) = 34, f(8191) = 1856. The run for
10^12 + 39 takes a few minutes.
"""

import numba
import numpy as np

FIB = [0, 1]
while len(FIB) < 91:
    FIB.append(FIB[-1] + FIB[-2])
FIB_ARR = np.array(FIB, dtype=np.int64)


@numba.njit(cache=True)
def qsum(u, v):
    s = 0
    while v:
        s += u // v
        u, v = v, u % v
    return s if u == 1 else -(10**9)


@numba.njit(cache=True)
def modinv(a, m):
    g, x = m, 0
    r, s = a % m, 1
    while r:
        q = g // r
        g, r = r, g - q * r
        x, s = s, x - q * s
    return x % m


@numba.njit(cache=True)
def try_update(n, m, best):
    """Try m and its reversal partners; update best (sum, m)."""
    if m < 1 or m >= n:
        return
    s = qsum(n, m)
    if s < 0:
        return
    if s < best[0] or (s == best[0] and m < best[1]):
        best[0], best[1] = s, m
    w = modinv(m % n, n)
    for cand in (w, n - w):
        if 1 <= cand < n:
            s2 = qsum(n, cand)
            if s2 >= 0 and (s2 < best[0] or (s2 == best[0] and cand < best[1])):
                best[0], best[1] = s2, cand


@numba.njit(cache=True)
def warm_start(n, width, best):
    phi_inv = (5**0.5 - 1) / 2
    m0 = int(n * phi_inv)
    lo = max(1, m0 - width)
    hi = min(n - 1, m0 + width)
    for m in range(lo, hi + 1):
        s = qsum(n, m)
        if s > 0 and s <= best[0]:
            try_update(n, m, best)


@numba.njit(cache=True)
def dfs(n, t_thresh, fib, p, pp, q, qp, s1, best):
    if p >= t_thresh:
        if pp == 0:
            if p == n:
                try_update(n, q, best)
            return
        ulo = (n + p + pp - 1) // (p + pp)
        uhi = n // p
        if ulo > uhi:
            return
        if pp == 1:
            u = ulo
        else:
            inv = modinv(p % pp, pp)
            u = ulo + ((n % pp) * inv % pp - ulo % pp) % pp
        while u <= uhi:
            v = (n - p * u) // pp
            if 0 <= v and (v < u or (v == 1 and u == 1)):
                s2 = qsum(u, v)
                if s2 >= 0 and s1 + s2 <= best[0]:
                    try_update(n, q * u + qp * v, best)
            if pp > 1:
                u += pp
            else:
                u += 1
        return
    t = 1
    a = 1
    while True:
        p2 = a * p + pp
        if p2 > n:
            break
        s = s1 + a
        if s > best[0]:
            break
        target = (n + p2 + p - 1) // (p2 + p)
        while t > 1 and fib[t] >= target:
            t -= 1
        while fib[t + 1] < target:
            t += 1
        if s + t <= best[0]:
            # m-prune: in this subtree m >= q2 * ceil(n / (p2 + p))
            q2 = a * q + qp
            if s + t < best[0] or q2 * target < best[1]:
                dfs(n, t_thresh, fib, p2, p, q2, q, s, best)
        a += 1
    return


def f_fast(n):
    t_thresh = max(2, int(n**0.5))
    best = np.array([2**40, 2**62], dtype=np.int64)
    warm_start(n, 200000, best)
    dfs(n, t_thresh, FIB_ARR, 1, 0, 0, 1, 0, best)
    return int(best[0]) - 1, int(best[1])


if __name__ == "__main__":
    print(f_fast(10**12 + 39)[1])  # 367554579311
