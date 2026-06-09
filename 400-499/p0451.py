import numba
import numpy as np

@numba.jit(cache=True)
def smallest_prime_factors(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

@numba.jit(cache=True)
def mod_inverse(a: int, m: int) -> int:
    """Inverse of a mod m via the extended Euclidean algorithm (gcd(a, m)=1)."""
    a %= m
    g, x = m, 0
    g1, x1 = a, 1
    while g1 != 0:
        q = g // g1
        g, g1 = g1, g - q * g1
        x, x1 = x1, x - q * x1
    return x % m

@numba.jit(cache=True)
def sum_inverses(n_max: int, spf: np.ndarray) -> int:
    """Sum of I(n) for 3<=n<=n_max, where I(n) is the largest m<n-1 with
    m^2 ≡ 1 (mod n). Since the self-inverse residues pair up as (m, n-m),
    I(n) = n - s(n) where s(n) is the smallest such residue exceeding 1.
    The residues are CRT combinations of the square roots of 1 modulo each
    prime-power factor (±1 for odd p; 1/2/4 roots for the power of two)."""
    total = 0
    powers = np.empty(16, dtype=np.int64)   # prime-power factors of n
    basis = np.empty(16, dtype=np.int64)    # CRT basis: basis[i] ≡ 1 mod powers[i], 0 elsewhere
    n_roots = np.empty(16, dtype=np.int64)
    roots = np.empty((16, 4), dtype=np.int64)
    sols = np.empty(512, dtype=np.int64)
    nxt = np.empty(512, dtype=np.int64)

    for n in range(3, n_max + 1):
        # prime-power factorisation and the unit square roots modulo each
        k = 0
        x = n
        while x > 1:
            p = spf[x]
            q = 1
            while x % p == 0:
                x //= p
                q *= p
            powers[k] = q
            if p == 2:
                if q == 2:
                    roots[k, 0] = 1
                    n_roots[k] = 1
                elif q == 4:
                    roots[k, 0] = 1
                    roots[k, 1] = 3
                    n_roots[k] = 2
                else:
                    roots[k, 0] = 1
                    roots[k, 1] = q - 1
                    roots[k, 2] = q // 2 - 1
                    roots[k, 3] = q // 2 + 1
                    n_roots[k] = 4
            else:
                roots[k, 0] = 1
                roots[k, 1] = q - 1
                n_roots[k] = 2
            k += 1

        for i in range(k):
            rest = n // powers[i]
            basis[i] = (rest % n) * mod_inverse(rest % powers[i], powers[i]) % n

        # combine the per-factor roots into all residues with residue^2 ≡ 1
        count = 1
        sols[0] = 0
        for i in range(k):
            c = 0
            for j in range(count):
                base = sols[j]
                for r in range(n_roots[i]):
                    nxt[c] = (base + roots[i, r] * basis[i]) % n
                    c += 1
            count = c
            for j in range(count):
                sols[j] = nxt[j]

        smallest = n - 1
        for j in range(count):
            v = sols[j]
            if 1 < v < smallest:
                smallest = v
        total += n - smallest
    return total

if __name__ == "__main__":
    n_max = 2 * 10**7
    spf = smallest_prime_factors(n_max)
    print(sum_inverses(n_max, spf))  # 153651073760956
