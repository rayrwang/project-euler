from decimal import Decimal, getcontext

import numpy as np

def optimal_cost(n: int, a: float, b: float):
    """C(n, a, b): minimal worst-case cost to identify a hidden number in
    [1, n], paying `a` per 'guess is lower' answer and `b` per 'higher'.

    A strategy is a binary tree resolving one number per node; a number
    reached by i 'lower' and j 'higher' answers costs ia + jb. Hence the
    number of values distinguishable within worst-case budget T is
    N(T) = sum_{ia + jb <= T} C(i + j, i), and C(n, a, b) is the smallest
    realizable budget v = ia + jb with N(v) >= n.

    Candidates are enumerated in an adaptive box (doubled until the
    optimum is provably interior), weights are Pascal-filled with a cap
    above n (exact int64), and the minimal qualifying value is found by
    prefix sums over the value-sorted candidates. Distinct true values
    differ by at least ~1/(i a + j b) >> float64 error, so float sorting
    is exact; ties only occur for rationally dependent (a, b) where the
    floats are exact too. Returns (i, j) of the optimum for exact
    reconstruction.
    """
    budget = 64.0 * max(a, b)
    cap = 4 * n
    while True:
        imax = int(budget / a) + 1
        jmax = int(budget / b) + 1
        w = np.zeros((imax + 1, jmax + 1), dtype=np.int64)
        w[0, 0] = 1
        for i in range(imax + 1):
            for j in range(jmax + 1):
                if i == 0 and j == 0:
                    continue
                t = (w[i - 1, j] if i else 0) + (w[i, j - 1] if j else 0)
                w[i, j] = t if t < cap else cap
        ii, jj = np.meshgrid(np.arange(imax + 1), np.arange(jmax + 1),
                             indexing="ij")
        vals = ii * a + jj * b
        order = np.argsort(vals, axis=None, kind="stable")
        flat_v = vals.ravel()[order]
        flat_w = w.ravel()[order]
        keep = flat_v <= budget
        flat_v = flat_v[keep]
        flat_w = flat_w[keep]
        csum = np.cumsum(flat_w)
        pos = np.searchsorted(csum, n)
        if pos < len(csum):
            idx = order[np.flatnonzero(keep)[pos]]
            oi, oj = divmod(int(idx), jmax + 1)
            v = oi * a + oj * b
            if v <= budget * 0.999:
                return oi, oj
        budget *= 2

def exact_value(i: int, j: int, ka: int, kb: int) -> Decimal:
    getcontext().prec = 40
    return i * Decimal(ka).sqrt() + j * Decimal(kb).sqrt()

def brute(n: int, a: float, b: float) -> float:
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def cost(lo: int, hi: int) -> float:
        if lo > hi:
            return 0.0
        best = float("inf")
        for g in range(lo, hi + 1):
            worst = max(
                a + cost(g + 1, hi) if g < hi else 0.0,
                b + cost(lo, g - 1) if g > lo else 0.0,
            )
            best = min(best, worst)
        return best

    return cost(1, n)

def fib(k: int) -> int:
    x, y = 1, 1
    for _ in range(k - 1):
        x, y = y, x + y
    return x

if __name__ == "__main__":
    i5, j5 = optimal_cost(5, 2.0, 3.0)
    assert i5 * 2 + j5 * 3 == 5  # given C(5, 2, 3) = 5
    i2, j2 = optimal_cost(20000, 5.0, 7.0)
    assert i2 * 5 + j2 * 7 == 82  # given C(20000, 5, 7) = 82
    import math
    for nn in (7, 13, 21):
        oi, oj = optimal_cost(nn, math.sqrt(2), math.sqrt(3))
        v = oi * math.sqrt(2) + oj * math.sqrt(3)
        assert abs(v - brute(nn, math.sqrt(2), math.sqrt(3))) < 1e-9, nn
    oi, oj = optimal_cost(500, math.sqrt(2), math.sqrt(3))
    assert abs(oi * math.sqrt(2) + oj * math.sqrt(3) - 13.22073197) < 1e-7
    oi, oj = optimal_cost(2_000_000, math.sqrt(5), math.sqrt(7))
    assert abs(oi * math.sqrt(5) + oj * math.sqrt(7) - 49.63755955) < 1e-7
    total = Decimal(0)
    for k in range(1, 31):
        fk = fib(k)
        oi, oj = optimal_cost(10**12, math.sqrt(k), math.sqrt(fk))
        total += exact_value(oi, oj, k, fk)
    print(total.quantize(Decimal("0.00000001")))  # 36813.12757207
