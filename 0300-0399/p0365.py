import numba
import numpy as np

from funcs import prime_sieve_int


def binom_mod_p(n: int, k: int, p: int, fact: list[int], inv_fact: list[int]) -> int:
    """C(n, k) mod p (p prime) via Lucas' theorem, using precomputed factorial
    and inverse-factorial tables modulo p."""
    res = 1
    while n > 0 or k > 0:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        res = res * fact[ni] % p * inv_fact[ki] % p * inv_fact[ni - ki] % p
        n //= p
        k //= p
    return res


@numba.jit(cache=True)
def triple_sum(primes: np.ndarray, res: np.ndarray, inv: np.ndarray) -> np.int64:
    """Sum over all i<j<k of CRT(res, primes) modulo primes[i]*primes[j]*primes[k].

    inv[i, j] holds the inverse of primes[j] modulo primes[i], so the inverse of
    (p_j p_k) mod p_i is inv[i, j] * inv[i, k]; the standard CRT combination then
    reconstructs C(n, k) mod (p_i p_j p_k)."""
    total = np.int64(0)
    m = len(primes)
    for i in range(m):
        pi = primes[i]
        ai = res[i]
        for j in range(i + 1, m):
            pj = primes[j]
            aj = res[j]
            pij = pi * pj
            iij = inv[i, j]  # inv(pj) mod pi
            iji = inv[j, i]  # inv(pi) mod pj
            for k in range(j + 1, m):
                pk = primes[k]
                ak = res[k]
                mod = pij * pk
                m1 = pj * pk
                m2 = pi * pk
                inv1 = iij * inv[i, k] % pi
                inv2 = iji * inv[j, k] % pj
                inv3 = inv[k, i] * inv[k, j] % pk
                x = (ai * m1 % mod) * inv1 % mod
                x += (aj * m2 % mod) * inv2 % mod
                x += (ak * pij % mod) * inv3 % mod
                total += x % mod
    return total


def inv_mod(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def solve() -> int:
    n, k = 10**18, 10**9
    primes = [int(p) for p in prime_sieve_int(5000) if p > 1000]

    res = []
    for p in primes:
        fact = [1] * p
        for i in range(1, p):
            fact[i] = fact[i - 1] * i % p
        inv_fact = [1] * p
        inv_fact[p - 1] = pow(fact[p - 1], p - 2, p)
        for i in range(p - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % p
        res.append(binom_mod_p(n, k, p, fact, inv_fact))

    parr = np.array(primes, dtype=np.int64)
    rarr = np.array(res, dtype=np.int64)
    m = len(primes)
    inv = np.zeros((m, m), dtype=np.int64)
    for i in range(m):
        for j in range(m):
            if i != j:
                inv[i, j] = inv_mod(primes[j], primes[i])

    return int(triple_sum(parr, rarr, inv))


if __name__ == "__main__":
    print(solve())  # 162619462356610313
