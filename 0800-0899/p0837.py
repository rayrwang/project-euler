"""Project Euler 837: Amidakuji.

A three-line Amidakuji is a word in the adjacent transpositions
x = (1 2) and y = (2 3); a(m, n) counts words with m letters x and n
letters y whose product is the identity.  The coefficient of e in an
element z of the group algebra is (1/|G|) sum_rho d_rho Tr rho(z), so
with z = (s x + t y)^(m+n) the trivial and sign representations each
contribute (s+t)^(m+n) for even length, and in the two-dimensional
representation the reflections X, Y satisfy XY + YX = -I, whence
(sX + tY)^2 = (s^2 - st + t^2) I.  Therefore, with L = m + n even and
K = L/2,

  a(m,n) = (1/6) [ 2 binom(L, m) + 4 [s^m t^n](s^2 - st + t^2)^K ],

and the trinomial coefficient expands as
sum_j (-1)^j K! / (((m-j)/2)! j! ((n-j)/2)!) over j = m (mod 2).
The formula matches brute force for all m, n <= 7 and gives
a(3,3) = 2.

For the target both m and n are odd, so every j is odd and all signs
agree.  The modulus 1234567891 is prime and exceeds L, so factorials
need no Lucas treatment: one numba sweep to L = 1111111110 snapshots
the six factorials required, and the 6.2 * 10^7 terms are summed by
maintaining the running numerator product while multiplying each by a
precomputed suffix product of denominators, so a single modular
inversion finishes the job.  The given a(123, 321) = 172633303 is
reproduced en route.
"""

from __future__ import annotations

from itertools import combinations
from math import comb, factorial

import numpy as np
from numba import njit

MOD = 1234567891


@njit(cache=True)
def factorials_at(points: np.ndarray, mod: int) -> np.ndarray:
    out = np.empty(len(points), dtype=np.int64)
    f = 1
    idx = 0
    if points[0] == 0:
        out[0] = 1
        idx = 1
    n = 1
    while idx < len(points):
        f = f * n % mod
        if n == points[idx]:
            out[idx] = f
            idx += 1
        n += 1
    return out


@njit(cache=True)
def odd_term_sum(m: int, n: int, t_first: int, mod: int) -> int:
    """Sum of t_j over j = 1, 3, ..., min(m, n), where t_1 = t_first and
    t_{j+2} / t_j = ((m-j)/2)((n-j)/2) / ((j+1)(j+2))."""
    count = (min(m, n) - 1) // 2 + 1
    suffix = np.empty(count, dtype=np.int64)
    suffix[count - 1] = 1
    for i in range(count - 2, -1, -1):
        j = 1 + 2 * i
        v = ((j + 1) % mod) * ((j + 2) % mod) % mod
        suffix[i] = v * suffix[i + 1] % mod
    total = 0
    a = t_first
    for i in range(count):
        total = (total + a * suffix[i]) % mod
        if i < count - 1:
            j = 1 + 2 * i
            u = (((m - j) // 2) % mod) * (((n - j) // 2) % mod) % mod
            a = a * u % mod
    inv_all = 1
    base = suffix[0] % mod
    e = mod - 2
    while e:
        if e & 1:
            inv_all = inv_all * base % mod
        base = base * base % mod
        e >>= 1
    return total * inv_all % mod


def amidakuji(m: int, n: int) -> int:
    if (m + n) % 2 == 1:
        return 0
    assert m % 2 == 1 and n % 2 == 1
    length = m + n
    half = length // 2
    pts = np.array(
        sorted({(m - 1) // 2, (n - 1) // 2, m, n, half, length}), dtype=np.int64
    )
    facs = factorials_at(pts, MOD)
    fd = {int(p): int(f) for p, f in zip(pts, facs)}

    def inv(x: int) -> int:
        return pow(x, MOD - 2, MOD)

    binom = fd[length] * inv(fd[m]) % MOD * inv(fd[n]) % MOD
    t1 = fd[half] * inv(fd[(m - 1) // 2]) % MOD * inv(fd[(n - 1) // 2]) % MOD
    coeff = (-odd_term_sum(m, n, t1, MOD)) % MOD
    return (2 * binom + 4 * coeff) % MOD * inv(6) % MOD


def amidakuji_exact(m: int, n: int) -> int:
    if (m + n) % 2 == 1:
        return 0
    half = (m + n) // 2
    coeff = 0
    j = m % 2
    while j <= min(m, n):
        coeff += (
            (-1) ** j
            * factorial(half)
            // (factorial((m - j) // 2) * factorial(j) * factorial((n - j) // 2))
        )
        j += 2
    value = 2 * comb(m + n, m) + 4 * coeff
    assert value % 6 == 0
    return value // 6


def brute(m: int, n: int) -> int:
    length = m + n
    count = 0
    for pos in combinations(range(length), m):
        chosen = set(pos)
        perm = [0, 1, 2]
        for i in range(length):
            if i in chosen:
                perm[0], perm[1] = perm[1], perm[0]
            else:
                perm[1], perm[2] = perm[2], perm[1]
        if perm == [0, 1, 2]:
            count += 1
    return count


def main() -> None:
    for m in range(7):
        for n in range(7):
            assert amidakuji_exact(m, n) == brute(m, n)
    assert amidakuji_exact(3, 3) == 2
    assert amidakuji(123, 321) == 172633303
    print(amidakuji(123456789, 987654321))  # 428074856


if __name__ == "__main__":
    main()
