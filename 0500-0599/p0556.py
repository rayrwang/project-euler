"""
https://projecteuler.net/problem=556

A proper Gaussian integer has a > 0, b >= 0; it is squarefree if its
factorization into proper Gaussian primes has no repeats. f(n)
counts proper squarefree Gaussian integers of norm at most n; find
f(10^14).

Mobius inversion over Z[i]: [z squarefree] = sum over proper d with
d^2 | z of mu_G(d), so f(n) = sum_k m(k) G(floor(n / k^2)) where
G(M) counts proper Gaussian integers of norm in [1, M] - one quarter
of the nonzero circle-lattice count, G(M) = floor(sqrt(M)) +
sum_(x=1..sqrt(M)) floor(sqrt(M - x^2)) - and
m(k) = sum_(proper d, N(d) = k) mu_G(d). Since
sum m(k) k^(-s) = 1 / zeta_Q(i)(s), m is multiplicative with
m(2) = -1 (ramified), m(p) = -2 and m(p^2) = 1 for p = 1 mod 4
(split), m(p^2) = -1 for p = 3 mod 4 (inert, no norm-p elements),
and 0 at all other prime powers. m is built by a linear sieve to
k <= 10^7 and the G evaluations cost sqrt(n) H(10^7) ~ 1.6 * 10^8
integer square roots.

Verified against a literal brute force for n <= 300 (testing
divisibility of each proper z by d^2 over all proper d) and the
given f(10^2) = 54, f(10^4) = 5218, f(10^8) = 52126906.
"""

import numba
import numpy as np


@numba.njit(cache=True)
def _m_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    primes = np.zeros(n + 1, dtype=np.int32)
    cnt = 0
    m = np.zeros(n + 1, dtype=np.int8)
    m[1] = 1
    pe = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes[cnt] = i
            cnt += 1
            pe[i] = i
            m[i] = -1 if i == 2 else (-2 if i % 4 == 1 else 0)
        for j in range(cnt):
            p = primes[j]
            if p > spf[i] or i * p > n:
                break
            ip = i * p
            spf[ip] = p
            if i % p == 0:
                pe[ip] = pe[i] * p
                rest = ip // pe[ip]
                if p == 2:
                    mp = 0
                elif p % 4 == 1:
                    mp = 1 if pe[ip] == p * p else 0
                else:
                    mp = -1 if pe[ip] == p * p else 0
                m[ip] = m[rest] * mp
            else:
                pe[ip] = p
                m[ip] = m[i] * m[p]
    return m


@numba.njit(cache=True, inline="always")
def _isqrt(x: np.int64) -> np.int64:
    r = np.int64(np.sqrt(x))
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


@numba.njit(cache=True)
def _g(m: np.int64) -> np.int64:
    if m < 1:
        return np.int64(0)
    s = _isqrt(m)
    tot = s
    for x in range(1, s + 1):
        tot += _isqrt(m - x * x)
    return tot


@numba.njit(cache=True, parallel=True)
def f_of(n: int, m: np.ndarray) -> np.int64:
    k_max = _isqrt(np.int64(n))
    sums = np.zeros(64, dtype=np.int64)
    for tid in numba.prange(64):  # ty: ignore[not-iterable]
        sub = np.int64(0)
        for k in range(1 + tid, k_max + 1, 64):
            if m[k] != 0:
                sub += m[k] * _g(n // (k * k))
        sums[tid] = sub
    return sums.sum()


def _brute_f(n: int) -> int:
    def divides(da: int, db: int, za: int, zb: int) -> bool:
        nn = da * da + db * db
        return (za * da + zb * db) % nn == 0 and (da * zb - za * db) % nn == 0

    sq = []  # proper d^2 with 2 <= N(d), N(d)^2 <= n
    for a in range(1, int(n**0.5) + 2):
        for b in range(0, int(n**0.5) + 2):
            nd = a * a + b * b
            if 2 <= nd and nd * nd <= n:
                sq.append((a * a - b * b, 2 * a * b))
    cnt = 0
    for a in range(1, int(n**0.5) + 2):
        for b in range(0, int(n**0.5) + 2):
            if 1 <= a * a + b * b <= n:
                if not any(divides(da, db, a, b) for da, db in sq):
                    cnt += 1
    return cnt


if __name__ == "__main__":
    m = _m_sieve(10**7)
    assert _brute_f(10) == 7 == f_of(10, m)  # given
    for n in (30, 100, 300):
        assert _brute_f(n) == f_of(n, m), n
    assert f_of(10**2, m) == 54  # given
    assert f_of(10**4, m) == 5218  # given
    assert f_of(10**8, m) == 52126906  # given

    print(f_of(10**14, m))  # 52126939292957
