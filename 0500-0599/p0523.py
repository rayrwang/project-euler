"""Project Euler Problem 523: First Sort I.

The sort repeatedly finds the first out-of-order adjacent pair and moves the
smaller element of the pair to the front of the list, restarting the scan.
E(n) is the expected number of moves over a random permutation of 1..n;
find E(30) to two decimal places.

Moving an element to the front never changes the relative order of the other
elements, and the smaller member of any processed descent involving an
element below k only relocates elements below k.  Since the scan's prefix up
to the first descent is increasing, the small elements in it sit before all
larger ones and never separate two elements >= k.  So the process acts on the
subsequence of elements >= k exactly as it would on that pattern alone, where
k is its minimum: the number of moves of element k in S_n is distributed as
the number of moves of the minimum in a uniform permutation of size
m = n - k + 1.  Therefore E(n) = sum_{m=1}^{n} h(m) with h(m) the expected
number of moves of the minimum, and

    h(m) = (2^(m-1) - 1) / m,

verified below by running the algorithm on every permutation for all n <= 8
(which checks h(m) for m <= 8 via h(m) = E(m) - E(m-1)) and against the
given E(4) = 3.25 and E(10) = 115.725.  E(30) is computed with exact
rational arithmetic.
"""

from fractions import Fraction
from itertools import permutations
from math import factorial


def F(perm: tuple[int, ...]) -> int:
    """Number of moves the algorithm makes to sort perm."""
    lst = list(perm)
    moves = 0
    while True:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst.insert(0, lst.pop(i + 1))
                moves += 1
                break
        else:
            return moves


def E(n: int) -> Fraction:
    return sum((Fraction(2 ** (m - 1) - 1, m) for m in range(1, n + 1)), Fraction(0))


if __name__ == "__main__":
    for n in range(1, 9):
        total = sum(F(p) for p in permutations(range(1, n + 1)))
        assert Fraction(total, factorial(n)) == E(n), n
    assert E(4) == Fraction(13, 4), E(4)  # 3.25
    assert E(10) == Fraction(4629, 40), E(10)  # 115.725
    cents = round(E(30) * 100)
    print(f"{cents // 100}.{cents % 100:02d}")  # 37125450.44
