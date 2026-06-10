import numba
import numpy as np

MOD = 10**9 + 7

@numba.njit(cache=True)
def T(n, k):
    """Tuples of primes <= n whose bitwise OR is a prime <= n.
    Subset-sum (SOS) zeta transform F(m) = #primes submask of m, raise to
    k-th power, Moebius (inverse SOS) back, sum over prime masks."""
    B = 20
    while (1 << B) <= n:
        B += 1
    size = 1 << B
    sieve = np.ones(n + 1, dtype=np.bool_)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    F = np.zeros(size, dtype=np.int64)
    for p in range(2, n + 1):
        if sieve[p]:
            F[p] = 1
    for b in range(B):
        bit = 1 << b
        for m in range(size):
            if m & bit:
                F[m] += F[m ^ bit]
    # G = F^k mod MOD
    G = np.zeros(size, dtype=np.int64)
    for m in range(size):
        base = F[m] % MOD
        e = k
        r = 1
        while e:
            if e & 1:
                r = r * base % MOD
            base = base * base % MOD
            e >>= 1
        G[m] = r
    # inverse SOS
    for b in range(B):
        bit = 1 << b
        for m in range(size):
            if m & bit:
                G[m] = (G[m] - G[m ^ bit]) % MOD
    total = 0
    for q in range(2, n + 1):
        if sieve[q]:
            total = (total + G[q]) % MOD
    return total

if __name__ == "__main__":
    assert T(5, 2) == 5
    assert T(100, 3) == 3355
    assert T(1000, 10) == 2071632
    print(T(10**6, 999983))  # 557988060
