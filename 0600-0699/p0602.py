import numba
import numpy as np

P = 10**9 + 7

@numba.jit(cache=True)
def mod_exp(a: int, b: int, mod: int) -> int:
    prod = 1
    a %= mod
    while b > 0:
        if b & 1:
            prod = prod * a % mod
        a = a * a % mod
        b >>= 1
    return prod

@numba.jit(cache=True)
def eulerian(n: int, m: int, mod: int) -> int:
    """Eulerian number A(n, m) modulo a prime.

    A(n,m) = sum_{j=0}^m (-1)^j C(n+1, j) (m+1-j)^n. The binomial is built
    incrementally; modular inverses of 1..m come from the linear recurrence
    inv[i] = -(mod//i) * inv[mod % i].  mod^2 < 2^63 keeps products in int64.
    """
    inv = np.empty(m + 1, dtype=np.int64)
    if m >= 1:
        inv[1] = 1
    for i in range(2, m + 1):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod

    total = 0
    binom = 1  # C(n+1, 0)
    for j in range(m + 1):
        if j > 0:
            binom = binom * ((n + 2 - j) % mod) % mod * inv[j] % mod
        term = binom * mod_exp(m + 1 - j, n, mod) % mod
        if j & 1:
            total = (total - term) % mod
        else:
            total = (total + term) % mod
    return total % mod

def c(n: int, k: int) -> int:
    """Coefficient of p^k in e(n, p); equals the Eulerian number A(n, k-1)."""
    return int(eulerian(n, k - 1, P))

if __name__ == "__main__":
    print(c(10_000_000, 4_000_000))  # 269496760
