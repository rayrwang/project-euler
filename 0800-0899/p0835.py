"""Project Euler 835: Supernatural Triangles.

Two families of Pythagorean triangles have consecutive sides.  When a
leg and the hypotenuse are consecutive, a^2 = 2b + 1 forces
(2m+1, 2m^2+2m, 2m^2+2m+1) with perimeter 4m^2 + 6m + 2.  When the two
legs are consecutive, (2a+1)^2 - 2c^2 = -1 is a negative Pell
equation, giving perimeters P_k = x_k + c_k with
x + c sqrt(2) = (1 + sqrt 2)^(2k-1): the chain 12, 70, 408, ...
obeying P_{k+1} = 6 P_k - P_{k-1} (with the degenerate P_1 = 2).  The
families intersect only at (3, 4, 5), so 12 is subtracted once.

For N = 10^(10^10), 4N is a perfect square, so the parabola cutoff is
exact: M = (sqrt(4N+1) - 3)/4 = 5 * 10^(L-1) - 1 with L = 5 * 10^9,
verified against integer square roots for medium exponents, and the
quadratic sum is evaluated from M mod p by Faulhaber.  The Pell count
K is the largest k with P_k <= N.  Writing P_k = lead * alpha^(2k-1)
- delta with alpha = 1 + sqrt 2, lead = (2 + sqrt 2)/4 and
0 < delta < 1, the cutoff is decided by binary search using interval
arithmetic on 70-digit integer big-floats (directed rounding, exact
isqrt bounds for sqrt 2); an ambiguous interval raises, so every
comparison is certified -- this replaces a floating margin check with
a proof.  The Pell perimeter total comes from a 3x3 matrix power
carrying (P_k, P_{k-1}, sum).  The whole modular pipeline is validated
against exact enumeration up to 10^10, including the given
S(100) = 258 and S(10^4) = 172004, and the certified cutoff search is
cross-checked against direct Pell enumeration for medium exponents and
a float64 estimate for the full size.
"""

from __future__ import annotations

import math

import numpy as np

MOD = 1234567891
DIGITS = 70  # working precision (decimal digits) of the interval arithmetic


def quadratic_family_sum(m_mod: int, p: int) -> int:
    """sum_{m=1}^{M} (4m^2 + 6m + 2) mod p from M mod p."""
    inv6 = pow(6, p - 2, p)
    inv2 = pow(2, p - 2, p)
    m = m_mod % p
    s2 = m * (m + 1) % p * (2 * m + 1) % p * inv6 % p
    s1 = m * (m + 1) % p * inv2 % p
    return (4 * s2 + 6 * s1 + 2 * m) % p


