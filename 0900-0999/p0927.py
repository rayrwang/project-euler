"""Project Euler 927: Prime-ary Tree.

t_k(0) = 1 and t_k(n+1) = t_k(n)^k + 1 (the root is a leaf or has k
subtrees of height <= n), so m is in S_k iff the orbit of 1 under
x -> x^k + 1 mod m hits 0.

Key reduction: if gcd(e, lambda) = 1, where lambda = lcm of (l - 1) over
the primes l | m (m squarefree), then x -> x^e is a bijection on Z/l for
every l | m (it fixes 0 and permutes the units), hence x -> x^e + 1 is a
permutation of Z/m.  Permutations have no tails, so 0 is periodic and
the orbit of 1 = f(0) necessarily returns to 0.  By Dirichlet, prime
exponents realise every residue class coprime to lambda, and a prime p
has gcd(p mod lambda, lambda) > 1 only when p | lambda.  Therefore

    m in S  <=>  the orbit hits 0 for every prime p | lambda(m),

a handful of tests instead of infinitely many.  For prime l the tests
are the primes dividing l - 1; a Brent-cycle scan over all primes up to
10^7 leaves 28 "S-primes" (2, 5, 149, 293, 1601, 45197, ...).  S is
closed under divisors, and the square of every S-prime with q^2 <= 10^7
already fails the exponent-2 test, so S contains only squarefree
products of S-primes; each of the 63 candidate products <= 10^7 is
tested against the primes dividing lcm(l_i - 1).

Validated with the given R(20) = 18 and R(1000) = 2089 (the latter also
cross-checked by brute intersection of S_p over primes p < 2000).
"""

from math import gcd, isqrt

import numpy as np
from numba import njit


@njit(cache=True, inline="always")
def _f_step(x, e, m):
    r = 1
    b = x % m
    ee = e
    while ee:
        if ee & 1:
            r = r * b % m
        b = b * b % m
        ee >>= 1
    return (r + 1) % m


@njit(cache=True)
def hits_zero(m, e):
    """Does the orbit of 1 under x -> x^e + 1 mod m hit 0?  (Brent)."""
    if m == 1:
        return True
    power = 1
    lam = 1
    tort = 1
    hare = _f_step(1, e, m)
    if hare == 0:
        return True
    while tort != hare:
        if power == lam:
            tort = hare
            power *= 2
            lam = 0
        hare = _f_step(hare, e, m)
        if hare == 0:
            return True
        lam += 1
    return False


@njit(cache=True)
def s_primes_mask(primes):
    """l in S iff the orbit hits 0 for every prime p | l - 1."""
    out = np.zeros(len(primes), dtype=np.bool_)
    for i in range(len(primes)):
        m = primes[i] - 1
        ok = True
        d = 2
        while d * d <= m:
            if m % d == 0:
                if not hits_zero(primes[i], d):
                    ok = False
                    break
                while m % d == 0:
                    m //= d
            d += 1
        if ok and m > 1:
            ok = hits_zero(primes[i], m)
        out[i] = ok
    return out


def _prime_factors(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def compute_s(n_max: int) -> list[int]:
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, isqrt(n_max) + 1):
        if sieve[i]:
            sieve[i * i:: i] = False
    primes = np.flatnonzero(sieve).astype(np.int64)
    sp = [int(x) for x in primes[s_primes_mask(primes)]]

    # squares of S-primes all fail (so S is squarefree by closure)
    for q in sp:
        if q * q > n_max:
            break
        assert not hits_zero(q * q, 2), q

    s = set([1]) | set(sp)
    prods: list[tuple[int, tuple[int, ...]]] = []

    def gen(idx: int, prod: int, used: tuple[int, ...]) -> None:
        if len(used) >= 2:
            prods.append((prod, used))
        for i in range(idx, len(sp)):
            if prod * sp[i] > n_max:
                break
            gen(i + 1, prod * sp[i], used + (sp[i],))

    gen(0, 1, ())
    for prod, ls in prods:
        big_l = 1
        for ell in ls:
            big_l = big_l * (ell - 1) // gcd(big_l, ell - 1)
        if all(hits_zero(prod, p) for p in _prime_factors(big_l)):
            s.add(prod)
    return sorted(s)


def solve(n_max: int) -> int:
    return sum(compute_s(n_max))


if __name__ == "__main__":
    s_small = compute_s(1000)
    assert sum(m for m in s_small if m <= 20) == 18  # given
    assert sum(s_small) == 2089  # given R(1000)
    print(solve(10**7))  # 207282955
