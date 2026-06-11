"""
Project Euler Problem 797: Cyclogenic Polynomials
https://projecteuler.net/problem=797

A monic integer polynomial p is n-cyclogenic if p divides x^n - 1 and
divides no smaller x^k - 1.  P_n(x) sums all n-cyclogenic polynomials and
Q_N = sum_{n <= N} P_n.  Given Q_10(2) = 5598, find Q_{10^7}(2) modulo
10^9 + 7.

Structure.  Over the integers x^n - 1 = prod_{d | n} Phi_d(x) into distinct
irreducible cyclotomic factors, so the monic divisors of x^n - 1 are exactly
the products of Phi_d over subsets S of the divisors of n.  Such a product
divides x^k - 1 iff every d in S divides k, so the smallest valid k is
lcm(S): the polynomial is n-cyclogenic iff lcm(S) = n (taking lcm of the
empty set as 1, matching p = 1 being 1-cyclogenic).  All elements of a set
with lcm equal to m divide m, hence

    F(m) := prod_{e | m} (1 + Phi_e(2)) = sum_{d | m} P_d(2),

because expanding the product enumerates every subset of divisors of m
grouped by its lcm d.  Moebius inversion over the divisor lattice gives
P_n(2) = sum_{d | n} mu(n/d) F(d), and summing over n <= N collapses to

    Q_N(2) = sum_{d <= N} F(d) * M(floor(N / d)),

where M is the Mertens function.  Sanity checks: P_6(2) = 234 agrees with
the displayed P_6, and Q_10(2) = 5598.

Computation mod 10^9 + 7.  Phi_e(2) for all e <= 10^7 by a divisor sieve:
start T[e] = 2^e - 1 and for each e divide T[m] by Phi_e(2) for every proper
multiple m.  The division is legal because Phi_e(2) divides 2^e - 1, which
is nonzero mod p: the order of 2 modulo 10^9 + 7 is 500000003 > 10^7.  A
second divisor sieve accumulates F, a linear sieve gives mu, and the final
sum runs once over d.  Everything is O(N log N) in Numba.
"""

import numpy as np
from numba import njit

MOD = 10**9 + 7
N = 10**7


@njit(cache=True)
def cyclotomic_at_2(n):
    """T[e] = Phi_e(2) mod MOD for e = 1..n."""
    t = np.zeros(n + 1, dtype=np.int64)
    p2 = np.int64(1)
    for e in range(1, n + 1):
        p2 = p2 * 2 % MOD
        t[e] = p2 - 1
    for e in range(2, n // 2 + 1):
        # t[e] is now Phi_e(2); divide it out of all proper multiples
        inv = np.int64(1)
        base = t[e]
        b = MOD - 2
        while b > 0:
            if b & 1:
                inv = inv * base % MOD
            base = base * base % MOD
            b >>= 1
        for m in range(2 * e, n + 1, e):
            t[m] = t[m] * inv % MOD
    return t


@njit(cache=True)
def f_table(t):
    """F[m] = prod_{e | m} (1 + Phi_e(2)) mod MOD."""
    n = t.shape[0] - 1
    f = np.ones(n + 1, dtype=np.int64)
    for e in range(1, n + 1):
        v = (t[e] + 1) % MOD
        for m in range(e, n + 1, e):
            f[m] = f[m] * v % MOD
    return f


@njit(cache=True)
def mertens(n):
    """Prefix sums of the Moebius function for 0..n (linear sieve)."""
    mu = np.zeros(n + 1, dtype=np.int64)
    mu[1] = 1
    primes = np.zeros(n + 1, dtype=np.int64)
    np_count = 0
    is_comp = np.zeros(n + 1, dtype=np.bool_)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes[np_count] = i
            np_count += 1
            mu[i] = -1
        for j in range(np_count):
            p = primes[j]
            if i * p > n:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    for i in range(1, n + 1):
        mu[i] += mu[i - 1]
    return mu


def q_at_2(n, t=None):
    if t is None or t.shape[0] - 1 < n:
        t = cyclotomic_at_2(n)
    f = f_table(t[: n + 1])
    mert = mertens(n)
    answer = 0
    for d in range(1, n + 1):
        answer += int(f[d]) * int(mert[n // d])
    return answer % MOD


def main():
    t = cyclotomic_at_2(N)
    assert int(t[1]) == 1 and int(t[2]) == 3 and int(t[6]) == 3
    assert int(t[12]) == 13  # Phi_12(2) = 2^4 - 2^2 + 1
    assert q_at_2(10, t) == 5598
    return q_at_2(N, t)


if __name__ == "__main__":
    print(main())  # 47722272
