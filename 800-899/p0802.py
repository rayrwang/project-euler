import numba
import numpy as np

N = 10**7
MOD = 1020340567


@numba.jit(cache=True)
def mobius_sieve(n: int) -> np.ndarray:
    """Linear sieve computing the Mobius function mu(k) for 1 <= k <= n."""
    mu = np.zeros(n + 1, dtype=np.int8)
    mu[1] = 1
    primes = np.empty(n, dtype=np.int64)
    n_primes = 0
    is_comp = np.zeros(n + 1, dtype=np.bool_)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes[n_primes] = i
            n_primes += 1
            mu[i] = -1
        j = 0
        while j < n_primes:
            p = primes[j]
            ip = i * p
            if ip > n:
                break
            is_comp[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            else:
                mu[ip] = -mu[i]
            j += 1
    return mu


@numba.jit(cache=True)
def solve(n: int, mod: int) -> int:
    """P(n) = sum_{d=1}^n S(d) * M(floor(n/d)) (mod `mod`).

    The map f(x,y) = (x^2 - x - y^2, 2xy - y + pi) is, under z = x + iy,
    the complex polynomial g(z) = z^2 - z + i*pi. Points whose period
    divides k are the roots of the monic degree-2^k polynomial g^(k)(z) - z,
    so the sum of their x-coordinates is Re(-[subleading coeff]). That
    coefficient doubles each iteration, giving S(1) = 2 and S(k) = 2^(k-1)
    for k >= 2. Mobius inversion over the minimal period yields the form above
    with M the Mertens function (prefix sums of mu).
    """
    mu = mobius_sieve(n)
    # Mertens prefix sums M[k] = sum_{i<=k} mu(i).
    mert = np.empty(n + 1, dtype=np.int64)
    mert[0] = 0
    acc = 0
    for k in range(1, n + 1):
        acc += mu[k]
        mert[k] = acc

    total = 0
    pow2 = 1  # 2^(d-1) mod `mod`, starting at d = 1
    for d in range(1, n + 1):
        s = 2 % mod if d == 1 else pow2  # S(d)
        m = mert[n // d] % mod  # may be negative; reduce into [0, mod)
        total = (total + s * m) % mod
        pow2 = pow2 * 2 % mod
    return total % mod


if __name__ == "__main__":
    print(solve(N, MOD))  # 973873727
