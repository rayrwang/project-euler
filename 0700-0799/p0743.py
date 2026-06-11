"""
Project Euler Problem 743: Window into a Matrix
https://projecteuler.net/problem=743

A(k, n) counts 2 x n binary matrices in which every 2 x k contiguous window
has entry-sum exactly k.  Given A(3, 9) = 560 and A(4, 20) = 1060870, find
A(10^8, 10^16) modulo 10^9 + 7.

Structure.  Sliding a 2 x k window one column to the right swaps one column
out for another of equal total, so the column sums c_i in {0, 1, 2} satisfy
c_{i+k} = c_i: they are periodic with period k, and one period sums to k.
Since k | n, each residue class holds exactly n/k columns.  A class whose sum
is 0 or 2 fixes both entries of every column in it; a class whose sum is 1
leaves an independent row choice in each of its n/k columns, a factor
g = 2^(n/k) per such class.  If j classes have sum 1 (so j ≡ k mod 2), the
other k - j classes split evenly into m = (k - j)/2 zero-classes and m
two-classes, giving

    A(k, n) = sum_{j ≡ k (mod 2)} k! / (j! m! m!) * g^j .

Evaluation.  Walk j downward from k (term g^k, all-ones classes).  Stepping
j -> j - 2 multiplies the term by j(j-1) and divides by (m+1)^2 g^2, so with a
table of modular inverses of 1..k/2+1 each step costs a few multiplications.
"""

import numpy as np
from numba import njit

MOD = 1_000_000_007


@njit(cache=True)
def modpow(a, e, p):
    r = 1
    a %= p
    while e > 0:
        if e & 1:
            r = r * a % p
        a = a * a % p
        e >>= 1
    return r


@njit(cache=True)
def inverse_table(nmax, p):
    inv = np.ones(nmax + 1, dtype=np.int64)
    for i in range(2, nmax + 1):
        inv[i] = (p - (p // i) * inv[p % i] % p) % p
    return inv


@njit(cache=True)
def a_of(k, n_over_k, p):
    """A(k, n) mod p, where n_over_k = n // k."""
    g = modpow(2, n_over_k, p)
    ginv = modpow(g, p - 2, p)
    ginv2 = ginv * ginv % p
    inv = inverse_table(k // 2 + 2, p)
    # start j = k (m = 0): term = g^k
    term = modpow(g, k, p)
    total = term
    j = k
    m = 0
    while j - 2 >= 0:
        # j -> j-2, m -> m+1
        term = term * (j % p) % p * ((j - 1) % p) % p
        term = term * inv[m + 1] % p * inv[m + 1] % p
        term = term * ginv2 % p
        j -= 2
        m += 1
        total = (total + term) % p
    return total


def main():
    assert a_of(3, 3, MOD) == 560  # A(3, 9)
    assert a_of(4, 5, MOD) == 1060870  # A(4, 20)
    return a_of(10**8, 10**16 // 10**8, MOD)


if __name__ == "__main__":
    print(main())  # 259158998
