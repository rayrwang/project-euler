"""Project Euler Problem 625: Gcd Sum.

G(N) = sum_{j=1}^N sum_{i=1}^j gcd(i, j).  Find G(10^11) mod 998244353.

Using gcd(i, j) = sum_{d | i, d | j} phi(d) and grouping pairs by d (i = d a, j = d b
with 1 <= a <= b <= floor(N/d)):

    G(N) = sum_{d>=1} phi(d) * T(floor(N/d)),   T(m) = m(m+1)/2.

Group d by the value M = floor(N/d): each block contributes T(M) * (Phi(hi) -
Phi(lo-1)), where Phi is the summatory totient.  Phi is evaluated at the O(sqrt N)
points floor(N/d) by the standard recurrence

    Phi(v) = T(v) - sum_{d>=2} Phi(floor(v/d)),

computed bottom-up over the values floor(N/i) (small arguments from a sieve), all
modulo the prime 998244353.  Checks: G(10)=122, G(1000)=2475190, G(10^4)=317257140.
"""

import numpy as np
import numba

from funcs import totient_sieve

MOD = 998244353


@numba.jit(cache=True)
def _tri_mod(v: int) -> int:
    if v % 2 == 0:
        return ((v // 2) % MOD) * ((v + 1) % MOD) % MOD
    return (v % MOD) * (((v + 1) // 2) % MOD) % MOD


@numba.jit(cache=True)
def _isqrt(n: int) -> int:
    x = int(n**0.5)
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@numba.jit(cache=True)
def _solve(N: int, small: np.ndarray) -> int:
    L = small.shape[0] - 1
    large = np.zeros(L + 1, dtype=np.int64)
    for i in range(L, 0, -1):
        v = N // i
        cur = _tri_mod(v)
        d = 2
        while d <= v:
            q = v // d
            d2 = v // q
            phiq = small[q] if q <= L else large[N // q]
            cur = (cur - ((d2 - d + 1) % MOD) * phiq) % MOD
            d = d2 + 1
        large[i] = cur % MOD

    G = 0
    d = 1
    while d <= N:
        M = N // d
        hi = N // M
        phi_hi = small[hi] if hi <= L else large[N // hi]
        lo = d - 1
        phi_lo = small[lo] if lo <= L else large[N // lo]
        G = (G + _tri_mod(M) * ((phi_hi - phi_lo) % MOD)) % MOD
        d = hi + 1
    return G % MOD


def G(N: int) -> int:
    L = _isqrt(N)
    phi = totient_sieve(L + 1)
    small = np.zeros(L + 1, dtype=np.int64)
    run = 0
    for i in range(1, L + 1):
        run = (run + int(phi[i])) % MOD
        small[i] = run
    return int(_solve(N, small)) % MOD


if __name__ == "__main__":
    assert G(10) == 122, G(10)
    assert G(1000) == 2475190, G(1000)
    assert G(10**4) == 317257140, G(10**4)
    print(G(10**11))  # 551614306
