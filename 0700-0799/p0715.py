import numba
import numpy as np

MOD = 10**9 + 7

@numba.njit(cache=True)
def chi4_prefix(x):
    # sum of chi4(d) for d <= x: pattern 1,0,-1,0 -> prefix 1,1,0,0 repeating
    r = x % 4
    return 1 if r in (1, 2) else 0

@numba.njit(cache=True)
def G(n, x0):
    """G(n) = sum_{k<=n} g(k), g = Id3 * (mu chi4):
    g(p^e) = p^(3(e-1)) (p^3 - chi4(p)).
    H(x) = sum_{d<=x} mu(d) chi4(d) computed Mertens-style via
    (mu chi4) * chi4 = identity, i.e. sum_{d<=x} chi4(d) H(x/d) = 1.

    Derivation: f is multiplicative with f(p^e) = p^(6(e-1)) (p^6 - N0(p)),
    where N0(p) counts 6-tuples mod p whose square sum is 0 mod p. The
    classical Gauss-sum evaluation gives N0(p) = p^5 + (p-1) p^2 chi4(p)
    for odd p (the character of (-1)^3) and N0(2) = 32. Then
    g(k) = f(k)/(k^2 phi(k)) is multiplicative with
    g(p^e) = p^(3e) - chi4(p) p^(3(e-1)) for odd p and g(2^e) = 2^(3e),
    i.e. exactly (Id3 * mu chi4)(p^e). Hence
    G(n) = sum_d mu(d) chi4(d) * T3(n//d), T3(M) = (M(M+1)/2)^2,
    grouped over quotient blocks with H evaluated at all n//d arguments:
    small ones from a linear sieve up to x0 ~ n^(2/3), large ones by the
    standard O(x^(2/3)) recurrence. Verified against G(10) = 3053
    (also confirmed by hand: 1+8+28+64+124+224+344+512+756+992) and
    G(10^5) = 157612967."""
    # sieve h = mu*chi4 up to x0, prefix sums in int64
    mu = np.ones(x0 + 1, dtype=np.int8)
    is_comp = np.zeros(x0 + 1, dtype=np.bool_)
    primes = np.empty(6000000, dtype=np.int64)
    np_ = 0
    for i in range(2, x0 + 1):
        if not is_comp[i]:
            primes[np_] = i
            np_ += 1
            mu[i] = -1
        for j in range(np_):
            p = primes[j]
            if i * p > x0:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    H = np.zeros(x0 + 1, dtype=np.int32)
    acc = 0
    for d in range(1, x0 + 1):
        if d % 4 == 1:
            acc += mu[d]
        elif d % 4 == 3:
            acc -= mu[d]
        H[d] = acc
    # large H values: H_big[j] = H(n//j) for j with n//j > x0
    J = n // x0
    Hbig = np.zeros(J + 1, dtype=np.int64)
    for j in range(J, 0, -1):
        x = n // j
        if x <= x0:
            continue
        s = 1
        d = 2
        while d <= x:
            v = x // d
            d2 = x // v
            cnt = chi4_prefix(d2) - chi4_prefix(d - 1)
            if cnt != 0:
                hv = H[v] if v <= x0 else Hbig[j * d]  # x//d = n//(j*d)
                s -= cnt * hv
            d = d2 + 1
        Hbig[j] = s
    # G = sum over quotient blocks of (H(hi)-H(lo-1)) * T3(v)
    total = 0
    d = 1
    inv2 = (MOD + 1) // 2
    while d <= n:
        v = n // d
        d2 = n // v
        hi = H[d2] if d2 <= x0 else Hbig[n // d2]
        lo = H[d - 1] if d - 1 <= x0 else Hbig[n // (d - 1)]
        diff = (hi - lo) % MOD
        m = v % MOD
        t3 = m * (m + 1) % MOD * inv2 % MOD
        t3 = t3 * t3 % MOD
        total = (total + diff * t3) % MOD
        d = d2 + 1
    return total % MOD

if __name__ == "__main__":
    assert G(10, 5) == 3053
    assert G(10**5, 3000) == 157612967
    print(G(10**12, 10**8))  # 883188017
