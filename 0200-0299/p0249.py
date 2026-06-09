import numpy as np

# Classic subset-sum DP: dp[s] counts subsets of the primes below 5000 with
# sum s, updated one prime at a time (dp[s + p] += dp[s], vectorised as a
# shifted slice). All sums stay below 1548137, and values are kept modulo
# 10^16 (two reduced values fit in uint64). Finally add dp[q] over the prime
# sums q.


def _sieve(n: int) -> np.ndarray:
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return s


def solve(limit: int = 5000, mod: int = 10**16) -> int:
    primes = np.nonzero(_sieve(limit))[0]
    total = int(primes.sum())
    dp = np.zeros(total + 1, dtype=np.uint64)
    dp[0] = 1
    for p in primes:
        p = int(p)
        dp[p:] = (dp[p:] + dp[:-p]) % mod
    prime_sums = np.nonzero(_sieve(total))[0]
    return int(dp[prime_sums].sum(dtype=object) % mod)


if __name__ == "__main__":
    print(solve())  # 9275262564250418
