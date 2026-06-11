"""Project Euler 967: Trivisible Numbers.

F(N, B) counts n <= N whose distinct prime factors p <= B sum to a multiple
of 3. Whether n qualifies depends only on its support S among the primes
<= B, so F = sum over supports S with sum(S) = 0 mod 3 of #{n <= N with
exact support S}. Writing the exact-support count by inclusion-exclusion
over supersets and collecting terms by the squarefree product m of the
primes involved gives

    F(N, B) = sum over squarefree B-smooth m <= N of floor(N/m) c(m),

where c(m) = sum over subsets S of the primes of m of (-1)^(omega(m)-|S|)
[sum S = 0 mod 3]. Detecting the congruence with cube roots of unity omega,
c(m) = (1/3) sum_j prod_(p|m) (omega^(jp) - 1); the j = 0 product vanishes
for m > 1, and p = 3 contributes a factor omega^j - ... = 0, so m divisible
by 3 drops out entirely. For 3-free m,

    c(m) = (2/3) Re[(omega - 1)^k1 (omega^2 - 1)^k2],

depending only on the counts k1, k2 of prime factors congruent to 1, 2
mod 3. Since (omega - 1) = (-3 + i sqrt(3))/2 this is an exact rational.

Computationally: a Numba DFS enumerates all squarefree products m <= 10^18
of the 29 primes p <= 120, p != 3 and accumulates sum of floor(N/m) into a
bucket per (k1, k2) (each bucket stays below 2^63), and the final exact
combination with the rational c(k1, k2) is done with Fractions. Verified
against brute force and the given F(10, 4) = 5, F(10, 10) = 3,
F(100, 10) = 41.
"""

from fractions import Fraction

import numpy as np
from numba import njit

N = 10**18
B = 120


def primes_upto(b: int) -> list[int]:
    return [p for p in range(2, b + 1) if all(p % d for d in range(2, p))]


@njit(cache=True)
def enumerate_products(primes: np.ndarray, residues: np.ndarray, n: int) -> np.ndarray:
    """buckets[k1, k2] = sum of floor(n/m) over squarefree products m <= n
    of the given primes with k1 factors = 1 mod 3 and k2 factors = 2 mod 3."""
    np_ = len(primes)
    buckets = np.zeros((np_ + 1, np_ + 1), dtype=np.int64)
    # explicit-stack DFS: (next index, current product, k1, k2)
    idx_st = np.empty(np_ + 2, dtype=np.int64)
    m_st = np.empty(np_ + 2, dtype=np.int64)
    k1_st = np.empty(np_ + 2, dtype=np.int64)
    k2_st = np.empty(np_ + 2, dtype=np.int64)
    idx_st[0], m_st[0], k1_st[0], k2_st[0] = 0, 1, 0, 0
    sp = 0
    while sp >= 0:
        i, m, k1, k2 = idx_st[sp], m_st[sp], k1_st[sp], k2_st[sp]
        if i >= np_ or m > n // primes[i]:
            sp -= 1
            continue
        idx_st[sp] = i + 1  # later: skip prime i entirely
        # take prime i now
        m2 = m * primes[i]
        a1 = k1 + (1 if residues[i] == 1 else 0)
        a2 = k2 + (1 if residues[i] == 2 else 0)
        buckets[a1, a2] += n // m2
        sp += 1
        idx_st[sp], m_st[sp], k1_st[sp], k2_st[sp] = i + 1, m2, a1, a2
    return buckets


def solve(n: int = N, b: int = B) -> int:
    ps = [p for p in primes_upto(b) if p != 3]
    primes = np.array(sorted(ps), dtype=np.int64)
    residues = primes % 3
    buckets = enumerate_products(primes, residues, n)

    total = Fraction(n)  # m = 1 term, c(1) = 1
    w1 = (Fraction(-3, 2), Fraction(1, 2))  # omega - 1   = x + y*i*sqrt(3)
    for k1 in range(len(primes) + 1):
        for k2 in range(len(primes) + 1):
            if k1 + k2 == 0 or buckets[k1, k2] == 0:
                continue
            x, y = Fraction(1), Fraction(0)
            for _ in range(k1):
                x, y = x * w1[0] - 3 * y * w1[1], x * w1[1] + y * w1[0]
            for _ in range(k2):  # omega^2 - 1 is the conjugate
                x, y = x * w1[0] + 3 * y * w1[1], -x * w1[1] + y * w1[0]
            total += int(buckets[k1, k2]) * Fraction(2, 3) * x
    assert total.denominator == 1
    return int(total)


if __name__ == "__main__":
    print(solve())  # 357591131712034236
