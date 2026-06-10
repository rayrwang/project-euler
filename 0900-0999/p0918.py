"""Project Euler 918: Recursive Sequence Summation.

Pairing consecutive terms telescopes the sum:
a_{2n} + a_{2n+1} = 2 a_n + a_n - 3 a_{n+1} = 3 (a_n - a_{n+1}), so

    S(2M + 1) = a_1 + sum_{n=1}^{M} (a_{2n} + a_{2n+1})
              = 1 + 3 (a_1 - a_{M+1}) = 4 - 3 a_{M+1},
    S(2M)     = S(2M + 1) - a_{2M+1} = 4 - 3 a_{M+1} - (a_M - 3 a_{M+1})
              = 4 - a_M.

This reproduces the given S(10) = 4 - a_5 = 4 - 17 = -13.  A single
term a_n follows by binary descent on the pair (a_k, a_{k+1}):
(a_{2n}, a_{2n+1}) = (2 a_n, a_n - 3 a_{n+1}) and
(a_{2n+1}, a_{2n+2}) = (a_n - 3 a_{n+1}, 2 a_{n+1}), so
S(10^12) = 4 - a_{5 * 10^11} costs O(log N) integer operations.  Both
the closed form for S and the descent are verified against a direct
table of the first 800 terms.
"""

import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


@lru_cache(maxsize=None)
def pair(k: int) -> tuple[int, int]:
    """(a_k, a_{k+1})."""
    if k == 1:
        return (1, 2)
    n, r = divmod(k, 2)
    an, an1 = pair(n)
    if r == 0:
        return (2 * an, an - 3 * an1)
    return (an - 3 * an1, 2 * an1)


def s_sum(n: int) -> int:
    if n % 2 == 0:
        return 4 - pair(n // 2)[0]
    if n == 1:
        return 1
    return 4 - 3 * pair(n // 2 + 1)[0]


if __name__ == "__main__":
    m = 400
    vals = [0] * (2 * m + 2)
    vals[1] = 1
    for n in range(1, m + 1):
        vals[2 * n] = 2 * vals[n]
        vals[2 * n + 1] = vals[n] - 3 * vals[n + 1]
    assert vals[1:11] == [1, 2, -5, 4, 17, -10, -17, 8, -47, 34]
    for n in range(1, 2 * m):
        assert pair(n)[0] == vals[n], n
    prefix = 0
    for n in range(1, 2 * m):
        prefix += vals[n]
        assert s_sum(n) == prefix, n
    assert s_sum(10) == -13
    print(s_sum(10**12))  # -6999033352333308
