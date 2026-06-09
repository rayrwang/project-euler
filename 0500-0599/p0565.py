"""Project Euler Problem 565: Divisibility of Sum of Divisors.

S(n, d) = sum of the i <= n with d | sigma(i).  Find S(10^11, 2017).

sigma is multiplicative and d = 2017 is prime, so 2017 | sigma(n) exactly
when some exact prime-power component p^e || n has 2017 | sigma(p^e); call
such prime powers special.

Finding the special prime powers q = p^e <= N:
  e = 1: sigma(p) = p + 1, so p == -1 (mod 2017).  The candidates
         c = 2017 k - 1 <= N are sieved by every prime up to sqrt(N): each
         small prime r strikes an arithmetic progression of k (skipping the
         k with c = r itself).  A surviving candidate has no factor <=
         sqrt(N), hence is prime — no probabilistic tests needed.
  e >= 2: only p <= N^(1/e) matters, so sigma(p^e) mod 2017 is checked
         directly for all primes p <= sqrt(N).

The smallest special value for d = 2017 is 12101, and 12101^3 > 10^11, so an
n <= N contains at most two special components.  With T(M) = M(M+1)/2,

  S = sum_q q * [T(M) - p T(M//p)],  M = N // q   (the m with p not | m,
                                                   so p^e || q m exactly)
    - sum_{q1 q2 <= N, p1 != p2} q1 q2 * sum_{m <= N//(q1 q2),
                                              p1 not| m, p2 not| m} m,

the second sum removing the double count of n containing two special
components (computed with two-prime inclusion-exclusion on m).  Only special
q1 < sqrt(N) can occur in a pair, so the pair sum is tiny.  Totals exceed
int64 comfort, so the accumulation uses exact Python integers.

Checks: S(20, 7) = 49, S(10^6, 2017) = 150850429,
S(10^9, 2017) = 249652238344557.
"""

from bisect import bisect_left, bisect_right
from math import isqrt

import numpy as np
import numba


@numba.jit(cache=True)
def _strike(alive: np.ndarray, primes: np.ndarray, k0s: np.ndarray, d: int) -> None:
    """Mark composite candidates c = d*k - 1 (alive is indexed by k, 0..K)."""
    big = len(alive)
    for i in range(len(primes)):
        r = primes[i]
        k0 = k0s[i]
        if k0 < 0:  # r == d: c == -1 (mod d) is never divisible by d
            continue
        k_self = (r + 1) // d if (r + 1) % d == 0 else -1  # k where c == r
        for k in range(k0, big, r):
            if k != k_self:
                alive[k] = False


def _sigma_pe_mod(p: int, e: int, d: int) -> int:
    s = 0
    pw = 1
    for _ in range(e + 1):
        s = (s + pw) % d
        pw = pw * p % d
    return s


def _special_prime_powers(n: int, d: int) -> list[tuple[int, int]]:
    """All (q, p) with q = p^e <= n, p prime, and d | sigma(p^e)."""
    root = isqrt(n)
    sieve = np.ones(root + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(root**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    small_primes = np.flatnonzero(sieve).astype(np.int64)

    # e = 1: sieve the candidates c = d*k - 1 <= n.
    big = (n + 1) // d  # largest k
    alive = np.ones(big + 1, dtype=bool)
    alive[0] = False
    k0s = np.array(
        [pow(d, -1, int(r)) if r != d else -1 for r in small_primes],
        dtype=np.int64,
    )
    _strike(alive, small_primes, k0s, d)
    specials = []
    for k in np.flatnonzero(alive):
        c = d * int(k) - 1
        if c > 1:
            specials.append((c, c))

    # e >= 2.
    for p in small_primes:
        p = int(p)
        q = p * p
        e = 2
        while q <= n:
            if _sigma_pe_mod(p, e, d) == 0:
                specials.append((q, p))
            q *= p
            e += 1

    specials.sort()
    return specials


def T(m: int) -> int:
    return m * (m + 1) // 2


def S(n: int, d: int) -> int:
    specials = _special_prime_powers(n, d)
    if not specials:
        return 0
    assert specials[0][0] ** 3 > n, "three special components would fit"

    total = 0
    for q, p in specials:
        m = n // q
        total += q * (T(m) - p * T(m // p))

    # Subtract n containing two special components, counted twice above.
    qs = [q for q, _ in specials]
    for i in range(bisect_right(qs, isqrt(n) + 1)):
        q1, p1 = specials[i]
        if q1 * q1 > n:
            break
        for j in range(i + 1, bisect_left(qs, n // q1 + 1)):
            q2, p2 = specials[j]
            if p1 == p2:
                continue  # cannot both be exact components
            m = n // (q1 * q2)
            inner = (
                T(m)
                - p1 * T(m // p1)
                - p2 * T(m // p2)
                + p1 * p2 * T(m // (p1 * p2))
            )
            total -= q1 * q2 * inner
    return total


if __name__ == "__main__":
    assert S(20, 7) == 49, S(20, 7)
    assert S(10**6, 2017) == 150850429, S(10**6, 2017)
    assert S(10**9, 2017) == 249652238344557, S(10**9, 2017)
    print(S(10**11, 2017))  # 2992480851924313898
