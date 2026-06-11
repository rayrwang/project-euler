"""Project Euler 945: XOR-Equation C.

The XOR-product is multiplication in GF(2)[x], reading integers as
polynomials over GF(2). Since squaring is the Frobenius endomorphism there,
(a + b)^2 = a^2 + b^2 and the equation

    a (x) a  xor  2 (x) a (x) b  xor  b (x) b  =  c (x) c

becomes a^2 + x a b + b^2 = c^2, i.e. (c + a + b)^2 = x a b in GF(2)[x].
Squares in GF(2)[x] are exactly the polynomials whose exponents are all
even, and squaring is injective, so a pair (a, b) yields exactly one
solution c = a xor b xor sqrt(x a b) precisely when x a b is a square -
note c is unbounded in the problem, only 0 <= a <= b <= N is required.

Writing a = x^alpha a', b = x^beta b' with a', b' of nonzero constant term
(odd integers), x a b = x^(alpha+beta+1) a' b' is a square iff alpha + beta
is odd and a' b' is a square, the latter happening iff the squarefree parts
of a' and b' (products of their irreducible factors of odd multiplicity)
coincide. a = 0 pairs with every b (then c = b). Hence

    F(N) = (N + 1) + sum over squarefree-part classes of c0 * c1,

where c0, c1 count n in [1, N] in the class with even / odd number of
trailing zero bits. Squarefree parts of all odd polynomials up to N come
from a carryless least-irreducible-factor sieve plus a DP that multiplies
or divides out one irreducible per step. Verified against brute force over
all pairs (with carryless arithmetic directly on the defining equation) for
N <= 300 and the given F(10) = 21.
"""

import numba
import numpy as np

N = 10**7


@numba.njit(cache=True)
def clmul(x, y):
    r = 0
    while y:
        if y & 1:
            r ^= x
        x <<= 1
        y >>= 1
    return r


@numba.njit(cache=True)
def cldivmod(n, d):
    """Carryless division: returns (quotient, remainder) of n by d."""
    if n == 0:
        return 0, 0
    dn = 0
    t = n
    while t > 1:
        t >>= 1
        dn += 1
    dd = 0
    t = d
    while t > 1:
        t >>= 1
        dd += 1
    q = 0
    while dn >= dd:
        if (n >> dn) & 1:
            q ^= 1 << (dn - dd)
            n ^= d << (dn - dd)
        dn -= 1
    return q, n


@numba.njit(cache=True)
def f_of_n(limit):
    # sieve least irreducible factor, with a clean degree-based bound
    lf = np.zeros(limit + 1, np.int32)
    for p in range(3, limit + 1, 2):
        if lf[p] == 0:
            pd = 0
            t = p
            while t > 1:
                t >>= 1
                pd += 1
            mmax = ((limit + 1) >> pd) << 1  # any m with deg(p)+deg(m) fits
            m = 3
            while m <= mmax:
                v = clmul(p, m)
                if v <= limit and lf[v] == 0:
                    lf[v] = p
                m += 2
    # squarefree parts by DP over odd n
    sf = np.zeros(limit + 1, np.int32)
    sf[1] = 1
    for n in range(3, limit + 1, 2):
        p = lf[n]
        if p == 0:
            sf[n] = n
        else:
            m, _ = cldivmod(n, p)
            s = sf[m]
            q, r = cldivmod(s, p)
            if r == 0:
                sf[n] = q
            else:
                sf[n] = clmul(s, p)
    # count pairs with equal squarefree part and opposite tz-parity
    c0 = np.zeros(limit + 1, np.int64)
    c1 = np.zeros(limit + 1, np.int64)
    ans = np.int64(limit + 1)  # a = 0 with any 0 <= b <= N
    for n in range(1, limit + 1):
        t = 0
        m = n
        while m & 1 == 0:
            m >>= 1
            t += 1
        key = sf[m]
        if t & 1:
            ans += c0[key]
            c1[key] += 1
        else:
            ans += c1[key]
            c0[key] += 1
    return ans


def solve() -> int:
    return int(f_of_n(N))


if __name__ == "__main__":
    print(solve())  # 83357132
