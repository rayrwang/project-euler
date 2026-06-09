import numpy as np


def solve(limit: int = 1_000_000) -> int:
    # For consecutive primes p1 < p2, find least n with n == p1 (mod 10^d),
    # d = digits of p1, and n divisible by p2. Write n = p1 + k*10^d; then
    # k == -p1 * (10^d)^{-1} (mod p2). Sum n over all pairs with p1 <= limit.
    top = limit + 1000
    sieve = np.ones(top, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(top**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = [int(p) for p in np.nonzero(sieve)[0]]

    total = 0
    m = 10  # 10^(digits of p1), updated as p1 grows
    for idx in range(len(primes) - 1):
        p1 = primes[idx]
        if p1 < 5:
            continue
        if p1 > limit:
            break
        p2 = primes[idx + 1]
        while m <= p1:
            m *= 10
        k = (-p1 * pow(m, -1, p2)) % p2
        total += p1 + k * m
    return total


if __name__ == "__main__":
    print(solve())  # 18613426663617118
