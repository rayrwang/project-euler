"""Problem 440: GCD and Tiling.

T(n) counts tilings of a 1 x n board by dominoes and digit-bearing unit
squares, so T(n) = 10 T(n-1) + T(n-2) with T(0) = 1: that is the Lucas
sequence U(P=10, Q=-1) shifted by one, T(n) = U_{n+1}. Lucas U with
coprime parameters is a strong divisibility sequence,
gcd(U_m, U_n) = U_{gcd(m, n)}, hence
    gcd(T(c^a), T(c^b)) = U_{gcd(c^a + 1, c^b + 1)},
and the inner gcd is classical: with g = gcd(a, b) it equals c^g + 1
when a/g and b/g are both odd, and otherwise 2 (c odd) or 1 (c even).
So S(L) needs (i) the counts podd(L/g) of coprime odd pairs, by a
Mobius sum over odd d, and (ii) U_{c^g + 1} mod 987898789 for every c,
g <= L, walked as a chain of matrix powers Q^{c^g} = (Q^{c^{g-1}})^c
on the pair (U_k, U_{k+1}).
"""

from math import gcd

import numba
import numpy as np

MOD = 987898789

@numba.jit(cache=True)
def pair_mul(a0, a1, b0, b1, mod):
    """(U_m, U_{m+1}) x (U_n, U_{n+1}) -> (U_{m+n}, U_{m+n+1})
    via U_{m+n} = U_m U_{n+1} + U_{m-1} U_n, U_{m-1} = U_{m+1} - 10 U_m."""
    am1 = (a1 - 10 * a0) % mod
    c0 = (a0 * b1 + am1 * b0) % mod
    c1 = (a1 * b1 + a0 * b0) % mod
    return c0, c1

@numba.jit(cache=True)
def pair_pow(p0, p1, e, mod):
    """(U_k, U_{k+1}) -> (U_{ke}, U_{ke+1})."""
    r0, r1 = 0, 1  # U_0, U_1
    while e:
        if e & 1:
            r0, r1 = pair_mul(r0, r1, p0, p1, mod)
        p0, p1 = pair_mul(p0, p1, p0, p1, mod)
        e >>= 1
    return r0, r1

@numba.jit(cache=True)
def total_sum(limit: int, podd: np.ndarray, mod: int) -> int:
    """S(L) mod `mod`: podd[g] = #pairs (a,b)<=L with gcd g, both
    quotients odd."""
    rest = limit * limit
    for g in range(1, limit + 1):
        rest -= podd[g]
    total = 0
    for c in range(1, limit + 1):
        # chain (U_{c^g}, U_{c^g+1}) over g = 1..L
        p0, p1 = 0, 1
        # start: exponent c^1: power the base pair (U_1, U_2) by c
        p0, p1 = pair_pow(1, 10 % mod, c, mod)
        contrib = 0
        for g in range(1, limit + 1):
            if g > 1:
                p0, p1 = pair_pow(p0, p1, c, mod)
            contrib = (contrib + podd[g] * p1) % mod  # U_{c^g + 1}
        if c % 2 == 1:
            contrib = (contrib + (rest % mod) * 10) % mod  # U_2
        else:
            contrib = (contrib + rest % mod) % mod  # U_1
        total = (total + contrib) % mod
    return total % mod

def coprime_odd_pairs(limit: int) -> np.ndarray:
    """podd[g] = #{(a, b) in [1, L]^2 : gcd = g, a/g and b/g odd}."""
    mu = np.ones(limit + 1, dtype=np.int64)
    comp = np.zeros(limit + 1, dtype=bool)
    for p in range(2, limit + 1):
        if not comp[p]:
            for j in range(p, limit + 1, p):
                if j > p:
                    comp[j] = True
                mu[j] = -mu[j]
            for j in range(p * p, limit + 1, p * p):
                mu[j] = 0
    podd = np.zeros(limit + 1, dtype=np.int64)
    for g in range(1, limit + 1):
        n = limit // g
        s = 0
        for d in range(1, n + 1, 2):
            if mu[d]:
                k = (n // d + 1) // 2
                s += mu[d] * k * k
        podd[g] = s
    return podd

def total_sum_py(limit: int, podd, mod: int) -> int:
    """Python big-int twin of total_sum, for exact small-L validation."""
    def pmul(a0, a1, b0, b1):
        am1 = (a1 - 10 * a0) % mod
        return (a0 * b1 + am1 * b0) % mod, (a1 * b1 + a0 * b0) % mod
    def ppow(p0, p1, e):
        r0, r1 = 0, 1
        while e:
            if e & 1:
                r0, r1 = pmul(r0, r1, p0, p1)
            p0, p1 = pmul(p0, p1, p0, p1)
            e >>= 1
        return r0, r1
    rest = limit * limit - sum(int(podd[g]) for g in range(1, limit + 1))
    total = 0
    for c in range(1, limit + 1):
        p0, p1 = ppow(1, 10 % mod, c)
        contrib = 0
        for g in range(1, limit + 1):
            if g > 1:
                p0, p1 = ppow(p0, p1, c)
            contrib = (contrib + int(podd[g]) * p1) % mod
        contrib = (contrib + rest * (10 if c % 2 else 1)) % mod
        total = (total + contrib) % mod
    return total

def s_brute(limit: int):
    """Exact S(L) with big integers (tiny L)."""
    tt = {0: 1, 1: 10}
    def t(n):
        if n not in tt:
            tt[n] = 10 * t(n - 1) + t(n - 2)
        return tt[n]
    return sum(gcd(t(c**a), t(c**b))
               for a in range(1, limit + 1)
               for b in range(1, limit + 1)
               for c in range(1, limit + 1))

if __name__ == "__main__":
    # verify the inner gcd identity numerically
    for c in range(1, 9):
        for a in range(1, 7):
            for b in range(1, 7):
                g = gcd(a, b)
                want = (c**g + 1 if (a // g) % 2 and (b // g) % 2
                        else (2 if c % 2 else 1))
                assert gcd(c**a + 1, c**b + 1) == want
    podd2 = coprime_odd_pairs(2)
    podd3 = coprime_odd_pairs(3)
    podd4 = coprime_odd_pairs(4)
    assert total_sum_py(2, podd2, 10**40) == s_brute(2) == 10444  # given
    assert (total_sum_py(3, podd3, 10**40) == s_brute(3)
            == 1292115238446807016106539989)  # given
    assert total_sum(4, podd4, MOD) == total_sum_py(4, podd4, MOD) \
        == 670616280  # given
    print(total_sum(2000, coprime_odd_pairs(2000), MOD))  # 970746056
