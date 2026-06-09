"""Project Euler 952: Order Modulo Factorial.

R(p, n) = ord of p modulo n! = lcm over prime powers q^e || n! of ord(p mod q^e).
For odd q: ord(p mod q^e) = ord(p mod q) * q^max(0, e - v) with
v = v_q(p^{ord(p mod q)} - 1)  (lifting the exponent).
For q = 2: ord(p mod 2^e) = 2^j with j minimal s.t. v2(p^{2^j}-1) >= e, where
v2(p^{2^j}-1) = v2(p-1) + v2(p+1) + j - 1 for j >= 1.

The lcm is accumulated as max prime exponents (all primes involved are < n,
since ord(p mod q) | q-1), then multiplied out modulo 10^9 + 7.
"""

import numpy as np

P = 10 ** 9 + 7


def spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    spf[1] = 1
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf


def legendre(n: int, q: int) -> int:
    e = 0
    qq = q
    while qq <= n:
        e += n // qq
        qq *= q
    return e


def ord2(p: int, e: int) -> int:
    """v2 exponent j such that ord(p mod 2^e) = 2^j (p odd)."""
    if e <= 0:
        return 0
    v1 = ((p - 1) & -(p - 1)).bit_length() - 1
    if e <= v1:
        return 0
    v2 = ((p + 1) & -(p + 1)).bit_length() - 1
    # for j >= 1: v2(p^(2^j)-1) = v1 + v2 + j - 1
    return max(1, e - (v1 + v2) + 1)


def solve(n: int, p: int) -> int:
    spf = spf_sieve(n)
    maxexp: dict[int, int] = {}

    def bump(prime: int, e: int) -> None:
        if e > maxexp.get(prime, 0):
            maxexp[prime] = e

    bump(2, ord2(p, legendre(n, 2)))

    q = 3
    while q <= n:
        if spf[q] == q:  # prime
            # multiplicative order of p mod q
            d = q - 1
            # factor q-1 with spf
            fac = {}
            m = q - 1
            while m > 1:
                f = int(spf[m])
                fac[f] = fac.get(f, 0) + 1
                m //= f
            for f in fac:
                while d % f == 0 and pow(p, d // f, q) == 1:
                    d //= f
            # exponent of q in n! and lifting
            e = legendre(n, q)
            if e >= 2:
                v = 1
                qq = q * q
                while pow(p, d, qq) == 1:
                    v += 1
                    qq *= q
                bump(q, max(0, e - v))
            # accumulate prime factorization of d into lcm
            m = d
            while m > 1:
                f = int(spf[m])
                c = 0
                while m % f == 0:
                    m //= f
                    c += 1
                bump(f, c)
        q += 2

    ans = 1
    for prime, e in maxexp.items():
        if e:
            ans = ans * pow(prime, e, P) % P
    return ans


if __name__ == "__main__":
    print(solve(10 ** 7, P))  # 794394453
