"""Project Euler Problem 530: GCD of Divisors.

f(n) = sum_{d|n} gcd(d, n/d),  F(k) = sum_{n=1}^k f(n).  Find F(10^15).

Summing f over n<=N is the same as summing gcd(d, e) over every ordered pair with
d*e <= N (each n contributes its divisor pairs (d, n/d)).  Using
gcd(d, e) = sum_{g | d, g | e} phi(g) and writing d = g a, e = g b:

    F(N) = sum_{d e <= N} gcd(d, e)
         = sum_{g>=1} phi(g) * #{(a,b) : a b <= floor(N/g^2)}
         = sum_{g^2 <= N} phi(g) * D(floor(N/g^2)),

where D(M) = sum_{a<=M} floor(M/a) is the divisor-summatory function, evaluated in
O(sqrt M) by the hyperbola method.  The whole sum costs about O(sqrt(N) log N).
F(10) = 32 and F(1000) = 12776 serve as checks.
"""

import numpy as np
import numba

from funcs import totient_sieve


@numba.jit(cache=True)
def _isqrt(n: int) -> int:
    x = int(n**0.5)
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@numba.jit(cache=True)
def _D(M: int) -> int:
    # sum_{a=1}^{M} floor(M/a) via hyperbola
    s = _isqrt(M)
    total = 0
    for a in range(1, s + 1):
        total += M // a
    return 2 * total - s * s


@numba.jit(cache=True)
def _F(N: int, phi: np.ndarray) -> int:
    total = 0
    g = 1
    while g * g <= N:
        total += phi[g] * _D(N // (g * g))
        g += 1
    return total


def F(N: int) -> int:
    r = _isqrt(N)
    phi = totient_sieve(r + 1)
    return int(_F(N, phi))


if __name__ == "__main__":
    assert F(10) == 32, F(10)
    assert F(1000) == 12776, F(1000)
    print(F(10**15))  # 207366437157977206
