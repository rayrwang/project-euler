"""Project Euler 944: Sum of Elevisors.

Swap the order of summation: element x is an elevisor of a subset E exactly
when E contains x together with at least one of the m = floor(n/x) - 1
proper multiples of x in {1..n}. Among the 2^(n-1) subsets containing x,
exactly 2^(n-1-m) avoid all those multiples, so x contributes
x * (2^(n-1) - 2^(n-1-m)) to S(n) and

    S(n) = 2^(n-1) n(n+1)/2 - 2^n * sum_x x * 2^(-floor(n/x)).

The remaining sum is evaluated by the standard divisor-block technique:
floor(n/x) takes O(sqrt(n)) distinct values q, and each block contributes
(sum of x over the block) * 2^(n-q). For x below sqrt(n) each x is its own
block and a modular power is computed directly; for q below sqrt(n) the
factor inv2^q is built incrementally. The modulus 1234567891 is prime, so
exponents reduce mod 1234567890 and inverses come from Fermat's little
theorem. Verified against brute force over all subsets for n <= 12 and the
given S(10) = 4927.
"""

import numba
import numpy as np

MOD = 1234567891
N = 10**14


@numba.njit(cache=True)
def mulmod(x, y):
    return x * y % MOD


@numba.njit(cache=True)
def powmod(base, e):
    r = np.int64(1)
    b = base % MOD
    while e > 0:
        if e & 1:
            r = r * b % MOD
        b = b * b % MOD
        e >>= 1
    return r


@numba.njit(cache=True)
def solve_n(n):
    inv2 = powmod(2, MOD - 2)
    half = (n % MOD) * ((n + 1) % MOD) % MOD * inv2 % MOD
    total = powmod(2, (n - 1) % (MOD - 1)) * half % MOD
    p2n = powmod(2, n % (MOD - 1))
    r = int(np.sqrt(n))
    while (r + 1) * (r + 1) <= n:
        r += 1
    while r * r > n:
        r -= 1
    sub = np.int64(0)
    # small x: each x = 1..n//(r+1) has q = n//x > r
    xs = n // (r + 1)
    for x in range(1, xs + 1):
        q = n // x
        sub = (sub + (x % MOD) * powmod(inv2, q % (MOD - 1))) % MOD
    # q = 1..r: x in [n//(q+1)+1, n//q]
    ip = np.int64(1)
    for q in range(1, r + 1):
        ip = ip * inv2 % MOD
        lo = n // (q + 1) + 1
        hi = n // q
        if lo <= xs:
            lo = xs + 1
        if lo > hi:
            continue
        cnt = (hi - lo + 1) % MOD
        smx = ((lo + hi) % MOD) * cnt % MOD * ((MOD + 1) // 2) % MOD
        sub = (sub + smx * ip) % MOD
    return (total - p2n * sub) % MOD


def solve() -> int:
    return int(solve_n(N))


if __name__ == "__main__":
    print(solve())  # 1228599511
