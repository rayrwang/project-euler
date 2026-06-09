import numba
import numpy as np

MOD = 10**9 + 7

@numba.jit(cache=True)
def spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

@numba.jit(cache=True)
def mod_pow(a: int, b: int, p: int) -> int:
    r = 1
    a %= p
    while b > 0:
        if b & 1:
            r = r * a % p
        a = a * a % p
        b >>= 1
    return r

@numba.jit(cache=True)
def factor_term(q: int, e: int, mod: int) -> int:
    """sigma* factor for prime power q^e: q^e + 1 if e > 0, else 1."""
    if e == 0:
        return 1
    pe = 1
    for _ in range(e):
        pe = pe * q % mod
    return (pe + 1) % mod

@numba.jit(cache=True)
def binomial_retraction_sum(n: int, mod: int) -> int:
    """sum_{k=1}^{n-1} R(C(n, k)) mod `mod`, with R(m) = sigma*(m) - m.

    Slide k upward: C(n, k+1) = C(n, k) * (n - k) / (k + 1), so only the
    primes of n - k and k + 1 change. Keep the exponent of every prime in
    the current C, its value V mod p, and its unitary divisor sum
    S = prod (q^e + 1) mod p; each changed prime updates S by one modular
    inverse (Fermat) and one fresh factor.
    """
    spf = spf_sieve(n)
    exp = np.zeros(n + 1, dtype=np.int32)
    v = 1  # C(n, k) mod p
    s = 1  # sigma*(C(n, k)) mod p
    total = 0
    for k in range(n - 1):
        # C(n, k) -> C(n, k+1): multiply n - k, divide k + 1
        for x, sign in ((n - k, 1), (k + 1, -1)):
            while x > 1:
                q = spf[x]
                d = 0
                while x % q == 0:
                    x //= q
                    d += 1
                e0 = exp[q]
                e1 = e0 + sign * d
                exp[q] = e1
                s = s * mod_pow(factor_term(q, e0, mod), mod - 2, mod) % mod
                s = s * factor_term(q, e1, mod) % mod
                if sign > 0:
                    v = v * mod_pow(q, d, mod) % mod
                else:
                    v = v * mod_pow(mod_pow(q, d, mod), mod - 2, mod) % mod
        total = (total + s - v) % mod
    return total % mod

def brute(n: int) -> int:
    from math import comb

    def sigma_star(m: int) -> int:
        prod = 1
        d = 2
        while d * d <= m:
            if m % d == 0:
                pe = 1
                while m % d == 0:
                    pe *= d
                    m //= d
                prod *= pe + 1
            d += 1
        if m > 1:
            prod *= m + 1
        return prod

    return sum(sigma_star(comb(n, k)) - comb(n, k) for k in range(1, n))

if __name__ == "__main__":
    assert binomial_retraction_sum(20, MOD) == brute(20) % MOD
    assert binomial_retraction_sum(35, MOD) == brute(35) % MOD
    assert binomial_retraction_sum(100_000, MOD) == 628701600  # given
    print(binomial_retraction_sum(10**7, MOD))  # 659104042
