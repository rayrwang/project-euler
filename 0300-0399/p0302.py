import sys
from bisect import bisect_right
from math import gcd, isqrt

import numpy as np

from funcs import prime_sieve_bool


def icbrt(n: int) -> int:
    c = round(n ** (1 / 3))
    while c**3 > n:
        c -= 1
    while (c + 1) ** 3 <= n:
        c += 1
    return c


def solve(limit: int) -> int:
    """Count Strong Achilles numbers below `limit`.

    n is Achilles if all prime exponents are >= 2 with gcd 1; Strong if
    phi(n) is also Achilles.  If the largest prime p of n had exponent 2,
    phi(n) would contain p exactly once (q = 1 mod p needs q > p), so the
    largest prime is cubed and every prime factor is <= limit^(1/3).
    Build n by a DFS over primes in descending order; a prime added with
    exponent 2 must already divide phi (i.e. divide r - 1 for some chosen
    larger prime r), since smaller primes can never supply it.
    """
    pmax = icbrt(limit)
    is_pr = prime_sieve_bool(pmax + 1)
    primes = np.flatnonzero(is_pr).tolist()
    npr = len(primes)
    index = {p: i for i, p in enumerate(primes)}

    # Factor p - 1 for every prime p <= pmax via a smallest-prime-factor sieve.
    spf = np.zeros(pmax + 1, dtype=np.int64)
    for p in primes:
        sl = spf[p::p]
        sl[sl == 0] = p
    fac_pm1: list[list[tuple[int, int]]] = []
    for p in primes:
        m = p - 1
        f = []
        while m > 1:
            q = int(spf[m])
            e = 0
            while m % q == 0:
                m //= q
                e += 1
            f.append((index[q], e))
        fac_pm1.append(f)

    phi_exp = [0] * npr  # exponent of primes[i] in phi(n so far)
    present: list[int] = []  # indices with phi_exp > 0, insertion order
    cnt1 = 0  # number of indices with phi_exp == 1 (phi powerful iff 0)
    count = 0

    def bump(j: int, e: int) -> None:
        nonlocal cnt1
        old = phi_exp[j]
        if old == 0:
            present.append(j)
        phi_exp[j] = old + e
        cnt1 += (old + e == 1) - (old == 1)

    def unbump(j: int, e: int) -> None:
        nonlocal cnt1
        old = phi_exp[j]
        phi_exp[j] = old - e
        cnt1 += (old - e == 1) - (old == 1)
        if old - e == 0:
            present.pop()

    def dfs(i: int, budget: int, n_exp_gcd: int) -> None:
        nonlocal count
        # The current node is itself a candidate n.
        if n_exp_gcd == 1 and cnt1 == 0:
            g = 0
            for j in present:
                g = gcd(g, phi_exp[j])
                if g == 1:
                    break
            if g == 1:
                count += 1
        # Children with exponent >= 3 (or 2 when phi already contains q).
        j_cap = bisect_right(primes, min(icbrt(budget), primes[i] - 1)) - 1
        for j in range(j_cap, -1, -1):
            q = primes[j]
            e0 = 2 if phi_exp[j] >= 1 else 3
            qe = q * q if e0 == 2 else q * q * q
            e = e0
            while qe <= budget:
                bump(j, e - 1)
                for k, f in fac_pm1[j]:
                    bump(k, f)
                dfs(j, budget // qe, gcd(n_exp_gcd, e))
                for k, f in reversed(fac_pm1[j]):
                    unbump(k, f)
                unbump(j, e - 1)
                qe *= q
                e += 1
        # Exponent-2-only children above the cube root: q must already
        # divide phi, so enumerate the present primes.
        lo = 0 if j_cap < 0 else primes[j_cap]
        hi = min(isqrt(budget), primes[i] - 1)
        for j2 in present:
            q = primes[j2]
            if lo < q <= hi:
                bump(j2, 1)
                for k, f in fac_pm1[j2]:
                    bump(k, f)
                dfs(j2, budget // (q * q), gcd(n_exp_gcd, 2))
                for k, f in reversed(fac_pm1[j2]):
                    unbump(k, f)
                unbump(j2, 1)

    for i in range(npr):
        p = primes[i]
        pe = p * p * p
        if pe > limit:
            break
        e = 3
        while pe <= limit:
            bump(i, e - 1)
            for k, f in fac_pm1[i]:
                bump(k, f)
            dfs(i, (limit - 1) // pe, e)
            for k, f in reversed(fac_pm1[i]):
                unbump(k, f)
            unbump(i, e - 1)
            pe *= p
            e += 1
    return count


if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    assert solve(10**4) == 7
    assert solve(10**8) == 656
    print(solve(10**18))  # 1170060
