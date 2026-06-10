"""
https://projecteuler.net/problem=586

f(n, r) counts k <= n expressible as k = a^2 + 3ab + b^2 with
a > b > 0 in exactly r ways. Find f(10^15, 40).

Completing the square, 4k = (2a + 3b)^2 - 5 b^2, so representations
correspond to elements xi = (u + v sqrt(5))/2 of the ring of
integers of Q(sqrt(5)) with norm k, u = 2a + 3b, v = b, subject to
v > 0 and u > 5v, i.e. 1/phi^2 < xi'/xi < 1. Multiplying by the
norm-one unit phi^2 scales the ratio by phi^(-4), so the window is
exactly half a unit period: each orbit {+-phi^(2j) xi, +-phi^(2j)
xi'} contributes exactly one representation, with boundary ratios
(v = 0 and a = b) excluded. Since h(Q(sqrt 5)) = 1 and N(phi) = -1,
orbits correspond to conjugate-pairs of ideals of norm k, and
self-conjugate ideals land exactly on the excluded boundary. Hence

    r(k) = (A(k) - S(k)) / 2,

A(k) = sum_(d|k) chi_5(d) the ideal count (multiplicative: split
p = +-1 mod 5 give e+1; inert p = +-2 mod 5 force even exponents;
5 is free) and S(k) = 1 iff every split exponent is even. r = 40
means A - S = 80: either A = 80 (which always contains an even
factor, consistent with S = 0) or A = 81 (all factors odd, so all
split exponents even, consistent with S = 1).

Counting: k = g * (split part), where g ranges over the "background"
values 5^a m^2 with m composed of inert primes (14.1M values up to
10^15, from an inert-composed sieve to sqrt(n)), and the split part
realizes a multiplicative partition of 80 or 81 as prod (e_i + 1)
over distinct split primes. For each background value and partition,
a DFS assigns split primes to exponents (equal exponents in
increasing order), and the innermost level is counted via a
pi_split table instead of enumerated, subtracting used primes in
range. Total work is proportional to the number of solutions
(~10^8).

Verified against a literal representation-count histogram for all
k <= 10^5 (several r values, including the given f(10^5, 4) = 237),
the identity r(k) = (A - S)/2 checked by factorization for all
k <= 30000, and the given f(10^8, 6) = 59517.
"""

from math import isqrt

import numba
import numpy as np


