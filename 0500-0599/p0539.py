"""Project Euler Problem 539: Odd Elimination.

From the list 1..n, repeatedly delete every other number, sweeping left to
right first (removing 1, 3, 5, ...), then right to left, alternating until one
number P(n) remains.  S(n) = sum_{k=1}^n P(k).  Find S(10^18) mod 987654321.

The first sweep leaves the evens 2, 4, ..., 2*floor(n/2) and the process
continues right-to-left on a list of length m = floor(n/2).  The whole
remaining process is the mirror image of the original one, so it ends on the
element in mirrored position m + 1 - P(m), giving

    P(n) = 2 * (floor(n/2) + 1 - P(floor(n/2))),    P(1) = 1,

which reproduces P(9) = 6 and P(1000) = 510.  Summing the recurrence over
k = 2..N and grouping k = 2m with k = 2m+1 (both have floor(k/2) = m) turns
the sum of P into sums of m and of P(m) over m <= floor(N/2) and
m <= floor((N-1)/2):

    S(N) = 1 + 2(N-1) + 2*[T(a) + T(b)] - 2*[S(a) + S(b)],

with a = floor(N/2), b = floor((N-1)/2) and T(M) = M(M+1)/2.  The arguments
reachable by repeatedly halving stay within O(log^2 N) distinct values, so a
memoised recursion is instant; all arithmetic is exact Python ints and the
result is reduced mod 987654321 at the end.  S(1000) = 268271 is the check.
"""

import sys
from functools import cache

MOD = 987654321


@cache
def P(n: int) -> int:
    if n <= 1:
        return n
    return 2 * (n // 2 + 1 - P(n // 2))


@cache
def S(n: int) -> int:
    if n <= 1:
        return n

    def T(m: int) -> int:
        return m * (m + 1) // 2

    a, b = n // 2, (n - 1) // 2
    return 1 + 2 * (n - 1) + 2 * (T(a) + T(b)) - 2 * (S(a) + S(b))


def P_simulated(n: int) -> int:
    nums = list(range(1, n + 1))
    left_to_right = True
    while len(nums) > 1:
        if left_to_right:
            nums = nums[1::2]
        else:
            nums = nums[-2::-2][::-1]
        left_to_right = not left_to_right
    return nums[0]


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    for k in range(1, 200):
        assert P(k) == P_simulated(k), k
    assert P(1) == 1, P(1)
    assert P(9) == 6, P(9)
    assert P(1000) == 510, P(1000)
    assert S(1000) == sum(P(k) for k in range(1, 1001)) == 268271, S(1000)
    print(S(10**18) % MOD)  # 426334056
