import numba
import numpy as np

from funcs import prime_sieve_int

MOD = 10**9 + 7

@numba.jit(cache=True)
def mod_pow32(a: int, b: int, p: int) -> int:
    r = 1
    a %= p
    while b > 0:
        if b & 1:
            r = r * a % p
        a = a * a % p
        b >>= 1
    return r

@numba.jit(cache=True)
def sqrt_minus_one(p: int) -> int:
    """A root of x^2 = -1 mod a prime p = 1 (mod 4), via Tonelli-Shanks
    on the cyclic group: z^((p-1)/4) works for any non-residue z."""
    z = 2
    while mod_pow32(z, (p - 1) // 2, p) != p - 1:
        z += 1
    return mod_pow32(z, (p - 1) // 4, p)

@numba.jit(cache=True)
def retraction_quartic_sum(n_max: int, mod: int) -> int:
    """F(N) = sum_{n=1}^{N} R(n^4 + 4) mod `mod`, with R(n) = sigma*(n) - n.

    Sophie Germain: n^4 + 4 = A B with A = (n-1)^2 + 1, B = (n+1)^2 + 1.
    An odd prime dividing both would divide 4n and hence n, forcing it to
    divide 2 — impossible. So sigma*(A B) splits into the odd parts of A
    and B times the power-of-2 part (e_2 = 1 per odd m in m^2 + 1, so the
    factor is 5 for even n and 1 for odd n).

    The odd parts come from one sieve over val[m] = m^2 + 1: each prime
    p = 1 (mod 4) divides m^2 + 1 exactly on m = +-sqrt(-1) (mod p);
    divide out, count the exponent e, and fold (p^e + 1) into g[m].
    Whatever remains in val[m] exceeds the sieve bound, hence is prime
    (two such factors would multiply past m^2 + 1).
    """
    m_top = n_max + 1
    val = np.empty(m_top + 1, dtype=np.int64)
    g = np.ones(m_top + 1, dtype=np.int64)
    for m in range(m_top + 1):
        val[m] = m * m + 1
        if m % 2 == 1:
            val[m] //= 2  # e_2 is exactly 1 for odd m
    for p in prime_sieve_int(m_top + 1):
        if p % 4 != 1:
            continue
        r = sqrt_minus_one(p)
        for start in (r, p - r):
            for m in range(start, m_top + 1, p):
                e = 0
                while val[m] % p == 0:
                    val[m] //= p
                    e += 1
                pe = 1
                for _ in range(e):
                    pe *= p
                g[m] = g[m] * ((pe + 1) % mod) % mod
    for m in range(m_top + 1):
        if val[m] > 1:  # leftover large prime
            g[m] = g[m] * ((val[m] + 1) % mod) % mod
    total = 0
    for n in range(1, n_max + 1):
        sigma = g[n - 1] * g[n + 1] % mod
        if n % 2 == 0:
            sigma = sigma * 5 % mod
        nm = n % mod
        n4 = nm * nm % mod
        n4 = n4 * n4 % mod
        total = (total + sigma - (n4 + 4)) % mod
    return total % mod

def brute(n_max: int) -> int:
    def sigma_star(factors: dict[int, int]) -> int:
        prod = 1
        for p, e in factors.items():
            prod *= p**e + 1
        return prod

    def factorize_into(v: int, factors: dict[int, int]) -> None:
        d = 2
        while d * d <= v:
            while v % d == 0:
                factors[d] = factors.get(d, 0) + 1
                v //= d
            d += 1
        if v > 1:
            factors[v] = factors.get(v, 0) + 1

    total = 0
    for n in range(1, n_max + 1):
        f: dict[int, int] = {}
        factorize_into((n - 1) ** 2 + 1, f)
        factorize_into((n + 1) ** 2 + 1, f)
        total += sigma_star(f) - (n**4 + 4)
    return total

if __name__ == "__main__":
    exact_1024 = brute(1024)
    assert exact_1024 == 77532377300600  # given in the problem
    assert retraction_quartic_sum(1024, MOD) == exact_1024 % MOD
    print(retraction_quartic_sum(10**7, MOD))  # 907803852
