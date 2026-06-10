"""
https://projecteuler.net/problem=533

The Carmichael function lambda(n) is the least m with a^m = 1
(mod n) for all a coprime to n. L(n) is the least m such that
lambda(k) >= n for all k >= m, i.e. L(n) - 1 is the largest k with
lambda(k) < n. Find L(20000000) mod 10^9.

lambda(k) is the lcm of the components lambda(p^e): p^(e-1)(p-1) for
odd p, and 1, 2, 2^(e-2) for p = 2 with e = 1, 2, >= 3. If
lambda(k) = L0 then every component divides L0, so k is at most

  K(L0) = 2-part * prod over odd primes p with (p-1) | L0
          of p^(1 + v_p(L0)),

where the 2-part is 2^(v_2(L0) + 2) for even L0 (lambda(2^e) =
2^(e-2) must divide L0) and 2 for odd L0. Conversely
lambda(K(L0)) divides L0, hence is < n whenever L0 < n. Therefore
L(n) - 1 = max over L0 < n of K(L0).

The values K(L0) are astronomically large, so a sieve accumulates
log K(L0) for all L0 < n: each prime p adds ln p at multiples of
p - 1, plus ln p at multiples of (p-1) p^j for the valuation term
(p-1 and p^j are coprime), plus one extra ln 2 at even L0. Distinct
huge products can be too close for floating point, so the top 200
candidates by log are recomputed exactly with big integers (factor
L0, run over its divisors d with d + 1 prime) and the true maximum
taken.

Verified against a direct lambda sieve (smallest-prime-factor
factorisation, lcm of components) for n in {3, 4, 6, 10, 16, 24}
where L(n) - 1 falls inside the 3 * 10^6 table, including the given
L(6) = 241; the given L(100) = 20174525281 is also asserted.
"""

import sys
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402


@numba.njit(cache=True)
def _build_logk(n: int, primes: np.ndarray) -> np.ndarray:
    """log K(L0) for 0 <= L0 < n."""
    logk = np.zeros(n, dtype=np.float64)
    for p in primes:
        lp = np.log(np.float64(p))
        d = p - 1
        for m in range(d, n, d):
            logk[m] += lp
        pj = np.int64(p)
        while True:
            step = d * pj  # lcm(p-1, p^j); coprime parts
            if step >= n:
                break
            for m in range(step, n, step):
                logk[m] += lp
            if pj > n // p:
                break
            pj *= p
    ln2 = np.log(2.0)
    for m in range(2, n, 2):
        logk[m] += ln2
    return logk


def _k_exact(l0: int, prime_bool: np.ndarray) -> int:
    """Exact maximal k with lambda(k) dividing l0."""
    v2 = 0
    t = l0
    while t % 2 == 0:
        t //= 2
        v2 += 1
    k = 2 ** (v2 + 2) if l0 % 2 == 0 else 2
    fac: dict[int, int] = {}
    m = l0
    d = 2
    while d * d <= m:
        while m % d == 0:
            fac[d] = fac.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        fac[m] = fac.get(m, 0) + 1
    divs = [1]
    for q, e in fac.items():
        divs = [dv * q**i for dv in divs for i in range(e + 1)]
    for dv in divs:
        p = dv + 1
        if p > 2 and p < len(prime_bool) and prime_bool[p]:
            vp = 0
            t = l0
            while t % p == 0:
                t //= p
                vp += 1
            k *= p ** (1 + vp)
    return k


def l_of(n: int, primes: np.ndarray, prime_bool: np.ndarray) -> int:
    logk = _build_logk(n, primes)
    best = 0
    for l0 in np.argsort(logk)[::-1][:200]:
        if l0 >= 1:
            best = max(best, _k_exact(int(l0), prime_bool))
    return best + 1


@numba.njit(cache=True)
def _lambda_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    lam = np.ones(n + 1, dtype=np.int64)
    for k in range(2, n + 1):
        m = k
        val = np.int64(1)
        while m > 1:
            p = spf[m]
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            if p == 2:
                comp = np.int64(1) if e == 1 else np.int64(2) ** max(1, e - 2)
            else:
                comp = np.int64(p) ** (e - 1) * (p - 1)
            val = (val // np.gcd(val, comp)) * comp
        lam[k] = val
    return lam


if __name__ == "__main__":
    primes = prime_sieve_int(20_000_001)
    prime_bool = np.zeros(20_000_002, dtype=bool)
    prime_bool[primes] = True

    lam = _lambda_sieve(3 * 10**6)
    assert int(lam[8]) == 2 and int(lam[240]) == 4  # given examples
    for n in (3, 4, 6, 10, 16, 24):
        last = 0
        for k in range(1, len(lam)):
            if lam[k] < n:
                last = k
        assert l_of(n, primes, prime_bool) == last + 1, n
    assert l_of(6, primes, prime_bool) == 241  # given
    assert l_of(100, primes, prime_bool) == 20174525281  # given

    print(l_of(20_000_000, primes, prime_bool) % 10**9)  # 789453601
