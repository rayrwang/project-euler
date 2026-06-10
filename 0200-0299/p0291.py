import numba
import numpy as np

# Reducing p = (x^4 - y^4)/(x^3 + y^3) = (x - y)(x^2 + y^2)/(x^2 - xy + y^2)
# with x = ga, y = gb, gcd(a, b) = 1: the denominator a^2 - ab + b^2 is
# coprime to both (a - b) and a^2 + b^2, so it must divide g, leaving
# p = t (a - b)(a^2 + b^2). Primality forces t = 1 and a = b + 1, i.e.
#     p = n^2 + (n + 1)^2 = 2n^2 + 2n + 1,
# and conversely every such prime is attained (g = n^2 + n + 1). The
# characterisation was cross-checked against a direct (x, y) search.
#
# Counting primes 2n^2 + 2n + 1 < 5e15: the value is ((2n+1)^2 + 1)/2, so
# every prime factor is 2 or = 1 (mod 4) - and it is odd, so all factors
# are 1 mod 4. Sieving the n-array by the roots of 2n^2 + 2n + 1 = 0
# (mod q), i.e. 2n + 1 = +-sqrt(-1) (mod q), for ALL primes
# q = 1 (mod 4) up to sqrt(5e15) < 7.1e7 therefore removes every composite
# exactly, with no primality testing needed afterwards. sqrt(-1) mod q is
# r^((q-1)/4) for a quadratic non-residue r, and q^2 fits in 64 bits.


@numba.njit(cache=True)
def _mod_pow(a: int, e: int, m: int) -> int:
    r = 1
    a %= m
    while e:
        if e & 1:
            r = r * a % m
        a = a * a % m
        e >>= 1
    return r


@numba.njit(cache=True)
def _count(limit: int) -> int:
    # n max: 2n^2 + 2n + 1 < limit
    nmax = int(((2 * limit - 1) ** 0.5 - 1) / 2)
    while 2 * (nmax + 1) ** 2 + 2 * (nmax + 1) + 1 < limit:
        nmax += 1
    while 2 * nmax * nmax + 2 * nmax + 1 >= limit:
        nmax -= 1
    qmax = 1
    while (qmax + 1) * (qmax + 1) < limit:
        qmax += 1
    sieve = np.ones(qmax + 1, dtype=np.bool_)
    sieve[:2] = False
    for i in range(2, int(qmax**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    good = np.ones(nmax + 1, dtype=np.bool_)
    good[0] = False
    inv2 = 0
    for q in range(5, qmax + 1, 4):
        if not sieve[q]:
            continue
        # sqrt(-1) mod q via a non-residue
        s = 0
        for r in range(2, q):
            t = _mod_pow(r, (q - 1) // 2, q)
            if t == q - 1:
                s = _mod_pow(r, (q - 1) // 4, q)
                break
        inv2 = (q + 1) // 2
        for sign in range(2):
            root = s if sign == 0 else q - s
            n0 = (root - 1) % q * inv2 % q
            n = n0
            while n <= nmax:
                if n > 0:
                    if n < 6000 and 2 * n * n + 2 * n + 1 == q:
                        pass
                    else:
                        good[n] = False
                n += q
    count = 0
    for n in range(1, nmax + 1):
        if good[n]:
            count += 1
    return count


def solve(limit: int = 5 * 10**15) -> int:
    return int(_count(limit))


if __name__ == "__main__":
    print(solve())  # 4037526
