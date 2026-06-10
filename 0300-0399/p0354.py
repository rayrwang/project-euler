import math

import numpy as np


def _primes_upto(n: int) -> np.ndarray:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.nonzero(sieve)[0]


def solve(limit: int = 5 * 10**11) -> int:
    """Count distances L <= limit with B(L) = 450 in a unit-hexagon honeycomb,
    where B(L) is the number of cells whose centre is exactly L from a fixed cell.

    Cell centres form a triangular lattice; a centre a*v1 + b*v2 sits at squared
    distance L^2 = 3*(a^2 + a b + b^2). So B(L) equals the number of integer
    representations of m = L^2 / 3 by the Loeschian form a^2 + a b + b^2, which is
        r(m) = 6 * prod_{p == 1 (mod 3)} (e_p + 1),
    zero unless every prime == 2 (mod 3) occurs to an even power (3 is neutral).
    Each Loeschian m with r(m) = 450 yields exactly one distance L = sqrt(3 m), so
    we count Loeschian m <= limit^2 / 3 with r(m) = 450.

    r(m) = 450 means prod (e_p + 1) = 75 over primes p == 1 (mod 3). The
    factorizations of 75 into parts >= 2 give the exponent patterns
        {74}, {2, 24}, {4, 14}, {2, 4, 4}.
    Write m = K * M, where K carries the == 1 (mod 3) primes with one of those
    patterns and M has no prime == 1 (mod 3) and every == 2 (mod 3) prime to an
    even power, i.e. M = 3^c * t^2 with t composed only of == 2 (mod 3) primes.
    Then the answer is sum over valid K of G(N / K), with N = limit^2 / 3 and
        G(y) = #{M <= y} = sum_{c >= 0} T( floor( sqrt(y / 3^c) ) ),
    where T(z) counts the z-or-smaller integers all of whose prime factors are
    == 2 (mod 3).
    """
    n_max = limit * limit // 3

    # exponent-2 prime in {2,4,4} ranges up to ~sqrt(N / 7^4 / 13^4); size the sieve to it.
    prime_bound = int(math.isqrt(n_max // (7**4 * 13**4))) + 1000
    p1 = [int(p) for p in _primes_upto(prime_bound) if p % 3 == 1]

    # enumerate the == 1 (mod 3) parts K for each exponent pattern
    ks: list[int] = []
    for p in p1:  # pattern {74}
        if p**74 <= n_max:
            ks.append(p**74)
        else:
            break
    for q in p1:  # pattern {2, 24}
        if q**24 > n_max:
            break
        for p in p1:
            if p == q:
                continue
            v = p * p * q**24
            if v <= n_max:
                ks.append(v)
            else:
                break
    for q in p1:  # pattern {4, 14}
        if q**14 > n_max:
            break
        for p in p1:
            if p == q:
                continue
            v = p**4 * q**14
            if v <= n_max:
                ks.append(v)
            else:
                break
    for i, q in enumerate(p1):  # pattern {2, 4, 4}: q < s carry exponent 4, p carries 2
        if i + 1 < len(p1) and q**4 * p1[i + 1] ** 4 > n_max:
            break
        for j in range(i + 1, len(p1)):
            s = p1[j]
            base = q**4 * s**4
            if base > n_max:
                break
            for p in p1:
                if p == q or p == s:
                    continue
                v = p * p * base
                if v <= n_max:
                    ks.append(v)
                else:
                    break

    # T(z): count of z-smooth-by-(==2 mod 3) integers; sieve up to max needed sqrt
    z_max = int(math.isqrt(n_max // min(ks))) + 10
    spf = np.zeros(z_max + 1, dtype=np.int64)
    primes: list[int] = []
    is_comp = bytearray(z_max + 1)
    for i in range(2, z_max + 1):
        if not is_comp[i]:
            primes.append(i)
            spf[i] = i
        for p in primes:
            if i * p > z_max:
                break
            is_comp[i * p] = 1
            spf[i * p] = p
            if i % p == 0:
                break
    smooth = np.zeros(z_max + 1, dtype=bool)
    smooth[1] = True
    for m in range(2, z_max + 1):
        p = spf[m]
        smooth[m] = (p % 3 == 2) and smooth[m // p]
    t_prefix = np.cumsum(smooth.astype(np.int64))

    def g(y: int) -> int:
        total = 0
        pow3 = 1
        while pow3 <= y:
            total += int(t_prefix[int(math.isqrt(y // pow3))])
            pow3 *= 3
        return total

    return sum(g(n_max // k) for k in ks)


if __name__ == "__main__":
    print(solve())  # 58065134
