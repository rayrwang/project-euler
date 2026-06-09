import numba
import numpy as np

MOD = 10**9 + 7

@numba.njit(cache=True)
def jordan2_sieve(limit):
    """J_2(k) = k^2 * prod_{p | k} (1 - 1/p^2) for k = 1..limit, by a
    smallest-prime-factor style sieve. J_2 is multiplicative with
    J_2(p^e) = p^(2e) - p^(2e-2)."""
    j2 = np.arange(limit + 1, dtype=np.int64)
    j2 *= j2  # start from k^2
    for p in range(2, limit + 1):
        if j2[p] == p * p:  # p is prime (untouched so far)
            p2 = p * p
            for m in range(p, limit + 1, p):
                j2[m] -= j2[m] // p2
    return j2

@numba.njit(cache=True)
def S(n):
    """sum_{m <= n} g(m) where g(m) is the largest square dividing m.

    Writing m = a^2 b with b squarefree gives g(m) = a^2, so
        S(n) = sum_a a^2 Q(n // a^2)
    with Q the squarefree counting function. Expanding
    Q(x) = sum_d mu(d) * (x // d^2) and grouping by k = a*d yields
        S(n) = sum_{k^2 <= n} J_2(k) * (n // k^2),
    since sum_{d | k} mu(d) (k/d)^2 = J_2(k), the Jordan totient.
    """
    root = int(np.sqrt(n))
    while root * root > n:
        root -= 1
    while (root + 1) * (root + 1) <= n:
        root += 1
    j2 = jordan2_sieve(root)
    total = 0
    for k in range(1, root + 1):
        total = (total + (j2[k] % MOD) * ((n // (k * k)) % MOD)) % MOD
    return total

if __name__ == "__main__":
    assert S(10) == 24
    assert S(100) == 767
    print(S(10**14))  # 94586478
