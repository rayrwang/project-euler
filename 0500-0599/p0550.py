"""
https://projecteuler.net/problem=550

k piles, each of 2..n stones. A move replaces a pile of m stones by
two piles a, b with 1 < a, b < m and a | m, b | m. The player unable
to move loses. f(n, k) counts the first-player-winning starting
positions (ordered k-tuples); find f(10^7, 10^12) mod 987654321.

Sprague-Grundy: piles are independent, so a position wins iff the XOR
of the pile Grundy values g(m) is nonzero, where

    g(m) = mex { g(a) xor g(b) : 1 < a, b < m, a | m, b | m }.

Replacing a pile never mixes piles, so g depends only on m's prime
signature: divisors of m correspond to sub-vectors of the exponent
vector. There are only a few hundred canonical signatures below 10^7,
so the Grundy table is computed once per signature (mex over XOR pairs
of the distinct sub-signature values), then every m <= 10^7 is mapped
through a smallest-prime-factor sieve to its signature and tallied
into counts c_v = #{m : g(m) = v}.

Counting XOR-zero k-tuples is a k-fold XOR convolution: with the
Walsh-Hadamard transform W of c (length the next power of two above
max g), the number of XOR-zero tuples is sum_i W_i^k / size, and

    f(n, k) = (n - 1)^k - sum_i W_i^k / size  (mod 987654321),

where the division is by the modular inverse of the (odd-coprime)
power of two. Verified against direct Grundy recursion for m <= 5000,
brute-force tuple DP for small (n, k), and the given f(10, 5) = 40085.
"""

import sys
from functools import lru_cache
from pathlib import Path

import numba
import numpy as np
from numba import types
from numba.typed import Dict

sys.path.append(str(Path(__file__).parent.parent))

MOD = 987654321
PRIMES8 = [2, 3, 5, 7, 11, 13, 17, 19]  # 8 primes suffice below 10^7


def gen_signatures(n: int) -> list[tuple[int, ...]]:
    sigs = []

    def rec(idx: int, max_e: int, val: int, cur: list[int]) -> None:
        sigs.append(tuple(cur))
        if idx >= len(PRIMES8):
            return
        p = PRIMES8[idx]
        e, v = 1, val * p
        while e <= max_e and v <= n:
            cur.append(e)
            rec(idx + 1, e, v, cur)
            cur.pop()
            e += 1
            v *= p

    rec(0, 60, 1, [])
    return sigs


def pack(sig: tuple[int, ...]) -> int:
    key = 0
    for e in sig:
        key = (key << 5) | e
    return key


def grundy_by_signature(n: int) -> dict[tuple[int, ...], int]:
    """Grundy value of every canonical signature realizable <= n."""
    from itertools import product as iproduct

    g: dict[tuple[int, ...], int] = {}
    # order by total exponent weight so sub-signatures come first
    for sig in sorted(gen_signatures(n), key=lambda s: (sum(s), s)):
        if not sig:
            continue  # m = 1 is not a pile
        subs = set()
        for d in iproduct(*[range(e + 1) for e in sig]):
            if any(d) and d != sig:
                subs.add(g[tuple(sorted((x for x in d if x), reverse=True))])
        opts = {a ^ b for a in subs for b in subs}
        mex = 0
        while mex in opts:
            mex += 1
        g[sig] = mex
    return g


@numba.njit(cache=True)
def _spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def _counts(n: int, spf: np.ndarray, gtable, max_g: int) -> np.ndarray:
    cnt = np.zeros(max_g + 1, dtype=np.int64)
    exps = np.empty(8, dtype=np.int64)
    for m in range(2, n + 1):
        mm = m
        k = 0
        while mm > 1:
            p = spf[mm]
            e = 0
            while mm % p == 0:
                mm //= p
                e += 1
            exps[k] = e
            k += 1
        # insertion sort descending
        for a in range(1, k):
            x = exps[a]
            b = a - 1
            while b >= 0 and exps[b] < x:
                exps[b + 1] = exps[b]
                b -= 1
            exps[b + 1] = x
        key = np.int64(0)
        for j in range(k):
            key = (key << 5) | exps[j]
        cnt[gtable[key]] += 1
    return cnt


def f_of(n: int, k: int) -> int:
    gsig = grundy_by_signature(n)
    max_g = max(gsig.values())
    gtable = Dict.empty(types.int64, types.int64)
    for sig, v in gsig.items():
        gtable[pack(sig)] = v
    spf = _spf_sieve(n)
    cnt = _counts(n, spf, gtable, max_g)
    size = 1
    while size <= max_g:
        size <<= 1
    c = [int(cnt[v]) if v <= max_g else 0 for v in range(size)]
    # exact Walsh-Hadamard transform (size is small)
    w = c[:]
    h = 1
    while h < size:
        for start in range(0, size, 2 * h):
            for i in range(start, start + h):
                x, y = w[i], w[i + h]
                w[i], w[i + h] = x + y, x - y
        h *= 2
    zeros = sum(pow(wi % MOD, k, MOD) for wi in w) % MOD
    zeros = zeros * pow(size, -1, MOD) % MOD  # MOD is odd: gcd(size, MOD) = 1
    return (pow(n - 1, k, MOD) - zeros) % MOD


def f_brute(n: int, k: int) -> int:
    """Direct Grundy recursion plus tuple DP over XOR values."""

    @lru_cache(maxsize=None)
    def g(m: int) -> int:
        ds = [d for d in range(2, m) if m % d == 0]
        opts = {g(a) ^ g(b) for a in ds for b in ds}
        mex = 0
        while mex in opts:
            mex += 1
        return mex

    vals = [g(m) for m in range(2, n + 1)]
    size = 1
    while size <= max(vals):
        size <<= 1
    dp = [0] * size
    dp[0] = 1
    for _ in range(k):
        nxt = [0] * size
        for x, c in enumerate(dp):
            if c:
                for v in vals:
                    nxt[x ^ v] += c
        dp = nxt
    return ((n - 1) ** k - dp[0]) % MOD


if __name__ == "__main__":
    # signature Grundy agrees with the direct recursion
    gsig = grundy_by_signature(5000)

    @lru_cache(maxsize=None)
    def g_direct(m: int) -> int:
        ds = [d for d in range(2, m) if m % d == 0]
        opts = {g_direct(a) ^ g_direct(b) for a in ds for b in ds}
        mex = 0
        while mex in opts:
            mex += 1
        return mex

    def sig_of(m: int) -> tuple[int, ...]:
        e = []
        d = 2
        while d * d <= m:
            if m % d == 0:
                c = 0
                while m % d == 0:
                    m //= d
                    c += 1
                e.append(c)
            d += 1
        if m > 1:
            e.append(1)
        return tuple(sorted(e, reverse=True))

    for m in range(2, 5001):
        assert g_direct(m) == gsig[sig_of(m)], m

    assert f_of(10, 5) == f_brute(10, 5) == 40085
    for nn, kk in [(6, 3), (12, 4), (30, 6)]:
        assert f_of(nn, kk) == f_brute(nn, kk), (nn, kk)

    print(f_of(10**7, 10**12))  # 328104836
