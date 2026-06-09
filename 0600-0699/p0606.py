import numba
import numpy as np

from funcs import prime_sieve_int

MOD = 10**9

@numba.jit(cache=True)
def _tri(v: int) -> int:
    """v(v+1)/2 mod MOD without overflowing int64 (v can be ~10^12)."""
    if v % 2 == 0:
        return (v // 2) % MOD * ((v + 1) % MOD) % MOD
    return (v % MOD) * (((v + 1) // 2) % MOD) % MOD

@numba.jit(cache=True)
def _lookup(y: int, n: int, r: int, small: np.ndarray, large: np.ndarray) -> int:
    if y <= r:
        return small[y]
    return large[n // y]

@numba.jit(cache=True)
def lucy_cube_sum(n: int, primes: np.ndarray):
    """Lucy_Hedgehog for Pi3(x) = sum of cubes of primes <= x, mod MOD.

    Returns (small, large) where small[v] = Pi3(v) for v <= r = floor(sqrt n)
    and large[i] = Pi3(n // i). Initial values are the full cube prefix sums
    (T(v)^2 - 1, excluding 1); each prime sieves out composite contributions.
    """
    r = int(n**0.5)
    while (r + 1) * (r + 1) <= n:
        r += 1
    small = np.empty(r + 1, dtype=np.int64)
    for v in range(r + 1):
        T = _tri(v)
        small[v] = (T * T - 1) % MOD
    large = np.empty(r + 1, dtype=np.int64)
    for i in range(1, r + 1):
        v = n // i
        T = _tri(v)
        large[i] = (T * T - 1) % MOD

    for idx in range(len(primes)):
        p = int(primes[idx])
        if p > r:
            break
        sp = small[p - 1]
        p3 = p * p * p % MOD
        pp = p * p
        for i in range(1, r + 1):
            v = n // i
            if v < pp:
                break
            large[i] = (large[i] - p3 * (_lookup(v // p, n, r, small, large) - sp)) % MOD
        for v in range(r, pp - 1, -1):
            small[v] = (small[v] - p3 * (small[v // p] - sp)) % MOD
    return small, large

@numba.jit(cache=True)
def total(n: int, primes: np.ndarray) -> int:
    """sum_{p<q primes, pq<=n} (pq)^3 = sum_p p^3 (Pi3(n//p) - Pi3(p)), mod MOD."""
    small, large = lucy_cube_sum(n, primes)
    r = len(small) - 1
    s = 0
    for idx in range(len(primes)):
        p = int(primes[idx])
        if p > r:
            break
        s = (s + (p * p * p % MOD) * ((large[p] - small[p]) % MOD)) % MOD
    return s % MOD

def S(N: int) -> int:
    """Sum of k <= N having exactly 252 gozinta chains, mod 10^9.

    g depends only on the prime signature, and the unique signature giving 252
    is (3, 3): k = (p q)^3 with distinct primes p, q. So k <= N iff p q <= N^(1/3),
    and S(N) = sum over p < q with p q <= floor(N^(1/3)) of (p q)^3.
    """
    B = round(N ** (1 / 3))
    while (B + 1) ** 3 <= N:
        B += 1
    while B**3 > N:
        B -= 1
    primes = prime_sieve_int(int(B**0.5) + 2)
    return int(total(B, primes))

if __name__ == "__main__":
    print(S(10**36))  # 158452775
