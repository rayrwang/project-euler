"""
https://projecteuler.net/problem=517

For real a > 1, g_a(x) = 1 for x < a and g_a(x) = g_a(x-1) +
g_a(x-a) otherwise; G(n) = g_(sqrt(n))(n). Find the sum of G(p) over
primes 10^7 < p < 10^7 + 10^4, modulo 1000000007.

Unfolding the recursion, g_a(x) counts step sequences over {-1, -a}
where every proper prefix keeps the value at least a and the full
sum drops below a; since steps are positive decrements only the
last-but-one value matters. Splitting by the number j of a-steps and
the final step type (a = sqrt(n) is irrational for prime n, and
floor(k a) = isqrt(k^2 n) exactly):

  - last step 1: the count of 1-steps is forced to
    L_j = x - floor((j+1)a), contributing C(L_j - 1 + j, j) when
    L_j >= 1 (the first i+j-1 steps are arranged freely);
  - last step a (j >= 1): i ranges over [max(0, L_j), x-floor(ja)-1]
    contributing C(i + j - 1, j - 1), which the hockey-stick
    identity collapses to C(U + j, j) - C(max(0, L_j) + j - 1, j).

So G(n) is a sum of O(sqrt(n)) binomial terms, evaluated modulo the
prime with precomputed factorials. The formula is verified against a
direct memoized expansion of the recursion (with exact integer
comparisons (n-i)^2 < (j+1)^2 n) for a range of n including the
given G(90) = 7564511.
"""

import sys
from functools import lru_cache
from math import isqrt
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402

MOD = 1_000_000_007
NMAX = 10_100_000

_fact_l = [1] * NMAX
f = 1
for i in range(1, NMAX):
    f = f * i % MOD
    _fact_l[i] = f
_inv = [1] * NMAX
_inv[NMAX - 1] = pow(_fact_l[NMAX - 1], MOD - 2, MOD)
for i in range(NMAX - 1, 0, -1):
    _inv[i - 1] = _inv[i] * i % MOD


def _c(n: int, k: int) -> int:
    if k < 0 or k > n or n < 0:
        return 0
    return _fact_l[n] * _inv[k] % MOD * _inv[n - k] % MOD


def g_mod(n: int) -> int:
    """G(n) mod MOD via the binomial expansion."""
    total = 0
    x = n
    j = 0
    fj1a = isqrt(n)  # floor((j+1) a) for j = 0
    while True:
        fja = isqrt(j * j * n) if j else 0
        if j >= 1 and fja >= x:
            break
        ell = x - fj1a
        if ell >= 1:
            total += _c(ell - 1 + j, j)
        if j >= 1:
            u = x - fja - 1
            lc = max(0, ell)
            if u >= lc:
                total += _c(u + j, j) - _c(lc + j - 1, j)
        j += 1
        fj1a = isqrt((j + 1) * (j + 1) * n)
    return total % MOD


def _g_direct(n: int) -> int:
    sys.setrecursionlimit(100000)

    @lru_cache(maxsize=None)
    def g(i: int, j: int) -> int:
        r = n - i
        if r < 0 or r * r < (j + 1) * (j + 1) * n:
            return 1
        return g(i + 1, j) + g(i, j + 1)

    return g(0, 0)


if __name__ == "__main__":
    for n in (5, 7, 10, 13, 20, 31, 50, 77, 90, 101, 137):
        assert _g_direct(n) % MOD == g_mod(n), n
    assert _g_direct(90) == 7564511  # given

    primes = prime_sieve_int(10_010_000)
    sel = primes[primes > 10_000_000]
    print(sum(g_mod(int(p)) for p in sel) % MOD)  # 581468882
