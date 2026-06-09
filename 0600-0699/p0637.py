"""Project Euler Problem 637: Flexible Digit Sum.

One step inserts plus signs into the base-B digits and adds.  The minimum
split sum is the plain digit sum (merging digits a,b costs a(B-1) >= 0),
so f(i, B) = 1 exactly when ds_B(i) < B.  And f(i, B) = 2 exactly when
some proper split sum v has ds_B(v) < B.  Finally f never exceeds 3 here:
the finest split gives f(i) <= 1 + f(ds_B(i)), the digit sums are at most
70 (base 10) resp. 30 (base 3), and every value that small has f <= 2
(checked by brute force; the smallest base-3 number with f = 3 is 1781).

So classification only needs an exists-test over proper splits: a DFS over
cut positions accumulating completed parts, early-exiting as soon as a
finished split's sum lands in the precomputed "digit sum < B" table, and
trying single-digit parts first since the finest splits hit most often.
Base 10 has at most 2^7 splits; base 3 up to 2^14, but the digit-sum
precheck resolves a third of all i instantly, nearly all the rest exit
within a few nodes, and full traversals happen only for the very rare
f = 3 numbers.

Checks: g(100, 10, 3) = 3302 (given) and full agreement of both
classifiers with a brute-force recursive f for all i <= 3^10.
"""

import numba
import numpy as np


def digit_sums(n: int, base: int) -> np.ndarray:
    ds = np.zeros(n + 1, dtype=np.int8)
    for v in range(1, n + 1):
        ds[v] = ds[v // base] + v % base
    return ds


@numba.jit(cache=True)
def digit_sums_nb(n: int, base: int) -> np.ndarray:
    ds = np.zeros(n + 1, dtype=np.int8)
    for v in range(1, n + 1):
        ds[v] = ds[v // base] + v % base
    return ds


@numba.jit(cache=True)
def has_good_split(d: np.ndarray, k: int, base: int, good: np.ndarray) -> bool:
    """Does some proper split of digits d[0:k] sum into the good set?"""
    # iterative DFS over (position, partial sum); parts tried shortest-first
    pos_stack = np.empty(k + 1, dtype=np.int64)
    sum_stack = np.empty(k + 1, dtype=np.int64)
    end_stack = np.empty(k + 1, dtype=np.int64)
    top = 0
    pos_stack[0] = 0
    sum_stack[0] = 0
    end_stack[0] = 0  # next part length - 1 to try
    while top >= 0:
        pos = pos_stack[top]
        end = pos + end_stack[top]
        if end >= k:
            top -= 1
            continue
        end_stack[top] += 1  # next time, try a longer part
        w = 0
        for t in range(pos, end + 1):
            w = w * base + d[t]
        if end == k - 1:  # this part finishes the split
            if pos > 0 and good[sum_stack[top] + w]:  # proper split only
                return True
        else:
            top += 1
            pos_stack[top] = end + 1
            sum_stack[top] = sum_stack[top - 1] + w
            end_stack[top] = 0
    return False


@numba.jit(cache=True)
def classify(n: int, base: int) -> np.ndarray:
    """f(i, base) for all i <= n (f is always 0..3 in this range)."""
    ds = digit_sums_nb(n, base)
    good = ds < base
    f = np.full(n + 1, 2, dtype=np.int8)
    d = np.empty(32, dtype=np.int64)
    for i in range(1, n + 1):
        if i < base:
            f[i] = 0
        elif good[i]:
            f[i] = 1
        elif good[ds[i]]:
            f[i] = 2  # finest split works
        else:
            k = 0
            v = i
            while v:
                d[k] = v % base
                v //= base
                k += 1
            d[:k] = d[:k][::-1]
            f[i] = 2 if has_good_split(d, k, base, good) else 3
    return f


def f_brute(i: int, base: int, cache: dict) -> int:
    if i < base:
        return 0
    if i in cache:
        return cache[i]
    d = []
    v = i
    while v:
        d.append(v % base)
        v //= base
    d = d[::-1]
    k = len(d)
    best = 4
    for mask in range(1, 1 << (k - 1)):
        s = cur = 0
        for idx in range(k):
            cur = cur * base + d[idx]
            if idx < k - 1 and (mask >> (k - 2 - idx)) & 1:
                s += cur
                cur = 0
        best = min(best, f_brute(s + cur, base, cache))
    cache[i] = 1 + best
    return 1 + best


if __name__ == "__main__":
    for base in (10, 3):
        small = classify(3**10, base)
        cache: dict = {}
        assert all(
            small[i] == f_brute(i, base, cache) for i in range(1, 3**10 + 1)
        ), base
    f10 = classify(10**7, 10)
    f3 = classify(10**7, 3)
    match = f10 == f3
    idx = np.arange(10**7 + 1, dtype=np.int64)
    assert int(idx[:101][match[:101]].sum()) == 3302  # g(100, 10, 3)
    print(int(idx[match].sum()))  # 49000634845039
