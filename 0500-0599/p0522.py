"""
https://projecteuler.net/problem=522

Each of n floors sends power to one other floor (f(i) != i). The
hotel works iff the functional graph is a single n-cycle. F(n) sums,
over all (n-1)^n arrangements, the minimum number of edge rewirings
needed to reach an n-cycle. Find F(12344321) mod 135707531.

The edges kept from f must form disjoint simple paths (in/out degree
at most 1, no cycle) unless f already is the n-cycle, and any linear
forest of size n - r extends to an n-cycle with r rewirings. At each
vertex all but one incoming edge must go, costing
sum_v (indeg(v) - 1)^+; each cycle of f must also lose an edge, but
in a cyclic component whose cycle carries a tree attachment the
in-degree surplus can be spent on a cycle edge for free - only
*bare* cycles (components that are exactly cycles) cost one extra.
Hence

  min rewirings = sum_v (indeg(v)-1)^+ + #bare cycles - [f is n-cycle].

Summing over all f: indegrees are Binomial(n-1, 1/(n-1)) and
E[(B-1)^+] = P(B = 0), so the first term totals
n (n-1) (n-2)^(n-1). A bare cycle on a chosen l-set ((l-1)! cyclic
orders) forbids outsiders from entering it, leaving (n-l-1)^(n-l)
completions, so the second totals
sum_(l=2..n) n!/(l (n-l)!) (n-l-1)^(n-l); the last is (n-1)!.

Verified against literal minimisation over all n-cycles for every
arrangement with n = 3, 4, 5, the structural cost formula for the
same range, and the given F(3) = 6, F(8) = 16276736,
F(100) = 84326147 mod 135707531.
"""

from itertools import permutations, product
from math import factorial

import numba
import numpy as np

MOD = 135707531


@numba.njit(cache=True)
def f_mod(n: int, p: int) -> np.int64:
    fact = np.zeros(n + 1, dtype=np.int64)
    fact[0] = 1
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % p

    def powmod(b, e, m):
        r = np.int64(1)
        b %= m
        while e > 0:
            if e & 1:
                r = r * b % m
            b = b * b % m
            e >>= 1
        return r

    invfact = np.zeros(n + 1, dtype=np.int64)
    invfact[n] = powmod(fact[n], p - 2, p)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % p
    t1 = n % p * ((n - 1) % p) % p * powmod((n - 2) % p, n - 1, p) % p
    t2 = np.int64(0)
    for el in range(2, n + 1):
        inv_l = invfact[el] * fact[el - 1] % p
        term = (
            fact[n]
            * inv_l
            % p
            * invfact[n - el]
            % p
            * powmod((n - el - 1) % p, n - el, p)
            % p
        )
        t2 = (t2 + term) % p
    return (t1 + t2 - fact[n - 1]) % p


def f_exact(n: int) -> int:
    t1 = n * (n - 1) * (n - 2) ** (n - 1)
    t2 = sum(
        factorial(n) // (el * factorial(n - el)) * (n - el - 1) ** (n - el)
        for el in range(2, n + 1)
    )
    return t1 + t2 - factorial(n - 1)


def _brute_true(n: int) -> int:
    ncycles = set()
    for perm in permutations(range(1, n)):
        order = [0, *perm]
        g = [0] * n
        for i in range(n):
            g[order[i]] = order[(i + 1) % n]
        ncycles.add(tuple(g))
    total = 0
    for f in product(*[[t for t in range(n) if t != i] for i in range(n)]):
        total += min(sum(1 for i in range(n) if f[i] != g[i]) for g in ncycles)
    return total


if __name__ == "__main__":
    assert f_exact(3) == 6 == _brute_true(3)  # given
    assert f_exact(4) == _brute_true(4)
    assert f_exact(5) == _brute_true(5)
    assert f_exact(8) == 16276736  # given
    assert int(f_mod(100, MOD)) == 84326147 == f_exact(100) % MOD  # given

    print(int(f_mod(12344321, MOD)))  # 96772715
