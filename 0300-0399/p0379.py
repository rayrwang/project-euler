import math

import numba
import numpy as np


@numba.njit
def _isqrt(n: int) -> int:
    if n < 0:
        return 0
    x = int(math.sqrt(n))
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@numba.njit
def d3_summatory(m: int) -> int:
    """sum_{n<=m} d_3(n) = number of ordered triples (a, b, c) with a*b*c <= m.

    Enumerate only sorted triples a <= b <= c with a <= cbrt(m) and
    b <= sqrt(m/a), then weight each by its number of orderings (6 if all
    distinct, 3 if exactly two are equal, 1 if all equal). The enumerated
    (a, b) pairs number O(m^(2/3)), which keeps this fast even at m = 10^12.
    """
    total = 0
    a = 1
    while a * a * a <= m:
        ma = m // a
        sb = _isqrt(ma)
        b = a
        while b <= sb:
            cmax = ma // b
            if cmax < b:
                break
            cnt = cmax - b + 1  # values of c in [b, cmax]
            if a == b:
                total += 1 + 3 * (cnt - 1)  # c=b all equal; c>b gives a=b<c
            else:
                total += 3 + 6 * (cnt - 1)  # c=b gives b=c; c>b all distinct
            b += 1
        a += 1
    return total


@numba.njit
def _d_sum(n: int, mu: np.ndarray, r: int) -> int:
    # D(N) = sum_{n<=N} d(n^2) = sum_{d<=sqrt N} mu(d) * D_3(N / d^2),
    # using d(n^2) = (1 * 1 * mu^2)(n) and mu^2(c) = sum_{d^2 | c} mu(d).
    s = 0
    for d in range(1, r + 1):
        if mu[d]:
            s += mu[d] * d3_summatory(n // (d * d))
    return s


def _mobius(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int64)
    primes = []
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


def g(n: int) -> int:
    """g(N) = sum_{i<=N} f(i), where f(i) counts couples (x, y), x <= y,
    lcm(x, y) = i.

    The number of ordered pairs with lcm = i is multiplicative and equals
    d(i^2) = prod (2*a_j + 1) over the prime exponents a_j; exactly one of
    these pairs is diagonal (x = y = i), so f(i) = (d(i^2) + 1) / 2. Summing,
    g(N) = (D(N) + N) / 2 with D(N) = sum_{i<=N} d(i^2)."""
    r = int(math.isqrt(n))
    return (_d_sum(n, _mobius(r), r) + n) // 2


if __name__ == "__main__":
    # f(6) = 5 couples, recovered as g(6) - g(5), and the given checkpoint.
    assert g(6) - g(5) == 5
    assert g(10**6) == 37429395
    print(g(10**12))  # 132314136838185
