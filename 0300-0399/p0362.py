import math
import sys
from functools import lru_cache


def _mobius_upto(n: int) -> list[int]:
    mu = [1] * (n + 1)
    primes: list[int] = []
    is_comp = bytearray(n + 1)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            is_comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def solve(n_max: int) -> int:
    """S(n_max) = sum_{k=2}^{n_max} Fsf(k), where Fsf(k) is the number of ways to
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
    """
    sq_root = int(math.isqrt(n_max))
    mu = _mobius_upto(sq_root + 10)

    # squarefree flags up to sqrt(n_max), for the explicitly recursed factors
    is_squarefree = bytearray([1]) * (sq_root + 2)
    is_squarefree[0] = 0
    for k in range(2, int(math.isqrt(sq_root)) + 1):
        for m in range(k * k, sq_root + 1, k * k):
            is_squarefree[m] = 0

    @lru_cache(maxsize=None)
    def squarefree_count(b: int) -> int:
        # number of squarefree integers in [1, b] = sum_k mu(k) floor(b / k^2)
        if b <= 0:
            return 0
        total = 0
        for k in range(1, int(math.isqrt(b)) + 1):
            if mu[k]:
                total += mu[k] * (b // (k * k))
        return total

    @lru_cache(maxsize=None)
    def f(n: int, lo: int) -> int:
        if n < lo:
            return 1  # only the empty multiset fits
        sq = int(math.isqrt(n))
        total = 1  # the empty multiset
        d = lo
        while d <= sq:
            if is_squarefree[d]:
                total += f(n // d, d)
            d += 1
        # factors d in [max(lo, sq+1), n] each occur alone; count squarefree ones
        lo2 = max(lo, sq + 1)
        total += squarefree_count(n) - squarefree_count(lo2 - 1)
        return total

    sys.setrecursionlimit(1 << 20)
    return f(n_max, 2) - 1


if __name__ == "__main__":
    # Fsf(54) = 2 (only 3*3*6 and 2*3*3*3); S(100) = 193.
    assert solve(100) == 193
    print(solve(10**10))  # 457895958010
