"""Project Euler Problem 994: Counting Triangles.

Segments join every bottom point ``(i, 1)``, ``1 <= i <= m``, to every top
point ``(j, 2)``, ``1 <= j <= n``; ``T(m, n)`` counts all triangles in the
picture, including those cut by other segments.  Given ``T(2,3) = 8``,
``T(3,5) = 146`` and ``T(12,23) = 756716``, find
``T(1234*10^8, 2345*10^8) mod 10^9 + 7``.

Classifying triangles by their three segments
---------------------------------------------
Two segments meet in at most one point: at a shared bottom endpoint, a shared
top endpoint, or a proper crossing (bottoms and tops in opposite order).
Three segments form a triangle iff they pairwise meet in three *distinct*
points, giving four shapes:

* apex at a bottom point: two segments share a bottom point, a third crosses
  both -- counting the valid orderings gives ``2 C(m,2) C(n,3)``;
* apex at a top point, symmetrically: ``2 C(n,2) C(m,3)``;
* one bottom apex and one top apex plus a crossing: choosing two bottoms and
  two tops yields exactly two such triangles, ``2 C(m,2) C(n,2)``;
* three pairwise crossings: bottoms increasing forces tops decreasing, so
  ``C(m,3) C(n,3)`` triples -- *minus* those whose three segments pass
  through a common point and enclose no area.

Concurrent triples
------------------
For bottoms ``a1 < a2 < a3`` and tops ``b1 > b2 > b3`` the three segments are
concurrent iff ``(a2-a1)(b2-b3) = (a3-a2)(b1-b2)``.  Writing the gaps as
``u, v`` (bottoms) and ``s, w`` (tops), the condition ``u w = v s`` is
parametrised exactly by ``u = alpha k, v = beta k, s = alpha l, w = beta l``
with ``gcd(alpha, beta) = 1``.  Grouping by ``c = alpha + beta`` (there are
``phi(c)`` coprime pairs for each ``c >= 2``) the concurrency count is

    X = sum_{c >= 2} phi(c) A_m(c) A_n(c),
    A_M(c) = sum_{k >= 1, ck <= M-1} (M - ck) = M K - c K(K+1)/2,

with ``K = floor((M-1)/c)``, and ``T = 2C(m,2)C(n,3) + 2C(n,2)C(m,3) +
2C(m,2)C(n,2) + C(m,3)C(n,3) - X``.  This reproduces all three given values
exactly.

Evaluating X for m, n ~ 2 * 10^11
---------------------------------
Group ``c`` into blocks where ``K_m = floor((m-1)/c)`` and
``K_n = floor((n-1)/c)`` are both constant (about ``2(sqrt m + sqrt n)``
blocks); inside a block ``A_m A_n`` is a quadratic polynomial in ``c``, so
each block needs the partial sums ``Phi_j(N) = sum_{c <= N} phi(c) c^j`` for
``j = 0, 1, 2`` at block edges.  Since ``sum_{c | t} phi(c) = t``,

    sum_{e >= 1} e^j Phi_j(floor(N/e)) = sum_{t <= N} t^{j+1},

giving the Mertens-style recursion ``Phi_j(N) = S_{j+1}(N) -
sum_{e >= 2} e^j Phi_j(floor(N/e))``.  A linear sieve supplies ``Phi_j`` up
to ``B ~ 2.4 * 10^7`` (stored as mod-p prefix arrays); the recursion,
evaluated bottom-up over the quotient sets of ``m-1`` and ``n-1`` (closed
under nested floor division), supplies the rest in ``O(N^(2/3))`` total.
Both the recursion and the block sweep were validated against a brute-force
``phi`` table, including with tiny ``B`` to exercise every code path.
"""

from __future__ import annotations

import numpy as np
from numba import njit

P = 10**9 + 7
INV2 = pow(2, P - 2, P)
INV6 = pow(6, P - 2, P)


@njit(cache=True)
def _phi_prefix(B: int, p: int) -> np.ndarray:
    """F[j][x] = Phi_j(x) mod p for x <= B, j = 0, 1, 2."""
    phi = np.arange(B + 1, dtype=np.int64)
    for i in range(2, B + 1):
        if phi[i] == i:  # prime
            for j in range(i, B + 1, i):
                phi[j] -= phi[j] // i
    F = np.zeros((3, B + 1), dtype=np.uint32)
    a0 = a1 = a2 = 0
    for c in range(1, B + 1):
        f = phi[c] % p
        cm = c % p
        a0 = (a0 + f) % p
        t = f * cm % p
        a1 = (a1 + t) % p
        a2 = (a2 + t * cm) % p
        F[0, c] = a0
        F[1, c] = a1
        F[2, c] = a2
    return F


@njit(cache=True, inline="always")
def _S(n: int, j: int, p: int, inv2: int, inv6: int) -> int:
    """sum_{t<=n} t^j mod p for j = 1, 2, 3."""
    nm = n % p
    n1 = (n + 1) % p
    if j == 1:
        return nm * n1 % p * inv2 % p
    if j == 2:
        return nm * n1 % p * ((2 * n + 1) % p) % p * inv6 % p
    t = nm * n1 % p * inv2 % p
    return t * t % p


