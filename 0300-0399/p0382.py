import sys
from functools import lru_cache

MOD = 10**9

# B(m) (the count of non-polygon subsets whose maximum is the m-th stick) obeys this
# order-9 linear recurrence, found from exactly computed values and verified on dozens more:
#   B(m) = 4 B(m-1) - 5 B(m-2) + 4 B(m-3) - 7 B(m-4) + 6 B(m-5) + 2 B(m-7) - 5 B(m-8) + 2 B(m-9).
_REC = [4, -5, 4, -7, 6, 0, 2, -5, 2]
_ORDER = len(_REC)


def _sticks(count: int) -> list[int]:
    s = [1, 2, 3]
    while len(s) < count:
        s.append(s[-1] + s[-3])
    return s


def _bad_counts(upto: int) -> list[int]:
    """B(m) for m = 3..upto: the number of subsets T of {s_1,...,s_{m-1}} with |T| >= 2 and
    sum(T) <= s_m. With the m-th stick as the (strict) maximum these are exactly the size->=3
    subsets that fail the polygon inequality max < sum of the rest."""
    s = _sticks(upto)
    prefix = [0] * upto
    for k in range(1, upto):
        prefix[k] = prefix[k - 1] + s[k - 1]

    result = []
    for m in range(3, upto + 1):

        @lru_cache(maxsize=None)
        def subsets_within(k: int, budget: int) -> int:
            # number of subsets of {s_1,...,s_k} with sum <= budget
            if budget < 0:
                return 0
            if k == 0:
                return 1
            if budget >= prefix[k]:
                return 1 << k
            return subsets_within(k - 1, budget) + subsets_within(k - 1, budget - s[k - 1])

        total = subsets_within(m - 1, s[m - 1])
        subsets_within.cache_clear()
        result.append(total - 1 - (m - 1))  # drop the empty set and the m-1 singletons
    return result


def _mat_mult(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n, p, q = len(a), len(b), len(b[0])
    out = [[0] * q for _ in range(n)]
    for i in range(n):
        row = a[i]
        for k in range(p):
            v = row[k]
            if v:
                bk = b[k]
                oi = out[i]
                for j in range(q):
                    oi[j] = (oi[j] + v * bk[j]) % MOD
    return out


def _mat_pow(m: list[list[int]], e: int) -> list[list[int]]:
    n = len(m)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while e:
        if e & 1:
            result = _mat_mult(result, m)
        m = _mat_mult(m, m)
        e >>= 1
    return result


def solve(n: int = 10**18) -> int:
    """Last 9 digits of f(n): the number of subsets of U_n = {s_1,...,s_n} (with
    s_i = s_{i-1} + s_{i-3}, s_1..s_3 = 1,2,3) that can form a polygon, i.e. that
    have at least three sticks and whose largest stick is shorter than the sum of
    the others.

    Splitting off the size->=3 subsets, f(n) = (2^n - 1 - n - C(n,2)) - sum_{m=3}^n
    B(m), where B(m) counts the failures whose maximum is s_m. The B sequence
    satisfies a fixed order-9 linear recurrence (its characteristic structure comes
    from the s_i recurrence x^3 = x^2 + 1), so its running total is advanced to
    n = 10^18 by matrix exponentiation modulo 10^9. The given f(5) = 7,
    f(10) = 501 and f(25) = 18635853 confirm the setup.
    """
    sys.setrecursionlimit(10000)
    base = max(2 * _ORDER + 3, 11)
    bad = _bad_counts(base)  # bad[i] = B(i + 3)

    # State [B(m), B(m-1), ..., B(m-8), S(m)] with S the running sum of B; advance one step.
    dim = _ORDER + 1
    transition = [[0] * dim for _ in range(dim)]
    for k in range(_ORDER):
        transition[0][k] = _REC[k] % MOD
    for i in range(1, _ORDER):
        transition[i][i - 1] = 1
    for k in range(_ORDER):
        transition[dim - 1][k] = _REC[k] % MOD
    transition[dim - 1][dim - 1] = 1

    start_m = base
    state = [[bad[start_m - 3 - k] % MOD] for k in range(_ORDER)]
    state.append([sum(bad[m - 3] for m in range(3, start_m + 1)) % MOD])

    if n <= start_m:
        bad_sum = sum(bad[m - 3] for m in range(3, n + 1)) % MOD
    else:
        powered = _mat_pow(transition, n - start_m)
        bad_sum = _mat_mult(powered, state)[dim - 1][0]

    size_ge_3 = (pow(2, n, MOD) - 1 - (n % MOD) - ((n * (n - 1) // 2) % MOD)) % MOD
    return (size_ge_3 - bad_sum) % MOD


if __name__ == "__main__":
    assert solve(5) == 7
    assert solve(10) == 501
    assert solve(25) == 18635853
    print(solve(10**18))  # 697003956