def _mult_partitions(t: int, maxf: int | None = None) -> list[list[int]]:
    if maxf is None:
        maxf = t
    if t == 1:
        return [[]]
    out = []
    f = min(maxf, t)
    while f >= 2:
        if t % f == 0:
            for rest in _mult_partitions(t // f, f):
                out.append([f, *rest])
        f -= 1
    return out


def _setup(n: int):
    lim = isqrt(n)
    sp = np.zeros(lim + 1, dtype=np.int32)
    for i in range(2, lim + 1):
        if sp[i] == 0:
            sp[i::i][sp[i::i] == 0] = i
    inert = np.zeros(lim + 1, dtype=np.int8)
    inert[1] = 1
    for i in range(2, lim + 1):
        p = int(sp[i])
        if p % 5 in (2, 3) and inert[i // p]:
            inert[i] = 1
    bg = []
    a = 1
    while a <= n:
        m = 1
        while a * m * m <= n:
            if inert[m]:
                bg.append(a * m * m)
            m += 1
        a *= 5
    bg_arr = np.array(sorted(bg), dtype=np.int64)
    plim = 5_000_000
    isp = np.ones(plim + 1, dtype=np.int8)
    isp[:2] = 0
    for i in range(2, isqrt(plim) + 1):
        if isp[i]:
            isp[i * i :: i] = 0
    split_mask = np.zeros(plim + 1, dtype=np.int8)
    for p in range(2, plim + 1):
        if isp[p] and p % 5 in (1, 4):
            split_mask[p] = 1
    pisplit = np.cumsum(split_mask).astype(np.int64)
    split_primes = np.nonzero(split_mask)[0].astype(np.int64)
    return bg_arr, pisplit, split_primes


@numba.njit(cache=True, inline="always")
def _iroot(x: np.int64, e: np.int64) -> np.int64:
    if e == 1:
        return x
    r = np.int64(x ** (1.0 / e))
    while r > 0 and r**e > x:
        r -= 1
    while (r + 1) ** e <= x:
        r += 1
    return r


@numba.njit(cache=True)
def _count_pattern(budget, exps, pisplit, split_primes, plim):
    t = len(exps)
    used = np.zeros(t, dtype=np.int64)
    idxs = np.zeros(t, dtype=np.int64)
    rem = np.zeros(t + 1, dtype=np.int64)
    rem[0] = budget
    total = np.int64(0)
    level = 0
    while True:
        if level == t - 1:
            e = exps[level]
            hi = _iroot(rem[level], e)
            if hi > plim:
                hi = plim
            lo_val = np.int64(0)
            if level > 0 and exps[level - 1] == e:
                lo_val = used[level - 1]
            c = pisplit[hi] - (pisplit[lo_val] if lo_val <= plim else pisplit[plim])
            if c > 0:
                for j in range(level):
                    if exps[j] != e and lo_val < used[j] <= hi:
                        c -= 1
                if c > 0:
                    total += c
            level -= 1
            if level < 0:
                break
            idxs[level] += 1
            continue
        e = exps[level]
        i = idxs[level]
        placed = False
        while i < len(split_primes):
            q = split_primes[i]
            v = np.int64(1)
            over = False
            for _ in range(e):
                v *= q
                if v > rem[level]:
                    over = True
                    break
            if over:
                break
            dup = False
            for j in range(level):
                if used[j] == q:
                    dup = True
                    break
            if not dup:
                used[level] = q
                rem[level + 1] = rem[level] // v
                idxs[level] = i
                level += 1
                idxs[level] = i + 1 if exps[level] == e else 0
                placed = True
                break
            i += 1
        if not placed:
            level -= 1
            if level < 0:
                break
            idxs[level] += 1
    return total


_SMALL_SPLIT = (11, 19, 29, 31, 41, 59, 61, 71, 79, 89, 101, 109)


def f_count(n: int, r: int, bg, pisplit, split_primes) -> int:
    plim = len(pisplit) - 1
    total = 0
    for tgt in (2 * r, 2 * r + 1):
        for part in _mult_partitions(tgt):
            if not part:
                continue
            exps = np.array(sorted((f - 1 for f in part), reverse=True), np.int64)
            mn = 1
            for i, e in enumerate(exps):
                mn *= _SMALL_SPLIT[i] ** int(e)
                if mn > n:
                    break
            if mn > n:
                continue
            for g in bg:
                if int(g) * mn > n:
                    break
                total += int(
                    _count_pattern(n // int(g), exps, pisplit, split_primes, plim)
                )
    return total


def _brute_hist(n: int) -> np.ndarray:
    cnt = np.zeros(n + 1, dtype=np.int32)
    b = 1
    while 5 * b * b <= n:
        a = b + 1
        while a * a + 3 * a * b + b * b <= n:
            cnt[a * a + 3 * a * b + b * b] += 1
            a += 1
        b += 1
    return cnt


def _r_by_factoring(k: int) -> int:
    a_cnt, s = 1, 1
    x = k
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if p != 5:
                if p % 5 in (1, 4):
                    a_cnt *= e + 1
                    if e % 2:
                        s = 0
                elif e % 2:
                    return 0
        p += 1
    if x > 1 and x != 5:
        if x % 5 in (1, 4):
            a_cnt *= 2
            s = 0
        else:
            return 0
    return (a_cnt - s) // 2


if __name__ == "__main__":
    bg, pisplit, split_primes = _setup(10**15)
    hist = _brute_hist(10**5)
    for k in range(1, 30001):
        assert _r_by_factoring(k) == hist[k], k
    for r in (1, 2, 3, 4, 6):
        assert f_count(10**5, r, bg, pisplit, split_primes) == int((hist == r).sum())
    assert f_count(10**5, 4, bg, pisplit, split_primes) == 237  # given
    assert f_count(10**8, 6, bg, pisplit, split_primes) == 59517  # given

    print(f_count(10**15, 40, bg, pisplit, split_primes))  # 82490213
