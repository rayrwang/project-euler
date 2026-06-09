import numpy as np
from numba import njit


@njit(cache=True)
def _solve(limit: int, target: int) -> int:
    # Sieve Euler's totient, then fill chain lengths in ascending order
    # (chains strictly decrease), summing primes (phi(i) = i - 1) of length target.
    phi = np.arange(limit, dtype=np.int64)
    for i in range(2, limit):
        if phi[i] == i:  # i is prime
            for j in range(i, limit, i):
                phi[j] -= phi[j] // i
    chain = np.zeros(limit, dtype=np.int8)
    if limit > 1:
        chain[1] = 1
    total = 0
    for i in range(2, limit):
        chain[i] = chain[phi[i]] + 1
        if chain[i] == target and phi[i] == i - 1:
            total += i
    return total


def solve(limit: int = 40_000_000, target: int = 25) -> int:
    return int(_solve(limit, target))


if __name__ == "__main__":
    print(solve())  # 1677366278943
