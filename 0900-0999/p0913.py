"""Project Euler 913: Row-major vs Column-major.

The minimum number of swaps to realise a permutation is (size) minus the
number of its cycles.  Transforming row-major to column-major moves the
value at 0-based row-major position k to position
(k mod n) m + (k div n) = k m mod (nm - 1) for k < nm - 1, with nm - 1
fixed -- the classical in-place transposition permutation.  Since
n m = 1 (mod nm - 1), multiplication by m and by n are inverse maps and
share the cycle structure.  The cycles of x -> n x on Z_M (M = nm - 1)
split by g = gcd(x, M): the phi(d) elements with d = M/g fall into free
orbits of size ord_d(n), so

    S(n, m) = nm - 1 - sum_{d | M} phi(d) / ord_d(n).

For S(n^4, m^4) the modulus is q^4 - 1 = (q-1)(q+1)(q^2+1) with
q = nm <= 10^4, so every part (and every prime-order helper p - 1)
factors by trial division below 10^4.  Orders modulo prime powers are
lifted stepwise (ord_{p^{j+1}} is ord_{p^j} or p times it), and the
divisor sum runs over exponent tuples carrying running phi and lcm of
orders.  Verified against literal matrix brute force for all
2 <= n <= m <= 11 and against the given total for 2 <= n <= m <= 100.
"""

import math
from functools import lru_cache

LIM = 10**4 + 10
_sieve = bytearray([1]) * LIM
_sieve[0:2] = b"\x00\x00"
for _i in range(2, int(LIM**0.5) + 1):
    if _sieve[_i]:
        _sieve[_i * _i :: _i] = b"\x00" * len(_sieve[_i * _i :: _i])
PRIMES = [i for i in range(LIM) if _sieve[i]]


def factor(x: int) -> dict[int, int]:
    f: dict[int, int] = {}
    for p in PRIMES:
        if p * p > x:
            break
        while x % p == 0:
            f[p] = f.get(p, 0) + 1
            x //= p
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


@lru_cache(maxsize=None)
def _factor_cached(x: int):
    return tuple(sorted(factor(x).items()))


def _ord_prime(a: int, p: int) -> int:
    o = p - 1
    for r, _ in _factor_cached(p - 1):
        while o % r == 0 and pow(a, o // r, p) == 1:
            o //= r
    return o


def cycles(big_m: int, a: int) -> int:
    """#cycles of x -> a x on Z_M, gcd(a, M) = 1."""
    if big_m == 1:
        return 1
    fac = sorted(factor(big_m).items())
    ords, phis = [], []
    for p, e in fac:
        o = [1, _ord_prime(a % p, p)]
        pj = p
        for _ in range(2, e + 1):
            pj *= p
            o.append(o[-1] if pow(a, o[-1], pj) == 1 else o[-1] * p)
        ords.append(o)
        phis.append([1] + [(p - 1) * p ** (j - 1) for j in range(1, e + 1)])
    total = 0

    def dfs(i: int, phi: int, lc: int) -> None:
        nonlocal total
        if i == len(fac):
            total += phi // lc
            return
        o, f = ords[i], phis[i]
        for j in range(fac[i][1] + 1):
            dfs(i + 1, phi * f[j], lc // math.gcd(lc, o[j]) * o[j])

    dfs(0, 1, 1)
    return total


def s_swaps(n: int, m: int) -> int:
    big_n = n * m
    return big_n - 1 - cycles(big_n - 1, n)


def s_brute(n: int, m: int) -> int:
    """Literal: build the R -> C permutation, count its cycles."""
    big_n = n * m
    perm = [(k % n) * m + k // n for k in range(big_n)]
    seen = [False] * big_n
    c = 0
    for k in range(big_n):
        if not seen[k]:
            c += 1
            x = k
            while not seen[x]:
                seen[x] = True
                x = perm[x]
    return big_n - c


def solve() -> int:
    return sum(s_swaps(n**4, m**4)
               for n in range(2, 101) for m in range(n, 101))


if __name__ == "__main__":
    assert s_swaps(3, 4) == 8
    for n in range(2, 12):
        for m in range(n, 12):
            assert s_swaps(n, m) == s_brute(n, m), (n, m)
    total = sum(s_swaps(n, m) for n in range(2, 101) for m in range(n, 101))
    assert total == 12578833  # given
    print(solve())  # 2101925115560555020
