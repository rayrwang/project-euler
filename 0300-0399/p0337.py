import numpy as np
from numba import njit

MOD = 10**8


def _totient_sieve(n: int) -> np.ndarray:
    phi = np.arange(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            phi[i::i] -= phi[i::i] // i
    return phi


@njit(cache=True)
def _count(n: int, phi: np.ndarray) -> int:
    """S(N) mod 1e8 for sequences starting at 6 with phi(a_i) < phi(a_{i+1}) < a_i < a_{i+1}.

    Let f(a) be the number of valid sequences ending at a. A predecessor b of a must satisfy
    phi(a) < b < a and phi(b) < phi(a), so

        f(a) = [a = 6] + sum_{phi(b) < phi(a)} f(b) - sum_{b <= phi(a)} f(b).

    The subtraction is exact because b <= phi(a) forces phi(b) < b <= phi(a), so those terms are
    precisely the ones with phi(b) < phi(a) but b too small. Processing a in increasing value (so
    every f(b), b < a, is ready) keeps two Fenwick trees -- one indexed by phi-value, one by value
    -- giving an O(N log N) sweep. S(N) is the running total of f."""
    size = n + 2
    by_phi = np.zeros(size + 1, dtype=np.int64)
    by_val = np.zeros(size + 1, dtype=np.int64)

    def update(tree, i, v):
        i += 1
        while i <= size:
            tree[i] = (tree[i] + v) % MOD
            i += i & (-i)

    def query(tree, i):
        i += 1
        s = 0
        while i > 0:
            s += tree[i]
            if s >= (1 << 62):
                s %= MOD
            i -= i & (-i)
        return s % MOD

    total = 0
    for a in range(6, n + 1):
        pa = phi[a]
        if a == 6:
            val = 1
        else:
            val = (query(by_phi, pa - 1) - query(by_val, pa)) % MOD
        update(by_phi, pa, val)
        update(by_val, a, val)
        total = (total + val) % MOD
    return total % MOD


def solve(n: int = 20_000_000) -> int:
    return _count(n, _totient_sieve(n))


if __name__ == "__main__":
    assert _count(10, _totient_sieve(10)) == 4
    assert _count(10_000, _totient_sieve(10_000)) == 73808307
    print(solve())  # 85068035
