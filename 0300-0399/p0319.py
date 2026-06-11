import numba
import numpy as np

MOD = 10**9


@numba.jit(cache=True)
def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    mu[0] = 0
    is_comp = np.zeros(n + 1, dtype=np.bool_)
    primes = np.zeros(n, dtype=np.int64)
    np_ = 0
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes[np_] = i
            np_ += 1
            mu[i] = -1
        for j in range(np_):
            p = primes[j]
            if i * p > n:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


@numba.jit(cache=True)
def big_mertens(n: int, small_m: np.ndarray) -> np.ndarray:
    """M(n // k) for k = 1..kmax where n // k exceeds the small table.

    Uses M(x) = 1 - sum_{j=2}^{x} M(x // j) over blocks of constant x // j,
    filling values in increasing order of x (decreasing k).
    """
    limit = len(small_m) - 1
    kmax = n // limit  # n // k > limit iff k < n / limit
    big = np.zeros(kmax + 1, dtype=np.int64)
    for k in range(kmax, 0, -1):
        x = n // k
        if x <= limit:
            big[k] = small_m[x]
            continue
        s = np.int64(1)
        j = 2
        while j <= x:
            v = x // j
            j2 = x // v  # last j with the same quotient
            mv = small_m[v] if v <= limit else big[k * j]
            s -= mv * (j2 - j + 1)
            j = j2 + 1
        big[k] = s
    return big


def f_sum(m: int) -> int:
    """sum_{j=1}^m (3^j - 2^j - 1) mod 10^9."""
    a = (pow(3, m + 1, 2 * MOD) - 3) % (2 * MOD) // 2  # (3^(m+1) - 3) / 2
    b = (pow(2, m + 1, MOD) - 2) % MOD
    return (a - b - m) % MOD


def t(n: int) -> int:
    """Number of bounded sequences of length n, mod 10^9.

    A sequence is valid iff x_i^(1/i) < (x_j + 1)^(1/j) for all i, j, i.e.
    iff some real t in (2, 3) has x_i = floor(t^i) throughout.  So t(n) is
    1 plus the number of distinct breakpoints m^(1/i) in (2, 3) with i <= n.
    Writing a breakpoint uniquely as q^(1/i) with minimal i (equivalently
    gcd(i, gcd of q's prime exponents) = 1), inclusion-exclusion over the
    squarefree divisors of i gives
        t(n) = 1 + sum_{d=1}^n mu(d) F(n // d),
    where F(m) = sum_{j<=m} (3^j - 2^j - 1) counts the integers strictly
    inside (2^j, 3^j).
    """
    limit = max(10, min(n, int(n ** (2 / 3)) + 1))
    mu = mobius_sieve(limit)
    small_m = np.cumsum(mu.astype(np.int64))
    big = big_mertens(n, small_m)

    def mertens(x: int) -> int:
        return int(small_m[x]) if x <= limit else int(big[n // x])

    total = 1
    d = 1
    while d <= n:
        v = n // d
        d2 = n // v
        total = (total + f_sum(v) * (mertens(d2) - mertens(d - 1))) % MOD
        d = d2 + 1
    return total


if __name__ == "__main__":
    assert t(5) == 293
    assert t(10) == 86195
    assert t(20) == 5227991891 % MOD
    print(t(10**10))  # 268457129
