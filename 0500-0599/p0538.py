"""
https://projecteuler.net/problem=538

f(S) is the perimeter of the maximum-area quadrilateral with side
lengths taken from four distinct positions of S (ties broken by
largest perimeter). With u_n = 2^B(3n) + 3^B(2n) + B(n+1) (B = bit
count) and U_n = (u_1..u_n), find the sum of f(U_n) for
4 <= n <= 3000000.

For fixed sides the maximum area is the cyclic quadrilateral's,
given by Brahmagupta: 16 area^2 = (2s-2a)(2s-2b)(2s-2c)(2s-2d) with
2s the perimeter, independent of side order. Increasing any non-max
side strictly increases the area (the log-derivative is
(1/(s-a) + 1/(s-b) + 1/(s-c) - 1/(s-d))/2 > 0 since s-a <= s-d), so
an optimal multiset is always a consecutive window of the values in
sorted descending order. A valid window can still lose to a deeper
one when its largest side nearly degenerates, so windows are scanned
downward with the rigorous prune 16 area^2 <= (2s/2)^4 <= (2 v_j)^4:
once (2 v_j)^4 cannot beat the best product, no deeper window can.

The u_n take only ~10^4 distinct values (2^a + 3^b + c with small
exponents), so the multiset is kept as counts over a descending
distinct-value list, and each step lazily expands just the top few
values. Areas are compared exactly with integer arithmetic
(16 area^2, then perimeter for ties).

Verified against literal enumeration of all 4-subsets with exact
lexicographic (area, perimeter) comparison for every n <= 60, plus
the given f(U_5) = 59, f(U_10) = 118, f(U_150) = 3223 and
sum 4..150 = 234761.
"""

import bisect
from itertools import combinations


def _b(k: int) -> int:
    return bin(k).count("1")


def u_of(n: int) -> int:
    return 2 ** _b(3 * n) + 3 ** _b(2 * n) + _b(n + 1)


def _brute_f(seq: list[int]) -> int:
    best = (-1, -1)
    for c in combinations(seq, 4):
        s2 = sum(c)
        if s2 - 2 * max(c) <= 0:
            continue
        p16 = 1
        for x in c:
            p16 *= s2 - 2 * x
        best = max(best, (p16, s2))
    return best[1]


def total(n_max: int, check: dict[int, int] | None = None) -> int:
    counts: dict[int, int] = {}
    distinct: list[int] = []  # negated, ascending = values descending
    grand = 0
    for n in range(1, n_max + 1):
        v = u_of(n)
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
            bisect.insort(distinct, -v)
        if n < 4:
            continue
        best_p, best_s = -1, -1
        vals: list[int] = []
        idx = 0
        i = 0
        while True:
            while len(vals) < i + 4 and idx < len(distinct):
                vv = -distinct[idx]
                vals.extend([vv] * counts[vv])
                idx += 1
            if len(vals) < i + 4:
                break
            a = vals[i]
            if best_p > 0 and (2 * a) ** 4 <= best_p:
                break
            s2 = a + vals[i + 1] + vals[i + 2] + vals[i + 3]
            if s2 - 2 * a > 0:
                p16 = s2 - 2 * a
                for j in range(1, 4):
                    p16 *= s2 - 2 * vals[i + j]
                if p16 > best_p or (p16 == best_p and s2 > best_s):
                    best_p, best_s = p16, s2
            i += 1
        f_n = best_s if best_s > 0 else 0
        if check is not None and n in check:
            assert f_n == check[n], (n, f_n)
        grand += f_n
    return grand


if __name__ == "__main__":
    seq = [u_of(i) for i in range(1, 61)]
    assert seq[:10] == [8, 9, 14, 9, 27, 16, 36, 9, 27, 28]  # given U_10
    checks = {5: 59, 10: 118, 150: 3223}  # given
    for n in range(4, 61):
        checks.setdefault(n, _brute_f(seq[:n]))
    assert total(150, checks) == 234761  # given sum for 4..150

    print(total(3_000_000))  # 22472871503401097
