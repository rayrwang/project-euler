import numba
import numpy as np

from funcs import is_prime, prime_sieve_int

MOD = 1234567891

@numba.jit(cache=True)
def lucy_pi(m: int):
    """Prime counts pi(x) at every distinct quotient x = m // i.

    Standard Lucy_Hedgehog sieve: small[i] = pi(i) for i <= sqrt(m) and
    large[i] = pi(m // i), refined prime by prime in O(m^(3/4)).
    """
    r = int(m**0.5)
    while (r + 1) * (r + 1) <= m:
        r += 1
    while r * r > m:
        r -= 1
    small = np.empty(r + 1, dtype=np.int64)
    large = np.empty(r + 1, dtype=np.int64)
    for i in range(1, r + 1):
        small[i] = i - 1
        large[i] = m // i - 1
    for p in range(2, r + 1):
        if small[p] == small[p - 1]:
            continue  # p not prime
        sp = small[p - 1]
        p2 = p * p
        imax = min(r, m // p2)
        for i in range(1, imax + 1):
            d = i * p
            if d <= r:
                large[i] -= large[d] - sp
            else:
                large[i] -= small[m // d] - sp
        for i in range(r, p2 - 1, -1):
            small[i] -= small[i // p] - sp
    return small, large

@numba.jit(cache=True)
def pi_at(x: int, m: int, small: np.ndarray, large: np.ndarray) -> int:
    if x <= len(small) - 1:
        return small[x]
    return large[m // x]

@numba.jit(cache=True)
def dfs(d: int, idx: int, fd: int, m: int, n_mod: int, primes: np.ndarray,
        binoms: np.ndarray, small: np.ndarray, large: np.ndarray,
        mod: int) -> int:
    """Sum of f over numbers built on the smooth base d.

    Adds (a) d times exactly one prime larger than all of d's, in bulk via
    pi(m/d); (b) numbers extending d by a prime power p_j^e with
    p_j^2 <= m/d — counted directly when e >= 2 (numbers whose largest
    prime is repeated), and recursed in all cases. Bases with largest
    prime to exponent 1 are never self-counted: the parent's bulk term
    already covered them.
    """
    total = 0
    quota = m // d
    cnt = pi_at(quota, m, small, large) - idx
    if cnt > 0:
        total = fd * n_mod % mod * (cnt % mod) % mod
    j = idx
    while j < len(primes) and primes[j] * primes[j] <= quota:
        p = primes[j]
        v = d * p
        e = 1
        while True:
            fe = fd * binoms[e] % mod
            if e >= 2:
                total = (total + fe) % mod
            total = (total + dfs(v, j + 1, fe, m, n_mod, primes, binoms,
                                 small, large, mod)) % mod
            if v > m // p:
                break
            v *= p
            e += 1
        j += 1
    return total % mod

def long_products(m: int, n: int, mod: int) -> int:
    """F(m, n): n-tuples of positive integers with product <= m, mod p.

    F = sum_{k<=m} d_n(k) with the n-dimensional divisor function
    d_n(k) = prod_p binom(e_p + n - 1, e_p) — multiplicative with the
    same value n at every prime. Split each k > 1 by whether its largest
    prime factor has exponent 1: those are base * (one larger prime),
    counted in bulk with Lucy prime counts; the rest have their largest
    prime squared, which forces the cascading condition p^2 <= m/base and
    makes the whole DFS reachable set small (about 10^6 nodes at 10^9).
    """
    small, large = lucy_pi(m)
    r = len(small) - 1
    primes = prime_sieve_int(r + 1)
    # binom(n - 1 + e, e) mod p for e up to log2(m)
    emax = m.bit_length() + 1
    binoms = np.empty(emax + 1, dtype=np.int64)
    binoms[0] = 1
    for e in range(1, emax + 1):
        binoms[e] = (binoms[e - 1] * ((n - 1 + e) % mod) % mod
                     * pow(e, mod - 2, mod) % mod)
    total = (1 + dfs(1, 0, 1, m, n % mod, primes, binoms, small, large,
                     mod)) % mod
    return total

def brute(m: int, n: int, mod: int) -> int:
    def d_n(k: int) -> int:
        out = 1
        d = 2
        while d * d <= k:
            if k % d == 0:
                e = 0
                while k % d == 0:
                    k //= d
                    e += 1
                b = 1
                for j in range(1, e + 1):
                    b = b * (n - 1 + j) // j
                out *= b % mod
            d += 1
        if k > 1:
            out *= n % mod
        return out % mod
    return sum(d_n(k) for k in range(1, m + 1)) % mod

if __name__ == "__main__":
    assert is_prime(MOD)
    assert long_products(10, 10, MOD) == 571  # given
    assert long_products(10**4, 7, MOD) == brute(10**4, 7, MOD)
    assert long_products(10**5, 10**5, MOD) == brute(10**5, 10**5, MOD)
    assert long_products(10**6, 10**6, MOD) == 252903833  # given
    print(long_products(10**9, 10**9, MOD))  # 345558983
