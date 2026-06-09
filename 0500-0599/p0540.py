"""Project Euler Problem 540: Counting Primitive Pythagorean Triples.

P(n) counts primitive triples a<b<c<=n.  Primitive triples correspond bijectively
to pairs (m,k) with m>k>=1, gcd(m,k)=1 and m,k of opposite parity, via
c = m^2 + k^2.  So P(N) counts such pairs with m^2 + k^2 <= N.

Among coprime pairs (m>k>=1, m^2+k^2<=N), exactly those of mixed parity are
primitive; the coprime pairs split into mixed-parity and both-odd (both-even is
impossible when coprime).  Hence P(N) = C - D where

    C = #{coprime pairs}          = sum_d mu(d) T(floor(N/d^2)),
    D = #{coprime both-odd pairs} = sum_{d odd} mu(d) Todd(floor(N/d^2)),

with T(X) = #{a>b>=1 : a^2+b^2<=X} and Todd(X) the same with a,b both odd.  Each is
obtained from a circle count in O(sqrt X).  Checks: P(20)=3, P(10^6)=159139.
"""

import numpy as np
import numba


@numba.jit(cache=True)
def _isqrt(n: int) -> int:
    if n < 0:
        return -1
    x = int(n**0.5)
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@numba.jit(cache=True)
def _mobius(R: int) -> np.ndarray:
    mu = np.zeros(R + 1, dtype=np.int64)
    comp = np.zeros(R + 1, dtype=np.bool_)
    primes = np.empty(R // 10 + 1000, dtype=np.int64)
    np_ = 0
    mu[1] = 1
    for i in range(2, R + 1):
        if not comp[i]:
            primes[np_] = i
            np_ += 1
            mu[i] = -1
        j = 0
        while j < np_:
            p = primes[j]
            ip = i * p
            if ip > R:
                break
            comp[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
            j += 1
    return mu


@numba.jit(cache=True)
def _T(X: int) -> int:
    # #{a>b>=1 : a^2+b^2 <= X}
    A = 0
    amax = _isqrt(X)
    for a in range(1, amax + 1):
        A += _isqrt(X - a * a)
    diag = _isqrt(X // 2)  # a=b>=1 with 2a^2<=X
    return (A - diag) // 2


@numba.jit(cache=True)
def _Todd(X: int) -> int:
    # #{a>b>=1, both odd : a^2+b^2 <= X}
    A = 0
    a = 1
    while a * a <= X:
        L = _isqrt(X - a * a)
        A += (L + 1) // 2          # count of odd b in [1, L]
        a += 2
    d = _isqrt(X // 2)
    diag = (d + 1) // 2            # odd a with 2a^2<=X
    return (A - diag) // 2


@numba.jit(cache=True)
def _P(N: int, mu: np.ndarray) -> int:
    R = _isqrt(N)
    C = 0
    D = 0
    for d in range(1, R + 1):
        md = mu[d]
        if md == 0:
            continue
        X = N // (d * d)
        C += md * _T(X)
        if d % 2 == 1:
            D += md * _Todd(X)
    return C - D


def P(N: int) -> int:
    R = _isqrt(N)
    mu = _mobius(R)
    return int(_P(N, mu))


if __name__ == "__main__":
    assert P(20) == 3, P(20)
    assert P(10**6) == 159139, P(10**6)
    print(P(3141592653589793))  # 500000000002845
