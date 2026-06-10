"""Project Euler Problem 642: Sum of Largest Prime Factors.

F(N) = sum of the largest prime factor over 2..N for N = 201820182018,
modulo 10^9.  Grouping i = p * m by its largest prime p,

    F(N) = sum_p p * Psi(N/p, p),    Psi(y, p) = #{m <= y : P(m) <= p},

split into three regimes:

* p > sqrt(N): every m <= N/p < p qualifies, so the contribution is
  p * floor(N/p), summed in quotient blocks against the prime-sum function
  S(v) from a Lucy_Hedgehog sieve over the quotient lattice (S kept modulo
  10^9 -- the sieve uses only ring operations).
* cbrt(N) < p <= sqrt(N): here p^2 >= N/p, so any non-smooth m <= N/p has
  exactly one prime factor q > p, with multiplicity one and cofactor < p;
  hence Psi(N/p, p) = floor(N/p) - sum_{p < q <= N/p} floor(N/(pq)),
  evaluated in quotient blocks against pi(v) from the same sieve.  The
  block walks total only a few million steps.
* p^3 <= N (just the 770-odd primes up to ~5865): an in-place ascending
  array DP over the quotient lattice applies Psi(v, p) = Psi(v, prev)
  + Psi(v/p, p) one prime at a time, reading off Psi(N/p, p) after each.

Checks: F(10) = 32, F(100) = 1915, F(10000) = 10118280 (given), plus
agreement with a brute-force largest-prime-factor sieve at several
irregular cutoffs up to 10^7.
"""

import numba
import numpy as np

MOD = 10**9


@numba.jit(cache=True)
def F(N: int) -> int:
    K = int(N**0.5)
    while K * K > N:
        K -= 1
    while (K + 1) * (K + 1) <= N:
        K += 1
    # quotient lattice: small[v] for v <= K, large[k] for v = N//k > K
    cnt_s = np.empty(K + 1, dtype=np.int64)
    cnt_l = np.empty(K + 1, dtype=np.int64)
    sum_s = np.empty(K + 1, dtype=np.int64)
    sum_l = np.empty(K + 1, dtype=np.int64)
    for v in range(1, K + 1):
        cnt_s[v] = v - 1
        a = v % (2 * MOD)
        sum_s[v] = (a * (a + 1) % (2 * MOD)) // 2 % MOD
        sum_s[v] = (sum_s[v] - 1) % MOD
    for k in range(1, K + 1):
        v = N // k
        cnt_l[k] = v - 1
        a = v % (2 * MOD)
        sum_l[k] = (a * (a + 1) % (2 * MOD)) // 2 % MOD
        sum_l[k] = (sum_l[k] - 1) % MOD

    # Lucy_Hedgehog: after sieving all p <= K, cnt = pi, sum = S (mod)
    for p in range(2, K + 1):
        if cnt_s[p] == cnt_s[p - 1]:
            continue
        cp = cnt_s[p - 1]
        sp = sum_s[p - 1]
        p2 = p * p
        kmax = min(K, N // p2)
        for k in range(1, kmax + 1):
            d = k * p
            if d <= K:
                c = cnt_l[d]
                s = sum_l[d]
            else:
                c = cnt_s[N // d]
                s = sum_s[N // d]
            cnt_l[k] -= c - cp
            sum_l[k] = (sum_l[k] - p * ((s - sp) % MOD)) % MOD
        for v in range(K, p2 - 1, -1):
            c = cnt_s[v // p]
            s = sum_s[v // p]
            cnt_s[v] -= c - cp
            sum_s[v] = (sum_s[v] - p * ((s - sp) % MOD)) % MOD

    total = 0

    # big primes p > K: contribution p * floor(N/p) over quotient blocks
    t = 1
    while True:
        hi = N // t
        if hi <= K:
            break
        lo = max(K, N // (t + 1))
        s_hi = sum_l[t] if hi > K else sum_s[hi]
        s_lo = sum_l[N // lo] if lo > K else sum_s[lo]
        total = (total + t * ((s_hi - s_lo) % MOD)) % MOD
        t += 1

    # boundary between DP and closed-form regimes: largest p with p^3 <= N
    B = 1
    while (B + 1) ** 3 <= N:
        B += 1

    # primes sieve up to K for direct iteration
    is_p = np.ones(K + 1, dtype=np.bool_)
    is_p[:2] = False
    for i in range(2, int(K**0.5) + 2):
        if is_p[i]:
            is_p[i * i :: i] = False

    # mid primes: B < p <= K, closed-form smooth count
    for p in range(B + 1, K + 1):
        if not is_p[p]:
            continue
        y = N // p
        psi = y
        t = 1
        while True:
            q_hi = y // t
            if q_hi <= p:
                break
            q_lo = max(p, y // (t + 1))
            pi_hi = cnt_l[p * t] if q_hi > K else cnt_s[q_hi]
            pi_lo = cnt_l[N // q_lo] if q_lo > K else cnt_s[q_lo]
            psi -= t * (pi_hi - pi_lo)
            t += 1
        total = (total + p % MOD * (psi % MOD)) % MOD

    # small primes: p^3 <= N, ascending in-place DP over the lattice
    smooth_s = np.ones(K + 1, dtype=np.int64)  # Psi(v, current p) for v <= K
    smooth_l = np.ones(K + 1, dtype=np.int64)  # ... for v = N//k
    smooth_s[0] = 0
    for p in range(2, B + 1):
        if not is_p[p]:
            continue
        for v in range(p, K + 1):  # ascending v
            smooth_s[v] += smooth_s[v // p]
        for k in range(K, 0, -1):  # descending k = ascending v = N//k
            d = k * p
            smooth_l[k] += smooth_l[d] if d <= K else smooth_s[N // d]
        total = (total + p * (smooth_l[p] % MOD)) % MOD
    return total


def brute(n: int) -> int:
    lpf = np.zeros(n + 1, dtype=np.int64)
    for p in range(2, n + 1):
        if lpf[p] == 0:
            lpf[p::p] = p
    return int(lpf[2:].sum() % MOD)


if __name__ == "__main__":
    assert F(10) == 32 and F(100) == 1915 and F(10000) == 10118280
    for n in (54321, 999983, 10**7):
        assert F(n) == brute(n), n
    print(F(201820182018))  # 631499044
