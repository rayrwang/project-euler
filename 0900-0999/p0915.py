"""Project Euler 915: Giant GCDs.

Write t(n) = s(n) - 1, so t(1) = 0 and t(n+1) = t(n)^3 + 1.  Since
t^3 + 1 = (t + 1)(t^2 - t + 1), s(n) = t(n) + 1 divides t(n+1), i.e.
t(n+1) = 0 = t(1) (mod s(n)); as both sides follow the same recurrence,
t(n + j) = t(j) (mod s(n)) for all j >= 1.  Hence for m > n,
gcd(s(m), s(n)) = gcd(t(m - n) + 1, s(n)) = gcd(s(m - n), s(n)), and
subtractive Euclid gives the divisibility-sequence identity

    gcd(s(m), s(n)) = s(gcd(m, n))     (verified exactly for m, n <= 8).

Applying it twice, gcd(s(s(a)), s(s(b))) = s(s(gcd(a, b))), so with
Phi(x) = sum_{k <= x} phi(k) (the number of pairs with gcd exactly g
being 2 Phi(N//g) - 1),

    T(N) = sum_{g <= N} s(s(g)) (2 Phi(N//g) - 1)   mod M.

M = 123456789 = 9 * 3607 * 3803, so s(s(g)) mod M follows by CRT from
each prime-power factor q.  Modulo q the map x -> x^3 + 1 has a tiny
orbit from t(1) = 0 (preperiod rho, period pi) = (0, 3), (53, 35),
(0, 963); for the giant index s(g) (g >= 7 guarantees s(g) > rho + 1)
only s(g) mod pi_q is needed, which iterates the same recurrence modulo
pi_q.  A single pass over g = 1..N carries t(g) modulo the three
periods and accumulates the weighted sum; weights use a phi sieve for
v <= sqrt(N) and the sublinear recursion
Phi(x) = x(x+1)/2 - sum_{d >= 2} Phi(x//d) for the large arguments.
The given T(3) = 12, T(4) = 24881925 and T(100) = 14416749 are all
reproduced.
"""

import numba
import numpy as np

M = 123456789
FACTORS = [9, 3607, 3803]


def _orbit(q: int):
    pos: dict[int, int] = {}
    vals: list[int] = []
    x, i = 0, 0
    while x not in pos:
        pos[x] = i
        vals.append(x)
        x = (x**3 + 1) % q
        i += 1
    return np.array(vals, dtype=np.int64), pos[x], i - pos[x]


def _phi_tables(n: int, v0: int):
    """bigW[g] = 2 Phi(n//g) - 1 for g <= v0;  PhiS[v] = Phi(v) mod M."""
    sieve_lim = min(5 * 10**6, max(1000, n))
    phi = np.arange(sieve_lim + 1, dtype=np.int64)
    for p in range(2, sieve_lim + 1):
        if phi[p] == p:
            phi[p::p] -= phi[p::p] // p
    phi_exact = np.cumsum(phi.astype(object))
    cache: dict[int, int] = {}

    def phi_sum(x: int) -> int:
        if x <= sieve_lim:
            return int(phi_exact[x])
        if x in cache:
            return cache[x]
        res = x * (x + 1) // 2
        d = 2
        while d <= x:
            v = x // d
            d2 = x // v
            res -= (d2 - d + 1) * phi_sum(v)
            d = d2 + 1
        cache[x] = res
        return res

    big_w = np.zeros(v0 + 1, dtype=np.int64)
    for g in range(1, v0 + 1):
        big_w[g] = (2 * (phi_sum(n // g) % M) - 1) % M
    phi_s = np.zeros(v0 + 1, dtype=np.int64)
    for v in range(1, v0 + 1):
        phi_s[v] = int(phi_exact[v]) % M
    return big_w, phi_s


@numba.njit(cache=True)
def _main_loop(n, v0, big_w, phi_s,
               vals9, rho9, pi9, c9,
               vals1, rho1, pi1, c1,
               vals2, rho2, pi2, c2,
               ssg_small):
    ans = 0
    y9 = y1 = y2 = 0  # t(g) mod pi_q, starting at g = 1
    for g in range(1, n + 1):
        if g <= 6:
            ssg = ssg_small[g]
        else:
            r9 = (vals9[rho9 + (y9 - rho9) % pi9] + 1) % 9
            r1 = (vals1[rho1 + (y1 - rho1) % pi1] + 1) % 3607
            r2 = (vals2[rho2 + (y2 - rho2) % pi2] + 1) % 3803
            ssg = (r9 * c9 + r1 * c1 + r2 * c2) % M
        w = big_w[g] if g <= v0 else (2 * phi_s[n // g] - 1) % M
        ans = (ans + w * ssg) % M
        y9 = (y9 * y9 % pi9 * y9 + 1) % pi9
        y1 = (y1 * y1 % pi1 * y1 + 1) % pi1
        y2 = (y2 * y2 % pi2 * y2 + 1) % pi2
    return ans


def solve(n: int) -> int:
    v0 = int(n**0.5)
    while (v0 + 1) * (v0 + 1) <= n:
        v0 += 1
    big_w, phi_s = _phi_tables(n, v0)
    orbs = {q: _orbit(q) for q in FACTORS}
    cs = {}
    for q in FACTORS:
        mq = M // q
        cs[q] = mq * pow(mq, -1, q) % M

    s = [0, 1]
    for _ in range(1, 12):
        s.append((s[-1] - 1) ** 3 + 2)

    def t_mod(idx: int, q: int) -> int:
        vals, rho, pi = orbs[q]
        i = idx - 1
        return int(vals[i]) if i < rho else int(vals[rho + (i - rho) % pi])

    ssg_small = np.zeros(7, dtype=np.int64)
    for g in range(1, 7):
        x = 0
        for q in FACTORS:
            x = (x + ((t_mod(s[g], q) + 1) % q) * cs[q]) % M
        ssg_small[g] = x

    v9, r9, p9 = orbs[9]
    v1, r1, p1 = orbs[3607]
    v2, r2, p2 = orbs[3803]
    return int(_main_loop(n, v0, big_w, phi_s,
                          v9, r9, p9, cs[9],
                          v1, r1, p1, cs[3607],
                          v2, r2, p2, cs[3803],
                          ssg_small))


if __name__ == "__main__":
    from math import gcd

    s = [0, 1]
    for _ in range(1, 10):
        s.append((s[-1] - 1) ** 3 + 2)
    for m in range(1, 9):
        for k in range(1, 9):
            assert gcd(s[m], s[k]) == s[gcd(m, k)]
    assert solve(3) == 12
    assert solve(4) == 24881925
    assert solve(100) == 14416749
    print(solve(10**8))  # 55601924
