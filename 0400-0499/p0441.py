"""Problem 441: The Inverse Summation of Coprime Couples.

Swapping the order of summation, a coprime pair p < q contributes
1/(pq) to R(M) for every M in [q, min(p + q, N)], so
    S(N) = sum_{p+q <= N} (p + 1)/(pq) + sum_{q <= N < p+q} (N+1-q)/(pq)
over coprime pairs. The first piece splits into
    A = sum 1/q  and  B = sum 1/(pq):
for A, pairs with q <= N/2 contribute phi(q)/q wholesale and larger q
need the partial coprime count by Mobius over divisors of q; for B,
grouping by s = p + q and using 1/(pq) = (1/s)(1/p + 1/q) collapses
each s to (1/s) * (coprime harmonic sum up to s - 1), again a Mobius
sum over divisors with a precomputed harmonic table. The boundary
piece C is a per-q ranged coprime harmonic sum. Magnitudes reach 1e6
over 1e7 terms, so Kahan summation keeps the float error far below
the 1e-4 requirement.
"""

import numba
import numpy as np

@numba.jit(cache=True)
def s_total(n: int) -> float:
    # smallest prime factor -> divisor lists on demand; here: mu and
    # divisor iteration via smallest prime factorisation
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    harm = np.zeros(n + 1, dtype=np.float64)
    hc = 0.0
    he = 0.0
    for i in range(1, n + 1):
        y = 1.0 / i - he
        t = hc + y
        he = (t - hc) - y
        hc = t
        harm[i] = hc
    phi = np.arange(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    # squarefree divisors with mu, per q, via spf
    divs = np.empty(64, dtype=np.int64)
    mus = np.empty(64, dtype=np.int64)
    total = 0.0
    comp = 0.0
    for q in range(2, n + 1):
        # build squarefree divisors of q
        m = q
        nd = 1
        divs[0] = 1
        mus[0] = 1
        while m > 1:
            p = spf[m]
            while m % p == 0:
                m //= p
            for i in range(nd):
                divs[nd + i] = divs[i] * p
                mus[nd + i] = -mus[i]
            nd *= 2
        contrib = 0.0
        # A: sum over coprime p < q with p + q <= N of 1/q
        if 2 * q <= n:
            contrib += float(phi[q]) / q
        else:
            cnt = 0
            x = n - q  # p <= N - q
            if x >= 1:
                for i in range(nd):
                    cnt += mus[i] * (x // divs[i])
            contrib += cnt / q
        # B: handled below grouped by s; C: boundary q > N/2
        if 2 * q > n:
            # C: p in (N - q, q), weight (N + 1 - q)/(p q)
            lo = n - q  # p > lo
            hs = 0.0
            for i in range(nd):
                d = divs[i]
                hs += mus[i] / d * (harm[(q - 1) // d] - harm[lo // d])
            contrib += (n + 1 - q) / q * hs
        # B grouped by s = p + q: coprime pairs p < q, p + q = s <= N:
        # (1/s) * sum_{p < s, gcd(p, s) = 1} 1/p  -- reuse q as s
        s = q
        if s >= 3:
            hs = 0.0
            for i in range(nd):
                d = divs[i]
                hs += mus[i] / d * harm[(s - 1) // d]
            contrib += hs / s
        y = contrib - comp
        t = total + y
        comp = (t - total) - y
        total = t
    return total

def s_brute(n: int) -> float:
    from math import gcd
    tot = 0.0
    for m in range(2, n + 1):
        for q in range(2, m + 1):
            for p in range(max(1, m - q), q):
                if p + q >= m and gcd(p, q) == 1:
                    tot += 1.0 / (p * q)
    return tot

if __name__ == "__main__":
    assert abs(s_total(2) - 0.5) < 1e-12  # given S(2) = 1/2
    assert abs(s_total(10) - s_brute(10)) < 1e-9
    assert round(s_total(10), 4) == 6.9147  # given
    assert abs(s_total(100) - s_brute(100)) < 1e-9
    assert round(s_total(100), 4) == 58.2962  # given
    assert abs(s_total(300) - s_brute(300)) < 1e-9
    print(f"{s_total(10**7):.4f}")  # 5000088.8395
