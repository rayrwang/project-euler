"""Project Euler Problem 632: Square Prime Factors.

C_k(N) counts the n <= N with exactly k square prime factors (primes p with
p^2 | n).  Let

    A_j(N) = sum over squarefree m with omega(m) = j of floor(N / m^2).

A number whose square-prime-factor set has size t is counted C(t, j) times
in A_j (once per j-subset m of that set), so A_j = sum_t C(t, j) C_t, and
the binomial transform inverts to

    C_k(N) = sum_{j >= k} (-1)^(j - k) C(j, k) A_j(N).

For N = 10^16 only m <= 10^8 matter, and the product of the first 9 primes
already exceeds 10^8, so j <= 8 (and likewise C_k = 0 for k > 8 since the
square of the first 9 primes' product exceeds 10^16).  A numba sieve up to
10^8 marks non-squarefree numbers and counts distinct prime factors, then a
single pass accumulates the A_j; everything fits in 64 bits since
sum floor(N / m^2) < N pi^2 / 6.  The answer is the product of the non-zero
C_k modulo 10^9 + 7.

Verified against every entry of the problem's table for N = 10, 10^2, ...,
10^8, and against direct factorisation for N <= 10^4.
"""

import numba
import numpy as np

MOD = 10**9 + 7


@numba.jit(cache=True)
def omega_squarefree_sieve(n: int) -> tuple:
    """Distinct-prime-factor counts and squarefree flags for 1..n."""
    omega = np.zeros(n + 1, dtype=np.int8)
    squarefree = np.ones(n + 1, dtype=np.bool_)
    for p in range(2, n + 1):
        if omega[p] == 0:  # p is prime
            for i in range(p, n + 1, p):
                omega[i] += 1
            for i in range(p * p, n + 1, p * p):
                squarefree[i] = False
    return omega, squarefree


@numba.jit(cache=True)
def a_sums(n: int, omega: np.ndarray, squarefree: np.ndarray) -> np.ndarray:
    a = np.zeros(10, dtype=np.int64)
    a[0] = n
    m = 2
    while m * m <= n:
        if squarefree[m]:
            a[omega[m]] += n // (m * m)
        m += 1
    return a


def counts(n: int, omega: np.ndarray, squarefree: np.ndarray) -> list[int]:
    """C_k(n) for k = 0..9, exact."""
    from math import comb

    a = a_sums(n, omega, squarefree)
    return [
        sum((-1) ** (j - k) * comb(j, k) * int(a[j]) for j in range(k, 10))
        for k in range(10)
    ]


def counts_brute(n: int) -> list[int]:
    c = [0] * 10
    for m in range(1, n + 1):
        k, x, p = 0, m, 2
        while p * p <= x:
            if x % p == 0:
                e = 0
                while x % p == 0:
                    x //= p
                    e += 1
                k += e >= 2
            p += 1
        c[k] += 1
    return c


if __name__ == "__main__":
    table = {
        10: [7, 3, 0, 0, 0, 0],
        10**2: [61, 36, 3, 0, 0, 0],
        10**3: [608, 343, 48, 1, 0, 0],
        10**4: [6083, 3363, 533, 21, 0, 0],
        10**5: [60794, 33562, 5345, 297, 2, 0],
        10**6: [607926, 335438, 53358, 3218, 60, 0],
        10**7: [6079291, 3353956, 533140, 32777, 834, 2],
        10**8: [60792694, 33539196, 5329747, 329028, 9257, 78],
    }
    omega, squarefree = omega_squarefree_sieve(10**8)
    for n, row in table.items():
        assert counts(n, omega, squarefree)[:6] == row
    assert counts(10**4, omega, squarefree) == counts_brute(10**4)

    answer = 1
    for c in counts(10**16, omega, squarefree):
        if c:
            answer = answer * (c % MOD) % MOD
    print(answer)  # 728378714
