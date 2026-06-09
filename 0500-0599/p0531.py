"""Project Euler Problem 531: Chinese Leftovers.

g(a, n, b, m) is the smallest non-negative x with x = a (mod n) and x = b (mod m),
or 0 if none exists.  With f(n, m) = g(phi(n), n, phi(m), m), find

    sum f(n, m)  over  10^6 <= n < m < 1005000.

A solution to the two congruences exists iff gcd(n, m) | (a - b); then, writing
gg = gcd(n, m), the unique solution modulo lcm(n, m) is

    x = a + n * (((b - a)/gg) * inv(n/gg, m/gg)  mod  (m/gg)).

We sieve phi over the (small) range and sum the ~1.25e7 pairs directly.
"""

import numpy as np
import numba

from funcs import totient_sieve

LO = 1_000_000
HI = 1_005_000


@numba.jit(cache=True)
def _egcd_inv(a: int, mod: int) -> int:
    # modular inverse of a mod `mod`, assuming gcd(a, mod) = 1, result in [0, mod)
    if mod == 1:
        return 0
    g0, x0 = mod, 0
    g1, x1 = a % mod, 1
    while g1 != 0:
        q = g0 // g1
        g0, g1 = g1, g0 - q * g1
        x0, x1 = x1, x0 - q * x1
    return x0 % mod


@numba.jit(cache=True)
def _g(a: int, n: int, b: int, m: int) -> int:
    # gcd of n, m
    u, v = n, m
    while v:
        u, v = v, u % v
    gg = u
    if (b - a) % gg != 0:
        return 0
    mr = m // gg
    inv = _egcd_inv((n // gg) % mr, mr)
    k = (b - a) // gg
    t = (k % mr) * inv % mr
    lcm = (n // gg) * m
    x = (a + n * t) % lcm
    return x


@numba.jit(cache=True)
def _sum(phi: np.ndarray) -> int:
    total = 0
    for n in range(LO, HI):
        pn = phi[n]
        for m in range(n + 1, HI):
            total += _g(pn, n, phi[m], m)
    return total


def solve() -> int:
    phi = totient_sieve(HI)
    return int(_sum(phi))


if __name__ == "__main__":
    assert _g(2, 4, 4, 6) == 10
    assert _g(3, 4, 4, 6) == 0
    print(solve())  # 4515432351156203105
