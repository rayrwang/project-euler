"""Project Euler 961: Removing Digits.

Digit values do not matter, only whether each digit is zero: the legal moves
and the winning condition (removing the last nonzero digit) depend only on
the zero/nonzero pattern. Removing the leading nonzero digit additionally
strips the run of zeros that follows it; removing a zero deletes just that
zero. So the game is solved by memoised search over binary patterns starting
with a nonzero -- there are only 2^17 patterns for up to 18 digits.

A d-digit pattern with k nonzero positions corresponds to exactly 9^k
integers, so W(10^18) is the sum of 9^k over winning patterns of length 1
to 18. The naive (k, #zeros) classification fails -- e.g. some (3, 1)
patterns win and others lose -- but the pattern game agrees with full
brute force over actual integers: W(100) = 18, W(10^4) = 1656,
W(10^5) = 91656.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def wins(s: str) -> bool:
    """Pattern over 'n'/'z' (starts with 'n'). Does the player to move win?"""
    k = s.count("n")
    for i in range(len(s)):
        if s[i] == "n":
            if k == 1:
                return True
            t = (s[:i] + s[i + 1 :]).lstrip("z")
        else:
            t = s[:i] + s[i + 1 :]
        if not wins(t):
            return True
    return False


def solve(max_digits: int) -> int:
    total = 0
    for d in range(1, max_digits + 1):
        for mask in range(1 << (d - 1)):
            s = "n" + "".join("z" if (mask >> j) & 1 else "n" for j in range(d - 1))
            if wins(s):
                total += 9 ** s.count("n")
    return total


if __name__ == "__main__":
    print(solve(18))  # 166666666689036288
