import numpy as np

MOD = 101**4


def solve(big_g: int, big_l: int, n: int) -> int:
    """Count size-n lists with gcd >= big_g and lcm <= big_l, mod 101^4.

    Factoring out the gcd: a list with gcd exactly g is g times a list with
    gcd 1, and its lcm is at most big_l iff the reduced list's lcm is at
    most m = big_l // g. So f = sum over g >= big_g of C(big_l // g), where
    C(m) counts lists with gcd 1 and lcm <= m. Since g >= big_g, only
    m <= M = big_l // big_g occurs, and the number of g giving each m is a
    floor-division block count.

    Counting by exact lcm: the number of lists with lcm exactly l is
    multiplicative with D(p^e) = (e+1)^n - e^n (each entry's exponent is at
    most e and some entry attains it). Splitting a list with lcm exactly l
    by its gcd d gives D(l) = sum over d | l of c(l / d), where c counts
    gcd-1 lists by exact lcm; Mobius inversion turns this into the
    divisor-sum sieve c = mu * D, and C is the prefix sum of c.

    Everything runs over 1..M with arrays: D via smallest-prime-factor
    decomposition, c via one harmonic-series pass of numpy slices, and the
    final sum pairs C(m) with the block counts.
    """
    m_max = big_l // big_g

    # Smallest prime factor and Mobius sieves.
    spf = np.zeros(m_max + 1, dtype=np.int64)
    for p in range(2, m_max + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    mu = np.ones(m_max + 1, dtype=np.int64)
    primes = np.nonzero(spf[2:] == np.arange(2, m_max + 1))[0] + 2
    for p in primes:
        mu[p::p] *= -1
        mu[p * p :: p * p] = 0

    # D(l) = prod over p^e || l of (e+1)^n - e^n, computed bottom-up using
    # the exponent of the smallest prime factor.
    max_e = m_max.bit_length()
    f = [(pow(e + 1, n, MOD) - pow(e, n, MOD)) % MOD for e in range(max_e + 1)]
    spf_l = spf.tolist()
    exp_l = [0] * (m_max + 1)
    rest_l = [0] * (m_max + 1)
    d_l = [0] * (m_max + 1)
    rest_l[1] = d_l[1] = 1
    for v in range(2, m_max + 1):
        p = spf_l[v]
        q = v // p
        if spf_l[q] == p:
            exp_l[v] = exp_l[q] + 1
            rest_l[v] = rest_l[q]
        else:
            exp_l[v] = 1
            rest_l[v] = q
        d_l[v] = d_l[rest_l[v]] * f[exp_l[v]] % MOD
    d_arr = np.array(d_l, dtype=np.int64)

    # c = mu * D (Dirichlet convolution), then C = prefix sums of c.
    c = np.zeros(m_max + 1, dtype=np.int64)
    for a in range(1, m_max + 1):
        if mu[a]:
            c[a::a] += mu[a] * d_arr[1 : m_max // a + 1]
    c %= MOD
    big_c = np.cumsum(c) % MOD

    # Pair C(m) with the number of g in [big_g, big_l] having
    # big_l // g == m.
    total = 0
    for m in range(1, m_max + 1):
        count = big_l // m - max(big_l // (m + 1), big_g - 1)
        if count > 0:
            total += count % MOD * int(big_c[m])
    return total % MOD


if __name__ == "__main__":
    assert solve(10, 100, 1) == 91
    assert solve(10, 100, 2) == 327
    assert solve(10, 100, 3) == 1135
    assert solve(10, 100, 1000) == 3286053
    print(solve(10**6, 10**12, 10**18))  # 84664213
