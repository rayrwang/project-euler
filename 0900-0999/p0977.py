"""Project Euler 977: Iterated Functions.

Setting x = 1 in f^(x)(y) = f^(y)(x) gives f(y) = f^(y)(1); conversely if
f(y) = f^(y)(1) for all y then f^(x)(y) = f^(x+y-1)(1) is symmetric. So valid
f are exactly those determined by the orbit of 1: f(y) = t_y where
t_k = f^(k)(1).

Let the orbit of 1 be a rho with tail length m >= 0 and cycle length c >= 1:
distinct values u_0 = 1, u_1, ..., u_{m+c-1}. Writing sigma(j) for the orbit
position of the j-th iterate (sigma(j) = j for j < m+c, else m + (j-m) mod c),
consistency of f(y) = t_y with f(u_k) = u_{next(k)} forces

    sigma(u_k) = next(k)   for k = 1, ..., m+c-1,

i.e. each u_k is either exactly the small value next(k), or any value
>= m+c congruent to next(k) mod c (the latter only for cycle positions).
Hence the tail is forced to be 1, 2, ..., m-1, and each cycle position picks
from one residue class; the class of m is shared by two positions (an ordered
distinct pair). With D = n - m and D = Qc + r (0 <= r < c) the counts of
available large values are floor((D - i)/c), giving closed forms

    N(m, c) = (Q+1)^(r+1) Q^(c-r)        for m >= 2,
    N(1, c) = Q^(c-r) (Q+1)^r            with D = n - 1,
    N(0, c) = Q' (Q'+1)^a Q'^b           with n = Q'c + r',
              a = max(0, min(r', c-1) - 1), b = c - 2 - a   (N(0,1) = 1).

Summing N(m, c) over m >= 2 groups by Q: each full block of c values of r is
the geometric sum (Q+1) Q ((Q+1)^c - Q^c); truncated blocks use
sum_{r<=R} Q^(c-r) (Q+1)^(r+1) = (Q+1) Q^(c-R) ((Q+1)^(R+1) - Q^(R+1)).
That is O(sum_c n/c) = O(n log n) modular exponentiations.

Verified: brute force F(1..7) = 1, 3, 8, 21, 46, 96, 174 (matching the given
F(3) = 8 and F(7) = 174) and exact F(100) = 570271270297640131.
"""

import numba

MOD = 10**9 + 7


@numba.njit(cache=True)
def modpow(b: int, e: int, m: int) -> int:
    b %= m
    r = 1
    while e > 0:
        if e & 1:
            r = r * b % m
        b = b * b % m
        e >>= 1
    return r


@numba.njit(cache=True)
def solve(n: int, mod: int) -> int:
    total = 0
    for c in range(1, n + 1):
        # m = 0: 1 lies on the cycle
        if c == 1:
            total += 1
        else:
            qp, rp = divmod(n, c)
            a = max(0, min(rp, c - 1) - 1)
            b = (c - 2) - a
            total += qp % mod * modpow(1 + qp, a, mod) % mod * modpow(qp, b, mod)
        # m = 1
        if 1 + c <= n:
            q, r = divmod(n - 1, c)
            total += modpow(q, c - r, mod) * modpow(1 + q, r, mod)
        total %= mod
        # m >= 2, grouped by q = (n - m) // c
        for q in range(1, (n - 2) // c + 1):
            rmax = min(c - 1, n - 2 - q * c)
            term = (
                (q + 1)
                % mod
                * modpow(q, c - rmax, mod)
                % mod
                * ((modpow(q + 1, rmax + 1, mod) - modpow(q, rmax + 1, mod)) % mod)
                % mod
            )
            total = (total + term) % mod
    return total % mod


if __name__ == "__main__":
    print(solve(10**6, MOD))  # 537945304
