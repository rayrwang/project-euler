import numba
import numpy as np

"""Problem 735: F(N) = sum_{n<=N} #{d <= n : d | 2 n^2}.

Writing d = g e, n = g m with gcd(e, m) = 1, the divisibility d | 2 n^2
collapses to e | 2 g, and d <= n becomes e <= m. Counting admissible g
for each coprime pair gives floor(N/(e m)) when e is odd and
floor(N/(u m)) when e = 2u (forcing m odd, 2u <= m). Moebius inversion
of the coprimality condition (only odd k survive) reduces everything to
the two unrestricted hyperbola sums A0, B0 below, each O(M^(3/4)) via
quotient blocks, for a total of about 1.7e9 operations."""

@numba.njit(cache=True)
def A0(M):
    """sum over e odd, m >= e, em <= M of floor(M/(em))."""
    tot = 0
    e = 1
    while e * e <= M:
        X = M // e
        # sum_{m=e}^{X} floor(X/m) by quotient blocks
        m = e
        while m <= X:
            v = X // m
            m2 = X // v
            tot += v * (m2 - m + 1)
            m = m2 + 1
        e += 2
    return tot

@numba.njit(cache=True)
def B0(M):
    """sum over m odd, 1 <= u <= (m-1)/2, um <= M of floor(M/(um))."""
    tot = 0
    u = 1
    while True:
        L = 2 * u + 1
        if u * L > M:
            break
        X = M // u
        # sum over odd m in [L, X] of floor(X/m)
        m = L
        while m <= X:
            v = X // m
            m2 = X // v
            # count odd integers in [m, m2]
            cnt = (m2 + 1) // 2 - m // 2
            tot += v * cnt
            m = m2 + 1
        u += 1
    return tot

@numba.njit(cache=True)
def F(N):
    # sieve mu up to sqrt(N)
    K = int(N**0.5) + 1
    mu = np.ones(K + 1, dtype=np.int8)
    is_comp = np.zeros(K + 1, dtype=np.bool_)
    primes = np.empty(K, dtype=np.int64)
    np_ = 0
    for i in range(2, K + 1):
        if not is_comp[i]:
            primes[np_] = i
            np_ += 1
            mu[i] = -1
        for j in range(np_):
            p = primes[j]
            if i * p > K:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    tot = 0
    k = 1
    while k * k <= N:
        if mu[k] != 0:
            M = N // (k * k)
            tot += mu[k] * (A0(M) + B0(M))
        k += 2
    return tot

if __name__ == "__main__":
    assert F(15) == 63
    assert F(1000) == 15066
    print(F(10**12))  # 174848216767932
