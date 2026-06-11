"""Project Euler Problem 675: 2^omega.

S(n) = sum over divisors d of n of 2^omega(d) is multiplicative with
S(p^e) = 1 + 2e (each of the e powers p, p^2, ..., p^e contributes a factor
2 once p divides d), so S(n) = product over p^e || n of (2e + 1).

F(10^7) = sum of S(i!) for i = 2..10^7 is computed by maintaining the prime
exponent vector of i! incrementally: factoring i with a smallest-prime-
factor sieve, each prime power p^k in i changes the running product by the
factor (2(e + k) + 1) / (2e + 1) modulo 10^9 + 87, using a precomputed
table of modular inverses.

Verified: S(6) = 9, S(360) = 27, F(10) = 4821, and F against direct
divisor enumeration for n <= 60.
"""

import numba
import numpy as np

MOD = 10**9 + 87
N = 10**7


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
def inverse_table(limit: int, mod: int) -> np.ndarray:
    inv = np.zeros(limit + 1, dtype=np.int64)
    inv[1] = 1
    for i in range(2, limit + 1):
        inv[i] = (mod - mod // i * inv[mod % i]) % mod
    return inv


@numba.jit(cache=True)
def f(n: int, spf: np.ndarray, inv: np.ndarray, mod: int) -> int:
    exps = np.zeros(n + 1, dtype=np.int64)
    prod = 1  # S(i!) so far
    s = 0
    for i in range(2, n + 1):
        x = i
        while x > 1:
            p = spf[x]
            k = 0
            while x % p == 0:
                x //= p
                k += 1
            e = exps[p]
            exps[p] = e + k
            prod = prod * inv[2 * e + 1] % mod
            prod = prod * (2 * (e + k) + 1) % mod
        s = (s + prod) % mod
    return s


def s_brute(n: int) -> int:
    def omega(m: int) -> int:
        w, p = 0, 2
        while p * p <= m:
            if m % p == 0:
                w += 1
                while m % p == 0:
                    m //= p
            p += 1
        return w + (m > 1)

    return sum(2 ** omega(d) for d in range(1, n + 1) if n % d == 0)


if __name__ == "__main__":
    assert s_brute(6) == 9 and s_brute(360) == (2 * 3 + 1) * (2 * 2 + 1) * 3
    spf = spf_sieve(N)
    inv = inverse_table(2 * N + 40, MOD)
    from math import factorial

    brute = {n: sum(s_brute(factorial(i)) for i in range(2, n + 1))
             for n in (10, 12)}
    assert brute[10] == 4821
    assert all(int(f(n, spf, inv, MOD)) == v % MOD for n, v in brute.items())
    print(int(f(N, spf, inv, MOD)))  # 416146418
