import numba
import numpy as np

from funcs import is_prime, prime_sieve_bool

# C(n) = (n - phi(n)) / (n - 1) is a unit fraction iff (n - phi(n)) | (n - 1).
# n must be squarefree: if p^2 | n then p divides both n and n - phi(n), and
# n - phi(n) | n - 1 would force p | 1. Two disjoint cases cover all
# squarefree composites.
#
# Semiprimes n = p q: with k = (n-1)/(n-phi(n)) the condition rearranges to
# (p - k)(q - k) = k^2 - k + 1 =: M, so for each k enumerate divisor pairs
# d e = M and test p = k + d, q = k + e. The smallest reachable n is about
# (k + sqrt(M))^2 >= (2k - 1)^2, bounding k by (sqrt(limit) + 1) / 2. M is
# odd and every odd prime factor of x^2 - x + 1 is 3 or = 1 (mod 3), so trial
# division only needs those primes.
#
# Three or more factors: write n = m q with q the largest prime, m composite
# and squarefree. From (n - 1) = k (n - phi(n)) with c = m - phi(m):
# q (m - k c) = k phi(m) + 1, so q is determined for each k with m - k c > 0
# (k <= smallest prime of m, keeping the scan short). Enumerate m by DFS over
# ascending primes; m p < limit is needed for any valid q > p to exist.


@numba.jit(cache=True)
def _semiprimes(limit: int, factor_primes: np.ndarray, small_sieve: np.ndarray) -> int:
    total = 0
    divisors = np.empty(8192, dtype=np.int64)
    k = 2
    while (2 * k - 1) * (2 * k - 1) <= limit:
        m = k * k - k + 1
        divisors[0] = 1
        nd = 1
        rem = m
        for i in range(len(factor_primes)):
            p = factor_primes[i]
            if p * p > rem:
                break
            if rem % p == 0:
                e = 0
                while rem % p == 0:
                    rem //= p
                    e += 1
                base = nd
                pw = 1
                for _ in range(e):
                    pw *= p
                    for j in range(base):
                        divisors[nd] = divisors[j] * pw
                        nd += 1
        if rem > 1:
            base = nd
            for j in range(base):
                divisors[nd] = divisors[j] * rem
                nd += 1
        for j in range(nd):
            d = divisors[j]
            if d * d >= m:
                continue
            e = m // d
            p, q = k + d, k + e
            if p * q <= limit and small_sieve[p] and is_prime(q):
                total += p * q
        k += 1
    return total


@numba.jit(cache=True)
def _multi_factor(
    limit: int, primes: np.ndarray, idx: int, m: int, phi: int, depth: int
) -> int:
    total = 0
    for i in range(idx, len(primes)):
        p = primes[i]
        m2 = m * p
        if m2 * p >= limit:  # any valid q must exceed p
            break
        phi2 = phi * (p - 1)
        if depth + 1 >= 2:
            c = m2 - phi2
            k = 1
            while True:
                den = m2 - k * c
                if den <= 0:
                    break
                num = k * phi2 + 1
                if num % den == 0:
                    q = num // den
                    if q > p and m2 * q <= limit and is_prime(q):
                        n = m2 * q
                        if (n - 1) % (n - phi2 * (q - 1)) == 0:
                            total += n
                k += 1
        total += _multi_factor(limit, primes, i + 1, m2, phi2, depth + 1)
    return total


def solve(limit: int = 2 * 10**11) -> int:
    k_max = (int(limit**0.5) + 1) // 2 + 2
    sieve = prime_sieve_bool(2 * k_max + 10)
    pr = np.nonzero(sieve)[0].astype(np.int64)
    factor_primes = pr[(pr % 3 == 1) | (pr == 3)]
    dfs_primes = np.nonzero(prime_sieve_bool(int((limit // 2) ** 0.5) + 10))[0].astype(
        np.int64
    )
    return int(_semiprimes(limit, factor_primes, sieve)) + int(
        _multi_factor(limit, dfs_primes, 0, 1, 1, 0)
    )


if __name__ == "__main__":
    print(solve())  # 288084712410001
