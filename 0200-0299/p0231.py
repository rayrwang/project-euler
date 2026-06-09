import numpy as np
from numba import njit


@njit(cache=True)
def _sum_factor_terms(n: int, k: int, primes: np.ndarray) -> int:
    # By Legendre's formula the exponent of p in n! is sum_i floor(n / p^i),
    # so its exponent in C(n, k) is that of n! minus those of k! and (n-k)!.
    total = 0
    for idx in range(len(primes)):
        p = primes[idx]
        e = 0
        q = p
        while q <= n:
            e += n // q - k // q - (n - k) // q
            q *= p
        total += p * e
    return total


def solve(n: int = 20_000_000, k: int = 15_000_000) -> int:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = np.nonzero(sieve)[0].astype(np.int64)
    return int(_sum_factor_terms(n, k, primes))


if __name__ == "__main__":
    print(solve())  # 7526965179680
