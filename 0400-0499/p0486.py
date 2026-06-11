"""Project Euler 486: Palindrome-containing Strings.

F5(n) counts binary strings of length at most n containing a palindromic
substring of length >= 5; D(L) counts 5 <= n <= L with F5(n) divisible by
M = 87654321 = 3^2 * 1997 * 4877. Find D(10^18).

A string contains a palindrome of length >= 5 iff it contains one of length
exactly 5 or 6 (long palindromes contain central ones two shorter), so the
avoiding strings form a regular language tracked by the last five bits. Their
count A(m) turns out to be eventually periodic: for m >= 7 it cycles through
(32, 32, 32, 34, 36, 34) with period 6 and period sum 200. Hence the
cumulative count G(n) is linear along each residue class mod 6, and
F5(n) = 2^(n+1) - 2 - G(n).

The divisibility condition splits by r = n mod O, where O = ord_M(2) =
lcm(6, 1996, 4876) = 7299372 fixes 2^(n+1) mod M. Within a class
n = j0 + 6t (j0 in 7..12, j0 = r mod 6), G(n) = G(j0) + 200 t, so the
condition is the linear congruence 200 t = 2^(r+1) - 2 - G(j0) (mod M), which
has a unique solution t* since gcd(200, M) = 1, pinning n modulo 6M. CRT with
n = r (mod O) (the moduli share exactly the factor 6, and the constraints
agree mod 6 by construction) gives exactly one solution class modulo
T = M * O = 639821496386412 per residue r. Counting members of each of the
O classes in [7, L] gives D(L); D(10^7) = 0 and D(5 * 10^9) = 51 check out.
"""

import math

import numpy as np
from numba import njit

M = 87654321
LIMIT = 10**18


def avoiding_counts(length):
    """A(m) for m = 1..length: binary strings with no palindrome of length >= 5."""
    counts = {(): 1}
    res = []
    for _ in range(length):
        new = {}
        for st, c in counts.items():
            for b in (0, 1):
                t = st + (b,)
                if len(t) >= 5 and t[-5:] == t[-5:][::-1]:
                    continue
                if len(t) >= 6 and t[-6:] == t[-6:][::-1]:
                    continue
                key = t[-5:]
                new[key] = new.get(key, 0) + c
        counts = new
        res.append(sum(counts.values()))
    return res


@njit(cache=True)
def count_divisible(limit, m, big_o, inv200, inv_m_o6, g_vals):
    o6 = big_o // 6
    t_mod = m * big_o
    total = np.int64(0)
    p = np.int64(2)  # 2^(r+1) mod m for r = 0
    for r in range(big_o):
        j0 = r % 6
        if j0 == 0:
            j0 = 12
        elif j0 < 7:
            j0 += 6
        t = (p - 2 - g_vals[j0 - 7]) % m * inv200 % m
        nstar = j0 + 6 * t
        delta = (r - nstar) % big_o
        k = (delta // 6) % o6 * inv_m_o6 % o6
        x = nstar + 6 * m * k
        if x <= limit:
            total += (limit - x) // t_mod + 1
        p = p * 2 % m
    return total


def solve(limit, a_series):
    g = np.cumsum(a_series)  # g[i] = G(i + 1)
    g_vals = np.array([g[j0 - 1] % M for j0 in range(7, 13)], dtype=np.int64)
    big_o = 1
    for q, phi in ((9, 6), (1997, 1996), (4877, 4876)):
        o = phi
        for f in (2, 3, 23, 53, 499):
            while o % f == 0 and pow(2, o // f, q) == 1:
                o //= f
        big_o = big_o * o // math.gcd(big_o, o)
    inv200 = pow(200, -1, M)
    inv_m_o6 = pow(M, -1, big_o // 6)
    return int(count_divisible(limit, M, big_o, inv200, inv_m_o6, g_vals))


if __name__ == "__main__":
    A = avoiding_counts(60)
    assert A[6:12] * 5 == A[6:36]  # period 6 from m = 7
    f5 = lambda n: 2 ** (n + 1) - 2 - sum(A[:n])  # noqa: E731
    assert [f5(n) for n in (4, 5, 6, 11)] == [0, 8, 42, 3844]
    assert solve(10**7, A) == 0
    assert solve(5 * 10**9, A) == 51
    print(solve(LIMIT, A))  # 11408450515
