"""
https://projecteuler.net/problem=551

a_0 = 1 and a_n is the sum of the digits of all preceding terms, which
collapses to a_n = a_(n-1) + digitsum(a_(n-1)) for n >= 2 (the running
digit total IS the previous term). Given a_(10^6) = 31054319, find
a_(10^15).

The walk is memoryless given the current value, and while the digits
above position k stay fixed, the evolution of the low k digits depends
only on (low value L, digit sum h of the high part). Define
jump(k, L, h) = (number of steps until the low-k block overflows, the
block's value after the carry). A single step adds at most
digitsum(v) < 1000, so for k >= 3 the block overflows by exactly one
carry, making the jump well defined. jump(3, ., .) is simulated
directly; jump(k, ., .) peels the top digit d of the block and chains
ten level-(k-1) jumps with high sum h + d. Memoising on (k, L, h)
keeps the table tiny (~8000 entries) because exit values recur.

The driver repeatedly applies the largest block jump that fits in the
remaining step budget, falling back to single steps at the bottom.
Verified against direct simulation for several n up to 10^6 including
the given a_(10^6).
"""

import sys


def ds(x: int) -> int:
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


memo: dict[tuple[int, int, int], tuple[int, int]] = {}


def jump(k: int, low: int, h: int) -> tuple[int, int]:
    """Steps until the low-k-digit block overflows, and the block value
    after the single carry, starting from block value `low` with the
    digits above the block summing to h."""
    key = (k, low, h)
    if key in memo:
        return memo[key]
    if k == 3:
        steps = 0
        while low < 1000:
            low += h + ds(low)
            steps += 1
        res = (steps, low - 1000)
    else:
        p = 10 ** (k - 1)
        steps = 0
        d, sub = divmod(low, p)
        while True:
            s, sub = jump(k - 1, sub, h + d)  # d is one digit: ds(d) = d
            steps += s
            d += 1
            if d == 10:
                res = (steps, sub)
                break
    memo[key] = res
    return res


def a_of(n: int) -> int:
    """a_n, with a_0 = a_1 = 1."""
    if n == 0:
        return 1
    v, i = 1, 1
    while i < n:
        rem = n - i
        for k in range(16, 2, -1):
            pk = 10**k
            high, low = divmod(v, pk)
            s, low2 = jump(k, low, ds(high))
            if s <= rem:
                v = (high + 1) * pk + low2
                i += s
                break
        else:
            while i < n:  # remaining budget below one 3-digit block
                v += ds(v)
                i += 1
    return v


def a_brute(n: int) -> int:
    v = 1
    for _ in range(n - 1):
        v += ds(v)
    return v


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    for nn in (2, 10, 100, 1000, 12345, 10**6):
        assert a_of(nn) == a_brute(nn), nn
    assert a_of(10**6) == 31054319  # given

    print(a_of(10**15))  # 73597483551591773
