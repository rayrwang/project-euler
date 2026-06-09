import numba
import numpy as np


@numba.njit
def middle_coeff(exps: np.ndarray) -> int:
    """Largest coefficient of the polynomial prod_i (1 + x + ... + x^{a_i}).

    The divisors of n = prod p_i^{a_i} form a product of chains under
    divisibility; by the de Bruijn-Tengbergen-Kruyswijk theorem this poset is
    rank-symmetric and rank-unimodal, so its widest antichain is the largest
    rank level. A divisor's rank is the sum of its chosen exponents, hence the
    level sizes are exactly the coefficients of prod_i (1 + x + ... + x^{a_i}),
    and the maximum (central, by unimodality) coefficient is N(n).
    """
    total = 0
    for a in exps:
        total += a
    poly = np.zeros(total + 1, dtype=np.int64)
    poly[0] = 1
    cur = 1
    for a in exps:
        new = np.zeros(cur + a, dtype=np.int64)
        for i in range(cur):
            c = poly[i]
            if c:
                for j in range(a + 1):
                    new[i + j] += c
        cur = cur + a
        poly[:cur] = new
    m = 0
    for i in range(cur):
        if poly[i] > m:
            m = poly[i]
    return m


@numba.njit
def run(n_max: int, spf: np.ndarray) -> int:
    """Sum of N(n) for 1 <= n <= n_max, factoring each n via its smallest prime
    factor and reducing to the multiset of exponents (the primes themselves are
    irrelevant to the antichain width)."""
    total = 1  # N(1) = 1
    exps = np.zeros(32, dtype=np.int64)
    for n in range(2, n_max + 1):
        x = n
        cnt = 0
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            exps[cnt] = e
            cnt += 1
        total += middle_coeff(exps[:cnt])
    return total


@numba.njit
def make_spf(n_max: int) -> np.ndarray:
    """Smallest-prime-factor sieve up to n_max."""
    spf = np.zeros(n_max + 1, dtype=np.int32)
    i = 2
    while i * i <= n_max:
        if spf[i] == 0:
            for j in range(i * i, n_max + 1, i):
                if spf[j] == 0:
                    spf[j] = i
        i += 1
    for k in range(2, n_max + 1):
        if spf[k] == 0:
            spf[k] = k
    return spf


def sum_N(n_max: int) -> int:
    return run(n_max, make_spf(n_max))


if __name__ == "__main__":
    # S(30) has maximum antichain {2, 3, 5}, so N(30) = 3.
    assert middle_coeff(np.array([1, 1, 1], dtype=np.int64)) == 3
    # sum_{1<=n<=10^6} N(n) = 4153927 (matches an independent slow check).
    assert sum_N(10**6) == 4153927
    print(sum_N(10**8))  # 528755790
