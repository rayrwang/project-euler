"""Project Euler Problem 636: Restricted Factorisations.

A factorisation n! = a * b1^2 b2^2 * c1^3 c2^3 c3^3 * d1^4 ... d4^4
assigns to every prime p a split of v_p(n!) across the ten slots with
weights (1, 2, 2, 3, 3, 3, 4, 4, 4, 4); the bases are determined by the
exponent vectors, so equality of two bases means equality at every
prime simultaneously.  Distinctness of the ten bases is handled by
Moebius inclusion-exclusion over the partition lattice of the slots:

    #labelled distinct = sum over set partitions pi of
        prod_blocks (-1)^(|B|-1) (|B|-1)!  *  prod_p N_{W(pi)}(v_p(n!))

where merging a block adds its weights, W(pi) is the multiset of block
weight sums, and N_W(E) counts nonnegative solutions of
sum w_i x_i = E.  The per-partition count depends only on W, so the
115975 partitions collapse to 966 weight-sum signatures with integer
coefficients.  Dividing by 2! 3! 4! removes the orderings inside
equal-exponent groups (valid since all bases are distinct).

N_W is computed as a coin-counting DP table mod p (vectorised as
strided cumulative sums).  Exponents of n! cluster: only ~2300 distinct
values occur for n = 10^6, each handled with one table lookup and one
modular power.  For the few huge exponents of the smallest primes,
N_W(E) is a quasipolynomial of degree |W| - 1 and period lcm(W), which
is at most Landau(30) = 4620 because the block sums partition 30; it is
evaluated by Lagrange interpolation on the DP values at
E mod L, E mod L + L, ..., all below 10 * 4620 < table size.

Verified: 256 as square times fourth power in 3 ways, F(10!) = 2 and
F(20!) = 41680 for the six-slot variant, and F(25!) = 4933,
F(100!) = 693952493, F(1000!) = 6364496 from the statement.
"""

import math
from collections import Counter
from functools import reduce

import numpy as np

MOD = 1_000_000_007
LIM = 50_000


def set_partitions(items: list[int]):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield [*part[:i], [first, *part[i]], *part[i + 1 :]]
        yield [[first], *part]


def signatures(slot_weights: list[int]) -> dict[tuple[int, ...], int]:
    """Coefficient per multiset of block weight sums."""
    agg: Counter = Counter()
    for part in set_partitions(list(range(len(slot_weights)))):
        mu = 1
        sums = []
        for block in part:
            mu *= (-1) ** (len(block) - 1) * math.factorial(len(block) - 1)
            sums.append(sum(slot_weights[i] for i in block))
        agg[tuple(sorted(sums))] += mu
    return dict(agg)


def nsolve_table(weights: tuple[int, ...], lim: int) -> np.ndarray:
    dp = np.zeros(lim + 1, dtype=np.int64)
    dp[0] = 1
    for w in weights:
        for r in range(w):
            dp[r::w] = np.cumsum(dp[r::w]) % MOD
    return dp


def interp(dp: np.ndarray, weights: tuple[int, ...], e: int) -> int:
    """Quasipolynomial evaluation of N_W at huge e."""
    k = len(weights)
    period = reduce(math.lcm, weights, 1)
    r = e % period
    ys = [int(dp[r + j * period]) for j in range(k)]
    t = (e - r) // period % MOD
    res = 0
    for j in range(k):
        num, den = 1, 1
        for i in range(k):
            if i != j:
                num = num * (t - i) % MOD
                den = den * (j - i) % MOD
        res = (res + ys[j] * num % MOD * pow(den, MOD - 2, MOD)) % MOD
    return res


def legendre(n: int, p: int) -> int:
    e = 0
    while n:
        n //= p
        e += n
    return e


def primes_upto(n: int) -> list[int]:
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i :: i] = b"\x00" * len(sieve[i * i :: i])
    return [i for i in range(n + 1) if sieve[i]]


def f_of_exponents(exp_counts: dict[int, int],
                   slot_weights: list[int]) -> int:
    sym = 1
    for cnt in Counter(slot_weights).values():
        sym *= math.factorial(cnt)
    max_e = max(exp_counts)
    lim = min(LIM, max_e)
    total = 0
    for w_multiset, coef in signatures(slot_weights).items():
        dp = nsolve_table(w_multiset, lim)
        prod = 1
        for e, cnt in exp_counts.items():
            v = int(dp[e]) if e <= lim else interp(dp, w_multiset, e)
            prod = prod * pow(v, cnt, MOD) % MOD
        total = (total + coef * prod) % MOD
    return total * pow(sym, MOD - 2, MOD) % MOD


def f_factorial(n: int, slot_weights: list[int]) -> int:
    exps = Counter(legendre(n, p) for p in primes_upto(n))
    return f_of_exponents(dict(exps), slot_weights)


if __name__ == "__main__":
    assert f_of_exponents({8: 1}, [2, 4]) == 3  # 256, square x 4th power
    assert f_factorial(10, [1, 2, 2, 3, 3, 3]) == 2
    assert f_factorial(20, [1, 2, 2, 3, 3, 3]) == 41680
    slots = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    assert f_factorial(25, slots) == 4933
    assert f_factorial(100, slots) == 693952493
    assert f_factorial(1000, slots) == 6364496
    print(f_factorial(10**6, slots))  # 888316
