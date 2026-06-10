import numpy as np

# Alcuin's sequence T(p) counts integer triangles of perimeter p:
# round(p^2/48) for even p, round((p+3)^2/48) for odd p (verified against
# direct enumeration for p < 60). On each residue class p = 12k + r, T is
# the exact quadratic 3k^2 + A_r k + B_r, so the cumulative
# F(x) = sum_(p <= x) T(p) evaluates in O(12) with Faulhaber sums. Every
# triangle is a unique multiple of a primitive one, F(N) = sum_d P(N/d),
# so Mobius inversion gives P(N) = sum_d mu(d) F(floor(N/d)), evaluated by
# hyperbola blocks with Mertens prefix sums of a mobius sieve. Verified
# against brute-force primitive-triangle counting for N = 20, 50, 100.


def _alcuin(p: int) -> int:
    if p % 2 == 0:
        return round(p * p / 48)
    return round((p + 3) ** 2 / 48)


def _cumulative(x: int) -> int:
    total = 0
    for r in range(12):
        if r == 0:
            kmin, kmax = 1, x // 12
        else:
            kmin, kmax = 0, (x - r) // 12
        if kmax < kmin:
            continue
        t0 = _alcuin(12 * kmin + r)
        t1 = _alcuin(12 * (kmin + 1) + r)
        a = (t1 - t0) - 3 * (2 * kmin + 1)
        b = t0 - 3 * kmin * kmin - a * kmin

        def s1(n: int) -> int:
            return n * (n + 1) // 2

        def s2(n: int) -> int:
            return n * (n + 1) * (2 * n + 1) // 6

        total += (
            3 * (s2(kmax) - s2(kmin - 1))
            + a * (s1(kmax) - s1(kmin - 1))
            + b * (kmax - kmin + 1)
        )
    return total


def solve(n: int = 10**7) -> int:
    mu = np.ones(n + 1, dtype=np.int8)
    primes = np.ones(n + 1, dtype=bool)
    primes[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i * i :: i] = False
            mu[i::i] *= -1
            mu[i * i :: i * i] = 0
    for i in range(int(n**0.5) + 1, n + 1):
        if primes[i]:
            mu[i::i] *= -1
    mu[0] = 0
    mertens = np.cumsum(mu.astype(np.int64))
    total = 0
    d = 1
    while d <= n:
        v = n // d
        d2 = n // v
        total += int(mertens[d2] - mertens[d - 1]) * _cumulative(v)
        d = d2 + 1
    return total


if __name__ == "__main__":
    print(solve())  # 5777137137739632912
