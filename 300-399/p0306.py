import numba
import numpy as np


@numba.jit(cache=True)
def grundy_values(n_max: int) -> np.ndarray:
    """Grundy value of a single strip of length k, for 0 <= k <= n_max.

    Painting two adjacent squares of a length-k strip splits it into two
    independent strips whose lengths sum to k - 2, so
        G(k) = mex { G(a) XOR G(b) : a + b = k - 2,  a, b >= 0 }.
    """
    g = np.zeros(n_max + 1, dtype=np.int64)
    for k in range(2, n_max + 1):
        seen = np.zeros(k + 2, dtype=np.bool_)
        for a in range(0, k - 1):
            v = g[a] ^ g[k - 2 - a]
            if v < seen.size:
                seen[v] = True
        m = 0
        while seen[m]:
            m += 1
        g[k] = m
    return g


def find_period(g: np.ndarray) -> tuple[int, int]:
    """Smallest (preperiod, period) such that g is periodic past the preperiod,
    verified over the full computed tail."""
    n = len(g)
    for period in range(1, n // 4):
        for pre in range(0, n - 3 * period):
            if all(g[i] == g[i + period] for i in range(pre, n - period)):
                return pre, period
    raise AssertionError("no period detected; extend n_max")


def solve(limit: int) -> int:
    g = grundy_values(4000)
    pre, period = find_period(g)
    wins = 0
    for n in range(1, limit + 1):
        gv = g[n] if n < len(g) else g[pre + (n - pre) % period]
        if gv != 0:
            wins += 1
    return wins


if __name__ == "__main__":
    # For 1 <= n <= 5 the winning n are 2, 3, 4.
    assert solve(5) == 3
    print(solve(1_000_000))  # 852938
