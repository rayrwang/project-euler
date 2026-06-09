import numba
import numpy as np

from funcs import prime_sieve_bool


@numba.jit(cache=True)
def partition_counts(n: int) -> np.ndarray:
    """min(P(v), 2) for 0 <= v < n, where P(v) counts partitions of v into
    parts 2^i * 3^j such that no part divides another.

    A part 2^i*3^j divides 2^k*3^l iff i<=k and j<=l, so a valid partition is
    an antichain: its points (i, j) have strictly increasing i as j strictly
    decreases. Sweeping the powers of three from high to low, each column may
    contribute at most one point, whose exponent i must exceed every i chosen
    so far. The DP state is (largest i used, running sum); a prefix sum over
    the "largest i" axis supplies all earlier states with a smaller i at once.
    Counts are clamped at 2 since only P(q) = 1 matters.
    """
    max_i = 0
    while (1 << (max_i + 1)) < n:
        max_i += 1
    n_states = max_i + 2  # state index L = (last i) + 1; 0 means "nothing yet"

    threes = []
    p = 1
    while p < n:
        threes.append(p)
        p *= 3

    dp = np.zeros((n_states, n), dtype=np.int8)
    dp[0, 0] = 1  # empty antichain
    for jdx in range(len(threes) - 1, -1, -1):
        tj = threes[jdx]
        cum = np.zeros((n_states, n), dtype=np.int8)
        for s in range(n):
            acc = 0
            for el in range(n_states):
                acc += dp[el, s]
                if acc > 2:
                    acc = 2
                cum[el, s] = acc
        newdp = dp.copy()
        for i in range(max_i + 1):
            val = (1 << i) * tj
            if val >= n:
                break
            l_new = i + 1
            for s in range(n - val):
                x = newdp[l_new, s + val] + cum[i, s]  # cum[i]: states with last i < i
                newdp[l_new, s + val] = 2 if x > 2 else x
        dp = newdp

    counts = np.zeros(n, dtype=np.int8)
    for v in range(n):
        acc = 0
        for el in range(n_states):
            acc += dp[el, v]
            if acc > 2:
                acc = 2
        counts[v] = acc
    return counts


def solve(limit: int) -> int:
    counts = partition_counts(limit)
    is_prime = prime_sieve_bool(limit)
    return int(sum(q for q in range(2, limit) if is_prime[q] and counts[q] == 1))


if __name__ == "__main__":
    assert solve(100) == 233
    print(solve(1_000_000))  # 3053105
