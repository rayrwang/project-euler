"""Project Euler 903: Total Permutation Powers.

Using the Lehmer code, rank(rho) - 1 = sum_{i<j} [rho(j) < rho(i)] (n-i)!,
so Q(n) - n!^2 is a sum over position pairs (i, j) and (pi, k) of the
indicator [pi^k(j) < pi^k(i)].  Conjugating pi by the transposition (i j)
is an involution that swaps the two image values whenever both lie outside
{i, j}, so that bulk contributes exactly half.  The boundary cases are
controlled by four counts (sums over k = 1..n! of the number of pi with):

    a: pi^k fixes i and j           b: pi^k swaps i and j
    c: pi^k fixes i, moves j        d: pi^k(i) = j, pi^k(j) not in {i,j}

and within c and d the free image value is equidistributed over the n - 2
remaining values (conjugate by transpositions of outside values).  The key
enumeration fact: the number of permutations with prescribed "cycle of i
has length l with j at offset t" or "i in an l-cycle, j in a separate
m-cycle" is exactly (n-2)! in every case.  Together with
#{k <= n! : d | k} = n!/d this gives

    A = (n-2)! n! [ S_lcm + sum_l (l-1)/l ]      (l | k and m | k)
    B = (n-2)! n! sum_{l even} 1/l               (l | 2k, l !| k)
    C = (n-2)! n! [ sum_{l+m<=n} 1/l - S_lcm ]   (l | k, m !| k)
    D = (n-2)! n! [ n - H(n) - H(n/2)/2 ]        (l !| 2k)

where S_lcm = sum_{l+m<=n} 1/lcm(l, m).  Substituting lcm = l m / gcd and
Mobius-inverting the coprimality condition collapses S_lcm to

    S_lcm = sum_e (phi(e)/e^2) G(n//e),  G(M) = sum_{a+b<=M} 1/(ab),

with G evaluated only at the O(sqrt n) distinct values of n//e via a
harmonic-number convolution.  The per-pair weight depends only on j - i,
so the final assembly over (i, j) is a single O(n) loop.  All divisions
are exact over the integers and are done with modular inverses.  Verified
against full enumeration for n = 3..7 and the given Q(10).
"""

import numpy as np

P = 10**9 + 7


def solve(n: int) -> int:
    if n < 3:  # Q(2) = 5; the (n-2) denominator needs n >= 3
        return [0, 1, 5][n]
    size = n + 1
    inv = np.zeros(size, dtype=np.int64)
    inv[1] = 1
    for i in range(2, size):
        inv[i] = (P - (P // i) * inv[P % i]) % P
    harm = np.zeros(size, dtype=np.int64)  # harm[x] = sum_{b<=x} 1/b
    for i in range(1, size):
        harm[i] = (harm[i - 1] + inv[i]) % P

    fact = [1] * size
    for i in range(1, size):
        fact[i] = fact[i - 1] * i % P
    nfact = fact[n]
    nf2 = nfact * nfact % P

    phi = np.arange(size, dtype=np.int64)
    for p in range(2, size):
        if phi[p] == p:
            phi[p::p] -= phi[p::p] // p

    g_cache: dict[int, int] = {}

    def g_sum(m: int) -> int:
        """G(M) = sum_{a+b<=M} 1/(ab) = sum_a (1/a) H(M-a)."""
        if m not in g_cache:
            if m < 2:
                g_cache[m] = 0
            else:
                g_cache[m] = int(
                    (inv[1:m] * harm[m - 1:0:-1] % P).sum() % P)
        return g_cache[m]

    s_lcm = 0  # sum_{l+m<=n} 1/lcm(l,m)
    for e in range(1, n + 1):
        m = n // e
        if m < 2:
            break
        s_lcm = (s_lcm + phi[e] % P * inv[e] % P * inv[e] % P
                 * g_sum(m)) % P

    s_l = ((n % P) * harm[n - 1] - (n - 1)) % P  # sum_{l+m<=n} 1/l

    pref = fact[n - 2] * nfact % P
    aa = pref * ((s_lcm + n - harm[n]) % P) % P
    bb = pref * (inv[2] * harm[n // 2] % P) % P
    cc = pref * ((s_l - s_lcm) % P) % P
    dd = pref * ((n - harm[n] - inv[2] * harm[n // 2]) % P) % P

    inv_n2 = pow(n - 2, P - 2, P)
    bulk = ((nf2 - aa - bb - 2 * cc - 2 * dd) % P) * inv[2] % P
    bulk = (bulk + bb) % P

    total = nf2
    for r in range(1, n):  # r = n - i
        half = (r * (r + 1) // 2) % P
        rm = r % P
        cu = (rm * ((n - 1) % P) - half) % P
        dv = (rm * ((n - 3) % P) + half) % P
        term = (rm * bulk + (cc * cu + dd * dv) % P * inv_n2) % P
        total = (total + fact[r] * term) % P
    return total % P


if __name__ == "__main__":
    assert solve(3) == 88
    assert solve(6) == 133103808
    assert solve(10) == 468421536
    print(solve(10**6))  # 128553191
