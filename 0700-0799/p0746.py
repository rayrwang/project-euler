"""
Project Euler Problem 746: A Messy Dinner
https://projecteuler.net/problem=746

n four-person families sit at a circular table of 4n labeled seats with men
and women alternating.  M(n) counts the seatings in which no family occupies
four consecutive seats; find S(2021) = sum_{k=2}^{2021} M(k) modulo 10^9 + 7.

Inclusion-exclusion over which families are forced into a consecutive block.
Forcing j families to sit as blocks: j disjoint blocks of 4 consecutive seats
fit on a 4k-cycle in (4k)/(4k-3j) * C(4k-3j, j) ways; the j families fill the
blocks in k!/(k-j)! orders with 2! * 2! = 4 internal arrangements each
(father/son in the block's two male seats, mother/daughter in the two female
seats); the remaining 2k-2j men and 2k-2j women fill their seat classes in
((2k-2j)!)^2 ways; and a global factor 2 chooses which parity class holds the
men.  Therefore

    M(k) = 2 sum_{j=0}^{k} (-1)^j C(k,j) j! (4k)/(4k-3j) C(4k-3j, j)
                 4^j ((2k-2j)!)^2 .

(C(k, j) j! = k!/(k-j)!.)  The check value M(3) = 890880 confirms the
arithmetic; summing M(k) over k <= 2021 is a double loop with precomputed
factorials.
"""

import numba as nb
import numpy as np

MOD = 1_000_000_007
NMAX = 2021


@nb.njit(cache=True)
def _powmod(a, e, m):
    r = 1
    a %= m
    while e > 0:
        if e & 1:
            r = r * a % m
        a = a * a % m
        e >>= 1
    return r


@nb.njit(cache=True)
def main():
    lim = 4 * NMAX + 10
    fact = np.ones(lim + 1, dtype=np.int64)
    for i in range(1, lim + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = np.ones(lim + 1, dtype=np.int64)
    inv_fact[lim] = _powmod(fact[lim], MOD - 2, MOD)
    for i in range(lim, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def comb(a, b):
        if b < 0 or b > a:
            return 0
        return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

    def m_of(k):
        total = 0
        for j in range(k + 1):
            d = 4 * k - 3 * j  # number of "super-seats" on the reduced cycle
            if d <= 0:
                # block count (4k)/(4k-3j) C(4k-3j, j): for d == 0 the whole table is
                # j blocks, possible only when j == k and 4k == 3j is impossible for k>0,
                # so this branch does not contribute for the valid range.
                continue
            # cyclic count of j non-overlapping blocks of length 4 on a 4k-cycle:
            # (4k)/(4k-3j) * C(4k-3j, j)
            block = (4 * k) % MOD * _powmod(d % MOD, MOD - 2, MOD) % MOD * comb(d, j) % MOD
            term = (
                fact[k] * inv_fact[k - j] % MOD  # k!/(k-j)! = C(k,j) j!
                * block % MOD
                * _powmod(4, j, MOD) % MOD
                * (fact[2 * k - 2 * j] ** 2 % MOD) % MOD
            )
            if j & 1:
                total = (total - term) % MOD
            else:
                total = (total + term) % MOD
        return 2 * total % MOD

    assert m_of(3) == 890880
    total = 0
    for k in range(2, NMAX + 1):
        total = (total + m_of(k)) % MOD
    return total


if __name__ == "__main__":
    print(main())  # 867150922
