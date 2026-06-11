from array import array
from math import isqrt

import numpy as np


def _smallest_prime_factors(limit: int) -> array:
    spf = np.arange(limit + 1, dtype=np.int64)
    for i in range(2, isqrt(limit) + 1):
        if spf[i] == i:
            seg = spf[i * i :: i]
            idx = np.arange(i * i, limit + 1, i, dtype=np.int64)
            seg[seg == idx] = i
            spf[i * i :: i] = seg
    return array("q", spf.tolist())


def h(r: int) -> int:
    """Sum of the positive z-coordinates over all lattice points on the sphere
    of radius r:  h(r) = sum_{z=1}^{r} z * r2(r^2 - z^2), where r2(m) counts the
    ordered signed representations m = x^2 + y^2.

    Each r^2 - z^2 = (r - z)(r + z) is factored through a smallest-prime-factor
    sieve, and r2(m) = 4 * prod_{p=1 (4)}(e_p + 1) when every prime = 3 (mod 4)
    occurs to an even power, else 0 (the power of 2 is irrelevant).
    """
    spf = _smallest_prime_factors(2 * r)
    total = 0
    for z in range(1, r):
        acc: dict[int, int] = {}
        for n in (r - z, r + z):
            while n > 1:
                p = spf[n]
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                acc[p] = acc.get(p, 0) + e
        cnt = 4
        ok = True
        for p, e in acc.items():
            pm = p & 3
            if pm == 1:
                cnt *= e + 1
            elif pm == 3 and (e & 1):
                ok = False
                break
        if ok:
            total += z * cnt
    return total + r  # z = r gives r2(0) = 1


def scary_sphere(a: int, b: int) -> int:
    """S(2^a * 5^b) = sum over lattice points on the sphere of |x| + |y| + |z|.

    By symmetry S(r) = 3 * sum|z| = 6 * h(r), and h is multiplicative, so
    h(2^a * 5^b) = h(2^a) * h(5^b); only h(5^b) is non-trivial to evaluate.
    """
    return 6 * h(2**a) * h(5**b)


if __name__ == "__main__":
    assert 6 * h(45) == 34518  # S(45), validates S = 6h directly
    assert 6 * h(4) * h(25) == 23064  # S(100), validates multiplicativity
    print(scary_sphere(10, 10))  # 878825614395267072
