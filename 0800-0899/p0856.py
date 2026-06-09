from fractions import Fraction
from functools import cache


@cache
def _expect(c1: int, c2: int, c3: int, c4: int, j: int) -> Fraction:
    """Expected further draws; c_i ranks have i cards left, last rank has j.

    The c_i include the last drawn card's rank (which sits in class j).
    Drawing one of the j matching cards ends the process; any other card
    moves its rank from class i to class i - 1 and becomes the new last.
    """
    remaining = c1 + 2 * c2 + 3 * c3 + 4 * c4
    if remaining == 0:
        return Fraction(0)
    total = Fraction(1)  # the next draw always happens
    cs = (c1, c2, c3, c4)
    for i in (1, 2, 3, 4):
        avail = i * cs[i - 1] - (j if i == j else 0)
        if avail == 0:
            continue
        nxt = list(cs)
        nxt[i - 1] -= 1
        if i >= 2:
            nxt[i - 2] += 1
        total += Fraction(avail, remaining) * _expect(*nxt, i - 1)
    return total


def expected_draws() -> Fraction:
    # First draw: no rank to pair with; 13 ranks of 4 cards each.
    return 1 + _expect(0, 0, 1, 12, 3)


if __name__ == "__main__":
    # Check the recursion on a tiny deck (2 ranks x 2 cards): direct
    # enumeration of the 6 arrangements gives expectation 18/6 = 3.
    assert 1 + _expect(1, 1, 0, 0, 1) == 3
    e = expected_draws()
    print(f"{float(e):.8f}")  # 17.09661501
