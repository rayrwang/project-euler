import numpy as np
from numba import njit

MOD = 10**18


@njit
def _divisor_sieve(m: int) -> np.ndarray:
    """Linear sieve of the divisor-count function d(x) for x in [0, m]."""
    d = np.ones(m + 1, dtype=np.int32)
    low_exp = np.zeros(m + 1, dtype=np.int32)  # exponent of the smallest prime factor
    primes = np.empty(m // 10 + 1000, dtype=np.int32)
    n_primes = 0
    is_comp = np.zeros(m + 1, dtype=np.uint8)
    d[0] = 0
    for i in range(2, m + 1):
        if is_comp[i] == 0:
            primes[n_primes] = i
            n_primes += 1
            d[i] = 2
            low_exp[i] = 1
        for pj in range(n_primes):
            p = primes[pj]
            ip = i * p
            if ip > m:
                break
            is_comp[ip] = 1
            if i % p == 0:
                low_exp[ip] = low_exp[i] + 1
                d[ip] = d[i] // (low_exp[i] + 1) * (low_exp[i] + 2)
                break
            low_exp[ip] = 1
            d[ip] = d[i] * 2
    return d


@njit
def _dt_values(n: int, d: np.ndarray) -> np.ndarray:
    """dT(i) for i = 1..n, where dT(i) is the number of divisors of the i-th
    triangular number T(i) = i(i+1)/2. Since gcd(i, i+1) = 1, splitting off the
    factor of 2 gives two coprime parts and dT(i) = d(a) * d(b)."""
    dv = np.empty(n, dtype=np.int32)
    for i in range(1, n + 1):
        if i % 2 == 0:
            a, b = i // 2, i + 1
        else:
            a, b = i, (i + 1) // 2
        dv[i - 1] = d[a] * d[b]
    return dv


@njit
def _fen_update(tree: np.ndarray, i: int) -> None:
    while i < len(tree):
        tree[i] += 1
        i += i & (-i)


@njit
def _fen_query(tree: np.ndarray, i: int) -> int:
    r = 0
    while i > 0:
        r += tree[i]
        i -= i & (-i)
    return r


@njit
def _count_triples(dv: np.ndarray, max_d: int) -> int:
    """Number of triples i < j < k with dv[i] > dv[j] > dv[k], modulo MOD.

    For each middle index j, the count of valid triples through j is
    (#earlier values greater than dv[j]) * (#later values less than dv[j]).
    Two Fenwick trees over the dv-values give both factors in O(n log max_d).
    """
    n = len(dv)
    right = np.empty(n, dtype=np.int64)
    tree = np.zeros(max_d + 1, dtype=np.int64)
    for j in range(n - 1, -1, -1):
        right[j] = _fen_query(tree, dv[j] - 1)  # later values strictly smaller
        _fen_update(tree, dv[j])

    tree_left = np.zeros(max_d + 1, dtype=np.int64)
    total = 0
    seen = 0
    for j in range(n):
        greater_before = seen - _fen_query(tree_left, dv[j])
        total = (total + (greater_before % MOD) * (right[j] % MOD)) % MOD
        _fen_update(tree_left, dv[j])
        seen += 1
    return total


def solve(n: int = 60_000_000) -> int:
    """Last 18 digits of Tr(n): the number of triples 1 <= i < j < k <= n with
    dT(i) > dT(j) > dT(k), where dT is the divisor count of the triangular
    numbers."""
    d = _divisor_sieve(n + 2)
    dv = _dt_values(n, d)
    return _count_triples(dv, int(dv.max()))


if __name__ == "__main__":
    # Tr(20) = 14, Tr(100) = 5772, Tr(1000) = 11174776.
    d_check = _divisor_sieve(1002)
    for limit, expected in ((20, 14), (100, 5772), (1000, 11174776)):
        vals = _dt_values(limit, d_check)
        assert _count_triples(vals, int(vals.max())) == expected
    print(solve())  # 147534623725724718
