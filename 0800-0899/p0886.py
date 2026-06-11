from collections import defaultdict
from functools import lru_cache
from math import factorial, gcd

import numba
import numpy as np

# Coprimality of x and y only depends on their squarefree kernels over the
# primes p with 2p <= n (a larger prime has a single multiple in range, so
# it never creates a conflict).  Numbers sharing a kernel are interchangeable,
# so P(n) = (number of words over the kernel classes, with prescribed
# multiplicities, where adjacent kernels are disjoint) times the product of
# the class factorials.  For n = 34 there are 18 classes with multiplicities
# (5, 3, 4, 2, 2, 2, 4, 1, ..., 1), and a DP over (used counts, last class)
# sweeps the 33 177 600 x 18 mixed-radix state space in one pass: a state
# reads its 18 predecessors at index - stride(last), which stream
# sequentially alongside the sweep, so the 2.4 GB table stays cache-friendly.

MOD = 83456729
PRIMES = [2, 3, 5, 7, 11, 13, 17]


def classes(n: int):
    groups: defaultdict = defaultdict(int)
    for x in range(2, n + 1):
        m = 0
        for i, p in enumerate(PRIMES):
            if 2 * p <= n and x % p == 0:
                m |= 1 << i
        groups[m] += 1
    masks = list(groups)
    caps = [groups[m] for m in masks]
    return masks, caps


def count_small(n: int) -> int:
    """Reference implementation with memoised dict states (small n)."""
    masks, caps = classes(n)
    k = len(masks)

    @lru_cache(maxsize=None)
    def f(counts: tuple, last: int) -> int:
        if counts[last] == 0:
            return 0
        if sum(counts) == 1:
            return 1
        prev = list(counts)
        prev[last] -= 1
        pc = tuple(prev)
        return sum(
            f(pc, p) for p in range(k) if pc[p] > 0 and not masks[p] & masks[last]
        )

    words = sum(f(tuple(caps), last) for last in range(k))
    for c in caps:
        words *= factorial(c)
    return words


def brute(n: int) -> int:
    nums = list(range(2, n + 1))
    count = 0

    def dfs(last: int, used: int, depth: int) -> None:
        nonlocal count
        if depth == len(nums):
            count += 1
            return
        for i, x in enumerate(nums):
            if not (used >> i) & 1 and (last == 0 or gcd(last, x) == 1):
                dfs(x, used | (1 << i), depth + 1)

    dfs(0, 0, 0)
    return count


@numba.njit(cache=True)
def sweep(caps: np.ndarray, compat: np.ndarray, mod: int) -> int:
    k = caps.shape[0]
    strides = np.empty(k, dtype=np.int64)
    s = 1
    for i in range(k):
        strides[i] = s
        s *= caps[i] + 1
    f = np.zeros(s * k, dtype=np.int32)
    d = np.zeros(k, dtype=np.int64)
    tot = 0
    for idx in range(s):
        if tot >= 1:
            base = idx * k
            for last in range(k):
                if d[last] >= 1:
                    if tot == 1:
                        f[base + last] = 1
                    else:
                        pbase = (idx - strides[last]) * k
                        acc = 0
                        for prev in range(k):
                            if compat[prev, last] and d[prev] - (prev == last) >= 1:
                                acc += f[pbase + prev]
                        f[base + last] = acc % mod
        for i in range(k):  # odometer
            if d[i] < caps[i]:
                d[i] += 1
                tot += 1
                break
            tot -= d[i]
            d[i] = 0
    base = (s - 1) * k
    out = 0
    for last in range(k):
        out = (out + f[base + last]) % mod
    return out


def count_big(n: int, mod: int) -> int:
    masks, caps = classes(n)
    k = len(masks)
    compat = np.zeros((k, k), dtype=np.uint8)
    for i in range(k):
        for j in range(k):
            compat[i, j] = not masks[i] & masks[j]
    res = sweep(np.array(caps, dtype=np.int64), compat, mod)
    for c in caps:
        res = res * factorial(c) % mod
    return res


if __name__ == "__main__":
    assert count_small(4) == 2  # given
    assert count_small(10) == 576  # given
    for n in range(4, 12):
        assert count_small(n) == brute(n)
    for n in (10, 12, 16):
        for m in (MOD, 999999937):
            assert count_big(n, m) == count_small(n) % m
    print(count_big(34, MOD))  # 5570163
