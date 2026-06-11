"""Project Euler 844: k-Markov Numbers.

The Hurwitz equation sum x_i^2 = k prod x_i admits Vieta jumping: for
any coordinate, x -> k (prod of the others) - x maps solutions to
solutions, and by Hurwitz's classical theorem every solution of the
a = n case descends to the unique fundamental solution (1, ..., 1).
Representing a solution by its multiset of "active" coordinates
(those exceeding one), a breadth-first search from the empty active
set generates all solutions whose values stay below N: promoting a 1
gives the new value k * prod(active) - 1, and jumping an active a
gives k * prod(other actives) - a.  Trees are tiny because values grow
multiplicatively; collecting the distinct coordinates yields M_k(N).

Branching beyond the basic chain first happens at value
k u_1 u_2 - 1 ~ k^4, where u_0 = 1, u_1 = k - 1 and
u_j = k u_{j-1} - u_{j-2} is the two-active chain.  Hence for
k > 32000 (so k^4 > 10^18) the k-Markov numbers below 10^18 are
exactly {1, u_1, ..., u_J} with J <= 3, and M_k(N) is a small
polynomial in k on each range between the thresholds where u_j(k)
crosses N.  The tail of S is therefore a handful of exact Faulhaber
sums, while k <= 32000 is handled by the explicit search; the two
methods agree on overlapping windows, and the code reproduces the
given M_3(10^3) = 2797, M_8(10^8) = 131493335, S(4, 10^2) = 229 and
S(10, 10^8) = 2383369980.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

MOD = 1405695061
BFS_LIMIT = 32000


def markov_values(k: int, n: int) -> set[int]:
    """All k-Markov numbers <= n via BFS over active multisets."""
    vals = {1}
    seen: set[tuple[int, ...]] = {()}
    stack: list[tuple[int, ...]] = [()]
    while stack:
        act = stack.pop()
        m = len(act)
        prod = 1
        for a in act:
            prod *= a
        if m < k:
            new = k * prod - 1
            if new <= n:
                child = tuple(sorted((*act, new)))
                if child not in seen:
                    seen.add(child)
                    vals.add(new)
                    stack.append(child)
        for i in range(m):
            a = act[i]
            new = k * (prod // a) - a
            if a < new <= n:
                child = tuple(sorted(act[:i] + act[i + 1 :] + (new,)))
                if child not in seen:
                    seen.add(child)
                    vals.add(new)
                    stack.append(child)
    return vals


def markov_sum(k: int, n: int) -> int:
    return sum(markov_values(k, n))


def power_sum(n: int, d: int) -> int:
    """Exact sum_{k=1}^{n} k^d via Faulhaber with B_1 = -1/2 plus n^d."""
    bern = [Fraction(1)]
    for m in range(1, d + 1):
        s = sum((comb(m + 1, j) * bern[j] for j in range(m)), Fraction(0))
        bern.append(-s / (m + 1))
    s = Fraction(0)
    for j in range(d + 1):
        s += comb(d + 1, j) * bern[j] * Fraction(n) ** (d + 1 - j)
    s = s / (d + 1) + Fraction(n) ** d
    assert s.denominator == 1
    return s.numerator


def chain_value(k: int, j: int) -> int:
    a, b = 1, k - 1
    for _ in range(j - 1):
        a, b = b, k * b - a
    return b if j >= 1 else 1


def chain_sum_range(lo: int, hi: int, n: int) -> int:
    """Sum over k in [lo, hi] of (1 + chain values u_j(k) <= n), exact.

    Valid only where no branching occurs, i.e. k u_1 u_2 - 1 > n."""
    total = 0
    length = 0
    while chain_value(lo, length + 1) <= n:
        length += 1
    for j in range(length, 0, -1):
        best = lo - 1
        a, b = lo, hi
        while a <= b:
            mid = (a + b) // 2
            if chain_value(mid, j) <= n:
                best = mid
                a = mid + 1
            else:
                b = mid - 1
        if best < lo:
            continue
        # polynomial 1 + sum_{i=1}^{j} u_i(k)
        pa, pb = [1], [-1, 1]
        polys = [pb]
        for _ in range(j - 1):
            shifted = [0, *pb]
            pn = [
                s - (pa[idx] if idx < len(pa) else 0) for idx, s in enumerate(shifted)
            ]
            pa, pb = pb, pn
            polys.append(pn)
        coef = [0] * max(len(p) for p in polys)
        coef[0] = 1
        for p in polys:
            for idx, c in enumerate(p):
                coef[idx] += c
        for d, c in enumerate(coef):
            if c:
                total += c * (power_sum(best, d) - power_sum(lo - 1, d))
        lo = best + 1
    if lo <= hi:
        total += hi - lo + 1  # only the value 1 remains
    return total


def grand_sum(big_k: int, n: int) -> int:
    cutoff = min(big_k, BFS_LIMIT)
    total = sum(markov_sum(k, n) for k in range(3, cutoff + 1))
    if big_k > cutoff:
        a = cutoff + 1
        assert a * (a - 1) * (a * a - a - 1) - 1 > n
        total += chain_sum_range(a, big_k, n)
    return total


def main() -> None:
    assert markov_sum(3, 10**3) == 2797
    assert markov_sum(8, 10**8) == 131493335
    assert grand_sum(4, 10**2) == 229
    assert grand_sum(10, 10**8) == 2383369980
    n = 10**18
    direct = sum(markov_sum(k, n) for k in range(32001, 32101))
    assert direct == chain_sum_range(32001, 32100, n)
    print(grand_sum(10**18, 10**18) % MOD)  # 101805206


if __name__ == "__main__":
    main()
