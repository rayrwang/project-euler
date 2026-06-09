import numba
import numpy as np

from funcs import mod_exp_bounded, prime_sieve_bool

MOD = 993353399


@numba.jit(cache=True)
def a_prime_power(q: int, e: int, mod: int) -> int:
    """A(q^e) mod `mod`, where A(m) = sum_k T(k)^2 counts pairs (i,j) in
    (Z/m)^2 with i*j = k. Derived closed form (all sums/products, no division):

        phi(q^j) = q^(j-1)(q-1),
        Z = q^(2e) - sum_{t=0}^{e-1} (t+1) q^t phi(q^(e-t))^2,
        A(q^e) = Z^2 + sum_{t=0}^{e-1} (t+1)^2 q^(2t) phi(q^(e-t))^3.

    `mod` < 2^30, so products of two reduced residues stay below 2^63.
    """
    qm = q % mod
    qm1 = (qm - 1) % mod
    sum_z = 0
    sum_a = 0
    qt = 1  # q^t
    for t in range(e):
        j = e - t
        phi = mod_exp_bounded(qm, j - 1, mod) * qm1 % mod
        phi2 = phi * phi % mod
        phi3 = phi2 * phi % mod
        sum_z = (sum_z + (t + 1) % mod * qt % mod * phi2) % mod
        q2t = qt * qt % mod
        sum_a = (sum_a + ((t + 1) * (t + 1)) % mod * q2t % mod * phi3) % mod
        qt = qt * qm % mod
    q2e = mod_exp_bounded(qm, 2 * e, mod)
    z = (q2e - sum_z) % mod
    return (z * z + sum_a) % mod


@numba.jit(cache=True)
def segmented_primes(n0: int, width: int, base: np.ndarray) -> np.ndarray:
    """Boolean mask of primes in [n0, n0+width] using base primes up to sqrt."""
    is_comp = np.zeros(width + 1, dtype=np.bool_)
    for q in base:
        start = ((n0 + q - 1) // q) * q
        if start < q * q:
            start = q * q
        for m in range(start, n0 + width + 1, q):
            is_comp[m - n0] = True
    return ~is_comp


@numba.jit(cache=True)
def a_values(m0: int, width: int, base: np.ndarray, mod: int) -> np.ndarray:
    """For every g = m0+x (x in [0,width]) compute A(g) mod `mod` by sieving
    out each base-prime factor; any residue > 1 left over is a single prime."""
    res = np.empty(width + 1, dtype=np.int64)
    for x in range(width + 1):
        res[x] = m0 + x
    aval = np.ones(width + 1, dtype=np.int64)
    for q in base:
        start = ((m0 + q - 1) // q) * q
        for v in range(start, m0 + width + 1, q):
            x = v - m0
            e = 0
            while res[x] % q == 0:
                res[x] //= q
                e += 1
            aval[x] = aval[x] * a_prime_power(q, e, mod) % mod
    for x in range(width + 1):
        if res[x] > 1:
            aval[x] = aval[x] * a_prime_power(res[x], 1, mod) % mod
    return aval


def solve(n0: int, width: int) -> int:
    limit = int((n0 + width) ** 0.5) + 100
    base = np.nonzero(prime_sieve_bool(limit))[0].astype(np.int64)
    prime_mask = segmented_primes(n0, width, base)
    aval = a_values(n0 - 1, width, base, MOD)  # A(p-1) lives at index x
    total = 0
    for x in np.nonzero(prime_mask)[0]:
        p = n0 + int(x)
        total = (total + (p - 1) * (p - 1) + int(aval[x])) % MOD
    return total


if __name__ == "__main__":
    print(solve(10**16, 10**6))  # 638129754
