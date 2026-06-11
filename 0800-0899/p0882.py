import random
from fractions import Fraction
from functools import lru_cache
from math import ceil, floor

# This is a partisan game under normal play: Dr. One (Left) deletes a 1-digit,
# Dr. Zero (Right) deletes a 0-digit, leading zeros evaporate.  A skip is a
# move in a spare component {|0} = -1 that only Right can use, so Dr. Zero
# (moving second) wins with s skips iff  G - s <= 0,  where G is the game
# value of the starting collection.  Every single-number position turns out
# to be a surreal *number* (each Left option is strictly below each Right
# option, asserted during the computation), so values add across the
# collection, G is a dyadic rational, and
#     S(n) = ceil( sum_v  v * G(v) ).
# The value of a binary string follows from the simplicity rule applied to
# its one-digit-deleted options; all strings of <= 17 digits are memoised,
# e.g. G("1") = 1, G("10") = {0 | 1} = 1/2, G("11") = 2, G("100") = 1/4,
# G("101") = {1 | 2} = 3/2.

N = 10**5


def simplest_between(lo, hi):
    """Simplest dyadic strictly between lo and hi (None = unbounded)."""
    if lo is None and hi is None:
        return Fraction(0)
    if hi is None:
        return Fraction(max(0, floor(lo) + 1))
    if lo is None:
        return Fraction(min(0, ceil(hi) - 1))
    assert lo < hi
    if lo < 0 < hi:
        return Fraction(0)
    if floor(lo) + 1 < hi:  # an integer fits; take the one closest to zero
        return Fraction(floor(lo) + 1 if lo >= 0 else ceil(hi) - 1)
    k = 1
    while True:
        num = floor(lo * (1 << k)) + 1
        f = Fraction(num, 1 << k)
        if lo < f < hi:
            return f
        k += 1


@lru_cache(maxsize=None)
def value(s: str) -> Fraction:
    """Game value of a binary string position (Left deletes 1s, Right 0s)."""
    if not s:
        return Fraction(0)
    left, right = [], []
    for i, ch in enumerate(s):
        rest = (s[:i] + s[i + 1 :]).lstrip("0")
        (left if ch == "1" else right).append(value(rest))
    lo = max(left) if left else None
    hi = min(right) if right else None
    return simplest_between(lo, hi)


def s_of(numbers: list[int]) -> int:
    total = sum(value(bin(v)[2:]) for v in numbers)
    return max(0, ceil(total))


def s_problem(n: int) -> int:
    return ceil(sum(v * value(bin(v)[2:]) for v in range(1, n + 1)))


def brute(numbers: list[int]) -> int:
    """Direct minimax: minimal skip budget for Dr. Zero to win."""

    @lru_cache(maxsize=None)
    def f_one(state: tuple) -> int:
        best = -1
        for idx, s in enumerate(state):
            for i, ch in enumerate(s):
                if ch == "1":
                    t = (s[:i] + s[i + 1 :]).lstrip("0")
                    ns = list(state)
                    if t:
                        ns[idx] = t
                    else:
                        ns.pop(idx)
                    best = max(best, f_zero(tuple(sorted(ns))))
        return 0 if best < 0 else best

    @lru_cache(maxsize=None)
    def f_zero(state: tuple) -> int:
        best = 1 + f_one(state)  # skip
        for idx, s in enumerate(state):
            for i, ch in enumerate(s):
                if ch == "0":
                    ns = list(state)
                    ns[idx] = s[:i] + s[i + 1 :]
                    best = min(best, f_one(tuple(sorted(ns))))
        return best

    return f_one(tuple(sorted(bin(v)[2:] for v in numbers)))


if __name__ == "__main__":
    for n, expect in [(2, 2), (5, 17), (10, 64)]:  # given
        assert s_problem(n) == expect
    for n in range(1, 6):
        nums = [v for v in range(1, n + 1) for _ in range(v)]
        assert brute(nums) == s_problem(n)
    rng = random.Random(2)
    for _ in range(25):
        nums = [rng.randint(1, 12) for _ in range(rng.randint(1, 5))]
        assert brute(nums) == s_of(nums), nums
    print(s_problem(N))  # 15800662276
