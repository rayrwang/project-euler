import numba
import numpy as np

MOD = 10**9 + 7

@numba.jit(cache=True)
def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    is_comp = np.zeros(n + 1, dtype=np.bool_)
    for p in range(2, n + 1):
        if not is_comp[p]:
            for j in range(p, n + 1, p):
                if j > p:
                    is_comp[j] = True
                mu[j] = -mu[j]
            p2 = p * p
            for j in range(p2, n + 1, p2):
                mu[j] = 0
    return mu

@numba.jit(cache=True)
def triangle_mod(x: int, mod: int) -> int:
    """x(x+1)/2 mod `mod`, halving the even factor before reducing."""
    a, b = x, x + 1
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    return (a % mod) * (b % mod) % mod

@numba.jit(cache=True)
def d1(m: int, mod: int) -> int:
    """sum_{d*k <= m} d = sum_{k <= m} T(floor(m/k)), by quotient blocks."""
    total = 0
    k = 1
    while k <= m:
        q = m // k
        k2 = m // q
        total = (total + ((k2 - k + 1) % mod) * triangle_mod(q, mod)) % mod
    # (loop advance below)
        k = k2 + 1
    return total

@numba.jit(cache=True)
def retraction_sum(n: int, mod: int) -> int:
    """F(N) = sum_{n=2}^{N} R(n) mod `mod`.

    A retraction needs a^2 = a and ab = 0 (mod n) with a != 0, and each
    idempotent a admits gcd(a, n) values of b, so summing over the 2^omega
    idempotents gives sigma*(n) (the unitary divisor sum) minus n for the
    excluded a = 0. Hence F(N) = sum sigma*(n) - N(N+1)/2.

    Unitary divisors unfold as sum_{n<=N} sigma*(n) =
    sum_{d k <= N, gcd(d,k)=1} d, and Mobius inversion over g = gcd gives
    sum_g mu(g) g D(floor(N/g^2)) with D the unrestricted hyperbola sum,
    each evaluated in O(sqrt) quotient blocks.
    """
    gmax = int(n**0.5)
    while gmax * gmax > n:
        gmax -= 1
    mu = mobius_sieve(gmax)
    total = 0
    for g in range(1, gmax + 1):
        if mu[g] != 0:
            total = (total + int(mu[g]) * (g % mod) * d1(n // (g * g), mod)) % mod
    total = (total - triangle_mod(n, mod)) % mod
    return total % mod

def brute(n: int) -> int:
    def r_of(m: int) -> int:
        count = 0
        for a in range(1, m):
            if a * a % m == a:
                count += sum(1 for b in range(m) if a * b % m == 0)
        return count
    return sum(r_of(m) for m in range(2, n + 1))

if __name__ == "__main__":
    assert retraction_sum(60, MOD) == brute(60)
    assert retraction_sum(10**7, MOD) == 638042271  # given in the problem
    print(retraction_sum(10**14, MOD))  # 530553372
