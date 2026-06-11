"""Project Euler Problem 678: Fermat-like Equations.

Count (a, b, c, e, f) with 0 < a < b, e >= 2, f >= 3, a^e + b^e = c^f <= N
for N = 10^18.

Targets: enumerate all pairs (c, f) with c >= 2, f >= 3, c^f <= N (about
10^6, dominated by cubes) and record the multiplicity w(m) = #(c, f) of
each distinct value m.  Then the answer is sum over e of
sum_m w(m) R_e(m), with R_e(m) the number of 0 < a < b with a^e + b^e = m.

e = 2: factor m (= a known c to a known power f, and c <= 10^6 factors by
sieve) and apply the sum-of-two-squares count: with B the product of
(e_p + 1) over primes p = 1 mod 4, and zero if any p = 3 mod 4 has odd
exponent, the number of 0 < a < b is (B - [m square] - [m/2 square]) / 2.

e = 3: by Fermat's Last Theorem a^3 + b^3 is never a perfect cube, so only
the ~4 * 10^4 distinct m that are NOT cubes (f = 4, 5, 7, ... powers) can
occur.  For those, a^3 + b^3 = s q with s = a + b, q = s^2 - 3ab, which
forces the divisor s of m into the window m^(1/3) < s <= (4m)^(1/3); each
divisor s there yields at most one (a, b), recovered from ab = (s^2 - q)/3
and the discriminant.

e >= 4: a^e + b^e <= N forces b <= N^(1/e) <= 31623, so all pairs (about
5 * 10^8, almost all from e = 4) are enumerated directly in numba, binary
searching each sum in the sorted list of distinct perfect powers.

Verified: F(10^3) = 7, F(10^5) = 53, F(10^7) = 287, plus full agreement
with an independent brute force for N <= 10^5.
"""

from math import isqrt

import numba
import numpy as np

N = 10**18


def kth_root(n: int, k: int) -> int:
    """Floor of the k-th root."""
    r = round(n ** (1 / k))
    while r**k > n:
        r -= 1
    while (r + 1) ** k <= n:
        r += 1
    return r


def perfect_powers(n: int) -> dict[int, list[tuple[int, int]]]:
    """m -> list of (c, f) with c^f = m, c >= 2, f >= 3, m <= n."""
    powers: dict[int, list[tuple[int, int]]] = {}
    f = 3
    while 2**f <= n:
        for c in range(2, kth_root(n, f) + 1):
            powers.setdefault(c**f, []).append((c, f))
        f += 1
    return powers


def spf_sieve(n: int) -> list[int]:
    spf = list(range(n + 1))
    for i in range(2, isqrt(n) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor(c: int, spf: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    while c > 1:
        p = spf[c]
        while c % p == 0:
            c //= p
            out[p] = out.get(p, 0) + 1
    return out


def r2(m: int, fac: dict[int, int]) -> int:
    """#{(a, b): 0 < a < b, a^2 + b^2 = m}."""
    b = 1
    for p, e in fac.items():
        if p % 4 == 3:
            if e % 2:
                return 0
        elif p % 4 == 1:
            b *= e + 1
    is_sq = isqrt(m) ** 2 == m
    is_2sq = m % 2 == 0 and isqrt(m // 2) ** 2 == m // 2
    return (b - is_sq - is_2sq) // 2


def r3(m: int, fac: dict[int, int]) -> int:
    """#{(a, b): 0 < a < b, a^3 + b^3 = m}, via divisors s = a + b."""
    divisors = [1]
    for p, e in fac.items():
        divisors = [d * p**k for d in divisors for k in range(e + 1)]
    lo, hi = kth_root(m, 3), kth_root(4 * m, 3)
    count = 0
    for s in divisors:
        if lo < s <= hi:
            q = m // s  # = s^2 - 3ab
            if (s * s - q) % 3:
                continue
            ab = (s * s - q) // 3
            disc = s * s - 4 * ab  # = (b - a)^2
            if disc <= 0:
                continue
            root = isqrt(disc)
            if root * root == disc and (s - root) % 2 == 0 and s > root:
                count += 1
    return count


@numba.jit(cache=True)
def pow_capped(base: int, exp: int, cap: int) -> int:
    """base^exp, or cap + 1 as soon as it exceeds cap (no overflow)."""
    r = 1
    for _ in range(exp):
        r *= base
        if r > cap:
            return cap + 1
    return r


@numba.jit(cache=True)
def high_e_count(n: int, values: np.ndarray, mult: np.ndarray) -> int:
    """Tuples with e >= 4: enumerate a < b, binary search a^e + b^e."""
    total = 0
    for e in range(4, 64):
        if pow_capped(2, e, n) + 1 > n:
            break
        b = 2
        while True:
            be = pow_capped(b, e, n)
            if be >= n:
                break
            for a in range(1, b):
                m = a**e + be
                if m > n:
                    break
                lo, hi = 0, len(values)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if values[mid] < m:
                        lo = mid + 1
                    else:
                        hi = mid
                if lo < len(values) and values[lo] == m:
                    total += mult[lo]
            b += 1
    return total


def f(n: int) -> int:
    powers = perfect_powers(n)
    spf = spf_sieve(kth_root(n, 3) + 1)

    total = 0
    for m, reps in powers.items():
        c, fexp = reps[-1]  # largest f = smallest c, cheapest to factor
        fac = {p: e * fexp for p, e in factor(c, spf).items()}
        w = len(reps)
        total += w * r2(m, fac)
        if kth_root(m, 3) ** 3 != m:  # FLT: cubes are never a^3 + b^3
            total += w * r3(m, fac)

    values = np.array(sorted(powers), dtype=np.int64)
    mult = np.array([len(powers[int(v)]) for v in values], dtype=np.int64)
    return total + int(high_e_count(n, values, mult))


def f_brute(n: int) -> int:
    powers = perfect_powers(n)
    count = 0
    for m, reps in powers.items():
        e = 2
        while 1 + 2**e <= m:
            for a in range(1, n):
                ae = a**e
                if 2 * ae >= m:
                    break
                rest = m - ae
                b = kth_root(rest, e)
                if b**e == rest:
                    count += len(reps)
            e += 1
    return count


if __name__ == "__main__":
    assert f(10**3) == f_brute(10**3) == 7
    assert f(10**4) == f_brute(10**4)
    assert f(10**5) == f_brute(10**5) == 53
    assert f(10**7) == 287
    print(f(N))  # 1986065
