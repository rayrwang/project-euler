from bisect import bisect_right
from math import isqrt


def primes_upto(n: int) -> list[int]:
    bs = bytearray([1]) * (n + 1)
    bs[0] = bs[1] = 0
    for i in range(2, isqrt(n) + 1):
        if bs[i]:
            bs[i * i :: i] = bytearray(len(bs[i * i :: i]))
    return [i for i in range(2, n + 1) if bs[i]]


def hungarian(cost: list[list[float]]) -> list[int]:
    """Min-cost assignment of every row to a distinct column (rows <= cols).

    Returns col chosen per row.  Standard O(n^2 m) potential method.
    """
    n, m = len(cost), len(cost[0])
    inf = float("inf")
    u = [0.0] * (n + 1)
    v = [0.0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [inf] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = inf
            j1 = -1
            for j in range(1, m + 1):
                if not used[j]:
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    res = [-1] * n
    for j in range(1, m + 1):
        if p[j] > 0:
            res[p[j] - 1] = j - 1
    return res


def coprime_max_sum(n: int) -> int:
    """Maximal sum of a pairwise-coprime subset of {1, ..., n}.

    Pairwise coprimality means the chosen numbers have disjoint prime
    supports, so each prime is "owned" by at most one number.  Always take
    1, and every prime above sqrt(n) standalone (its only multiple <= n is
    itself, so it never conflicts).  Since there are far more large primes
    than small ones, bundling two small primes into one number is never
    optimal (splitting them across two large primes uses an extra valuable
    prime); thus every small prime appears either as a standalone prime
    power q^a or attached to one large prime as q^a * P.

    Attaching q to P replaces the standalone q^a and the standalone P by the
    single number q^a*P, a gain of q^a*P - q^a - P, and each large prime can
    host at most one small prime -- a maximum-weight assignment between
    small primes and large primes, solved exactly with the Hungarian method.
    """
    if n == 1:
        return 1
    primes = primes_upto(n)
    s = isqrt(n)
    small = [p for p in primes if p <= s]
    large = [p for p in primes if p > s]
    total = 1 + sum(large)

    standalone = {}
    for q in small:
        v = q
        while v * q <= n:
            v *= q
        standalone[q] = v
        total += v

    # Candidate large primes: the top T under each cap n / q^a (T >= #small
    # guarantees enough distinct primes to resolve every conflict).
    cap_count = len(small) + 2
    cand_set: set[int] = set()
    for q in small:
        qa = q
        while qa <= n:
            cap = n // qa
            if cap > s:
                idx = bisect_right(large, cap)
                for j in range(max(0, idx - cap_count), idx):
                    cand_set.add(large[j])
            qa *= q
    cand = sorted(cand_set)
    col = {p: j for j, p in enumerate(cand)}

    inf = float("inf")
    rows, cols = len(small), len(cand)
    width = cols + rows  # extra dummy columns allow staying standalone
    cost = [[inf] * width for _ in range(rows)]
    for i, q in enumerate(small):
        st = standalone[q]
        row = cost[i]
        for p in cand:
            cap2 = n // p
            if cap2 < q:
                continue
            qa = q
            while qa * q <= cap2:
                qa *= q
            profit = qa * p - p - st
            if profit > 0:
                row[col[p]] = -profit
        for k in range(rows):
            row[cols + k] = 0.0  # standalone option, profit 0

    res = hungarian(cost)
    for i in range(rows):
        j = res[i]
        if j < cols:
            total += int(-cost[i][j])
    return total


if __name__ == "__main__":
    assert coprime_max_sum(10) == 30
    assert coprime_max_sum(30) == 193
    assert coprime_max_sum(100) == 1356
    print(coprime_max_sum(200000))  # 1726545007
