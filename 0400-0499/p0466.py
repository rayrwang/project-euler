import sys
from math import gcd

sys.setrecursionlimit(10000)

def table_distinct(r: int, n: int) -> int:
    """P(r, n): distinct entries of the r x n multiplication table.

    The table's values are the union of A_i = {i j : j <= n}, and an
    intersection over a set S is the multiples of lcm(S) up to
    n * min(S), so inclusion-exclusion gives
        P = sum_{S != {}} (-1)^(|S|+1) floor(n min(S) / lcm(S)).
    Group subsets by their minimum m and search the rest depth-first.
    Two prunes make this tractable: if the current lcm L already exceeds
    n m, every deeper floor is zero and the alternating sum vanishes;
    and if the next element i divides L, the subsets with and without i
    pair up with equal lcm and opposite signs, cancelling the entire
    subtree. Memoisation on (i, L) per m finishes the job.
    """
    total = 0
    for m in range(1, r + 1):
        bound = n * m
        memo: dict[tuple[int, int], int] = {}

        def g(i: int, lcm_v: int) -> int:
            if lcm_v > bound:
                return 0
            if i > r:
                return bound // lcm_v
            if lcm_v % i == 0:
                return 0
            key = (i, lcm_v)
            if key in memo:
                return memo[key]
            res = g(i + 1, lcm_v) - g(i + 1, lcm_v * i // gcd(lcm_v, i))
            memo[key] = res
            return res

        total += g(m + 1, m)
    return total

def brute(r: int, n: int) -> int:
    return len({i * j for i in range(1, r + 1) for j in range(1, n + 1)})

if __name__ == "__main__":
    assert table_distinct(3, 4) == brute(3, 4) == 8  # given
    assert table_distinct(7, 50) == brute(7, 50)
    assert table_distinct(64, 64) == brute(64, 64) == 1263  # given
    assert table_distinct(12, 345) == brute(12, 345) == 1998  # given
    assert table_distinct(32, 10**15) == 13826382602124302  # given
    print(table_distinct(64, 10**16))  # 258381958195474745
