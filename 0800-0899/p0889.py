import random
from fractions import Fraction
from math import comb

# With x = a/M for M = 2^k + 1 and a = (2^t+1)^r mod M, doubling mod M has
# period dividing 2k (2^k = -1 mod M), so the blancmange series becomes the
# finite F = sum_(n<2k) 2^(2k-n) c_n / M with c_n = min(b_n, M - b_n) and
# b_n = 2^n a mod M.  Since b_(n+k) = M - b_n, the halves pair up and M
# cancels:  F = sum_(n<k) 2^(k-n) c_n  — manifestly an integer.
#
# Writing b_n = 2^n a - M D_n, where D_n is the n-digit prefix of the
# repeating binary block, and noting that the first k digits of that block
# are exactly the bits of A = a - 1 (the block is bin(a-1) ++ bin(2^k - a)),
# everything collapses to sums over the set bits of A:
#     F = a 2^k T1 - M (A T1 - U) + 2 M A,    T1 = k - 2 popcount(A),
#     U = sum_m (1 - 2 bit_(m-1)(A)) (A mod 2^m)
#       = sum_(p in bits(A)) 2^p (k - p)  -  2 (A + sum_(p in bits(A)) A mod 2^p).
# For the target parameters rt < k, so a = (2^t+1)^r needs no reduction and
# its bits are 63 binomial-coefficient blocks at offsets t i — about 1500
# set bits in total, each handled in O(log) time.

MOD = 1000062031


def f_series(k: int, t: int, r: int, terms: int = 120) -> int:
    """(2^2k - 1) T(x) straight from the definition, with a tail bound."""
    x = Fraction((2**t + 1) ** r, 2**k + 1)
    total = Fraction(0)
    for n in range(terms):
        y = (2**n * x) % 1
        total += min(y, 1 - y) / 2**n
    val = (2 ** (2 * k) - 1) * total
    assert (2 ** (2 * k) - 1) * Fraction(1, 2**terms) < Fraction(1, 4)
    nearest = round(val)
    assert abs(val - nearest) < Fraction(1, 4)
    return int(nearest)


def f_orbit(k: int, t: int, r: int) -> int:
    """F = sum_(n<k) 2^(k-n) min(b_n, M - b_n), exact integers."""
    big_m = (1 << k) + 1
    b = pow(2**t + 1, r, big_m)
    total = 0
    for n in range(k):
        total += (1 << (k - n)) * min(b, big_m - b)
        b = 2 * b % big_m
    return total


def f_sparse(k: int, t: int, r: int, mod: int) -> int:
    """Closed form over the set bits of A = (2^t+1)^r - 1; needs rt < k."""
    coeffs = [comb(r, i) for i in range(r + 1)]
    assert all(c.bit_length() <= t for c in coeffs[1:]) and r * t < k
    a_mod = sum(c * pow(2, t * i, mod) for i, c in enumerate(coeffs)) % mod
    big_a = (a_mod - 1) % mod
    pop = sum(c.bit_count() for c in coeffs[1:])
    t1 = (k - 2 * pop) % mod
    s1 = 0  # sum over set bits p of 2^p (k - p)
    s2 = 0  # sum over set bits p of (A mod 2^p)
    prefix = 0  # full blocks below the current one
    for i in range(1, r + 1):
        c = coeffs[i]
        base = pow(2, t * i, mod)
        for j in range(c.bit_length()):
            if (c >> j) & 1:
                p = t * i + j
                s1 = (s1 + pow(2, p, mod) * ((k - p) % mod)) % mod
                s2 = (s2 + prefix + (c % (1 << j)) * base) % mod
        prefix = (prefix + c * base) % mod
    u = (s1 - 2 * (big_a + s2)) % mod
    pk = pow(2, k, mod)
    big_m = (pk + 1) % mod
    return (
        a_mod * pk % mod * t1 - big_m * ((big_a * t1 - u) % mod) + 2 * big_m * big_a
    ) % mod


if __name__ == "__main__":
    assert f_series(3, 1, 1) == f_orbit(3, 1, 1) == 42  # given
    assert f_series(13, 3, 3, 160) == f_orbit(13, 3, 3) == 23093880  # given
    assert f_orbit(103, 13, 6) % MOD == 878922518  # given
    cases = [(3, 1, 1), (13, 3, 3), (103, 13, 6), (200, 17, 9), (500, 23, 11)]
    rng = random.Random(1)
    for _ in range(30):
        r = rng.randint(1, 12)
        mb = max(comb(r, i).bit_length() for i in range(1, r + 1))
        t = rng.randint(mb, mb + 12)
        cases.append((rng.randint(r * t + 1, r * t + 200), t, r))
    assert all(f_orbit(k, t, r) % MOD == f_sparse(k, t, r, MOD) for k, t, r in cases)
    print(f_sparse(10**18 + 31, 10**14 + 31, 62, MOD))  # 424315113
