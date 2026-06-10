import numba
import numpy as np

# Area/Perimeter = r/2 with r the inradius, so ratio k requires integer
# sides and r = 2k. Writing x = s-a, y = s-b, z = s-c, Heron gives
# x y z = r^2 (x + y + z); the half-integer branch is impossible for even r
# (parity), so x <= y <= z are positive integers. Multiplying through by x
# yields the key factorisation
#     (x y - r^2)(x z - r^2) = r^2 (x^2 + r^2),
# so for each k <= 1000 and each x <= sqrt(3) r, the solutions correspond
# to divisor pairs d1 <= d2 of N = r^2 (x^2 + r^2) with x | d1 + r^2 and
# x | d2 + r^2, giving y = (d1 + r^2)/x and z = (d2 + r^2)/x (y >= x
# checked). N factors cheaply: r is tiny and x^2 + r^2 <= 4 r^2 <= 1.6e7
# is handled by a smallest-prime-factor sieve; divisors are generated from
# the merged factorisation. The perimeter 2(x + y + z) is accumulated.
# Verified against direct (x, y) scanning for k <= 10.


@numba.njit(cache=True)
def _spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def _solve(kmax: int, spf: np.ndarray) -> int:
    total = 0
    primes = np.empty(20, dtype=np.int64)
    exps = np.empty(20, dtype=np.int64)
    divisors = np.empty(40000, dtype=np.int64)
    for k in range(1, kmax + 1):
        r = 2 * k
        r2 = r * r
        x = 1
        while x * x <= 3 * r2:
            q = x * x + r2
            n_val = r2 * q
            # factor r2 * q: factor r via spf (r <= 2000), exponents doubled,
            # then q via spf, merging
            np_cnt = 0
            t = r
            while t > 1:
                p = spf[t]
                e = 0
                while t % p == 0:
                    t //= p
                    e += 1
                primes[np_cnt] = p
                exps[np_cnt] = 2 * e
                np_cnt += 1
            t = q
            while t > 1:
                p = spf[t]
                e = 0
                while t % p == 0:
                    t //= p
                    e += 1
                found = False
                for i in range(np_cnt):
                    if primes[i] == p:
                        exps[i] += e
                        found = True
                        break
                if not found:
                    primes[np_cnt] = p
                    exps[np_cnt] = e
                    np_cnt += 1
            # generate divisors
            divisors[0] = 1
            nd = 1
            for i in range(np_cnt):
                p = primes[i]
                old = nd
                pw = 1
                for _e in range(exps[i]):
                    pw *= p
                    for j in range(old):
                        divisors[nd] = divisors[j] * pw
                        nd += 1
            for i in range(nd):
                d1 = divisors[i]
                if d1 * d1 <= n_val and (d1 + r2) % x == 0:
                    d2 = n_val // d1
                    if (d2 + r2) % x == 0:
                        y = (d1 + r2) // x
                        z = (d2 + r2) // x
                        if x <= y <= z:
                            total += 2 * (x + y + z)
            x += 1
    return total


def solve(kmax: int = 1000) -> int:
    spf = _spf_sieve(16_004_001)
    return int(_solve(kmax, spf))


if __name__ == "__main__":
    print(solve())  # 28038042525570324