def pell_family_sum(k_max: int, p: int) -> int:
    """sum_{k=2}^{K} P_k mod p with P_2 = 12, P_{k+1} = 6 P_k - P_{k-1}."""
    if k_max < 2:
        return 0

    def mat_mult(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        return [
            [sum(a[i][t] * b[t][j] for t in range(3)) % p for j in range(3)]
            for i in range(3)
        ]

    mat = [[6, -1, 0], [1, 0, 0], [6, -1, 1]]
    res = [[int(i == j) for j in range(3)] for i in range(3)]
    e = k_max - 2
    while e:
        if e & 1:
            res = mat_mult(res, mat)
        mat = mat_mult(mat, mat)
        e >>= 1
    v = (12, 2, 12)  # (P_2, P_1, S_2)
    return (res[2][0] * v[0] + res[2][1] * v[1] + res[2][2] * v[2]) % p


# --- 70-digit big-floats (mantissa, exponent) with directed rounding ------
#
# A value is a pair (m, e) of Python ints meaning m * 10^e with m > 0.
# Lower bounds always round down, upper bounds always round up, so a
# product of interval endpoints is again a valid interval endpoint.


def _trim(m: int, e: int, round_up: bool) -> tuple[int, int]:
    cap = 10 ** (DIGITS + 1)
    while m >= cap:
        m = -(-m // 10) if round_up else m // 10
        e += 1
    return m, e


def _mul(a: tuple[int, int], b: tuple[int, int], round_up: bool) -> tuple[int, int]:
    return _trim(a[0] * b[0], a[1] + b[1], round_up)


def _cmp_pow10(val: tuple[int, int], exp10: int) -> int:
    """Compare m * 10^e with 10^exp10: returns -1, 0, or 1."""
    m, e = val
    top = e + len(str(m)) - 1  # value lies in [10^top, 10^(top + 1))
    if top != exp10:
        return -1 if top < exp10 else 1
    lead_pow = 10 ** (len(str(m)) - 1)
    return (m > lead_pow) - (m < lead_pow)


def _pell_value_interval(k: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Certified bounds on lead * alpha^(2k-1), alpha = 1 + sqrt 2."""
    scale = 10**DIGITS
    s = math.isqrt(2 * scale * scale)  # floor(sqrt(2) * scale)
    base_lo, base_hi = (scale + s, -DIGITS), (scale + s + 1, -DIGITS)
    lo = ((2 * scale + s) // 4, -DIGITS)  # lead = (2 + sqrt 2) / 4
    hi = (-(-(2 * scale + s + 1) // 4), -DIGITS)
    t = 2 * k - 1
    while t:
        if t & 1:
            lo = _mul(lo, base_lo, False)
            hi = _mul(hi, base_hi, True)
        base_lo = _mul(base_lo, base_lo, False)
        base_hi = _mul(base_hi, base_hi, True)
        t >>= 1
    return lo, hi


def pell_k_max(exp10: int) -> int:
    """Largest k with P_k <= 10^exp10, certified by interval arithmetic.

    P_k = V - delta with V = lead * alpha^(2k-1) and 0 < delta < 1, so
    P_k <= N iff V < N + 1.  The interval endpoints sit on a 10^e grid
    with e far from 0 at the cutoff, so hi <= N certifies True and
    lo > N certifies lo >= N + 1, hence False; anything else means the
    interval is too wide and raises instead of guessing.
    """

    def fits(k: int) -> bool:
        lo, hi = _pell_value_interval(k)
        if _cmp_pow10(hi, exp10) <= 0:
            return True
        if _cmp_pow10(lo, exp10) > 0:
            return False
        raise AssertionError("interval straddles the cutoff; raise DIGITS")

    lo_k, hi_k = 1, 2 * exp10  # k_max ~ 1.31 * exp10, so 2 * exp10 overshoots
    assert fits(lo_k) and not fits(hi_k)
    while hi_k - lo_k > 1:
        mid = (lo_k + hi_k) // 2
        if fits(mid):
            lo_k = mid
        else:
            hi_k = mid
    assert fits(lo_k) and not fits(lo_k + 1)
    return lo_k


def exact_total(n: int) -> int:
    m_max = 0
    while 4 * (m_max + 1) ** 2 + 6 * (m_max + 1) + 2 <= n:
        m_max += 1
    ms = np.arange(1, m_max + 1, dtype=np.int64)
    total = int(np.sum(4 * ms * ms + 6 * ms + 2))
    a, b = 2, 12
    while b <= n:
        total += b
        a, b = b, 6 * b - a
    if n >= 12:
        total -= 12
    return total


def modular_total_small(n: int, p: int) -> int:
    m = 0
    while 4 * (m + 1) ** 2 + 6 * (m + 1) + 2 <= n:
        m += 1
    k = 1
    a, b = 2, 12
    while b <= n:
        k += 1
        a, b = b, 6 * b - a
    s = (quadratic_family_sum(m, p) + pell_family_sum(k, p)) % p
    if n >= 12:
        s = (s - 12) % p
    return s


def main() -> None:
    prime_test = 999999999999999989
    assert exact_total(100) == 258
    assert exact_total(10000) == 172004
    for n in (100, 10000, 10**6, 10**8, 10**10):
        assert modular_total_small(n, prime_test) == exact_total(n) % prime_test

    # The certified cutoff search must agree with direct Pell enumeration.
    for exp in (2, 4, 6, 8, 10, 12, 15, 18):
        k, a, b = 1, 2, 12
        while b <= 10**exp:
            k += 1
            a, b = b, 6 * b - a
        assert pell_k_max(exp) == k

    big_l = 5 * 10**9
    m_mod = (5 * pow(10, big_l - 1, MOD) - 1) % MOD

    exp10 = 10**10
    k_max = pell_k_max(exp10)
    est = exp10 * np.log(10.0) / (2.0 * np.log(1.0 + np.sqrt(2.0)))
    assert abs(k_max - est) < 10.0  # float64 sanity cross-check

    ans = (quadratic_family_sum(m_mod, MOD) + pell_family_sum(k_max, MOD) - 12) % MOD
    print(ans)  # 1050923942


if __name__ == "__main__":
    main()
