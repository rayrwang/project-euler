"""Project Euler problem 569: Prime Mountain Range.

Mountains have 45-degree slopes; the k-th up-slope rises p_{2k-1} and the
down-slope falls p_{2k}.  From the k-th peak Tenzing looks back and counts
the visible previous peaks, P(k).  Find the sum of P(k) for k <= 2500000.

Peak k sits at X_k = sum of the first 2k - 1 primes and
Y_k = alternating sum p_1 - p_2 + ... + p_{2k-1}.  Since consecutive
primes increase, Y is strictly increasing.  Because every line between
two peaks has |slope| < 1 while the terrain slopes are exactly 1, valleys
never block sight, so peak j is visible from k iff its sight angle
(Y_j - Y_k) / (X_k - X_j) strictly exceeds the angle of every peak between
them - i.e. the visible peaks are the strict records of the angle
sequence scanned from k - 1 leftward.

A plain backward scan is Theta(n^2) here (all angles are negative since Y
is monotone, so no height-based pruning applies).  Instead, each next
visible peak is the rightmost j with (Y_j - Y_k) bdx + bdy (X_j - X_k) > 0
where bdy / bdx is the current best angle - a "rightmost point above a
line" query.  A segment tree whose nodes store the upper convex hull of
their range answers it in O(log^2 n): the linear functional is maximised
on a hull by binary search on edge slopes, and the tree is descended
right-first.  With sum P(k) about 2 * 10^7, the whole run is a few
seconds.  All geometric predicates are exact: coordinates reach 2 * 10^14
so cross products overflow int64, and a 128-bit comparison (32-bit limb
split) is used throughout, including hull construction.

Verified: P(3) = 1, P(9) = 3 and the given sum 227 for k <= 100, plus
agreement with an exact Fraction-based brute force for all k < 2000.
"""

import sys
from pathlib import Path

import numpy as np
from numba import njit

sys.path.append(str(Path(__file__).resolve().parent.parent))
from funcs import prime_sieve_int  # noqa: E402

N = 2_500_000


@njit(cache=True, inline="always")
def cmp_prod(a, b, c, d):
    """Sign of a*b - c*d, exact for |a|,|c| < 2^31 and |b|,|d| < 2^48."""
    sa = (1 if a > 0 else (-1 if a < 0 else 0)) * (1 if b > 0 else (-1 if b < 0 else 0))
    sc = (1 if c > 0 else (-1 if c < 0 else 0)) * (1 if d > 0 else (-1 if d < 0 else 0))
    if sa != sc:
        return 1 if sa > sc else -1
    if sa == 0:
        return 0
    ma, mb, mc, md = abs(a), abs(b), abs(c), abs(d)
    p1 = ma * (mb & 0xFFFFFFFF)
    p2 = mc * (md & 0xFFFFFFFF)
    hi1 = ma * (mb >> 32) + (p1 >> 32)
    hi2 = mc * (md >> 32) + (p2 >> 32)
    if hi1 != hi2:
        mag = 1 if hi1 > hi2 else -1
    else:
        lo1, lo2 = p1 & 0xFFFFFFFF, p2 & 0xFFFFFFFF
        mag = (1 if lo1 > lo2 else -1) if lo1 != lo2 else 0
    return mag * sa


@njit(cache=True)
def build_hulls(x, y, n):
    """Segment tree of upper hulls; node v's hull lives at hull[off[v]:+ln[v]]."""
    size = 1
    while size < n:
        size *= 2
    nv = 2 * size
    lo = np.empty(nv, np.int64)
    hi = np.empty(nv, np.int64)
    for v in range(size, nv):
        i = v - size
        lo[v] = min(i, n)
        hi[v] = min(i + 1, n)
    for v in range(size - 1, 0, -1):
        lo[v] = lo[2 * v]
        hi[v] = hi[2 * v + 1]
    total = 0
    off = np.empty(nv, np.int64)
    ln = np.zeros(nv, np.int64)
    for v in range(1, nv):
        off[v] = total
        total += max(0, hi[v] - lo[v])
    hull = np.empty(total, np.int32)
    stack = np.empty(n, np.int64)
    for v in range(1, nv):
        a, b = lo[v], hi[v]
        if b <= a:
            continue
        top = 0
        for j in range(a, b):
            while top >= 2:
                q1, q2 = stack[top - 2], stack[top - 1]
                if cmp_prod(y[q2] - y[q1], x[j] - x[q1], y[j] - y[q1], x[q2] - x[q1]) <= 0:
                    top -= 1
                else:
                    break
            stack[top] = j
            top += 1
        ln[v] = top
        for t in range(top):
            hull[off[v] + t] = stack[t]
    return off, ln, hull, size


