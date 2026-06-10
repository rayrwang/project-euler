from functools import lru_cache
from itertools import product

import numba
import numpy as np


def _base_digits(n: int, b: int) -> list[int]:
    d = []
    while n:
        d.append(n % b)
        n //= b
    return d if d else [0]


def _count_not_divisible(m: int, n: int, p: int) -> int:
    """Count i in [0, m) for which C(i, n) is NOT divisible by the prime p.

    By Kummer's theorem C(i, n) is divisible by p iff adding n to (i - n) in base
    p produces a carry; equivalently C(i, n) is coprime to p iff every base-p
    digit of n is <= the corresponding digit of i (Lucas' theorem). So this is a
    digit DP over base p counting i < m whose every digit dominates n's.
    """
    if m <= 0:
        return 0
    du = _base_digits(m - 1, p)
    dn = _base_digits(n, p)
    length = max(len(du), len(dn))
    du += [0] * (length - len(du))
    dn += [0] * (length - len(dn))

    @lru_cache(maxsize=None)
    def go(pos: int, tight: bool) -> int:
        if pos < 0:
            return 1
        hi = du[pos] if tight else p - 1
        total = 0
        for d in range(dn[pos], hi + 1):
            total += go(pos - 1, tight and d == hi)
        return total

    return go(length - 1, True)


@numba.njit
def _count_supermask(rs: np.ndarray, n: int, p5: int, m: int) -> int:
    # For each fixed low residue r (= i mod 5^k, chosen so the base-5 digits already
    # dominate n), sweep the high part h with i = h*5^k + r < m and keep those i that
    # are binary supermasks of n -- the base-2 non-divisibility condition (i & n) == n.
    total = 0
    for idx in range(len(rs)):
        r = rs[idx]
        hmax = (m - 1 - r) // p5
        for h in range(hmax + 1):
            i = h * p5 + r
            if (i & n) == n:
                total += 1
    return total


def _count_not_divisible_both(m: int, n: int) -> int:
    """Count i in [0, m) for which C(i, n) is divisible by neither 2 nor 5.

    Non-divisibility by 5 depends only on i mod 5^k (k chosen with 5^k > n), since
    only n's base-5 digits constrain i; enumerate the residues r whose base-5
    digits dominate n's. Non-divisibility by 2 is the binary-supermask condition
    (i & n) == n. For n = 10^12 - 10 most base-5 digits of n are 4 (forced), so
    only a few thousand residues r survive, and the high sweep is short.
    """
    k = 1
    while 5**k <= n:
        k += 1
    p5 = 5**k
    d5 = _base_digits(n, 5)
    d5 += [0] * (k - len(d5))
    residues = []
    for combo in product(*[range(d5[j], 5) for j in range(k)]):
        r = 0
        for j in range(k - 1, -1, -1):
            r = r * 5 + combo[j]
        residues.append(r)
    return _count_supermask(np.array(residues, dtype=np.int64), n, p5, m)


def T(m: int, n: int) -> int:
    """Number of binomial coefficients C(i, n) divisible by 10 for n <= i < m.

    C(i, n) is divisible by 10 iff divisible by both 2 and 5, so by inclusion-
    exclusion the count equals (total) - (not by 2) - (not by 5) + (not by either).
    The digit-domination conditions force i >= n, so counting over [0, m) is the
    same as over [n, m).
    """
    a2 = _count_not_divisible(m, n, 2)
    a5 = _count_not_divisible(m, n, 5)
    a10 = _count_not_divisible_both(m, n)
    return (m - n) - a2 - a5 + a10


if __name__ == "__main__":
    # Given checkpoint: T(10^9, 10^7 - 10) = 989697000.
    assert T(10**9, 10**7 - 10) == 989697000
    print(T(10**18, 10**12 - 10))  # 999998760323313995
