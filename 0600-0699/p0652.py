"""Project Euler Problem 652: Distinct values of a proto-logarithmic function.

Classes of g split by whether log_m(n) is rational.

Rational classes: m = a^e, n = a^f give the value f/e; by the two rules
all pairs with the same reduced ratio coincide, and a reduced ratio f/e
is attained in [2, N]^2 iff some a >= 2 has a^max(e,f) <= N, i.e.
2^max(e,f) <= N.  With L = floor(log2 N) that counts
1 + 2 * sum_{k=2..L} phi(k) values.

Irrational classes: pairs (m, n) that are multiplicatively independent.
Rule 1 never applies to them, and rule 2 identifies (a^e, b^e) with
(a^f, b^f), so each class corresponds to a primitive independent
ordered pair (a, b) (not jointly a perfect power), which itself lies in
[2, N]^2.  Hence the count is sum_k mu(k) J(floor(N^(1/k))) where J(M)
is the number of independent pairs in [2, M]^2.  Dependent pairs are
both powers of a common primitive base c, contributing
floor(log_c M)^2 each; grouping by t = floor(log_c M) needs only
Q(x) = #non-perfect-powers in [2, x] = sum_j mu(j) (floor(x^(1/j)) - 1),
so J(M) = (M - 1)^2 - sum_t t^2 (Q(M^(1/t)) - Q(M^(1/(t+1)))).

Everything is exact big-integer arithmetic with binary-search k-th
roots; the final value is reduced mod 10^9.

Verified: D(5) = 13, D(10) = 69, D(100) = 9607, D(10^4) = 99959605 from
the statement, plus a direct float-free brute force for small N that
classifies pairs by canonical joint roots.
"""

from math import gcd, isqrt

MOD = 10**9


def kth_root(n: int, k: int) -> int:
    if k == 1:
        return n
    if k == 2:
        return isqrt(n)
    if n < 2:
        return n
    hi = 1 << ((n.bit_length() + k - 1) // k)
    lo = 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


def mobius_upto(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    comp = [False] * (n + 1)
    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            comp[i * p] = True
            if i % p == 0:
                break
            mu[i * p] = -mu[i]
    return mu


MU = mobius_upto(64)


def non_powers(x: int) -> int:
    """Q(x): integers in [2, x] that are not perfect powers."""
    if x < 2:
        return 0
    total = 0
    j = 1
    while 2**j <= x:
        total += MU[j] * (kth_root(x, j) - 1)
        j += 1
    return total


def independent_pairs(m: int) -> int:
    """J(M): multiplicatively independent pairs in [2, M]^2."""
    if m < 2:
        return 0
    dependent = 0
    t = 1
    while 2**t <= m:
        cnt = non_powers(kth_root(m, t)) - non_powers(kth_root(m, t + 1))
        dependent += t * t * cnt
        t += 1
    return (m - 1) ** 2 - dependent


def totient_upto(n: int) -> list[int]:
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi


def d_of(n: int) -> int:
    lg = n.bit_length() - 1  # floor(log2 n) since n >= 2
    phi = totient_upto(max(lg, 1))
    rational = 1 + 2 * sum(phi[2 : lg + 1])
    irrational = 0
    k = 1
    while 2**k <= n:
        irrational += MU[k] * independent_pairs(kth_root(n, k))
        k += 1
    return rational + irrational


def d_brute(n: int) -> int:
    def primitive_root(v: int) -> tuple[int, int]:
        for j in range(v.bit_length(), 1, -1):
            r = kth_root(v, j)
            if r**j == v:
                return r, j
        return v, 1

    classes = set()
    for m in range(2, n + 1):
        rm, em = primitive_root(m)
        for v in range(2, n + 1):
            rv, ev = primitive_root(v)
            if rm == rv:  # dependent: value ev / em
                g = gcd(em, ev)
                classes.add((0, ev // g, em // g))
            else:
                g = gcd(em, ev)
                classes.add((1, rm, rv, em // g, ev // g))
    return len(classes)


if __name__ == "__main__":
    assert d_of(5) == 13
    assert d_of(10) == 69
    assert d_of(100) == 9607
    assert d_of(10**4) == 99959605
    for small in (5, 10, 30, 100, 300):
        assert d_brute(small) == d_of(small), small
    print(d_of(10**18) % MOD)  # 983924497
