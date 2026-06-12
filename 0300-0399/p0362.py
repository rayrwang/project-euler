"""Project Euler 362: Squarefree Factors.

S(n_max) = sum_{k=2}^{n_max} Fsf(k), where Fsf(k) is the number of ways to
write k as an unordered product of squarefree factors all greater than 1.

Summing Fsf over all k <= n_max counts every (k, factorization) pair, which is
exactly the number of multisets of squarefree integers > 1 whose product is at
most n_max. Count those multisets with factors taken in nondecreasing order:
    F(N, lo) = multisets (including empty) of squarefree factors, each >= lo,
               with product <= N.
A factor d > sqrt(N) can occur at most once (then no further factor fits), so
all such d contribute one multiset {d} each and are counted in bulk by the
squarefree-counting function; only factors d <= sqrt(N) are recursed on. The
answer is F(n_max, 2) - 1, dropping the empty multiset.

The recursion is memoized in numba typed.Dicts keyed by n*(sqrt+2)+lo (the
arguments satisfy lo <= sqrt(n_max)+1, so the key fits comfortably in int64),
replacing the pure-Python lru_cache version.
"""

import math

import numba as nb
import numpy as np
from numba.typed import Dict


@nb.njit(cache=True)
def _mobius_upto(n):
    mu = np.ones(n + 1, dtype=np.int8)
    is_comp = np.zeros(n + 1, dtype=np.uint8)
    primes = np.zeros(n + 1, dtype=np.int64)
    np_count = 0
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes[np_count] = i
            np_count += 1
            mu[i] = -1
        for j in range(np_count):
            p = primes[j]
            if i * p > n:
                break
            is_comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


@nb.njit(cache=True)
def _isqrt(n):
    x = np.int64(np.sqrt(np.float64(n)))
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@nb.njit(cache=True)
def _squarefree_count(b, mu, cache):
    """Number of squarefree integers in [1, b] = sum_k mu(k) floor(b / k^2)."""
    if b <= 0:
        return 0
    if b in cache:
        return cache[b]
    total = 0
    for k in range(1, _isqrt(b) + 1):
        if mu[k]:
            total += mu[k] * (b // (k * k))
    cache[b] = total
    return total


@nb.njit(cache=True)
def _f(n, lo, key_stride, is_squarefree, mu, f_cache, sf_cache):
    if n < lo:
        return 1  # only the empty multiset fits
    key = n * key_stride + lo
    if key in f_cache:
        return f_cache[key]
    sq = _isqrt(n)
    total = 1  # the empty multiset
    d = lo
    while d <= sq:
        if is_squarefree[d]:
            total += _f(n // d, d, key_stride, is_squarefree, mu, f_cache, sf_cache)
        d += 1
    # factors d in [max(lo, sq+1), n] each occur alone; count squarefree ones
    lo2 = max(lo, sq + 1)
    total += _squarefree_count(n, mu, sf_cache) - _squarefree_count(lo2 - 1, mu, sf_cache)
    f_cache[key] = total
    return total


def solve(n_max: int) -> int:
    sq_root = int(math.isqrt(n_max))
    mu = _mobius_upto(sq_root + 10)

    is_squarefree = np.ones(sq_root + 2, dtype=np.uint8)
    is_squarefree[0] = 0
    for k in range(2, int(math.isqrt(sq_root)) + 1):
        is_squarefree[k * k :: k * k] = 0

    f_cache = Dict.empty(nb.int64, nb.int64)
    sf_cache = Dict.empty(nb.int64, nb.int64)
    key_stride = sq_root + 2  # lo <= sqrt(n_max) + 1 < stride
    return int(_f(n_max, 2, key_stride, is_squarefree, mu, f_cache, sf_cache)) - 1


if __name__ == "__main__":
    # Fsf(54) = 2 (only 3*3*6 and 2*3*3*3); S(100) = 193.
    assert solve(100) == 193
    print(solve(10**10))  # 457895958010
