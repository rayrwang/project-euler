"""Project Euler Problem 641: A Long Row of Dice.

Die i is turned once for every j in 2..n dividing i, i.e. d(i) - 1 times,
so it ends showing 1 iff d(i) == 1 (mod 6).  Odd d forces i = m^2, and
with m = prod p^e we get d(i) = prod (2e + 1); modulo 3 the factor 2e + 1
is 1, 0, 2 for e == 0, 1, 2 (mod 3).  So d(i) == 1 (mod 6) demands every
exponent e of m to satisfy e != 1 (mod 3) (in particular e != 1, so m is
powerful) and the number of exponents with e == 2 (mod 3) to be even.

Every allowed exponent decomposes uniquely as e = 2u + 3v with u in {0,1}
(u = 1 iff e == 2 mod 3), giving a bijection m <-> (a, b) = a^2 b^3 with a
squarefree.  Writing Y = sqrt(N) = 10^18, the unweighted count and the
count weighted by (-1)^(number of e == 2 mod 3) = mu(a) are

    A(Y) = sum_{b^3 <= Y} Q(isqrt(Y/b^3)),   Q = squarefree count,
    B(Y) = sum_{b^3 <= Y} M(isqrt(Y/b^3)),   M = Mertens,

and f(N) = (A + B)/2.  Q(z) = sum_{d^2 <= z} mu(d) floor(z/d^2) costs
(Y/b^3)^(1/4) per term, about 4 * 10^6 operations in total.  A sieved
Mertens table to 4 * 10^7 covers every b >= 9 directly; the eight larger
arguments (up to 10^9) use the classic recursion M(x) = 1 -
sum_{k>=2} M(x/k) over quotient blocks with memoisation.

Checks: f(100) = 2 and f(10^8) = 69 (given), plus a brute-force
divisor-count sieve at several cutoffs up to 10^7.
"""

from functools import lru_cache
from math import isqrt

import numba
import numpy as np

L = 4 * 10**7


@numba.jit(cache=True)
def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    mu[0] = 0
    is_comp = np.zeros(n + 1, dtype=np.bool_)
    primes = np.empty(n // 10 + 100, dtype=np.int64)
    np_ = 0
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes[np_] = i
            np_ += 1
            mu[i] = -1
        for t in range(np_):
            p = primes[t]
            if i * p > n:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


MU = mobius_sieve(L)
MERTENS = np.cumsum(MU.astype(np.int64))  # MERTENS[x] = M(x)


@lru_cache(maxsize=None)
def mertens(x: int) -> int:
    if x <= L:
        return int(MERTENS[x])
    total = 1
    k = 2
    while k <= x:
        v = x // k
        k2 = x // v  # largest k with the same quotient
        total -= (k2 - k + 1) * mertens(v)
        k = k2 + 1
    return total


def squarefree_count(z: int) -> int:
    return sum(int(MU[d]) * (z // (d * d)) for d in range(1, isqrt(z) + 1))


def f(N: int) -> int:
    Y = isqrt(N)
    a_total = b_total = 0
    b = 1
    while b * b * b <= Y:
        w = isqrt(Y // (b * b * b))
        a_total += squarefree_count(w)
        b_total += mertens(w)
        b += 1
    assert (a_total + b_total) % 2 == 0
    return (a_total + b_total) // 2


def f_brute(n: int) -> int:
    d = np.zeros(n + 1, dtype=np.int32)
    for k in range(1, n + 1):
        d[k::k] += 1
    return int(np.count_nonzero(d[1:] % 6 == 1))


if __name__ == "__main__":
    assert f(100) == 2
    for n in (1000, 54321, 10**6, 10**7):
        assert f(n) == f_brute(n), n
    assert f(10**8) == 69
    print(f(10**36))  # 793525366
