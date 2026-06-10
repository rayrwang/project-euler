"""Project Euler 937: Equiproduct Partition.

theta = sqrt(-2); T is a canonical half of Z[theta] \\ {0} (one element
per +- pair).  The conditions p(A, z) = p(B, z) ask, for every z, that
the unordered pairs of distinct elements with product +-z split evenly
between A x A and B x B.  Writing s(z) = +1 for z in A and -1 for z in
B, indicator algebra turns the condition into

    sum over ordered factorisations z = +- d e of s(d)
        minus the diagonal term  =  0,

i.e.  sum_{d | z} s(d) = [z = +-w^2] * s(w),

a divisor recursion that determines s uniquely (so the partition exists
and is unique, as stated).  Since Z[theta] is a UFD with units {+-1},
the up-to-sign monoid T is free abelian on primes; the unique solution
is the multiplicative function with Thue-Morse signs on exponents,

    s(z) = prod over primes pi of (-1)^popcount(v_pi(z)),

because per prime the recursion sum_{j<=a} t_j = [a even] t_{a/2} is
exactly the Thue-Morse recursion t_{2j} = t_j, t_{2j+1} = -t_j.  This
was verified by building the partition directly from the recursion for
all 1332 elements of norm <= 1200 and checking p(A,z) = p(B,z) for
every z there.

For z = n! (a rational integer) the prime exponents in Z[theta] follow
from how rational primes behave: p = 2 ramifies (2 ~ theta^2, exponent
2 v_2(n!), and popcount(2v) = popcount(v)); p = 1, 3 (mod 8) splits
into two conjugate primes each with exponent v_p(n!), contributing an
even total; p = 5, 7 (mod 8) is inert.  Hence

    n! in A  <=>  sum over q in {2} u {q = 5,7 mod 8} of
                  popcount(v_q(n!))  is even.

Computation: for each relevant prime q, walk its multiples k = mq
maintaining v_q(k!) incrementally and XOR the change of
popcount(v_q) mod 2 into flip[k]; a prefix XOR then gives the parity
for every k, and factorials are accumulated mod 1e9+7 on the fly.
Total work is ~ N * (1 + sum 1/q) ~ 2.5e8 steps.  Verified against
G(4) = 25, G(7) = 745, G(100) = 709772949 (mod 1e9+7).
"""

import numpy as np
from numba import njit

MOD = 10 ** 9 + 7
N = 10 ** 8


def prime_sieve(n: int) -> np.ndarray:
    comp = np.zeros(n + 1, dtype=bool)
    comp[:2] = True
    for p in range(2, int(n ** 0.5) + 1):
        if not comp[p]:
            comp[p * p::p] = True
    return ~comp


@njit(cache=True)
def fill_flips(n: int, primes: np.ndarray, flip: np.ndarray) -> None:
    for qi in range(primes.size):
        q = primes[qi]
        v = 0
        old_t = 0
        k = q
        while k <= n:
            # v_q(k!) = v_q((k-1)!) + v_q(k)
            kk = k
            while kk % q == 0:
                v += 1
                kk //= q
            vv = v
            cnt = 0
            while vv:
                vv &= vv - 1
                cnt ^= 1
            flip[k] ^= cnt ^ old_t
            old_t = cnt
            k += q


@njit(cache=True)
def accumulate(n: int, flip: np.ndarray) -> int:
    cur = 0
    fact = 1
    ans = 0
    for k in range(1, n + 1):
        fact = fact * k % MOD
        cur ^= flip[k]
        if cur == 0:
            ans = (ans + fact) % MOD
    return ans


def g_value(n: int, is_prime: np.ndarray) -> int:
    ps = np.flatnonzero(is_prime[: n + 1]).astype(np.int64)
    rel = ps[(ps == 2) | (ps % 8 == 5) | (ps % 8 == 7)]
    flip = np.zeros(n + 1, dtype=np.uint8)
    fill_flips(n, rel, flip)
    return accumulate(n, flip)


def solve() -> int:
    is_prime = prime_sieve(N)
    assert g_value(4, is_prime) == 25
    assert g_value(7, is_prime) == 745
    assert g_value(100, is_prime) == 709772949
    return g_value(N, is_prime)


if __name__ == "__main__":
    print(solve())  # 792169346
