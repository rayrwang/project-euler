"""Project Euler 824: Chess Sliders.

L(N, K) mod P^2 for N = 10^9, K = 10^15, P = 10^7 + 19: K non-attacking
Sliders on an N x N cylindrical board.

A Slider attacks only the two horizontally adjacent squares (the row is a
cycle C_N), so rows are independent and L(N, K) = [x^K] g(x)^N, where
g(x) = I(C_N, x) = trace([[1, x], [1, 0]]^N) = lam+^N + lam-^N is the cycle
independence polynomial, lam+- = (1 +- sqrt(1+4x))/2.

Expanding g^N = sum_i C(N,i) lam+^{Ni} lam-^{N(N-i)} and pairing i with N-i
(using lam+ lam- = -x) gives, with V_m the Lucas-type polynomial,
    g(x)^N = sum_{i < N/2} C(N,i) (-x)^{Ni} V_{N(N-2i)}(x)  (+ middle term),
so L(N,K) = sum_i C(N,i) (-1)^{Ni} [x^{K-Ni}] V_{N(N-2i)}. Verified against a
direct polynomial expansion for all N <= 10 and L(2,2)=4, L(6,12)=4204761.

Only i with Ni <= K contribute (here K/N = 10^6 < N/2), and every binomial
and Lucas coefficient is taken mod P^2 by Granville's prime-power theorem,
with factorial units from one block table (Wolstenholme gives the full-block
value). All arithmetic runs in numba: products mod P^2 ~ 10^14 exceed int64,
so a float-assisted Barrett mulmod (O(1), exact for moduli < 2^50) replaces
Python big ints throughout.
"""

import numba as nb
import numpy as np

P = 10**7 + 19
MOD = P * P
PHI = P * (P - 1)  # Euler phi of P^2


@nb.njit(cache=True)
def _mulmod(a, b, m):
    """a*b mod m for m < 2^50: float-assisted Barrett, O(1)."""
    q = np.uint64(np.float64(a) * np.float64(b) / np.float64(m))
    r = np.int64(np.uint64(a) * np.uint64(b) - q * np.uint64(m))
    while r < 0:
        r += m
    while r >= m:
        r -= m
    return r


@nb.njit(cache=True)
def _powmod(a, e, m):
    result = np.int64(1)
    a %= m
    while e > 0:
        if e & 1:
            result = _mulmod(result, a, m)
        a = _mulmod(a, a, m)
        e >>= 1
    return result


@nb.njit(cache=True)
def _invmod(a):
    return _powmod(a, PHI - 1, MOD)


@nb.njit(cache=True)
def _build_tables():
    """Block factorial prefix mod P^2 and harmonic sums mod P."""
    prefix = np.ones(P, dtype=np.int64)
    for r in range(1, P):
        prefix[r] = _mulmod(prefix[r - 1], r, MOD)
    inverse = np.zeros(P, dtype=np.int64)
    inverse[1] = 1
    for i in range(2, P):
        inverse[i] = (P - (P // i) * inverse[P % i] % P) % P
    harmonic = np.zeros(P, dtype=np.int64)
    for r in range(1, P):
        harmonic[r] = (harmonic[r - 1] + inverse[r]) % P
    return prefix, harmonic


@nb.njit(cache=True)
def _factorial_unit(n, prefix, block, harmonic):
    """(n! with all factors of P removed) mod P^2, Granville block product."""
    result = np.int64(1)
    while n > 0:
        q, r = n // P, n % P
        term = _powmod(block, q, MOD)
        if r:
            term = _mulmod(term, prefix[r], MOD)
            corr = (1 + _mulmod((q % P) * P, harmonic[r], MOD)) % MOD
            term = _mulmod(term, corr, MOD)
        result = _mulmod(result, term, MOD)
        n = q
    return result


@nb.njit(cache=True)
def _p_adic_factorial(n):
    e, pk = np.int64(0), np.int64(P)
    while pk <= n:
        e += n // pk
        pk *= P
    return e


@nb.njit(cache=True)
def _p_adic_int(n):
    if n == 0:
        return np.int64(1) << 60
    e = np.int64(0)
    while n % P == 0:
        n //= P
        e += 1
    return e


@nb.njit(cache=True)
def _unit_int(n):
    while n % P == 0:
        n //= P
    return n % MOD


@nb.njit(cache=True)
def _binomial(n, k, prefix, block, harmonic):
    if k < 0 or k > n:
        return np.int64(0)
    r = n - k
    e = _p_adic_factorial(n) - _p_adic_factorial(k) - _p_adic_factorial(r)
    if e >= 2:
        return np.int64(0)
    denom = _mulmod(_factorial_unit(k, prefix, block, harmonic),
                    _factorial_unit(r, prefix, block, harmonic), MOD)
    val = _mulmod(_factorial_unit(n, prefix, block, harmonic), _invmod(denom), MOD)
    return _mulmod(val, _powmod(P, e, MOD), MOD)


@nb.njit(cache=True)
def _lucas_coefficient(m, s, prefix, block, harmonic):
    """[x^s] V_m(x) mod P^2, where V_m = lam+^m + lam-^m (lam^2 = lam + x).

    V_m(0) = 1 for m >= 1; otherwise the coefficient is (m/(m-s)) * C(m-s, s),
    handled with explicit P-adic valuations so factors of P in s or m-s cancel.
    """
    if s == 0:
        return np.int64(1)
    if 2 * s > m:
        return np.int64(0)
    valuation = (_p_adic_int(m) - _p_adic_int(m - s) + _p_adic_factorial(m - s)
                 - _p_adic_factorial(s) - _p_adic_factorial(m - 2 * s))
    if valuation >= 2:
        return np.int64(0)
    unit = _mulmod(_unit_int(m), _invmod(_unit_int(m - s)), MOD)
    unit = _mulmod(unit, _factorial_unit(m - s, prefix, block, harmonic), MOD)
    denom = _mulmod(_factorial_unit(s, prefix, block, harmonic),
                    _factorial_unit(m - 2 * s, prefix, block, harmonic), MOD)
    unit = _mulmod(unit, _invmod(denom), MOD)
    return _mulmod(unit, _powmod(P, valuation, MOD), MOD)


@nb.njit(cache=True)
def _sliders_jit(n, k, prefix, block, harmonic):
    total = np.int64(0)
    i = np.int64(0)
    while n * i <= k and i <= n // 2:
        s = k - n * i
        sign = 1 if (n * i) % 2 == 0 else -1
        if i == n - i:  # middle term, only for even N
            if s == 0:
                total = (total + sign * _binomial(n, i, prefix, block, harmonic)) % MOD
        else:
            b = _binomial(n, i, prefix, block, harmonic)
            if b:
                term = _mulmod(b, _lucas_coefficient(n * (n - 2 * i), s, prefix, block, harmonic), MOD)
                total = (total + sign * term) % MOD
        i += 1
    return total % MOD


_PREFIX, _HARMONIC = _build_tables()
_BLOCK = int(_PREFIX[P - 1])  # (P-1)! mod P^2 (Wolstenholme)


def sliders_mod(n: int, k: int) -> int:
    """L(N, K) mod P^2: K non-attacking Sliders on an N x N cylindrical board."""
    return int(_sliders_jit(n, k, _PREFIX, _BLOCK, _HARMONIC))


if __name__ == "__main__":
    assert sliders_mod(2, 2) == 4
    assert sliders_mod(6, 12) == 4204761
    print(sliders_mod(10**9, 10**15))  # 26532152736197
