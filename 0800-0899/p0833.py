"""Project Euler 833: Square Triangle Products.

T_a T_b is a square iff T_a and T_b share the same squarefree kernel
s, and with m = 2a + 1 the equation T_x = s y^2 is the Pell equation
m^2 - 8 s y^2 = 1.  Each kernel class is therefore the orbit of its
fundamental solution: the members are m_k = Ch_k(m_0) (Chebyshev,
m + sqrt(m^2 - 1) = gamma^k), and for a pair (i < j) inside the family

    c = sqrt(T_a T_b) = (m_0^2 - 1)/8 * U_{i-1}(m_0) U_{j-1}(m_0),

a polynomial of degree i + j in m_0.  A primitive (fundamental) m_0 is
an odd m >= 3 that is not Ch_k of a smaller odd m (powers of even
bases, like 7 = Ch_2(2), are genuine fundamentals since their roots
correspond to no integer index).

Since the cheapest pair costs c = m(m^2 - 1)/4 ~ m^3/4, the cutoffs
M_ij with c_ij(m) <= 10^35 shrink rapidly: about 550 pairs (i, j) with
i + j <= 49 contribute, with M_12 ~ 7 * 10^11.  For each pair the sum
of c_ij over all odd m in [3, M_ij] is an exact Faulhaber evaluation
of the coefficient polynomial (computed with rational Bernoulli
numbers and big integers, so no modular inverses are needed), and the
~3 * 10^5 non-primitive odd values up to M_12 -- Chebyshev powers of
smaller odd bases, collected into a set -- are subtracted termwise.
The machinery agrees exactly with direct family enumeration at
n = 10^2, 10^5 and 10^9, matching the given S values, and the final
total is reduced modulo 136101521.
"""

from __future__ import annotations

import bisect
from fractions import Fraction
from math import comb

MOD = 136101521

_BERNOULLI = [Fraction(1)]
for _m in range(1, 61):
    _s = sum((comb(_m + 1, _k) * _BERNOULLI[_k] for _k in range(_m)), Fraction(0))
    _BERNOULLI.append(-_s / (_m + 1))


def power_sum(n: int, d: int) -> int:
    """Exact sum_{k=1}^{n} k^d."""
    if n <= 0:
        return 0
    s = Fraction(0)
    for k in range(d + 1):
        s += comb(d + 1, k) * _BERNOULLI[k] * Fraction(n) ** (d + 1 - k)
    s = s / (d + 1) + Fraction(n) ** d
    assert s.denominator == 1
    return s.numerator


def odd_power_sum(m_max: int, d: int) -> int:
    """Exact sum of m^d over odd m with 3 <= m <= m_max (m_max odd)."""
    return power_sum(m_max, d) - (2**d) * power_sum(m_max // 2, d) - 1


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return r


def chebyshev_u_polys(k_max: int) -> list[list[int]]:
    us = [[1], [0, 2]]
    while len(us) <= k_max:
        nxt = [0] + [2 * c for c in us[-1]]
        for idx, c in enumerate(us[-2]):
            nxt[idx] -= c
        us.append(nxt)
    return us


def pair_value(m: int, i: int, j: int) -> int:
    """Exact c_ij(m) = (m^2 - 1)/8 * U_{i-1}(m) * U_{j-1}(m)."""
    uv = [1, 2 * m]
    while len(uv) <= j - 1:
        uv.append(2 * m * uv[-1] - uv[-2])
    return (m * m - 1) // 8 * uv[i - 1] * uv[j - 1]


def non_primitive(limit: int) -> list[int]:
    np_set: set[int] = set()
    m = 3
    while 2 * m * m - 1 <= limit:
        a, b = 1, m
        while True:
            a, b = b, 2 * m * b - a
            if b > limit:
                break
            np_set.add(b)
        m += 2
    return sorted(np_set)


def closed_form_total(n: int) -> int:
    pairs = []
    j = 2
    while pair_value(3, 1, j) <= n:
        i = 1
        while i < j and pair_value(3, i, j) <= n:
            pairs.append((i, j))
            i += 1
        j += 1

    def max_odd_m(i: int, j: int) -> int:
        hi = 1
        while pair_value(hi * 2 + 1, i, j) <= n:
            hi *= 2
        hi = hi * 2 + 1
        lo, best = 3, 1
        while lo <= hi:
            mid = (lo + hi) // 2 | 1
            if mid > hi:
                mid -= 2
            if pair_value(mid, i, j) <= n:
                best = mid
                lo = mid + 2
            else:
                hi = mid - 2
        return best

    excluded = non_primitive(max_odd_m(1, 2))
    u_polys = chebyshev_u_polys(max(j for _, j in pairs))
    total = 0
    for i, j in pairs:
        m_max = max_odd_m(i, j)
        if m_max < 3:
            continue
        q = poly_mul([-1, 0, 1], poly_mul(u_polys[i - 1], u_polys[j - 1]))
        s = 0
        for d, cf in enumerate(q):
            if cf:
                s += cf * odd_power_sum(m_max, d)
        assert s % 8 == 0
        s //= 8
        for mv in excluded[: bisect.bisect_right(excluded, m_max)]:
            s -= pair_value(mv, i, j)
        total += s
    return total


def enumerate_total(n: int) -> int:
    m_max = 3
    while (m_max + 2) * ((m_max + 2) ** 2 - 1) // 4 <= n:
        m_max += 2
    excluded = set(non_primitive(m_max))
    total = 0
    for m0 in range(3, m_max + 1, 2):
        if m0 in excluded:
            continue
        base = (m0 * m0 - 1) // 8
        uv = [1, 2 * m0]
        if base * uv[0] * uv[1] > n:
            continue
        while base * uv[0] * uv[-1] <= n:
            uv.append(2 * m0 * uv[-1] - uv[-2])
        for ii in range(len(uv)):
            for jj in range(ii + 1, len(uv)):
                c = base * uv[ii] * uv[jj]
                if c <= n:
                    total += c
                else:
                    break
    return total


def main() -> None:
    for nv, expected in ((100, 155), (10**5, 1479802), (10**9, 241614948794)):
        assert enumerate_total(nv) == closed_form_total(nv) == expected
    print(closed_form_total(10**35) % MOD)  # 43884302


if __name__ == "__main__":
    main()
