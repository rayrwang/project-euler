"""Project Euler Problem 521: Smallest Prime Factor.

smpf(n) = smallest prime factor of n.  S(n) = sum_{2<=i<=n} smpf(i).  Find
S(10^12) mod 10^9.

Group i by its smallest prime factor.  Numbers i <= n with smpf(i) = p are exactly
i = p*m with m having no prime factor < p, so their count is Phi(floor(n/p), p),
where Phi(x, p) = #{m <= x : m = 1 or every prime factor of m is >= p}.  Hence

    S(n) = sum_{p prime <= n} p * Phi(floor(n/p), p).

For p > sqrt(n) we have floor(n/p) < p, so Phi = 1 and the contribution is just p;
summed, that is PrimeSum(n) - PrimeSum(sqrt n).  For p <= sqrt(n) we read
Phi(floor(n/p), p) = 1 + C[floor(n/p)] - pi(p-1) from a Lucy_Hedgehog sieve, taken
just before sieving out p (so the array counts integers with no prime factor < p).
A parallel Lucy pass on prime sums (mod 10^9) supplies the large-prime tail.
"""

import numpy as np
import numba

MOD = 10**9


@numba.jit(cache=True)
def _tri_mod(v: int) -> int:
    # (v*(v+1)//2) mod MOD, overflow-safe for v up to ~1e12
    if v % 2 == 0:
        return ((v // 2) % MOD) * ((v + 1) % MOD) % MOD
    return (v % MOD) * (((v + 1) // 2) % MOD) % MOD


@numba.jit(cache=True)
def _isqrt(n: int) -> int:
    x = int(n**0.5)
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@numba.jit(cache=True)
def _solve(n: int) -> int:
    r = _isqrt(n)
    # count arrays (exact int64; values <= n < 2^63)
    Sc_s = np.empty(r + 1, dtype=np.int64)
    Sc_l = np.empty(r + 1, dtype=np.int64)
    # prime-sum arrays (kept modulo MOD)
    Ss_s = np.empty(r + 1, dtype=np.int64)
    Ss_l = np.empty(r + 1, dtype=np.int64)

    for v in range(1, r + 1):
        Sc_s[v] = v - 1
        Ss_s[v] = (_tri_mod(v) - 1) % MOD
    for i in range(1, r + 1):
        V = n // i
        Sc_l[i] = V - 1
        Ss_l[i] = (_tri_mod(V) - 1) % MOD

    ans = 0
    for p in range(2, r + 1):
        if Sc_s[p] == Sc_s[p - 1]:
            continue  # p composite
        spc = Sc_s[p - 1]   # pi(p-1)
        sps = Ss_s[p - 1]   # sum of primes < p (mod MOD)

        # contribution of prime p (p <= sqrt n) using current (pre-sieve) counts
        V = n // p
        cval = Sc_s[V] if V <= r else Sc_l[p]  # large index for n//p is p
        phi = 1 + cval - spc
        ans = (ans + (p % MOD) * (phi % MOD)) % MOD

        p2 = p * p
        # update large keys
        i = 1
        while i <= r and n // i >= p2:
            ip = i * p
            if ip <= r:
                c2 = Sc_l[ip]
                s2 = Ss_l[ip]
            else:
                w = n // ip
                c2 = Sc_s[w]
                s2 = Ss_s[w]
            Sc_l[i] -= c2 - spc
            Ss_l[i] = (Ss_l[i] - (p % MOD) * ((s2 - sps) % MOD)) % MOD
            i += 1
        # update small keys
        v = r
        while v >= p2:
            Sc_s[v] -= Sc_s[v // p] - spc
            Ss_s[v] = (Ss_s[v] - (p % MOD) * ((Ss_s[v // p] - sps) % MOD)) % MOD
            v -= 1

    # tail: sum of primes in (sqrt n, n]
    primesum_n = Ss_l[1] % MOD
    primesum_r = Ss_s[r] % MOD
    tail = (primesum_n - primesum_r) % MOD
    ans = (ans + tail) % MOD
    return ans % MOD


def S(n: int) -> int:
    return int(_solve(n)) % MOD


def _brute(n: int) -> int:
    spf = list(range(n + 1))
    for i in range(2, n + 1):
        if spf[i] == i:  # i prime
            for j in range(i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return sum(spf[2:])


if __name__ == "__main__":
    assert S(100) == 1257, S(100)
    for nn in (1000, 100000, 1_000_000):
        assert S(nn) % MOD == _brute(nn) % MOD, (nn, S(nn), _brute(nn))
    print(S(10**12))  # 44389811
