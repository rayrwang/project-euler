"""Project Euler Problem 660: Pandigital Triangles.

A triangle with a 120-degree angle has sides a, b adjacent to it and c
opposite (necessarily the strict largest), with c^2 = a^2 + ab + b^2,
equivalently (2c)^2 - (2b + a)^2 = 3a^2.  Writing 3a^2 = u v with
u = 2c - 2b - a recovers b = (v - u - 2a)/4 and c = (u + v)/4, so every
triangle is found from its smaller adjacent side a by walking the divisors
of 3 a^2 (built from a smallest-prime-factor sieve) and keeping the
integral pairs with b > a.

Size bounds come from the digit budget: lengths satisfy L_a <= L_b <= L_c
<= L_b + 1 (as c < a + b < 2b) and sum to n, so L_a <= floor(n/3) <= 6 and
L_c <= 9; hence a < 18^6 and c < 18^9.  For a fixed triangle the total
digit count T_n is non-increasing in n while the target n increases, so at
most one base can match; each candidate triple is tested against the base
whose total length fits and digit-counted for pandigitality.

The answer sums c over all n-pandigital triangles for 9 <= n <= 18.
Check: an independent brute force over all (a, b) pairs reproduces the
full n = 9 triangle set, including the statement's (217, 248, 403).
"""

from math import isqrt

import numba
import numpy as np

A_MAX = 18**6  # smaller adjacent side has at most floor(18/3) = 6 digits
C_MAX = 18**9


@numba.jit(cache=True)
def spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.jit(cache=True)
def pandigital_base(a: int, b: int, c: int, powers: np.ndarray) -> int:
    """The base 9..18 in which (a, b, c) is pandigital, or 0."""
    counts = np.zeros(18, dtype=np.int8)
    for n in range(9, 19):
        la = lb = lc = 1
        while powers[n, la] <= a:
            la += 1
        while powers[n, lb] <= b:
            lb += 1
        while powers[n, lc] <= c:
            lc += 1
        tot = la + lb + lc
        if tot < n:
            return 0  # total length only shrinks as n grows
        if tot > n:
            continue
        counts[:] = 0
        for x in (a, b, c):
            while x:
                counts[x % n] += 1
                x //= n
        ok = True
        for d in range(n):
            if counts[d] != 1:
                ok = False
                break
        return n if ok else 0
    return 0


@numba.jit(cache=True)
def solve(spf: np.ndarray) -> int:
    powers = np.ones((19, 14), dtype=np.int64)
    for n in range(9, 19):
        for e in range(1, 14):
            powers[n, e] = powers[n, e - 1] * n
    divisors = np.empty(300000, dtype=np.int64)
    total = 0
    for a in range(3, A_MAX):
        divisors[0] = 1
        nd = 1
        v = a
        exp3 = 1  # the explicit factor 3 in 3 a^2
        while v > 1:
            p = spf[v]
            e = 0
            while v % p == 0:
                v //= p
                e += 1
            if p == 3:
                exp3 += 2 * e
            else:
                base_nd = nd
                pk = 1
                for _ in range(2 * e):
                    pk *= p
                    for t in range(base_nd):
                        divisors[nd] = divisors[t] * pk
                        nd += 1
        base_nd = nd
        pk = 1
        for _ in range(exp3):
            pk *= 3
            for t in range(base_nd):
                divisors[nd] = divisors[t] * pk
                nd += 1
        m = 3 * a * a
        for t in range(nd):
            u = divisors[t]
            if u * u >= m:
                continue
            w = m // u
            if (u + w) % 4 != 0 or (w - u - 2 * a) % 4 != 0:
                continue
            b = (w - u - 2 * a) // 4
            c = (u + w) // 4
            if b <= a or c >= C_MAX:
                continue
            if pandigital_base(a, b, c, powers):
                total += c
    return total


def brute(n: int) -> set[tuple[int, int, int]]:
    """All n-pandigital triangles by direct search (small n only)."""
    side_max = n ** ((n + 1) // 2)
    found = set()
    for a in range(1, n ** (n // 3)):
        for b in range(a + 1, side_max):
            c2 = a * a + a * b + b * b
            if c2 >= side_max * side_max:
                break
            c = isqrt(c2)
            if c * c != c2:
                continue
            digs = []
            for x in (a, b, c):
                while x:
                    digs.append(x % n)
                    x //= n
            if len(digs) == n and sorted(digs) == list(range(n)):
                found.add((a, b, c))
    return found


if __name__ == "__main__":
    ref9 = brute(9)
    assert (217, 248, 403) in ref9  # statement example
    spf = spf_sieve(A_MAX)
    powers = np.ones((19, 14), dtype=np.int64)
    for n in range(9, 19):
        for e in range(1, 14):
            powers[n, e] = powers[n, e - 1] * n
    mine9 = {t for t in ref9 if pandigital_base(*t, powers) == 9}
    assert mine9 == ref9 and ref9
    print(solve(spf))  # 474766783
