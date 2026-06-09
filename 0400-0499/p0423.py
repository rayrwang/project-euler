import numba
import numpy as np

from funcs import prime_sieve_bool

MOD = 10**9 + 7

@numba.jit(cache=True)
def consecutive_throw_sum(limit: int, mod: int) -> int:
    """S(L) = sum_{n=1}^{L} C(n) mod `mod`.

    A sequence of n throws has c equal consecutive pairs by choosing which
    of the n-1 transitions repeat (1 way each) or change (5 ways each), so
    exactly c pairs happen in 6 * binom(n-1, c) * 5^(n-1-c) ways and
    C(n) = 6 * T, with the binomial tail T = sum_{c <= pi(n)} binom(k, c) 5^(k-c)
    for k = n - 1. T is maintained incrementally:
    - k -> k+1 (same m):  T <- 6T - binom(k, m) 5^(k-m), from Pascal's rule;
    - m -> m+1 at primes: T <- T + binom(k, m+1) 5^(k-m-1).
    The tracked binomial and power of 5 update in O(1) with precomputed
    modular inverses, so the whole sum is linear in L.
    """
    is_pr = prime_sieve_bool(limit + 2)
    inv = np.zeros(limit + 2, dtype=np.int64)  # inverses of 1..limit+1 mod p
    inv[1] = 1
    for i in range(2, limit + 2):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod
    inv5 = inv[5]

    # state at n: k = n-1, m = pi(n), T, b = binom(k, m), f = 5^(k-m)
    k = 0
    m = 0
    t = 1  # binom(0,0) * 5^0
    b = 1
    f = 1
    total = 6 * t % mod
    for n in range(2, limit + 1):
        # k -> k+1
        t = (6 * t - b * f) % mod
        b = b * (k + 1) % mod * inv[k + 1 - m] % mod
        f = f * 5 % mod
        k += 1
        if is_pr[n]:  # pi increments: m -> m+1
            b = b * (k - m) % mod * inv[m + 1] % mod
            f = f * inv5 % mod
            m += 1
            t = (t + b * f) % mod
        total = (total + 6 * t) % mod
    return total % mod

def c_exact(n: int) -> int:
    from math import comb
    pi = sum(1 for p in range(2, n + 1)
             if all(p % d for d in range(2, int(p**0.5) + 1)))
    return 6 * sum(comb(n - 1, c) * 5 ** (n - 1 - c) for c in range(pi + 1))

if __name__ == "__main__":
    assert c_exact(3) == 216
    assert c_exact(4) == 1290
    assert c_exact(11) == 361912500
    assert c_exact(24) == 4727547363281250000
    assert consecutive_throw_sum(50, MOD) == 832833871
    assert consecutive_throw_sum(40, MOD) == sum(
        c_exact(n) for n in range(1, 41)) % MOD
    print(consecutive_throw_sum(50_000_000, MOD))  # 653972374
