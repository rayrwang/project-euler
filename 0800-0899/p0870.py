from fractions import Fraction
from functools import lru_cache

import numba
import numpy as np

# By Schwenk's theorem for take-away games with constraint f(m) = floor(r m),
# the losing pile sizes are generated greedily: a_1 = 1 and
# a_(i+1) = a_i + a_j, where j = j(i) is least with floor(r a_j) >= a_i
# (the sequence stops if no j works, which happens exactly for r < 1).
# This is validated below against a direct game solver.  For r = p/q + eps
# the choice conditions read p a_j >= q a_i exactly, and as r increases the
# first decision to change is some j(i) dropping to j(i) - 1, which happens
# at r = a_i / a_(j(i)-1).  The next transition above p/q is therefore the
# minimum of those ratios — one candidate per j, taken at the first i of its
# block — and the whole transition list is enumerated by walking upward.
# Relevant candidates come from the linear ramp and the first growth rounds
# of the sequence, with values O(r^3); the scan window a_i <= 64 r^3 is
# verified by recomputing every answer with a window four times larger.

TARGET = 123456


@numba.njit(cache=True)
def next_transition(p, q, mult):
    """Smallest boundary above p/q, scanning while a_i <= mult * r^3."""
    r = p / q
    cap = np.int64(mult * r * r * r) + 1000
    a = np.empty(1 << 22, dtype=np.int64)
    a[0] = 1
    m = 1
    j = 0
    hp = np.int64(-1)
    hq = np.int64(1)
    while True:
        ai = a[m - 1]
        if ai > cap:
            break
        while j < m and p * a[j] < q * ai:
            j += 1
        if j >= m:
            return np.int64(-2), np.int64(1)  # r < 1: sequence terminates
        if j >= 1 and (hp < 0 or ai * hq < hp * a[j - 1]):
            hp, hq = ai, a[j - 1]
        if m >= a.shape[0]:
            return np.int64(-3), np.int64(1)
        a[m] = ai + a[j]
        m += 1
    return hp, hq


def walk(count: int, mult: float) -> tuple:
    p, q = 1, 1  # T(1) = 1
    for _ in range(count - 1):
        hp, hq = next_transition(p, q, mult)
        assert hp > 0
        g = np.gcd(hp, hq)
        p, q = int(hp // g), int(hq // g)
        cap = 128.0 * (p / q) ** 3  # values stay below ~2*cap
        assert cap * cap < 2.0**62 and p * cap < 2.0**62  # int64 safety
    return p, q


def schwenk_sequence(r: Fraction, limit: int) -> list[int]:
    a = [1]
    while a[-1] < limit:
        j = 0
        while j < len(a) and (r * a[j]).__floor__() < a[-1]:
            j += 1
        if j >= len(a):
            break
        a.append(a[-1] + a[j])
    return [v for v in a if v <= limit]


def losing_by_game(r: Fraction, limit: int) -> list[int]:
    """Direct minimax over (stones, take-limit) positions."""

    @lru_cache(maxsize=None)
    def wins(n: int, m: int) -> bool:
        for k in range(1, min(n, m) + 1):
            if not wins(n - k, (r * k).__floor__()):
                return True
        return False

    return [n for n in range(1, limit + 1) if not wins(n, n - 1)]


if __name__ == "__main__":
    for r in (
        Fraction(1, 2),
        Fraction(1),
        Fraction(3, 2),
        Fraction(2),
        Fraction(7, 3),
        Fraction(145, 23),
        Fraction(146, 23),
    ):
        assert schwenk_sequence(r, 55) == losing_by_game(r, 55), r
    assert losing_by_game(Fraction(2), 8) == [1, 2, 3, 5, 8]  # given L(2)

    p, q = walk(22, 64.0)
    assert (p, q) == (145, 23)  # given T(22) = 6.3043478261...

    p, q = walk(TARGET, 64.0)
    assert walk(TARGET, 256.0) == (p, q)  # window-size independence
    scaled = p * 10**10
    val = scaled // q + (1 if 2 * (scaled % q) >= q else 0)
    s = str(val)
    print(s[:-10] + "." + s[-10:])  # 229.9129353234
