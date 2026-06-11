import numba
import numpy as np

@numba.njit(cache=True)
def smallest_prime_factors(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

@numba.njit(cache=True)
def F(n):
    """Sum of p + q over reciprocal pairs (p, q) with p <= n.

    (p, q) is reciprocal iff some r < p satisfies rp = 1 mod q and
    rq = 1 mod p. Multiplying the two congruences shows r(p+q) = 1 mod pq,
    and since r < p the only possibility is r(p+q) = pq + 1. Writing
    s = p + q, the condition p q + 1 = 0 mod s becomes s | p^2 - 1, and
    conversely every divisor s > 2p of (p-1)(p+1) yields the valid pair
    q = s - p with r = p - (p^2-1)/s. So F(n) sums, for each p <= n, the
    divisors of p^2 - 1 exceeding 2p. Divisors are enumerated by merging
    the prime factorizations of p - 1 and p + 1 from an SPF sieve.
    """
    spf = smallest_prime_factors(n + 1)
    total = 0
    primes = np.empty(32, dtype=np.int64)
    exps = np.empty(32, dtype=np.int64)
    divisors = np.empty(8192, dtype=np.int64)
    for p in range(2, n + 1):
        # merged factorization of (p - 1) * (p + 1)
        m = 0
        for v0 in (p - 1, p + 1):
            v = v0
            while v > 1:
                f = spf[v]
                e = 0
                while v % f == 0:
                    v //= f
                    e += 1
                found = False
                for i in range(m):
                    if primes[i] == f:
                        exps[i] += e
                        found = True
                        break
                if not found:
                    primes[m] = f
                    exps[m] = e
                    m += 1
        # enumerate divisors of p^2 - 1, sum those exceeding 2p
        divisors[0] = 1
        cnt = 1
        for i in range(m):
            step = cnt
            pe = 1
            for _ in range(exps[i]):
                pe *= primes[i]
                for j in range(step):
                    divisors[cnt] = divisors[j] * pe
                    cnt += 1
        bound = 2 * p
        for i in range(cnt):
            if divisors[i] > bound:
                total += divisors[i]
    return total

if __name__ == "__main__":
    assert F(5) == 59
    assert F(10**2) == 697317
    print(F(2 * 10**6))  # 5833303012576429231
