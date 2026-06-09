import numba
import numpy as np

MOD = 10**9 + 7
N = 10**8

@numba.njit(cache=True)
def mobius_sieve(limit):
    mu = np.ones(limit + 1, dtype=np.int8)
    is_comp = np.zeros(limit + 1, dtype=np.bool_)
    primes = np.empty(limit // 10 + 100, dtype=np.int64)
    cnt = 0
    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes[cnt] = i
            cnt += 1
            mu[i] = -1
        for j in range(cnt):
            p = primes[j]
            if i * p > limit:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu

@numba.njit(cache=True)
def pow_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result

@numba.njit(cache=True)
def solve(n):
    """G(n) = prod_{m <= n} g(m) mod MOD, g the Gauss factorial.

    Mobius inversion over the coprimality condition gives
        g(m) = prod_{d | m} ((m/d)! * d^(m/d))^mu(d),
    so, swapping the product order with M = n // d and T(M) = M(M+1)/2,
        G(n) = prod_d (SF(M) * d^T(M))^mu(d),
    where SF(M) = prod_{m <= M} m! is the superfactorial. Group the d with
    equal quotient M = n // d (O(sqrt n) blocks): per block the factor is
        SF(M)^(sum mu(d)) * (prod d^mu(d))^T(M),
    needing only the running products of d over mu = +1 and mu = -1 and two
    modular powers. SF is evaluated at the block quotients during one linear
    factorial pass. Exponents of d reduce mod MOD - 1 by Fermat (d < MOD).
    Negative Mobius signs are collected into a denominator and inverted once.
    """
    mu = mobius_sieve(n)

    # Distinct quotients M = n // d in increasing order of d.
    quotients = np.empty(2 * int(np.sqrt(n)) + 4, dtype=np.int64)
    nq = 0
    d = 1
    while d <= n:
        m = n // d
        quotients[nq] = m
        nq += 1
        d = n // m + 1
    # SF at each quotient (quotients are decreasing in this order).
    sf_at = np.empty(nq, dtype=np.int64)
    fact = 1
    sf = 1
    ptr = nq - 1  # smallest quotient first
    for m in range(1, n + 1):
        fact = fact * m % MOD
        sf = sf * fact % MOD
        while ptr >= 0 and quotients[ptr] == m:
            sf_at[ptr] = sf
            ptr -= 1

    numer = 1
    denom = 1
    d = 1
    qi = 0
    while d <= n:
        m = n // d
        d_hi = n // m
        plus = 1  # product of d with mu = +1 in the block
        minus = 1
        s = 0  # sum of mu over the block
        for dd in range(d, d_hi + 1):
            if mu[dd] == 1:
                plus = plus * dd % MOD
                s += 1
            elif mu[dd] == -1:
                minus = minus * dd % MOD
                s -= 1
        t = m * (m + 1) // 2 % (MOD - 1)
        block_pow = pow_mod(plus, t, MOD) * pow_mod(pow_mod(minus, t, MOD), MOD - 2, MOD) % MOD
        sf_part = pow_mod(sf_at[qi], abs(s), MOD)
        if s >= 0:
            numer = numer * sf_part % MOD
        else:
            denom = denom * sf_part % MOD
        numer = numer * block_pow % MOD
        d = d_hi + 1
        qi += 1
    return numer * pow_mod(denom, MOD - 2, MOD) % MOD

if __name__ == "__main__":
    assert solve(10) == 23044331520000 % MOD
    print(solve(N))  # 785845900
