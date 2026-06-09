import numpy as np

import numba

M = 200
P = 10**9 + 7


def _small_primes(n: int) -> np.ndarray:
    """Primes up to n, used to trial-factor moduli below 8e7 (sqrt < 9000)."""
    bs = bytearray([1]) * (n + 1)
    bs[0] = bs[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if bs[i]:
            bs[i * i :: i] = bytearray(len(bs[i * i :: i]))
    return np.array([i for i in range(2, n + 1) if bs[i]], dtype=np.int64)


SMALL = _small_primes(9000)


@numba.jit(cache=True)
def igcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.jit(cache=True)
def mod_exp(b: int, e: int, m: int) -> int:
    r = 1 % m
    b %= m
    while e > 0:
        if e & 1:
            r = r * b % m
        b = b * b % m
        e >>= 1
    return r


@numba.jit(cache=True)
def order_pp(a: int, p: int, e: int, primes: np.ndarray) -> int:
    """Multiplicative order of a modulo p^e (with gcd(a, p) = 1)."""
    m = p**e
    phi = p ** (e - 1) * (p - 1)
    order = phi
    t = phi
    for i in range(len(primes)):
        q = primes[i]
        if q * q > t:
            break
        if t % q == 0:
            while t % q == 0:
                t //= q
            while order % q == 0 and mod_exp(a, order // q, m) == 1:
                order //= q
    if t > 1:
        q = t
        while order % q == 0 and mod_exp(a, order // q, m) == 1:
            order //= q
    return order


@numba.jit(cache=True)
def mult_order10(m: int, primes: np.ndarray) -> int:
    """Multiplicative order of 10 modulo m (with gcd(10, m) = 1), via CRT/lcm."""
    if m == 1:
        return 1
    res = 1
    t = m
    for i in range(len(primes)):
        p = primes[i]
        if p * p > t:
            break
        if t % p == 0:
            e = 0
            while t % p == 0:
                t //= p
                e += 1
            o = order_pp(10, p, e, primes)
            res = res // igcd(res, o) * o
    if t > 1:
        o = order_pp(10, t, 1, primes)
        res = res // igcd(res, o) * o
    return res


@numba.jit(cache=True)
def n_value(u3: int, v3: int, primes: np.ndarray) -> int:
    """N(u^3 / v^3) mod P, where r = u^3/v^3 is already in lowest terms.

    Writing an n-digit number as n = a*10^(d-1) + m (leading digit a, tail m),
    the shift gives s(n) = 10m + a, and s(n) = r*n forces
        m = a * (u3 * 10^(d-1) - v3) / (10 v3 - u3).
    With D = 10 v3 - u3 (>0 iff r < 10) and u3 = 10 v3 (mod D), divisibility
    reduces to D' | 10^d - 1 where D' = D / gcd(D, a v3); hence d must be a
    positive multiple of ord_{D'}(10). The smallest feasible (d, a) — subject to
    0 <= m < 10^(d-1) — yields N(r), as n increases with d then with a.
    """
    if u3 >= 10 * v3:
        return 0
    d_big = 10 * v3 - u3
    d_inv = mod_exp(d_big, P - 2, P)
    best_d = -1
    best_a = -1
    for a in range(1, 10):
        g = igcd(d_big, a * v3)
        dp = d_big // g
        if dp == 1:
            omega = 1
        else:
            if igcd(10, dp) != 1:
                continue
            omega = mult_order10(dp, primes)
        # lower bound on d from m >= 0: 10^(d-1) * u3 >= v3
        dlo = 1
        pw = 1
        while pw * u3 < v3:
            pw *= 10
            dlo += 1
        k = (dlo + omega - 1) // omega
        d = k * omega
        if d < 1:
            d = omega
        # upper bound on d from m < 10^(d-1)
        c = u3 * (a + 1) - 10 * v3
        if c > 0:
            # need 10^(d-1) * c < a*v3 <= 7.2e7, so 10^(d-1) < 1e8 => d-1 <= 7
            if d - 1 >= 8:
                continue
            pwr = 1
            for _ in range(d - 1):
                pwr *= 10
            if pwr * c >= a * v3:
                continue
        if best_d == -1 or d < best_d or (d == best_d and a < best_a):
            best_d = d
            best_a = a
    if best_d == -1:
        return 0
    d = best_d
    a = best_a
    pw = mod_exp(10, d - 1, P)
    m = a * ((u3 * pw - v3) % P) % P * d_inv % P
    return (a * pw + m) % P


@numba.jit(cache=True)
def solve(limit: int, primes: np.ndarray) -> int:
    total = 0
    for u in range(1, limit + 1):
        u3 = u * u * u
        for v in range(1, limit + 1):
            if igcd(u, v) != 1:
                continue
            total = (total + n_value(u3, v * v * v, primes)) % P
    return total


if __name__ == "__main__":
    print(solve(M, SMALL))  # 119719335
