"""Project Euler Problem 657: Incomplete Words.

A word over an alphabet of size alpha is incomplete if it misses at least one letter.
I(alpha, n) counts incomplete words of length <= n.  Find I(10^7, 10^12) mod 1e9+7.

By inclusion-exclusion over how many distinct letters are actually used,

    I(N, M) = sum_{i=0}^{N-1} (-1)^{N-1-i} C(N, i) * sum_{j=0}^{M} i^j,

since C(N, i) * sum_j i^j counts words restricted to some i-letter sub-alphabet.  The
geometric sum is (i^{M+1} - 1)/(i - 1) for i >= 2, equals M + 1 for i = 1, and equals
1 for i = 0.  Powers i^{M+1} are taken mod p with the exponent reduced mod p-1
(Fermat).  Checks: I(3,0)=1, I(3,2)=13, I(3,4)=79.
"""

import numba

P = 1_000_000_007


@numba.jit(cache=True)
def _mod_exp(base: int, exp: int, mod: int) -> int:
    base %= mod
    r = 1
    while exp:
        if exp & 1:
            r = r * base % mod
        base = base * base % mod
        exp >>= 1
    return r


@numba.jit(cache=True)
def _solve(N: int, M: int, p: int) -> int:
    inv = [0] * (N + 1)
    if N >= 1:
        inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (p - (p // i) * inv[p % i] % p) % p

    e = (M + 1) % (p - 1)  # exponent for i^{M+1} via Fermat
    ans = 0
    C = 1  # C(N, 0)
    for i in range(0, N):
        if i >= 1:
            C = C * ((N - i + 1) % p) % p * inv[i] % p
        if i == 0:
            g = 1
        elif i == 1:
            g = (M + 1) % p
        else:
            g = (_mod_exp(i, e, p) - 1) % p * inv[i - 1] % p
        term = C * g % p
        if (N - 1 - i) & 1:
            ans = (ans - term) % p
        else:
            ans = (ans + term) % p
    return ans % p


def count_incomplete(N: int, M: int) -> int:
    return int(_solve(N, M, P))


if __name__ == "__main__":
    assert count_incomplete(3, 0) == 1
    assert count_incomplete(3, 2) == 13
    assert count_incomplete(3, 4) == 79
    print(count_incomplete(10**7, 10**12))  # 219493139
