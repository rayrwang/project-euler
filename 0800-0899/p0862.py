from itertools import combinations_with_replacement
from math import factorial


def s(k: int) -> int:
    """Sum of T(n) over all k-digit numbers n.

    Group numbers by their digit multiset.  If a multiset can be arranged
    into m distinct valid k-digit numbers (no leading zero), then every
    unordered pair of them contributes exactly 1 to the T value of the
    smaller, so the multiset contributes m * (m - 1) / 2 in total.
    """
    total = 0
    fk, fk1 = factorial(k), factorial(k - 1)
    for digits in combinations_with_replacement(range(10), k):
        counts = [0] * 10
        for d in digits:
            counts[d] += 1
        denom = 1
        for c in counts:
            denom *= factorial(c)
        m = fk // denom
        if counts[0]:
            # arrangements with a leading zero
            m -= fk1 * counts[0] // denom
        total += m * (m - 1) // 2
    return total


if __name__ == "__main__":
    assert s(3) == 1701
    print(s(12))  # 6111397420935766740
