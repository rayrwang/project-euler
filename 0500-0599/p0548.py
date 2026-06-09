"""
https://projecteuler.net/problem=548

A gozinta chain for n is {1, a, b, ..., n} with each element properly
dividing the next; g(n) counts them. Find the sum of n <= 10^16 with
g(n) = n.

A chain is determined by its sequence of successive ratios, all > 1,
so g(n) is the number of ordered factorizations of n into parts
greater than 1, with the recurrence g(n) = sum over proper divisors
d < n of g(d), g(1) = 1. It depends only on n's prime signature (the
multiset of exponents).

Search: enumerate every canonical signature E (descending exponents)
whose minimal realization 2^e1 * 3^e2 * ... is at most 10^16 -- these
are exactly the A025487 numbers, 17563 of them. Compute g(E) by
summing memoized g over all proper sub-vectors of the exponent lattice
(signatures are processed in increasing minimal-realization order, and
any proper sub-vector canonicalizes to a strictly smaller one). g is
monotone under sub-vectors, so saturating the arithmetic at
CAP > 10^16 keeps every value <= 10^16 exact while avoiding int64
overflow. A signature E yields the solution v = g(E) iff v <= 10^16
and v's own signature equals E. Factoring v needs only primes to 10^6:
the remaining cofactor is 1, a prime, the square of a prime, or a
product of two distinct primes, distinguished by a square test and one
Miller-Rabin call.
"""

import sys
from math import isqrt
from pathlib import Path

import numba
import numpy as np
from numba import types
from numba.typed import Dict

sys.path.append(str(Path(__file__).parent.parent))
from funcs import is_prime, prime_sieve_int  # noqa: E402

N = 10**16
CAP = 4 * 10**16  # saturation cap, far above the target range
PRIMES16 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
PRIMES_ARR = np.array(PRIMES16, dtype=np.int64)


def gen_signatures(n: int) -> list[tuple[int, tuple[int, ...]]]:
    """All canonical signatures with minimal realization <= n, as
    (realization, descending exponent tuple), sorted by realization."""
    sigs = []

    def rec(idx: int, max_e: int, val: int, cur: list[int]) -> None:
        sigs.append((val, tuple(cur)))
        if idx >= len(PRIMES16):
            return
        p = PRIMES16[idx]
        e, v = 1, val * p
        while e <= max_e and v <= n:
            cur.append(e)
            rec(idx + 1, e, v, cur)
            cur.pop()
            e += 1
            v *= p

    rec(0, 60, 1, [])
    sigs.sort()
    return sigs


@numba.njit(cache=True)
def _g_for(sig: np.ndarray, memo, cap: int, primes: np.ndarray) -> int:
    """g of the signature sig: sum of memoized g over all proper
    sub-vectors of the exponent lattice, saturated at cap. Sub-vectors
    are canonicalized (sorted descending) and keyed by their minimal
    realization."""
    k = len(sig)
    if k == 0:
        return 1
    d = np.zeros(k, dtype=np.int64)
    tmp = np.empty(k, dtype=np.int64)
    total = 1  # the all-zeros sub-vector contributes g(1) = 1
    while True:
        # advance the mixed-radix counter over 0 <= d <= sig
        i = 0
        while i < k:
            if d[i] < sig[i]:
                d[i] += 1
                break
            d[i] = 0
            i += 1
        if i == k:
            break  # wrapped: all sub-vectors visited
        same = True
        for j in range(k):
            if d[j] != sig[j]:
                same = False
                break
        if same:
            continue  # exclude sig itself
        m = 0
        for j in range(k):
            if d[j] > 0:
                tmp[m] = d[j]
                m += 1
        for a in range(1, m):  # insertion sort, descending
            x = tmp[a]
            b = a - 1
            while b >= 0 and tmp[b] < x:
                tmp[b + 1] = tmp[b]
                b -= 1
            tmp[b + 1] = x
        key = np.int64(1)
        for j in range(m):
            p = primes[j]
            for _ in range(tmp[j]):
                key *= p
        total += memo[key]
        if total > cap:
            total = cap
    return total


@numba.njit(cache=True)
def _partial_factor(v: int, primes: np.ndarray) -> tuple[np.ndarray, int]:
    exps = np.empty(60, dtype=np.int64)
    m = 0
    for i in range(len(primes)):
        p = primes[i]
        if p * p > v:
            break
        if v % p == 0:
            e = 0
            while v % p == 0:
                v //= p
                e += 1
            exps[m] = e
            m += 1
    return exps[:m], v


def signature_of(v: int, small_primes: np.ndarray) -> tuple[int, ...]:
    exps, rem = _partial_factor(v, small_primes)
    sig = [int(e) for e in exps]
    if rem > 1:
        r = isqrt(rem)
        if r * r == rem:
            sig.append(2)  # rem = r^2 with r prime (no factor <= 10^6)
        elif is_prime(rem):
            sig.append(1)
        else:
            sig += [1, 1]  # product of two distinct primes > 10^6
    return tuple(sorted(sig, reverse=True))


def solve(n: int) -> tuple[int, dict[tuple[int, ...], int]]:
    sigs = gen_signatures(n)
    small_primes = prime_sieve_int(10**6)
    memo = Dict.empty(types.int64, types.int64)
    gvals: dict[tuple[int, ...], int] = {}
    total = 0
    for val, sig in sigs:
        gv = int(_g_for(np.array(sig, dtype=np.int64), memo, CAP, PRIMES_ARR))
        memo[val] = gv
        gvals[sig] = gv
        if 1 <= gv <= n and signature_of(gv, small_primes) == sig:
            total += gv
    return total, gvals


def brute_g(n_max: int) -> np.ndarray:
    """g(n) for all n <= n_max via the divisor recurrence."""
    g = np.zeros(n_max + 1, dtype=np.int64)
    g[1] = 1
    for d in range(1, n_max + 1):
        g[2 * d :: d] += g[d]
    return g


if __name__ == "__main__":
    total, gvals = solve(N)
    assert gvals[(2, 1)] == 8  # g(12) = 8
    assert gvals[(4, 1)] == 48  # g(48) = 48
    assert gvals[(3, 1, 1)] == 132  # g(120) = 132

    # brute force: every n <= 10^6 with g(n) = n, via the recurrence
    g = brute_g(10**6)
    matches = np.flatnonzero(g == np.arange(10**6 + 1))
    small = [int(m) for m in matches if m >= 1]
    assert small == [1, 48, 1280, 2496, 28672, 29808, 454656]
    small_total, _ = solve(10**6)
    assert small_total == sum(small)

    print(total)  # 12144044603581281
