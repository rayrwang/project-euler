"""Project Euler Problem 611: Hallway of Square Steps.

Door n is toggled once for every pair 0 < i < j with i^2 + j^2 = n, so it
ends open iff r(n) = #{(i, j) : 0 < i < j, i^2 + j^2 = n} is odd, and
F(N) counts such n <= N.  With n = 2^a * prod p^e * prod q^f (p == 1,
q == 3 mod 4), the lattice-point formula r_2(n) = 4 B [all f even] with
B = prod(e + 1) refines, after separating i = 0 and i = j points, to

    r(n) = (B - s) / 2,    s = [n is a square] + [n/2 is a square],

so r(n) is odd iff B == 2 + s (mod 4).  Two clean cases follow:

* B == 2 (mod 4), forcing s = 0: exactly one p has odd exponent, which
  must be == 1 (mod 4).  Uniquely n = 2^a p^(4t+1) m^2 with m odd, p
  coprime to 2m.  Counting these needs pi_1(X) = #primes == 1 (mod 4)
  up to X = N/(2^a m^2) -- all lattice quotients of N -- supplied by a
  Lucy_Hedgehog sieve split over the residue classes 1 and 3 mod 4
  (sieving starts at p = 3 since the classes hold odd numbers only).
  The rare t >= 1 cases use the explicit small-prime list.

* B == 3 (mod 4) with s = 1: n = 2^a m^2, m odd, where the number of
  primes == 1 (mod 4) dividing m to an odd power is odd -- a direct
  smallest-prime-factor sieve over m <= 10^6 with prefix counts.

Checks: F(5) = 1, F(100) = 27, F(1000) = 233, F(10^6) = 112168 (given),
plus a brute-force door-toggling simulation compared at many cutoffs.
"""

import numba
import numpy as np


@numba.jit(cache=True)
def F(N: int) -> int:
    K = int(N**0.5)
    while K * K > N:
        K -= 1
    while (K + 1) * (K + 1) <= N:
        K += 1

    # Lucy sieve over residue classes 1, 3 (mod 4)
    c1s = np.empty(K + 1, dtype=np.int64)
    c3s = np.empty(K + 1, dtype=np.int64)
    c1l = np.empty(K + 1, dtype=np.int64)
    c3l = np.empty(K + 1, dtype=np.int64)
    for v in range(1, K + 1):
        c1s[v] = (v + 3) // 4 - 1  # 5, 9, 13, ... <= v
        c3s[v] = (v + 1) // 4  # 3, 7, 11, ... <= v
    for k in range(1, K + 1):
        v = N // k
        c1l[k] = (v + 3) // 4 - 1
        c3l[k] = (v + 1) // 4
    for p in range(3, K + 1):
        if c1s[p] + c3s[p] == c1s[p - 1] + c3s[p - 1]:
            continue
        a1 = c1s[p - 1]
        a3 = c3s[p - 1]
        p2 = p * p
        kmax = min(K, N // p2)
        one_mod4 = p % 4 == 1
        for k in range(1, kmax + 1):
            d = k * p
            if d <= K:
                q1 = c1l[d]
                q3 = c3l[d]
            else:
                q1 = c1s[N // d]
                q3 = c3s[N // d]
            if one_mod4:
                c1l[k] -= q1 - a1
                c3l[k] -= q3 - a3
            else:
                c1l[k] -= q3 - a3
                c3l[k] -= q1 - a1
        for v in range(K, p2 - 1, -1):
            q1 = c1s[v // p]
            q3 = c3s[v // p]
            if one_mod4:
                c1s[v] -= q1 - a1
                c3s[v] -= q3 - a3
            else:
                c1s[v] -= q3 - a3
                c3s[v] -= q1 - a1

    # smallest prime factor for m <= K (odd m used)
    spf = np.zeros(K + 1, dtype=np.int64)
    for i in range(2, K + 1):
        if spf[i] == 0:
            for j in range(i, K + 1, i):
                if spf[j] == 0:
                    spf[j] = i

    # small primes == 1 (mod 4), for t >= 1 and divisor corrections
    small_p1 = np.empty(K, dtype=np.int64)
    np1 = 0
    for p in range(5, K + 1, 4):
        if spf[p] == p:
            small_p1[np1] = p
            np1 += 1

    total = 0
    # Case 2: n = 2^a m^2, odd #'odd-exponent 1-mod-4 primes' in m
    chi_count = np.zeros(K + 1, dtype=np.int64)  # prefix counts of chi=1
    for m in range(1, K + 1):
        good = 0
        if m % 2 == 1:
            v = m
            cnt = 0
            while v > 1:
                p = spf[v]
                e = 0
                while v % p == 0:
                    v //= p
                    e += 1
                if p % 4 == 1 and e % 2 == 1:
                    cnt += 1
            good = cnt & 1
        chi_count[m] = chi_count[m - 1] + good
    pw = 1  # 2^a
    while pw <= N:
        r = N // pw
        s = int(r**0.5)
        while s * s > r:
            s -= 1
        while (s + 1) * (s + 1) <= r:
            s += 1
        total += chi_count[min(s, K)]
        pw *= 2

    # Case 1: n = 2^a p^(4t+1) m^2, p == 1 (mod 4), p coprime to 2m
    divs = np.empty(16, dtype=np.int64)
    pw = 1
    while pw <= N // 5:
        budget = N // pw
        m = 1
        while m * m * 5 <= budget:
            X = budget // (m * m)
            # 1-mod-4 prime divisors of m
            nd = 0
            v = m
            while v > 1:
                p = spf[v]
                while v % p == 0:
                    v //= p
                if p % 4 == 1:
                    divs[nd] = p
                    nd += 1
            # t = 0: pi_1(X) minus divisors of m that are <= X
            k_idx = pw * m * m
            if k_idx <= K:
                cnt = c1l[k_idx]
            else:
                cnt = c1s[N // k_idx]
            for i in range(nd):
                if divs[i] <= X:
                    cnt -= 1
            total += cnt
            # t >= 1: p^(4t+1) <= X  (so p <= X^(1/5) <= 251 for X <= 10^12)
            for i in range(np1):
                p = small_p1[i]
                if p > 4000:  # 4000^5 would already exceed any X here
                    break
                step = p * p * p * p
                ppow = step * p
                if ppow > X:
                    break
                skip = False
                for d in range(nd):
                    if divs[d] == p:
                        skip = True
                        break
                while ppow <= X:
                    if not skip:
                        total += 1
                    if ppow > X // step:
                        break
                    ppow *= step
            m += 2
        pw *= 2
    return total


def F_brute(N: int) -> np.ndarray:
    doors = np.zeros(N + 1, dtype=bool)
    i = 1
    while 2 * i * i < N:
        j = i + 1
        while i * i + j * j <= N:
            doors[i * i + j * j] ^= True
            j += 1
        i += 1
    return np.cumsum(doors).astype(np.int64)


if __name__ == "__main__":
    cum = F_brute(10**6)
    for n in (5, 100, 1000, 54321, 10**6):
        assert F(n) == int(cum[n]), n
    assert int(cum[100]) == 27 and int(cum[1000]) == 233
    assert int(cum[10**6]) == 112168
    print(F(10**12))  # 49283233900
