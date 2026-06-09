"""
https://projecteuler.net/problem=536

S(n) sums the m <= n with a^(m+4) = a (mod m) for all integers a.
Find S(10^12).

Characterization (verified literally for m <= 1000 below): the property
holds iff m is squarefree and (p - 1) | (m + 3) for every prime p | m.
By CRT the condition splits over prime powers p^e || m. Taking a = p
forces e = 1 (p^(m+4) = p mod p^e needs p^(e-1) | p^(m+3) - 1, and
p^(m+3) - 1 = -1 mod p). For squarefree m and p | m, a coprime to p,
a^(m+3) = 1 (mod p) for all such a iff (p - 1) | (m + 3); a divisible
by p gives 0 = 0.

Consequences. m = 2 is the only even solution > 1 (an odd prime p | m
would need even p - 1 dividing odd m + 3). Since m = p * s gives
m = s (mod p - 1), the condition reads (p - 1) | (s + 3), so
p - 1 <= m/p + 3: every prime factor satisfies p(p - 4) <= m <= n,
hence p < 10^6 + 5 for n = 10^12.

Search: depth-first over the odd prime factors in decreasing order.
With chosen primes of product T and M = lcm(p - 1), the remaining
cofactor s solves T s = -3 (mod M), a single congruence s = r (mod K)
(solvable only if gcd(T, M) | 3, a strong prune). When the progression
r, r + K, ... up to n/T has at most B members, each candidate s is
checked directly (squarefree, all factors below the last chosen prime,
and (q - 1) | (m + 3) per factor); otherwise the next smaller prime is
branched on. M - 3 <= n bounds M (since M | m + 3 forces m >= M - 3).
"""

import sys
from math import gcd
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402

BRANCH_LIMIT = 1000  # max progression length enumerated at a leaf


@numba.njit(cache=True)
def _check_candidate(
    m: int, s: int, p_last: int, primes: np.ndarray, n_primes: int
) -> bool:
    """m = T * s with the congruences for the chosen primes already
    satisfied. Verify s is squarefree with all prime factors below
    p_last and (q - 1) | (m + 3) for every prime q | s."""
    if s == 1:
        return True
    rem = s
    for i in range(n_primes):
        q = primes[i]
        if q >= p_last:
            return False
        if q * q > rem:
            break
        if rem % q == 0:
            rem //= q
            if rem % q == 0:
                return False  # not squarefree
            if (m + 3) % (q - 1) != 0:
                return False
            if rem == 1:
                return True
    # rem is prime: it has no factor up to its square root
    if rem >= p_last:
        return False
    return (m + 3) % (rem - 1) == 0


@numba.njit(cache=True)
def _dfs(
    T: int,
    M: int,
    p_idx: int,
    first_p: int,
    n: int,
    primes: np.ndarray,
    n_primes: int,
    out: np.ndarray,
) -> None:
    # solve T * s = -3 (mod M) for the cofactor s
    a = T % M
    b = (-3) % M
    g = gcd(a, M)
    if b % g != 0:
        return
    K = M // g
    ag = (a // g) % K
    bg = (b // g) % K
    # modular inverse of ag mod K (extended Euclid); K = 1 gives r = 0
    t0, t1 = np.int64(0), np.int64(1)
    r0, r1 = K, ag
    while r1 != 0:
        q = r0 // r1
        t0, t1 = t1, t0 - q * t1
        r0, r1 = r1, r0 - q * r1
    r = (bg * (t0 % K)) % K
    if r == 0:
        r = K  # s >= 1
    smax = n // T
    if smax < r:
        return
    m_min = first_p * (first_p - 4)
    if (smax - r) // K + 1 <= BRANCH_LIMIT:
        # enumerate the whole progression
        p_last = primes[p_idx]
        s = r
        while s <= smax:
            m = T * s
            if (
                m >= m_min
                and m >= M - 3
                and _check_candidate(m, s, p_last, primes, n_primes)
            ):
                out[0] += m
                out[1] += 1
            s += K
        return
    # close with s = 1
    if (1 - r) % K == 0 and T >= m_min and T >= M - 3:
        out[0] += T
        out[1] += 1
    # branch on the next smaller prime
    for i in range(p_idx):
        q = primes[i]
        if T > n // q:
            break
        d = gcd(M, q - 1)
        M2 = (M // d) * (q - 1)
        if M2 - 3 > n:
            continue
        _dfs(T * q, M2, i, first_p, n, primes, n_primes, out)


@numba.njit(cache=True)
def s_of(n: int) -> int:
    limit = int(n**0.5) + 5
    primes = prime_sieve_int(limit)[1:]  # odd primes
    n_primes = len(primes)
    out = np.zeros(2, dtype=np.int64)
    out[0] = 3 if n >= 2 else 1  # m = 1 and m = 2
    for i in range(n_primes - 1, -1, -1):
        p = primes[i]
        if p > n or p * (p - 4) > n:
            continue
        _dfs(p, p - 1, i, p, n, primes, n_primes, out)
    return out[0]


def brute_charac(n: int) -> int:
    """Sum via the squarefree + (p-1) | (m+3) characterization, by
    direct factorization of every m."""
    total = 0
    for m in range(1, n + 1):
        mm = m
        ok = True
        p = 2
        while p * p <= mm:
            if mm % p == 0:
                mm //= p
                if mm % p == 0 or (p > 2 and (m + 3) % (p - 1) != 0):
                    ok = False
                    break
            else:
                p += 1
        if ok and mm > 1 and mm != m and (m + 3) % (mm - 1) != 0:
            ok = False
        if ok and mm == m and m > 1 and (m + 3) % (m - 1) != 0:
            ok = False
        if ok:
            total += m
    return total


def brute_literal(n: int) -> list[int]:
    """The property exactly as stated, testing every base a."""
    return [
        m for m in range(1, n + 1) if all(pow(a, m + 4, m) == a % m for a in range(m))
    ]


if __name__ == "__main__":
    # the characterization agrees with the literal definition
    literal = brute_literal(1000)
    assert literal[:5] == [1, 2, 3, 5, 21]
    assert sum(v for v in literal if v <= 100) == 32  # S(100) = 32
    assert brute_charac(1000) == sum(literal)
    # the search agrees with brute force
    for nn in (100, 10**4, 10**6):
        assert s_of(nn) == brute_charac(nn)

    print(s_of(10**12))  # 3557005261906288
