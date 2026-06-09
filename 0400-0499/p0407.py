import numba
import numpy as np

@numba.jit(cache=True)
def smallest_prime_factor_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:               # i is prime
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

@numba.jit(cache=True)
def modinv(a: int, m: int) -> int:
    """Inverse of a modulo m (a coprime to m), via extended Euclid."""
    a %= m
    old_r, r = a, m
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_s % m

@numba.jit(cache=True)
def total_idempotents(N: int, spf: np.ndarray) -> int:
    total = 0
    basis = np.empty(16, dtype=np.int64)   # CRT basis, one per prime power
    sums = np.empty(1 << 16, dtype=np.int64)
    for n in range(1, N + 1):
        # Factor n into prime powers q_i = p^e, building the CRT basis e_i with
        # e_i = 1 (mod q_i) and 0 (mod q_j) for j != i.
        m = 0
        x = n
        while x > 1:
            p = spf[x]
            q = 1
            while x % p == 0:
                x //= p
                q *= p
            r = n // q                         # coprime to q
            basis[m] = (r * modinv(r, q)) % n
            m += 1
        # Maximise the idempotent over all 2^m subset sums of the basis.
        sums[0] = 0
        cnt = 1
        for i in range(m):
            for j in range(cnt):
                sums[cnt + j] = sums[j] + basis[i]
            cnt *= 2
        best = 0
        for j in range(cnt):
            v = sums[j] % n
            if v > best:
                best = v
        total += best
    return total

if __name__ == "__main__":
    N = 10**7
    spf = smallest_prime_factor_sieve(N)
    assert total_idempotents(20, spf) == 75
    assert total_idempotents(100, spf) == 2549
    print(total_idempotents(N, spf))  # 39782849136421
