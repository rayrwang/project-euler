"""
https://projecteuler.net/problem=563

Robots weld up to 25 identical rectangles along an edge, starting from
unit squares, so a sheet a x b is constructible iff each side is a
product of factors in 2..25 -- exactly the 23-smooth numbers (primes
up to 23 all lie below 25, and any factor <= 25 splits into such
primes). A variant of area A is a pair (s, l) of 23-smooth sides with
s <= l <= 1.1 s and s l = A; M(n) is the least area with exactly n
variants. Find sum of M(n) for n = 2..100.

Enumeration: generate all 23-smooth numbers up to a bound B, then a
two-pointer sweep lists every pair (s, l) with 10 l <= 11 s, recording
the products. For any area A <= B^2 the smaller side satisfies
s <= sqrt(A) <= B, so every variant of A is captured: the count of
each such area is exact. Sorting the ~6.8 * 10^7 products and taking
the first (smallest) area attaining each count yields M(n). With
B = 10^8 every n in 2..100 is realized and the largest minimal area,
M(100) ~ 2.3 * 10^15, sits a factor four below the completeness
boundary B^2 = 10^16; the values are also cross-checked for agreement
against an independent run at B = 10^7. The given M(3) = 889200 with
variants 900 x 988, 912 x 975, 936 x 950 is asserted directly.
"""

import numba
import numpy as np

PRIMES = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23], dtype=np.int64)


@numba.njit(cache=True)
def _gen_smooth(bound: int) -> np.ndarray:
    stack_v = np.empty(4096, dtype=np.int64)
    stack_i = np.empty(4096, dtype=np.int64)
    # count first
    top = 0
    stack_v[0] = 1
    stack_i[0] = 0
    cnt = 0
    while top >= 0:
        v = stack_v[top]
        i = stack_i[top]
        top -= 1
        cnt += 1
        for j in range(i, 9):
            p = PRIMES[j]
            if v <= bound // p:
                top += 1
                stack_v[top] = v * p
                stack_i[top] = j
    out = np.empty(cnt, dtype=np.int64)
    top = 0
    stack_v[0] = 1
    stack_i[0] = 0
    k = 0
    while top >= 0:
        v = stack_v[top]
        i = stack_i[top]
        top -= 1
        out[k] = v
        k += 1
        for j in range(i, 9):
            p = PRIMES[j]
            if v <= bound // p:
                top += 1
                stack_v[top] = v * p
                stack_i[top] = j
    return np.sort(out)


@numba.njit(cache=True)
def _pair_areas(smooth: np.ndarray) -> np.ndarray:
    n = len(smooth)
    total = 0
    j = 0
    for i in range(n):
        hi = 11 * smooth[i] // 10
        if j < i:
            j = i
        while j < n and smooth[j] <= hi:
            j += 1
        total += j - i
    areas = np.empty(total, dtype=np.int64)
    k = 0
    j = 0
    for i in range(n):
        s = smooth[i]
        hi = 11 * s // 10
        if j < i:
            j = i
        while j < n and smooth[j] <= hi:
            j += 1
        for t in range(i, j):
            areas[k] = s * smooth[t]
            k += 1
    return areas


@numba.njit(cache=True)
def _best_per_count(areas: np.ndarray, complete_max: int, maxc: int) -> np.ndarray:
    """areas sorted ascending; best[c] = smallest area with exactly c
    variants, among areas <= complete_max (whose counts are exact)."""
    best = np.zeros(maxc + 1, dtype=np.int64)
    i = 0
    n = len(areas)
    while i < n:
        j = i
        a = areas[i]
        while j < n and areas[j] == a:
            j += 1
        c = j - i
        if a <= complete_max and c <= maxc and best[c] == 0:
            best[c] = a
        i = j
    return best


def m_table(bound: int, maxc: int = 120) -> np.ndarray:
    smooth = _gen_smooth(bound)
    areas = _pair_areas(smooth)
    areas.sort()
    return _best_per_count(areas, bound * bound, maxc)


def variants_direct(area: int) -> list[tuple[int, int]]:
    """All (s, l) for one area by direct divisor scan, for asserts."""

    def is_smooth(x: int) -> bool:
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
            while x % p == 0:
                x //= p
        return x == 1

    out = []
    s = 1
    while s * s <= area:
        if area % s == 0:
            ell = area // s
            if 10 * ell <= 11 * s and is_smooth(s) and is_smooth(ell):
                out.append((s, ell))
        s += 1
    return out


if __name__ == "__main__":
    assert variants_direct(889200) == [(900, 988), (912, 975), (936, 950)]

    best = m_table(10**8)
    assert all(best[n] > 0 for n in range(2, 101))  # every n realized
    assert best[3] == 889200  # M(3)
    assert int(best[2:101].max()) * 4 < 10**16  # well inside completeness

    # agreement with an independent smaller-bound run where defined
    small = m_table(10**7)
    for n in range(2, 101):
        if small[n] > 0:
            assert small[n] == best[n], n

    print(int(np.sum(best[2:101], dtype=np.int64)))  # 27186308211734760
