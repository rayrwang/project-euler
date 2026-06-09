"""
https://projecteuler.net/problem=578

n has "decreasing prime powers" if, writing n = p1^e1 ... pk^ek with
p1 < ... < pk, the exponents satisfy e1 >= e2 >= ... >= ek. C(n)
counts such integers up to n; find C(10^13).

Depth-first search over the prime factorizations in increasing prime
order, carrying the prefix product m and the maximum exponent allowed
next (the last exponent used). Each node counts its own prefix, then:

  - for primes q above the last one with q <= sqrt(n/m), every
    exponent e in 1..e_max with m q^e <= n recurses (such q can still
    be extended by further primes);
  - primes q with q > sqrt(n/m) can only appear to the first power and
    admit no further extension (the next prime would need to exceed q
    yet be at most (n/m)/q < q), so they are counted in bulk as
    pi(n/m) - pi(max(p_last, sqrt(n/m))).

All pi queries land on values of the form floor(n/m) or below
sqrt(n), exactly what one Lucy_Hedgehog sieve provides in O(n^(3/4)):
small[v] = pi(v) for v <= sqrt(n) and large[k] = pi(n//k). The sieve
is sanity-checked against pi(10^8) = 5761455, and the count against a
direct per-integer factorization for n <= 10^5 plus the given
C(100) = 94 and C(10^6) = 922052.
"""

import numba
import numpy as np


@numba.njit(cache=True)
def _isqrt(x: int) -> int:
    r = int(np.sqrt(x))
    while (r + 1) * (r + 1) <= x:
        r += 1
    while r * r > x:
        r -= 1
    return r


@numba.njit(cache=True)
def lucy_pi(n: int):
    """small[v] = pi(v) for v <= r and large[k] = pi(n//k) for k <= r,
    with r = isqrt(n)."""
    r = _isqrt(n)
    small = np.empty(r + 1, dtype=np.int64)
    large = np.empty(r + 1, dtype=np.int64)
    for v in range(r + 1):
        small[v] = v - 1
    for k in range(1, r + 1):
        large[k] = n // k - 1
    for p in range(2, r + 1):
        if small[p] == small[p - 1]:
            continue  # p is not prime
        sp = small[p - 1]
        p2 = p * p
        kmax = min(r, n // p2)
        for k in range(1, kmax + 1):
            d = k * p
            if d <= r:
                large[k] -= large[d] - sp
            else:
                large[k] -= small[n // d] - sp
        for v in range(r, p2 - 1, -1):
            small[v] -= small[v // p] - sp
    return small, large, r


@numba.njit(cache=True)
def _pi(x: int, n: int, small: np.ndarray, large: np.ndarray, r: int) -> int:
    if x <= r:
        return small[x]
    return large[n // x]


@numba.njit(cache=True)
def _dfs(
    m: int,
    p_idx: int,
    e_max: int,
    n: int,
    primes: np.ndarray,
    small: np.ndarray,
    large: np.ndarray,
    r: int,
) -> int:
    total = 1  # the prefix m itself
    rem = n // m
    s = _isqrt(rem)
    plast = primes[p_idx] if p_idx >= 0 else np.int64(1)
    lo = plast if plast > s else s
    if rem > lo:
        total += _pi(rem, n, small, large, r) - _pi(lo, n, small, large, r)
    for j in range(p_idx + 1, len(primes)):
        q = primes[j]
        if q > s:
            break
        qe = q
        e = 1
        while e <= e_max:
            total += _dfs(m * qe, j, e, n, primes, small, large, r)
            if qe > rem // q:
                break
            qe *= q
            e += 1
    return total


def c_of(n: int) -> int:
    small, large, r = lucy_pi(n)
    sieve = np.ones(r + 1, dtype=np.bool_)
    sieve[:2] = False
    for i in range(2, int(r**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = np.flatnonzero(sieve).astype(np.int64)
    return int(_dfs(1, -1, 64, n, primes, small, large, r))


def c_brute(n: int) -> int:
    cnt = 0
    for m in range(1, n + 1):
        mm = m
        ok = True
        last_e = 1 << 30
        d = 2
        while d * d <= mm:
            if mm % d == 0:
                e = 0
                while mm % d == 0:
                    mm //= d
                    e += 1
                if e > last_e:
                    ok = False
                    break
                last_e = e
            d += 1
        # a trailing prime has exponent 1 <= last_e, never a violation
        if ok:
            cnt += 1
    return cnt


if __name__ == "__main__":
    small, large, r = lucy_pi(10**8)
    assert int(large[1]) == 5761455  # pi(10^8)

    assert c_of(100) == c_brute(100) == 94
    assert c_of(10**5) == c_brute(10**5)
    assert c_of(10**6) == 922052  # given

    print(c_of(10**13))  # 9219696799346
