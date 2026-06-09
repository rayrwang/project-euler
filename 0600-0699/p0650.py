"""Project Euler Problem 650: Divisors of Binomial Product.

B(n) = prod_k binom(n, k) = (n!)^(n+1) / (prod_{k=0}^{n} k!)^2, so with the
superfactorial F(n) = prod_{k<=n} k! the exponent of a prime p in B(n) is

    e_p(B(n)) = (n + 1) e_p(n!) - 2 e_p(F(n)).

Walk n from 1 to 20000 maintaining e_p(n!) per prime (add the factorisation
of n each step, via a smallest-prime-factor sieve) and the cumulative
e_p(F(n)).  Then

    D(n) = sigma(B(n)) = prod_{p <= n} (p^(e_p + 1) - 1) / (p - 1)  mod p,

recomputed in full each step (the exponents of every prime change with n
because of the (n + 1) weight), about sum_n pi(n) = 2.6 * 10^7 modular
exponentiations under numba.  The largest exponent, (n + 1) e_2(n!), is
around 4 * 10^8 and fits comfortably in int64.

Checks: S(5) = 5736, S(10) = 141740594713218418 mod p, S(100) = 332792866.
"""

import numba
import numpy as np

MOD = 10**9 + 7
N = 20000


def primes_and_spf(n: int) -> tuple[np.ndarray, np.ndarray]:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    primes = np.flatnonzero(spf[2:] == np.arange(2, n + 1)) + 2
    return primes.astype(np.int64), spf


@numba.jit(cache=True)
def mod_pow(a: int, b: int, mod: int) -> int:
    r = 1
    a %= mod
    while b > 0:
        if b & 1:
            r = r * a % mod
        a = a * a % mod
        b >>= 1
    return r


@numba.jit(cache=True)
def S_values(checkpoints: np.ndarray, primes: np.ndarray, spf: np.ndarray,
             prime_index: np.ndarray) -> np.ndarray:
    inv_pm1 = np.empty(len(primes), dtype=np.int64)
    for i, p in enumerate(primes):
        inv_pm1[i] = mod_pow(p - 1, MOD - 2, MOD)

    e_fact = np.zeros(len(primes), dtype=np.int64)  # e_p(n!)
    e_super = np.zeros(len(primes), dtype=np.int64)  # e_p(F(n))
    out = np.zeros(len(checkpoints), dtype=np.int64)
    s = 0
    n_primes_used = 0  # primes <= n
    ci = 0
    for n in range(1, checkpoints[-1] + 1):
        m = n
        while m > 1:  # add the factorisation of n to e_p(n!)
            p = spf[m]
            while m % p == 0:
                m //= p
                e_fact[prime_index[p]] += 1
        while n_primes_used < len(primes) and primes[n_primes_used] <= n:
            n_primes_used += 1
        d = 1
        for i in range(n_primes_used):
            e_super[i] += e_fact[i]
            e = (n + 1) * e_fact[i] - 2 * e_super[i]
            if e > 0:
                term = (mod_pow(primes[i], e + 1, MOD) - 1) * inv_pm1[i] % MOD
                d = d * term % MOD
        s = (s + d) % MOD
        if n == checkpoints[ci]:
            out[ci] = s
            ci += 1
    return out


if __name__ == "__main__":
    primes, spf = primes_and_spf(N)
    prime_index = np.zeros(N + 1, dtype=np.int64)
    prime_index[primes] = np.arange(len(primes))
    s5, s10, s100, s20000 = S_values(
        np.array([5, 10, 100, N], dtype=np.int64), primes, spf, prime_index
    )
    assert s5 == 5736, s5
    assert s10 == 141740594713218418 % MOD, s10
    assert s100 == 332792866, s100
    print(s20000)  # 538319652
