"""Project Euler 410: Circle and Tangent Line.

Count integer quadruplets (r, a, b, c) such that the line through P(a, b) and
Q(-a, c) is tangent to x^2 + y^2 = r^2, for 0 < r <= R, 0 < a <= X; find
F(10^8, 10^9) + F(10^9, 10^8).

The tangency condition (distance from the origin equals r) is
a^2 (b+c)^2 = r^2 ((b-c)^2 + 4a^2). With g = gcd(r, a), a = g alpha,
r = g rho, the substitution b + c = rho sigma, b - c = alpha delta is forced,
leaving sigma^2 - delta^2 = 4 g^2. Its integer solutions correspond to
sigma = u + v, delta = v - u with u v = g^2 (both signs), i.e. 2 tau(g^2)
solutions. The integrality parity b = (s+d)/2 demands rho sigma = alpha delta
(mod 2), which is automatic unless g is even and exactly one of alpha, rho is
even, in which case u, v must both be even: 2 tau(g^2 / 4) solutions.

Summing the per-pair counts with Dirichlet rearrangement (tau(.^2) * mu has
value 2^omega, and the even-g corrections telescope similarly):

  F/2 = sum_e 2^omega(e) flo(X/e) flo(R/e)
      - 2 [ sum_{e = 2 mod 4} 2^omega(e/2) flo(X/e) flo(R/e)
          - sum_{e even} 2^omega(odd(e)) (flo(X/e) - flo(X/2e)) (flo(R/e) - flo(R/2e)) ],

with all sums over e <= min(R, X) = 10^8: one sieve of 2^omega and a linear
numba pass. The chain brute force = per-pair formula = closed form is
asserted, along with F(1,5) = 10, F(2,10) = 52, F(10,100) = 3384.
"""


import numpy as np
from numba import njit


def brute_count(rmax, xmax):
    cnt = 0
    for r in range(1, rmax + 1):
        for a in range(1, xmax + 1):
            bound = 2 * (r * r + a * a) + 10
            for b in range(-bound, bound + 1):
                for c in range(-bound, bound + 1):
                    if a * a * (b + c) ** 2 == r * r * ((b - c) ** 2 + 4 * a * a):
                        cnt += 1
    return cnt


def omega_pow2_sieve(limit):
    w = np.ones(limit + 1, dtype=np.int16)
    is_comp = np.zeros(limit + 1, dtype=bool)
    for p in range(2, limit + 1):
        if not is_comp[p]:
            w[p::p] <<= 1
            if p * p <= limit:
                is_comp[p * p :: p * p] = True
                is_comp[p * p :: p] = True
    return w


@njit(cache=True)
def fast_count(rmax, xmax, w):
    emax = min(rmax, xmax)
    s1 = np.int64(0)
    a_sum = np.int64(0)
    b_sum = np.int64(0)
    for e in range(1, emax + 1):
        fx = xmax // e
        fr = rmax // e
        s1 += np.int64(w[e]) * fx * fr
        if e % 2 == 0:
            wu = np.int64(w[e]) >> 1  # 2^omega of the odd part
            if e % 4 == 2:
                a_sum += wu * fx * fr
            b_sum += wu * (fx - xmax // (2 * e)) * (fr - rmax // (2 * e))
    return 2 * (s1 - 2 * (a_sum - b_sum))


if __name__ == "__main__":
    w_small = omega_pow2_sieve(100)
    assert fast_count(1, 5, w_small) == brute_count(1, 5) == 10
    assert fast_count(2, 10, w_small) == brute_count(2, 10) == 52
    assert fast_count(10, 100, w_small) == 3384
    w = omega_pow2_sieve(10**8)
    total = fast_count(10**8, 10**9, w) + fast_count(10**9, 10**8, w)
    print(total)  # 799999783589946560
