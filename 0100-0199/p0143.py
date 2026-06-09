from collections import defaultdict
from math import gcd


def solve(limit: int = 120000) -> int:
    # The Torricelli segments p,q,r meet at 120 degrees, so each side is
    # sqrt(p^2+pq+q^2); requiring integer sides means every pair (p,q) solves
    # p^2+pq+q^2 = square. Such "120-pairs" come from Eisenstein triples
    # A=m^2-n^2, B=2mn+n^2 and their multiples. Build the pair graph, then sum
    # the distinct p+q+r over triangles (mutually-paired triples) with sum<=limit.
    nbr: dict[int, set[int]] = defaultdict(set)
    m = 2
    while m * (m + 2) <= limit:
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            a0 = m * m - n * n
            b0 = 2 * m * n + n * n
            base = a0 + b0
            if base > limit:
                continue
            k = 1
            while k * base <= limit:
                u, v = k * a0, k * b0
                nbr[u].add(v)
                nbr[v].add(u)
                k += 1
        m += 1

    found: set[int] = set()
    for a in range(1, limit):
        na = nbr.get(a)
        if not na:
            continue
        bs = sorted(x for x in na if x > a)
        for i in range(len(bs)):
            b = bs[i]
            if a + 2 * b >= limit:  # smallest possible c > b
                break
            nb = nbr[b]
            for j in range(i + 1, len(bs)):
                c = bs[j]
                s = a + b + c
                if s > limit:
                    break
                if c in nb:
                    found.add(s)
    return sum(found)


if __name__ == "__main__":
    print(solve())  # 30758397