@njit(cache=True)
def _big_phi(
    M1: int, B: int, F: np.ndarray, p: int, inv2: int, inv6: int
) -> np.ndarray:
    """G[j][k] = Phi_j(M1 // k) mod p for every k with M1 // k > B."""
    kmax = 0
    if M1 > B:
        kmax = M1 // (B + 1)
        while kmax >= 1 and M1 // kmax <= B:
            kmax -= 1
    G = np.zeros((3, kmax + 2), dtype=np.int64)
    for k in range(kmax, 0, -1):
        v = M1 // k
        g0 = _S(v, 1, p, inv2, inv6)
        g1 = _S(v, 2, p, inv2, inv6)
        g2 = _S(v, 3, p, inv2, inv6)
        e = 2
        while e <= v:
            q = v // e
            e2 = v // q
            s0 = (e2 - e + 1) % p
            s1 = (_S(e2, 1, p, inv2, inv6) - _S(e - 1, 1, p, inv2, inv6)) % p
            s2 = (_S(e2, 2, p, inv2, inv6) - _S(e - 1, 2, p, inv2, inv6)) % p
            if q <= B:
                h0 = np.int64(F[0, q])
                h1 = np.int64(F[1, q])
                h2 = np.int64(F[2, q])
            else:
                kk = M1 // q
                h0 = G[0, kk]
                h1 = G[1, kk]
                h2 = G[2, kk]
            g0 = (g0 - s0 * h0) % p
            g1 = (g1 - s1 * h1) % p
            g2 = (g2 - s2 * h2) % p
            e = e2 + 1
        G[0, k] = g0 % p
        G[1, k] = g1 % p
        G[2, k] = g2 % p
    return G


@njit(cache=True)
def _concurrent(
    m: int,
    n: int,
    B: int,
    F: np.ndarray,
    Gm: np.ndarray,
    Gn: np.ndarray,
    p: int,
    inv2: int,
    inv6: int,
) -> int:
    """X = sum_{c>=2} phi(c) A_m(c) A_n(c) mod p, by constant-(K_m, K_n) blocks."""
    M1 = m - 1
    N1 = n - 1
    C = min(M1, N1)
    mm = m % p
    nn = n % p
    X = 0
    c = 2
    p0 = np.int64(F[0, 1])
    p1 = np.int64(F[1, 1])
    p2 = np.int64(F[2, 1])
    while c <= C:
        Km = M1 // c
        Kn = N1 // c
        r = min(M1 // Km, N1 // Kn)
        if r > C:
            r = C
        if r <= B:
            q0 = np.int64(F[0, r])
            q1 = np.int64(F[1, r])
            q2 = np.int64(F[2, r])
        else:
            k = M1 // r
            if M1 // k == r:
                q0 = Gm[0, k]
                q1 = Gm[1, k]
                q2 = Gm[2, k]
            else:
                k = N1 // r
                q0 = Gn[0, k]
                q1 = Gn[1, k]
                q2 = Gn[2, k]
        d0 = (q0 - p0) % p
        d1 = (q1 - p1) % p
        d2 = (q2 - p2) % p
        Kmp = Km % p
        Knp = Kn % p
        alpha = mm * Kmp % p
        gamma = Kmp * ((Km + 1) % p) % p * inv2 % p
        beta = nn * Knp % p
        delta = Knp * ((Kn + 1) % p) % p * inv2 % p
        t0 = alpha * beta % p
        t1 = (alpha * delta + beta * gamma) % p
        t2 = gamma * delta % p
        X = (X + t0 * d0 - t1 * d1 + t2 * d2) % p
        p0, p1, p2 = q0, q1, q2
        c = r + 1
    return int(X % p)


def triangles(m: int, n: int) -> int:
    """T(m, n) mod P."""
    B = min(24_000_000, max(1000, max(m, n)))
    F = _phi_prefix(B, P)
    Gm = _big_phi(m - 1, B, F, P, INV2, INV6)
    Gn = _big_phi(n - 1, B, F, P, INV2, INV6)
    X = int(_concurrent(m, n, B, F, Gm, Gn, P, INV2, INV6))

    def c2(x: int) -> int:
        return x % P * ((x - 1) % P) % P * INV2 % P

    def c3(x: int) -> int:
        return x % P * ((x - 1) % P) % P * ((x - 2) % P) % P * INV6 % P

    return (
        2 * c2(m) * c3(n) + 2 * c2(n) * c3(m) + 2 * c2(m) * c2(n) + c3(m) * c3(n) - X
    ) % P


if __name__ == "__main__":
    assert triangles(2, 3) == 8, "checkpoint T(2,3)"
    assert triangles(3, 5) == 146, "checkpoint T(3,5)"
    assert triangles(12, 23) == 756716, "checkpoint T(12,23)"
    print(triangles(1234 * 10**8, 2345 * 10**8))  # 350247268
