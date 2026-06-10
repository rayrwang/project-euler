"""
https://projecteuler.net/problem=535

S = 1, (1), 2, (1), 3, (2), 4, ... is characterised by: the circled
numbers are consecutive integers from 1; each non-circled a is
immediately preceded by exactly floor(sqrt(a)) circled numbers; and
deleting the circled numbers leaves S itself. T(n) sums the first n
elements; find T(10^18) mod 10^9.

Writing Q(n) for the sum of floor(sqrt(S_j)) over the first n
elements, the i-th non-circled element closes a prefix of length
L(i) = i + Q(i) containing the circled values 1..Q(i) and the
non-circled values S_1..S_i -- which are S again. Hence for any n,
with i the largest index satisfying i + Q(i) <= n and
r = n - i - Q(i) (automatically at most the next block length, by
maximality), the first n elements consist of the circled values
1..m, m = Q(i) + r, plus a copy of S's first i elements:

    T(n) = m (m + 1) / 2 + T(i),
    Q(n) = F(m) + Q(i),        F(m) = sum_(k<=m) floor(sqrt(k)),

with F in closed form. Since floor(sqrt(S_j)) >= 1, Q(i) >= i and the
recursion contracts n to roughly (3n/2)^(2/3); locating i is a binary
search whose probes evaluate Q one level down, all memoised, so
n = 10^18 resolves through three levels into a directly generated
table of the first 10^6 elements. The generator bootstraps from
S_1 = 1 and emits, for i = 1, 2, ..., floor(sqrt(S_i)) fresh circled
integers followed by the value S_i (available since the produced
prefix always runs ahead of the read pointer).

The generated prefix is validated against the 20 given terms and
both defining properties (circled entries are exactly the first
occurrences, in consecutive order, with correct block lengths before
every non-circled entry; deleting them reproduces S). The closed form
F matches a direct sum, and T(1) = 1, T(20) = 86, T(10^3) = 364089
and T(10^9) = 498676527978348241 are asserted exactly.
"""

import sys
from functools import lru_cache
from math import isqrt

import numba
import numpy as np

M = 10**6


@numba.njit(cache=True)
def _gen_table(m: int):
    cap = m + 100
    s = np.zeros(cap, dtype=np.int64)
    t = np.zeros(m + 1, dtype=np.int64)
    q = np.zeros(m + 1, dtype=np.int64)
    is_circ = np.zeros(cap, dtype=np.bool_)
    s[1] = 1  # bootstrap; reproduced by the construction itself
    length = 0
    circ = 0
    i = 1
    while length < m + 50:
        v = s[i]
        b = np.int64(np.sqrt(v))
        while b * b > v:
            b -= 1
        while (b + 1) * (b + 1) <= v:
            b += 1
        for _ in range(b):
            circ += 1
            length += 1
            s[length] = circ
            is_circ[length] = True
            if length >= m + 50:
                break
        if length >= m + 50:
            break
        length += 1
        s[length] = s[i]
        i += 1
    for j in range(1, m + 1):
        v = s[j]
        b = np.int64(np.sqrt(v))
        while b * b > v:
            b -= 1
        while (b + 1) * (b + 1) <= v:
            b += 1
        t[j] = t[j - 1] + v
        q[j] = q[j - 1] + b
    return s[: m + 1], t, q, is_circ[: m + 1]


_S, _T, _Q, _IC = _gen_table(M)


def _f(m: int) -> int:
    """Sum of floor(sqrt(k)) for k = 1..m, closed form."""
    s = isqrt(m)
    return (s - 1) * s * (2 * s - 1) // 3 + (s - 1) * s // 2 + s * (m - s * s + 1)


@lru_cache(maxsize=None)
def _locate(n: int):
    """Largest i with i + Q(i) <= n, plus Q(i)."""
    lo, hi = 1, n // 2 + 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid + _q(mid) <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo, _q(lo)


@lru_cache(maxsize=None)
def _q(n: int) -> int:
    if n <= M:
        return int(_Q[n])
    i, qi = _locate(n)
    return _f(qi + (n - i - qi)) + qi


def _t(n: int) -> int:
    if n <= M:
        return int(_T[n])
    i, qi = _locate(n)
    m = qi + (n - i - qi)
    return m * (m + 1) // 2 + _t(i)


def _validate_prefix(limit: int) -> None:
    seen: set[int] = set()
    run = 0  # consecutive circled immediately before current position
    sub = []  # non-circled subsequence
    circ_count = 0
    for j in range(1, limit + 1):
        v = int(_S[j])
        first = v not in seen
        seen.add(v)
        assert first == bool(_IC[j])  # circled = first occurrences
        if _IC[j]:
            circ_count += 1
            assert v == circ_count  # consecutive integers from 1
            run += 1
        else:
            assert run == isqrt(v)  # block length before non-circled
            run = 0
            sub.append(v)
    for k, v in enumerate(sub):  # deleting circled leaves S
        assert v == int(_S[k + 1])


if __name__ == "__main__":
    sys.setrecursionlimit(10000)

    assert list(_S[1:21]) == [
        1,
        1,
        2,
        1,
        3,
        2,
        4,
        1,
        5,
        3,
        6,
        2,
        7,
        8,
        4,
        9,
        1,
        10,
        11,
        5,
    ]
    _validate_prefix(10**5)
    for mm in list(range(1, 200)) + [10**6]:
        assert _f(mm) == sum(isqrt(k) for k in range(1, mm + 1))

    assert _t(1) == 1 and _t(20) == 86 and _t(10**3) == 364089  # given
    assert _t(10**9) == 498676527978348241  # given

    print(_t(10**18) % 10**9)  # 611778217
