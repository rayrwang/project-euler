"""Project Euler 834: Add and Divide.

The m-th term is a_m = n + sum_{k<=m}(n+k) = (m+1)(2n+m)/2.  Writing
d = n + m, expanding (d-n+1)(d+n) = d(d+1) + n - n^2 shows that
d | a_m reduces, modulo 2d, to: for odd d, 2d | n(n-1); for even d,
n(n-1) = d (mod 2d).  Both cases say d divides P = n(n-1) with the
2-adic valuation of d equal to 0 or v_2(P) — i.e. d is an odd divisor
of P, or such a divisor times the full power 2^(v_2(P)).  Brute-force
simulation of the sequence confirms this characterisation for dozens
of random n, and S(10) = {5, 8, 20, 35, 80} drops out as the
qualifying divisors of 90 above 10.

Hence T(n) sums d - n over qualifying divisors d > n of n(n-1).
Since n and n-1 are coprime, the odd divisors of P are products of
the odd divisors of each factor; a smallest-prime-factor sieve
generates each list once, and the list for n-1 is reused from the
previous iteration.  For every pair product o the two candidates o
and o * 2^(v_2(P)) are tested against n directly.  About 10^8 divisor
combinations cover all n <= 1234567 in roughly ten seconds, after the
code reproduces T(10) = 148, T(100) = 21828 and U(100) = 612572.
"""

from __future__ import annotations

import numpy as np


def grand_total(n_max: int) -> int:
    spf = np.zeros(n_max + 1, dtype=np.int32)
    for i in range(2, n_max + 1):
        if spf[i] == 0:
            seg = spf[i : n_max + 1 : i]
            seg[seg == 0] = i
    spf_l = spf.tolist()

    def odd_divisors(x: int) -> list[int]:
        ds = [1]
        while x > 1:
            p = spf_l[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if p != 2:
                ds = [a * p**i for a in ds for i in range(1, e + 1)] + ds
        return ds

    total = 0
    prev_odd = odd_divisors(2)
    for n in range(3, n_max + 1):
        cur_odd = odd_divisors(n)
        prod = n * (n - 1)
        v = (prod & -prod).bit_length() - 1
        s = 0
        cnt = 0
        for o1 in cur_odd:
            for o2 in prev_odd:
                o = o1 * o2
                if o > n:
                    s += o
                    cnt += 1
                oe = o << v
                if oe > n:
                    s += oe
                    cnt += 1
        total += s - cnt * n
        prev_odd = cur_odd
    return total


def sequence_indices(n: int, m_max: int) -> list[int]:
    out = []
    a = n
    for m in range(1, m_max):
        a += n + m
        if a % (n + m) == 0:
            out.append(m)
    return out


def qualifying_indices(n: int) -> list[int]:
    prod = n * (n - 1)
    v = (prod & -prod).bit_length() - 1
    odd = prod >> v
    ds = [1]
    x = odd
    d = 3
    fac: dict[int, int] = {}
    while d * d <= x:
        while x % d == 0:
            fac[d] = fac.get(d, 0) + 1
            x //= d
        d += 2
    if x > 1:
        fac[x] = fac.get(x, 0) + 1
    for p, e in fac.items():
        ds = [a * p**i for a in ds for i in range(e + 1)]
    full = ds + [a << v for a in ds]
    return sorted(d - n for d in full if d > n)


def main() -> None:
    for n in (7, 10, 33, 64, 100, 255):
        assert qualifying_indices(n) == sequence_indices(n, 10**6 // 2)
    assert sum(qualifying_indices(10)) == 148
    assert sum(qualifying_indices(100)) == 21828
    assert grand_total(100) == 612572
    print(grand_total(1234567))  # 1254404167198752370


if __name__ == "__main__":
    main()
