"""Project Euler 953: Factorisation Nim.

The game is ordinary Nim on the multiset of prime factors of n (with
multiplicity), so by the Sprague-Grundy theorem the first player loses
exactly when the XOR of the prime factors is zero. This was verified by
direct game-tree evaluation for all n <= 200 and matches the given
S(10) = 14 and S(100) = 455.

To sum such n <= 10^14: write the sorted prime factorisation as
p_1 <= ... <= p_k. XOR-zero forces p_k = p_1 ^ ... ^ p_(k-1), so n is
determined by its "prefix" m = p_1 ... p_(k-1): the top prime is
X = xor of the prefix primes, and validity requires X prime and
X >= p_(k-1) (so the decomposition removing one largest factor is unique
and every XOR-zero n is generated exactly once). Since n = m X >= m q^2
where q = p_(k-1), the prefix search tree is bounded by m q^2 <= N, i.e.
roughly sum over primes q of Psi(N/q^2, q) ~ 3*10^8 nodes, which Numba
handles in a few seconds. All primes involved are < 2^24, so X-primality
is a sieve lookup.

The lone k = 0 case is n = 1 (empty XOR is 0); k = 1 is impossible since
a prime is nonzero. Verified against brute force for N = 10, 100, 10^5.
"""

import numpy as np
from numba import njit

N = 10**14
MOD = 10**9 + 7
SIEVE_LIMIT = 1 << 24  # all primes and XOR values are below 2^24


def sieve(limit: int) -> np.ndarray:
    isp = np.ones(limit, dtype=np.bool_)
    isp[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if isp[i]:
            isp[i * i :: i] = False
    return isp


@njit(cache=True)
def dfs(primes: np.ndarray, isp: np.ndarray, n: int) -> int:
    """Sum (mod MOD) of m*q*X over prefixes m (XOR y) of XOR-zero numbers.

    Iterative DFS: each stack level holds a prefix (m, y) and the index j
    of the next prime to try as the new largest prefix prime q; the top
    factor X = y ^ q must then be a prime >= q with m*q*X <= n.
    """
    depth = 64
    m_st = np.empty(depth, dtype=np.int64)
    y_st = np.empty(depth, dtype=np.int64)
    j_st = np.empty(depth, dtype=np.int64)
    m_st[0], y_st[0], j_st[0] = 1, 0, 0
    sp = 0
    total = 0
    while sp >= 0:
        m, y, j = m_st[sp], y_st[sp], j_st[sp]
        if j >= len(primes):
            sp -= 1
            continue
        q = primes[j]
        mq = m * q
        if mq * q > n:
            sp -= 1
            continue
        j_st[sp] = j + 1
        x = y ^ q
        if x >= q and isp[x] and mq * x <= n:
            total = (total + mq * x) % MOD
        if mq * q <= n // q:  # m*q^3 <= n, room for a deeper prefix
            sp += 1
            m_st[sp], y_st[sp], j_st[sp] = mq, y ^ q, j
    return total


def solve(n: int = N) -> int:
    isp = sieve(SIEVE_LIMIT)
    max_q = int(n**0.5) + 1
    primes = np.flatnonzero(isp[:max_q]).astype(np.int64)
    return (1 + dfs(primes, isp, n)) % MOD


if __name__ == "__main__":
    print(solve())  # 176907658
