import numba
import numpy as np

MOD = 10**9 + 7

@numba.njit(cache=True)
def S(n_max):
    """The moves span a GF(2) linear code: a state is solvable iff it lies in
    the span of the n cyclic windows of length k, so F(n, k) = 2^rank. The
    circulant's rank is n - deg gcd(1 + x + ... + x^(k-1), x^n + 1) over
    GF(2); tracking the multiplicity of the factor (x + 1) separately from
    gcd(x^k + 1, x^n + 1) = x^gcd(n,k) + 1 gives the closed form
        F(n, k) = 2^(n - gcd(n, k) + [v2(k) <= v2(n)]),
    verified against brute-force ranks for all n <= 12.

    Group k by g = gcd(n, k): writing k = g j, n = g m with gcd(j, m) = 1,
    the bracket is 1 unless v2(j) > v2(m), which (as j must be coprime to m)
    happens only for m odd and j even - half of the phi(m) units when m > 1.
    Hence
        S(N) = sum_g sum_{m <= N/g} w(m) 2^(g(m-1)),
    with w(1) = 2, w(m) = 2 phi(m) for even m, w(m) = 3 phi(m) / 2 for odd
    m > 1.
    """
    phi = np.arange(n_max + 1, dtype=np.int64)
    for p in range(2, n_max + 1):
        if phi[p] == p:  # prime
            for q in range(p, n_max + 1, p):
                phi[q] -= phi[q] // p

    total = 0
    for g in range(1, n_max + 1):
        m_max = n_max // g
        # base = 2^g (mod MOD)
        b = 2
        ee = g
        base = 1
        while ee > 0:
            if ee & 1:
                base = base * b % MOD
            b = b * b % MOD
            ee >>= 1
        power = 1  # 2^(g(m-1)) for current m
        for m in range(1, m_max + 1):
            if m == 1:
                w = 2
            elif m % 2 == 0:
                w = 2 * phi[m] % MOD
            else:
                w = 3 * (phi[m] // 2) % MOD
            total = (total + w * power) % MOD
            power = power * base % MOD
    return total

if __name__ == "__main__":
    assert S(3) == 22
    assert S(10) == 10444
    assert S(10**3) == 853837042
    print(S(10**7))  # 709874991
