import numba
import numpy as np

MOD = 10**9  # = 2^9 * 5^9

@numba.jit(cache=True)
def half_prod(a: int, b: int, mod: int) -> int:
    """a*b/2 mod `mod` where a*b is even (exact halving first)."""
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    return (a % mod) * (b % mod) % mod

@numba.jit(cache=True)
def sigma_summatory(m: int, mod: int) -> int:
    """T(M) = sum_{k<=M} sigma(k) = sum_k k * floor(M/k), mod `mod`."""
    total = 0
    k = 1
    while k <= m:
        q = m // k
        k2 = m // q
        total = (total + (q % mod) * half_prod(k + k2, k2 - k + 1, mod)) % mod
        k = k2 + 1
    return total

@numba.jit(cache=True)
def sum_sigma_products(n: int, d0: int, mod: int) -> int:
    """S(N) = sum_{i,j<=N} sigma(i j) mod `mod`.

    From sigma(i j) = sum_{d | gcd(i,j)} mu(d) d sigma(i/d) sigma(j/d)
    (verified directly), summing over i, j decouples:
        S(N) = sum_d mu(d) d T(floor(N/d))^2,  T(M) = sum_{m<=M} sigma(m).
    Both factors live on the quotients of N: T by hyperbola blocks in
    O(sqrt M) each, and the weighted Mertens M_1(y) = sum_{d<=y} mu(d) d
    by the sublinear recurrence sum_k k M_1(y/k) = 1 over a sieved base.
    The composite modulus 10^9 only ever needs division by 2, handled by
    exact halving before reduction.
    """
    r = int(n**0.5)
    while (r + 1) * (r + 1) <= n:
        r += 1
    while r * r > n:
        r -= 1
    # Mobius sieve and prefix of mu(d)*d on the base
    mu = np.ones(d0 + 1, dtype=np.int8)
    comp = np.zeros(d0 + 1, dtype=np.bool_)
    for p in range(2, d0 + 1):
        if not comp[p]:
            for j in range(p, d0 + 1, p):
                if j > p:
                    comp[j] = True
                mu[j] = -mu[j]
            pp = p * p
            for j in range(pp, d0 + 1, pp):
                mu[j] = 0
    m1s = np.zeros(d0 + 1, dtype=np.int32)
    acc = 0
    for i in range(1, d0 + 1):
        if mu[i] != 0:
            acc = (acc + mu[i] * (i % mod)) % mod
        m1s[i] = acc
    # weighted Mertens at big quotients y = n // i
    nbig = n // d0
    m1b = np.zeros(nbig + 1, dtype=np.int64)
    for i in range(nbig, 0, -1):
        y = n // i
        s = 1
        k = 2
        while k <= y:
            q = y // k
            k2 = y // q
            if q <= d0:
                v = m1s[q]
            else:
                v = m1b[n // q]
            s = (s - half_prod(k + k2, k2 - k + 1, mod) * v) % mod
            k = k2 + 1
        m1b[i] = s
    # main sum over quotient blocks of d
    total = 0
    d = 1
    prev = 0  # M_1(d - 1)
    while d <= n:
        q = n // d
        d2 = n // q
        cur = m1s[d2] if d2 <= d0 else m1b[n // d2]
        t = sigma_summatory(q, mod)
        total = (total + (cur - prev) * (t * t % mod)) % mod
        prev = cur
        d = d2 + 1
    return total % mod

def brute(n: int) -> int:
    sig = np.zeros(n * n + 1, dtype=np.int64)
    for d in range(1, n * n + 1):
        sig[d::d] += d
    return int(sum(sig[i * j] for i in range(1, n + 1)
                   for j in range(1, n + 1)))

if __name__ == "__main__":
    assert sum_sigma_products(3, 10, MOD) == brute(3) == 59  # given
    assert sum_sigma_products(50, 10, MOD) == brute(50)
    assert sum_sigma_products(10**3, 100, MOD) == 563576517282 % MOD  # given
    assert sum_sigma_products(10**5, 2500, MOD) == 215766508  # given
    print(sum_sigma_products(10**11, 3 * 10**7, MOD))  # 968697378