@njit(cache=True, inline="always")
def node_above(v, off, ln, hull, x, y, yk, xk, bdy, bdx):
    """Does node v hold a point with (y_j - yk) bdx + bdy (x_j - xk) > 0?"""
    o, m = off[v], ln[v]
    loi, hii = 0, m - 1
    while loi < hii:
        mid = (loi + hii) // 2
        j1, j2 = hull[o + mid], hull[o + mid + 1]
        if cmp_prod(y[j2] - y[j1], bdx, -bdy, x[j2] - x[j1]) > 0:
            loi = mid + 1
        else:
            hii = mid
    j = hull[o + loi]
    return cmp_prod(y[j] - yk, bdx, bdy, xk - x[j]) > 0


@njit(cache=True)
def rightmost_above(ihi, off, ln, hull, x, y, yk, xk, bdy, bdx, size):
    """Rightmost j <= ihi strictly above the current sight line, or -1."""
    nodes = np.empty(64, np.int64)
    nn = 0
    v = 1
    lo = 0
    hi = size
    going = True
    while going:
        if hi <= ihi + 1:
            nodes[nn] = v
            nn += 1
            going = False
        else:
            mid = (lo + hi) // 2
            if ihi + 1 <= mid:
                v = 2 * v
                hi = mid
            else:
                nodes[nn] = 2 * v
                nn += 1
                v = 2 * v + 1
                lo = mid
    for t in range(nn - 1, -1, -1):
        v = nodes[t]
        if ln[v] == 0:
            continue
        if node_above(v, off, ln, hull, x, y, yk, xk, bdy, bdx):
            while v < size:
                rch = 2 * v + 1
                if ln[rch] > 0 and node_above(rch, off, ln, hull, x, y, yk, xk, bdy, bdx):
                    v = rch
                else:
                    v = 2 * v
            return v - size
    return -1


@njit(cache=True)
def total_p(x, y, n, off, ln, hull, size):
    tot = np.int64(0)
    for k in range(1, n):
        xk, yk = x[k], y[k]
        bdy = y[k - 1] - yk
        bdx = xk - x[k - 1]
        cnt = 1
        i = k - 2
        while i >= 0:
            j = rightmost_above(i, off, ln, hull, x, y, yk, xk, bdy, bdx, size)
            if j < 0:
                break
            cnt += 1
            bdy = y[j] - yk
            bdx = xk - x[j]
            i = j - 1
        tot += cnt
    return tot


def brute_p(xs: list[int], ys: list[int], k: int) -> int:
    from fractions import Fraction

    best = None
    cnt = 0
    for i in range(k - 1, -1, -1):
        ang = Fraction(ys[i] - ys[k], xs[k] - xs[i])
        if best is None or ang > best:
            cnt += 1
            best = ang
    return cnt


def main() -> None:
    primes = prime_sieve_int(98_000_000)
    assert len(primes) >= 2 * N
    ps = primes[: 2 * N].astype(np.int64)
    x = np.cumsum(ps)[0::2].copy()
    y = np.cumsum(np.where(np.arange(2 * N) % 2 == 0, ps, -ps))[0::2].copy()
    assert int(y.max()) < 2**31 and int(x.max()) < 2**48  # cmp_prod contract

    off, ln, hull, size = build_hulls(x, y, N)

    xs, ys = [int(v) for v in x[:2000]], [int(v) for v in y[:2000]]
    assert brute_p(xs, ys, 2) == 1  # P(3) = 1 (given)
    assert brute_p(xs, ys, 8) == 3  # P(9) = 3 (given)
    assert total_p(x, y, 100, off, ln, hull, size) == 227  # given
    fast2000 = total_p(x, y, 2000, off, ln, hull, size)
    assert fast2000 == sum(brute_p(xs, ys, k) for k in range(1, 2000))

    print(total_p(x, y, N, off, ln, hull, size))  # 21025060


if __name__ == "__main__":
    main()
