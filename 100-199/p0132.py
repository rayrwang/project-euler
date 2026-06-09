import numpy as np


def solve(k: int = 10**9, count: int = 40) -> int:
    # For prime p not in {2,3,5}, p | R(k) = (10^k - 1)/9 iff 10^k == 1 (mod p).
    # Test primes in order via fast modular exponentiation; sum the first `count`.
    limit = 1_000_000
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = np.nonzero(sieve)[0]

    total = 0
    found = 0
    for p in primes:
        pi = int(p)
        if pi in (2, 3, 5):
            continue
        if pow(10, k, pi) == 1:
            total += pi
            found += 1
            if found == count:
                return total
    raise ValueError("increase sieve limit")


if __name__ == "__main__":
    print(solve())  # 843296
