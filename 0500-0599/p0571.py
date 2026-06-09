"""
https://projecteuler.net/problem=571

A number is pandigital in base b if its base-b representation uses
every digit 0..b-1 at least once, and n-super-pandigital if it is
pandigital in every base 2..n. Find the sum of the 10 smallest
12-super-pandigital numbers.

Being pandigital in base n requires at least n base-n digits, so the
smallest candidates are exactly the n-digit base-n pandigitals: the
permutations of the digits 0..n-1 with a nonzero leading digit.
Enumerating permutations in lexicographic order within each leading
digit (and leading digits in increasing order) visits these numbers in
strictly increasing value, since they all have the same length. Each
candidate is tested for pandigitality in bases n-1 down to 2 with a
digit bitmask -- the highest base is by far the most selective, so it
goes first. The first `count` hits are the `count` smallest
n-super-pandigital numbers, provided they all fit in n base-n digits
(asserted; any (n+1)-digit number exceeds them all).

The 10 smallest 12-super-pandigitals emerge after sifting about
1.7 * 10^8 permutations. The search is validated on the given facts:
978 is the smallest 5-super-pandigital, 1093265784 the smallest
10-super-pandigital, and the 10 smallest 10-super-pandigitals sum to
20319792309.
"""

import numba
import numpy as np


@numba.njit(cache=True)
def _pandigital(v: int, b: int) -> bool:
    mask = 0
    full = (1 << b) - 1
    while v:
        mask |= 1 << (v % b)
        v //= b
    return mask == full


@numba.njit(cache=True)
def _next_perm(a: np.ndarray) -> bool:
    n = len(a)
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i < 0:
        return False
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1 :] = a[i + 1 :][::-1].copy()
    return True


@numba.njit(cache=True)
def _search(n: int, count: int) -> np.ndarray:
    """The `count` smallest n-super-pandigital numbers, found among the
    n-digit base-n pandigitals in increasing order."""
    found = np.zeros(count, dtype=np.int64)
    nf = 0
    for first in range(1, n):
        rest = np.empty(n - 1, dtype=np.int64)
        k = 0
        for d in range(n):
            if d != first:
                rest[k] = d
                k += 1
        while True:
            v = first
            for t in range(n - 1):
                v = v * n + rest[t]
            ok = True
            for b in range(n - 1, 1, -1):
                if not _pandigital(v, b):
                    ok = False
                    break
            if ok:
                found[nf] = v
                nf += 1
                if nf == count:
                    return found
            if not _next_perm(rest):
                break
    return found[:nf]


if __name__ == "__main__":
    assert int(_search(5, 1)[0]) == 978  # smallest 5-super-pandigital
    ten = _search(10, 10)
    assert int(ten[0]) == 1093265784  # smallest 10-super-pandigital
    assert int(ten.sum()) == 20319792309  # given sum for n = 10

    twelve = _search(12, 10)
    assert len(twelve) == 10  # all found within 12-digit candidates

    print(int(twelve.sum()))  # 30510390701978
