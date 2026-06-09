"""Project Euler Problem 601: Divisibility streaks.

streak(n) = smallest k >= 1 with (k+1) not dividing (n+k).  Since n+k divisible by
k+1 means n == 1 (mod k+1), we have

    streak(n) >= s  <=>  n == 1 (mod j) for j = 2, 3, ..., s  <=>  n == 1 (mod L_s),

where L_s = lcm(1, 2, ..., s).  Therefore, counting 1 < n < N,

    P(s, N) = floor((N-2)/L_s) - floor((N-2)/L_{s+1}).

The answer is sum_{i=1}^{31} P(i, 4^i).  Checks: P(3,14)=1 and P(6,10^6)=14286.
"""

from math import lcm


def P(s: int, N: int) -> int:
    Ls = lcm(*range(1, s + 1))
    Ls1 = lcm(*range(1, s + 2))
    return (N - 2) // Ls - (N - 2) // Ls1


if __name__ == "__main__":
    assert P(3, 14) == 1, P(3, 14)
    assert P(6, 10**6) == 14286, P(6, 10**6)
    print(sum(P(i, 4**i) for i in range(1, 32)))  # 1617243
