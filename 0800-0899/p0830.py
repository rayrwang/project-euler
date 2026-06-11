"""Project Euler 830: Binomials and Powers.

Expanding k^n in falling factorials with Stirling numbers and using
sum_k C(n,k) k^(j) = n^(j) 2^(n-j) gives

    S(n) = sum_{j=0}^{n} S2(n, j) * n^(j) * 2^(n-j),

where every term is an integer multiple of the falling factorial
n^(j) = n(n-1)...(n-j+1).  Modulo p^3 a term therefore dies as soon as
the descending window from n accumulates three factors of p, which for
n = 10^18 happens within j of order 4p — a few hundred terms per
prime.  Regrouping the surviving terms as C(n, j) * D_j * 2^(n-j),
with D_j = sum_i (-1)^(j-i) C(j, i) i^n the number of surjections onto
j blocks, avoids dividing by j! (not invertible mod p^3 once j >= p):
C(n, j) is computed exactly as a big integer for j <= 400 and reduced,
i^n by modular exponentiation.

The three residues modulo 83^3, 89^3 and 97^3 are combined by the
Chinese Remainder Theorem.  The machinery is validated against the
exact sum for n up to 500, including the given S(10) = 142469423360,
and evaluates S(10^18) instantly.
"""

from __future__ import annotations

from math import comb, prod

PRIMES = (83, 89, 97)
MOD = prod(p**3 for p in PRIMES)


def s_mod_p3(n: int, p: int) -> int:
    p3 = p**3
    cutoff = n
    v = 0
    j = 0
    while j < n:
        j += 1
        x = n - j + 1
        if x <= 0:
            break
        while x % p == 0:
            v += 1
            x //= p
        if v >= 3:
            cutoff = j - 1
            break
    cutoff = min(cutoff, n)
    total = 0
    for jj in range(cutoff + 1):
        surj = 0
        for i in range(jj + 1):
            t = comb(jj, i) % p3 * pow(i, n, p3) % p3
            surj = (surj + (1 if (jj - i) % 2 == 0 else -1) * t) % p3
        term = comb(n, jj) % p3 * surj % p3 * pow(2, n - jj, p3) % p3
        total = (total + term) % p3
    return total


def s_mod(n: int) -> int:
    x = 0
    for p in PRIMES:
        m = p**3
        r = s_mod_p3(n, p)
        big = MOD // m
        x += r * big * pow(big, -1, m)
    return x % MOD


def s_exact(n: int) -> int:
    return sum(comb(n, k) * k**n for k in range(n + 1))


def main() -> None:
    assert s_exact(10) == 142469423360
    for n in (1, 2, 5, 10, 50, 200, 500):
        assert s_mod(n) == s_exact(n) % MOD
    print(s_mod(10**18))  # 254179446930484376


if __name__ == "__main__":
    main()
