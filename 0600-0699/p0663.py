"""Project Euler Problem 663: Sums of Subarrays.

Tribonacci-driven point updates A[t_{2i-2} mod n] += 2(t_{2i-1} mod n)-n+1
hit an array of length n = 10000003; M_n(i) is the maximal contiguous
subarray sum after step i, and we need the sum of M over steps
10000001..10200000 only.

Since no queries occur during the first 10^7 steps, they are applied as
raw point updates.  Then a sqrt-decomposition takes over: each block of
about sqrt(n) elements stores the classic max-subarray summary (total,
best prefix, best suffix, best subsegment, all non-empty).  A step
recomputes the single block containing the touched index by a linear scan
and then folds the ~3200 block summaries left to right with the standard
merge (best = max(best_l, best_r, suf_l + pre_r), etc.), reading off M.
That is ~7000 operations per step for 200000 steps.

The tribonacci values are kept modulo n throughout.  Checks: the worked
n = 5 example with S(5, 6) = 32, plus S(5, 100) = 2416, S(14, 100) = 3881
and S(107, 1000) = 1618572 against a per-step Kadane brute force.
"""

import numba
import numpy as np

NEG = -(1 << 62)


@numba.jit(cache=True)
def S_range(n: int, skip: int, take: int) -> int:
    """Sum of M_n(i) for i in (skip, skip + take]."""
    A = np.zeros(n, dtype=np.int64)
    t0, t1, t2 = 0, 0, 1 % n  # (t_{2i-2}, t_{2i-1}, t_{2i}) mod n at step i

    # phase 1: raw updates, no queries
    for _ in range(skip):
        A[t0] += 2 * t1 - n + 1
        t0, t1, t2 = t2, (t0 + t1 + t2) % n, (t0 + 2 * t1 + 2 * t2) % n

    # build block summaries (total, prefix, suffix, best; all non-empty)
    L = max(1, int(n**0.5))
    nb = (n + L - 1) // L
    tot = np.zeros(nb, dtype=np.int64)
    pre = np.full(nb, NEG, dtype=np.int64)
    suf = np.full(nb, NEG, dtype=np.int64)
    best = np.full(nb, NEG, dtype=np.int64)
    for b in range(nb):
        rebuild_block(A, b, L, n, tot, pre, suf, best)

    # phase 2: update, rebuild one block, fold all blocks
    total = 0
    for _ in range(take):
        idx = t0
        A[idx] += 2 * t1 - n + 1
        t0, t1, t2 = t2, (t0 + t1 + t2) % n, (t0 + 2 * t1 + 2 * t2) % n
        rebuild_block(A, idx // L, L, n, tot, pre, suf, best)
        ct, cp, cs, cb = tot[0], pre[0], suf[0], best[0]
        for b in range(1, nb):
            nbest = max(cb, best[b], cs + pre[b])
            npre = max(cp, ct + pre[b])
            nsuf = max(suf[b], tot[b] + cs)
            ct += tot[b]
            cp, cs, cb = npre, nsuf, nbest
        total += cb
    return total


@numba.jit(cache=True)
def rebuild_block(A, b, L, n, tot, pre, suf, best):
    lo = b * L
    hi = min(lo + L, n)
    t = 0
    p = bb = NEG
    run = NEG
    for j in range(lo, hi):
        v = A[j]
        t += v
        if p < t:
            p = t
        run = v if run < 0 else run + v
        if bb < run:
            bb = run
    s = NEG
    t = 0
    for j in range(hi - 1, lo - 1, -1):
        t += A[j]
        if s < t:
            s = t
    tot[b] = A[lo:hi].sum()
    pre[b] = p
    suf[b] = s
    best[b] = bb


def S_brute(n: int, length: int) -> int:
    A = [0] * n
    t = [0, 0, 1 % n]
    total = 0
    for i in range(1, length + 1):
        A[t[0]] += 2 * t[1] - n + 1
        t = [t[2], (t[0] + t[1] + t[2]) % n, (t[0] + 2 * t[1] + 2 * t[2]) % n]
        run = best = -(1 << 62)
        for v in A:
            run = v if run < 0 else run + v
            best = max(best, run)
        total += best
    return total


if __name__ == "__main__":
    assert S_brute(5, 6) == 32
    assert S_brute(5, 100) == 2416
    assert S_brute(14, 100) == 3881
    assert S_brute(107, 1000) == 1618572
    assert S_range(5, 0, 100) == 2416
    assert S_range(14, 0, 100) == 3881
    assert S_range(107, 0, 1000) == 1618572
    assert S_range(107, 600, 400) == 1618572 - S_brute(107, 600)
    print(S_range(10000003, 10**7, 200000))  # 1884138010064752
