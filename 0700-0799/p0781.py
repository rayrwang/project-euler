"""
Project Euler Problem 781: Feynman Diagrams
https://projecteuler.net/problem=781

F(n) counts connected graphs with directed blue edges and undirected red
edges containing two degree-1 vertices -- a source with one outgoing and
a sink with one incoming blue edge -- and n degree-3 vertices, each with
one incoming blue edge, a different outgoing blue edge, and one red
edge.  Given F(4) = 5 and F(8) = 319, find F(50000) mod 10^9 + 7.

Structure.  Blue in- and out-degrees force the blue edges to form one
open path from source to sink (the spine, through k >= 0 internal
vertices) together with directed cycles of length >= 2 (no blue loops,
since the incoming and outgoing edges at a vertex must differ) covering
the other n - k vertices.  The red edges are a perfect matching on the
n internal vertices, so n is even.

Rigidity.  Diagrams are counted up to isomorphism, but every connected
diagram is rigid: an automorphism fixes source and sink (the unique
degree-1 vertices of each kind), hence the spine pointwise; a blue cycle
could a priori rotate or trade places with another, but each cycle
reaches the spine through a chain of red edges (connectivity), and a red
edge into an already-fixed vertex pins its other endpoint, so the
rigidity propagates outward and only the identity remains.  Therefore
F(n) = L(n)/n! where L counts vertex-labelled connected diagrams.  As a
check, the total count on 4 vertices is T(4) = (4-1)!! B(4) = 3 * 53 =
159 with B counting blue structures, and removing disconnected diagrams
via T_4 = L_4 + C(4,2) L_2 V_2 + V_4 with vacuum counts V_2 = 1,
V_4 = 27 gives L_4 = 120 = 5 * 4!, matching F(4) = 5.

Counting.  Every (not necessarily connected) diagram is one connected
spine diagram together with a vacuum diagram (blue derangement plus
matching) on the remaining vertices, so the exponential generating
functions satisfy T(x) = F(x) V(x), i.e. F = T / V as formal series.
With D the derangement numbers,

    t_i = B(i) (i-1)!! / i!,   B(i) = i! * sum_{j <= i} D(j)/j!
    v_i = D(i) (i-1)!! / i!,

(spine = sequence, EGF 1/(1-x); cycles of length >= 2 = derangements,
EGF e^(-x)/(1-x); the matching factor (i-1)!! is a Hadamard product),
and F(n) is the x^n coefficient of the quotient, an O(n^2/4) loop over
even indices modulo 10^9 + 7 -- under two seconds at n = 50000.
"""

import numpy as np
from numba import njit

MOD = 10**9 + 7
N = 50_000


@njit(cache=True)
def feynman(n):
    """F(n) mod MOD via the EGF quotient."""
    m = n + 1
    fact = np.empty(m, dtype=np.int64)
    fact[0] = 1
    for i in range(1, m):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = np.empty(m, dtype=np.int64)
    e = MOD - 2
    base = fact[m - 1]
    r = np.int64(1)
    while e:
        if e & 1:
            r = r * base % MOD
        base = base * base % MOD
        e >>= 1
    inv_fact[m - 1] = r
    for i in range(m - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    # derangement numbers
    der = np.empty(m, dtype=np.int64)
    der[0] = 1
    if m > 1:
        der[1] = 0
    for i in range(2, m):
        der[i] = (i - 1) * (der[i - 1] + der[i - 2]) % MOD
    # double factorial (i-1)!! for even i (matchings)
    dfac = np.zeros(m, dtype=np.int64)
    dfac[0] = 1
    for i in range(2, m, 2):
        dfac[i] = dfac[i - 2] * (i - 1) % MOD
    # EGF coefficients t (all diagrams) and v (vacuum diagrams)
    s = np.int64(0)
    t = np.zeros(m, dtype=np.int64)
    v = np.zeros(m, dtype=np.int64)
    for i in range(m):
        s = (s + der[i] * inv_fact[i]) % MOD
        if i % 2 == 0:
            t[i] = s * dfac[i] % MOD
            v[i] = der[i] * inv_fact[i] % MOD * dfac[i] % MOD
    # series quotient ell = t / v over even indices (v[0] = 1)
    ell = np.zeros(m, dtype=np.int64)
    for i in range(0, m, 2):
        acc = t[i]
        for j in range(2, i + 1, 2):
            acc = (acc - v[j] * ell[i - j]) % MOD
        acc %= MOD
        if acc < 0:
            acc += MOD
        ell[i] = acc
    return ell[n]


def main():
    assert feynman(2) == 1
    assert feynman(4) == 5
    assert feynman(8) == 319
    return int(feynman(N))


if __name__ == "__main__":
    print(main())  # 162450870
