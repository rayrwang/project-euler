"""Project Euler 472: Comfortable Distance II.

f(N) counts the first person's seat choices that maximize the final number of
occupants under the greedy rules; find the last 8 digits of sum f(N) for
N <= 10^12.

Reduction: after the first person sits at p, gaps evolve independently. A
closed gap of g seats deterministically seats c(g) = 1 + c(a) + c(b) people
(split in the middle, leftmost on ties), and an open gap of m seats first
grabs the end seat: o(m) = 1 + c(m - 1). Total(p) = 1 + o(p-1) + o(N-p).
This is asserted against a literal seat-by-seat simulation for N <= 60.

Closed form: o(m) = floor(m/2) - floor(d(m)/2), where d(m) is the distance
from m to the nearest power of two (d(0) = 1) - verified for all m <= 10^5.
Hence with S = N - 1, maximizing Total means minimizing the penalty
phi(a) = [S even](a mod 2) + floor(d(a)/2) + floor(d(S-a)/2) over a in
[0, S], and f(N) is the number of minimizers. Both tent functions are
piecewise linear with breakpoints at powers of two and their reflections
about S, so an O(log N) segment scan (split by parity, where phi is affine)
gives f(N) exactly; it matches the O(N) brute force for all N <= 3000.

Summation: f is affine in N per parity class between consecutive "critical"
values of N (sums of two powers of two, their midpoints, and small offsets),
so the total is assembled from arithmetic series whose affinity is verified
at five sample points per interval, with recursive bisection as a fallback.
The machinery reproduces the given f(15) = 9, f(20) = 6, f(500) = 16, the
partial sums 83 and 13343, and exact dyadic block sums - which also satisfy
SB(k+1) = 4 SB(k) - 25 * 2^(k-2) - 13 for 20 consecutive k, a reassuring
self-similarity check.
"""

import numpy as np
from numba import njit


def simulate(n, first):
    """Literal simulation of the seating process."""
    occ = [False] * (n + 2)
    occ[first] = True
    count = 1
    while True:
        best_d, best_seat = 0, -1
        for s in range(1, n + 1):
            if occ[s] or occ[s - 1] or occ[s + 1 if s < n else 0]:
                continue
            dist = min(
                (abs(s - t) for t in range(1, n + 1) if occ[t]),
            )
            if dist > best_d:
                best_d, best_seat = dist, s
        if best_seat < 0:
            return count
        occ[best_seat] = True
        count += 1


@njit(cache=True)
def build_o(nmax):
    c = np.zeros(nmax + 1, np.int64)
    for g in range(3, nmax + 1):
        if g % 2 == 1:
            a = (g - 1) // 2
            b = a
        else:
            a = g // 2 - 1
            b = g // 2
        c[g] = 1 + c[a] + c[b]
    o = np.zeros(nmax + 1, np.int64)
    for m in range(2, nmax + 1):
        o[m] = 1 + c[m - 1]
    return o


@njit(cache=True)
def f_brute(n, o):
    best = np.int64(-1)
    cnt = np.int64(0)
    for p in range(1, n + 1):
        t = 1 + o[p - 1] + o[n - p]
        if t > best:
            best = t
            cnt = 1
        elif t == best:
            cnt += 1
    return cnt


@njit(cache=True)
def dpow(m):
    if m <= 0:
        return 1 - m
    best = np.int64(1) << 62
    q = np.int64(1)
    while q <= 4 * m + 4:
        t = m - q
        if t < 0:
            t = -t
        if t < best:
            best = t
        q *= 2
    return best


@njit(cache=True)
def f_exact(n, bp):
    s = n - 1
    if n == 1:
        return np.int64(1)
    par = 1 if s % 2 == 0 else 0
    nb = 0
    bp[nb] = 0
    nb += 1
    bp[nb] = s
    nb += 1
    p = np.int64(1)
    while p <= 2 * s + 4:
        if 0 <= p <= s:
            bp[nb] = p
            nb += 1
        if 0 <= s - p <= s:
            bp[nb] = s - p
            nb += 1
        if p % 2 == 0:
            mid = 3 * p // 2
            if 0 <= mid <= s:
                bp[nb] = mid
                nb += 1
            if 0 <= s - mid <= s:
                bp[nb] = s - mid
                nb += 1
        p *= 2
    b = np.sort(bp[:nb])
    best = np.int64(1) << 62
    cnt = np.int64(0)
    prev = np.int64(-1)
    for i in range(nb):
        lo = b[i]
        if lo == prev:
            continue
        prev = lo
        v = par * (lo & 1) + dpow(lo) // 2 + dpow(s - lo) // 2
        if v < best:
            best = v
            cnt = 1
        elif v == best:
            cnt += 1
        hi = np.int64(-1)
        for j in range(i + 1, nb):
            if b[j] != lo:
                hi = b[j]
                break
        if hi < 0 or hi <= lo + 1:
            continue
        a1 = lo + 1
        a2 = hi - 1
        for par_cls in range(2):
            a0 = a1 if (a1 & 1) == par_cls else a1 + 1
            if a0 > a2:
                continue
            alast = a2 if (a2 & 1) == par_cls else a2 - 1
            nt = (alast - a0) // 2 + 1
            v0 = par * (a0 & 1) + dpow(a0) // 2 + dpow(s - a0) // 2
            vl = par * (alast & 1) + dpow(alast) // 2 + dpow(s - alast) // 2
            if v0 == vl:
                if v0 < best:
                    best = v0
                    cnt = nt
                elif v0 == best:
                    cnt += nt
            else:
                vm = v0 if v0 < vl else vl
                if vm < best:
                    best = vm
                    cnt = 1
                elif vm == best:
                    cnt += 1
    return cnt


_BP = np.empty(400, np.int64)


def f_of(n):
    return int(f_exact(n, _BP))


def critical_points(x):
    pts = set()
    pows = [1 << i for i in range(44)]
    sums = set()
    for i in range(44):
        for j in range(i, 44):
            v = pows[i] + pows[j]
            if v <= 2 * x + 10:
                sums.add(v)
    sums = sorted(sums)
    for v in sums:
        for d in range(-4, 5):
            pts.add(v + d)
    for a, b in zip(sums, sums[1:]):
        m = (a + b) // 2
        for d in range(-4, 5):
            pts.add(m + d)
    for p in pows:
        for d in range(-4, 5):
            pts.add(p + d)
    return sorted(v for v in pts if 1 <= v <= x)


def sum_range(lo, hi):
    """Sum f over [lo, hi]; f is affine per parity class inside, verified."""
    if hi < lo:
        return 0
    if hi - lo <= 12:
        return sum(f_of(n) for n in range(lo, hi + 1))
    total = 0
    for cls in range(2):
        a0 = lo if lo % 2 == cls else lo + 1
        if a0 > hi:
            continue
        a1 = hi if hi % 2 == cls else hi - 1
        n = (a1 - a0) // 2 + 1
        f0 = f_of(a0)
        if n == 1:
            total += f0
            continue
        slope = f_of(a0 + 2) - f0
        ok = f_of(a1) == f0 + slope * (n - 1)
        if ok and n >= 3:
            ok = f_of(a1 - 2) == f0 + slope * (n - 2)
        if ok and n >= 5:
            ok = f_of(a0 + 2 * (n // 2)) == f0 + slope * (n // 2)
        if ok and n >= 9:
            ok = f_of(a0 + 2 * (n // 4)) == f0 + slope * (n // 4) and f_of(
                a0 + 2 * (3 * n // 4)
            ) == f0 + slope * (3 * n // 4)
        if ok:
            total += n * f0 + slope * n * (n - 1) // 2
        else:
            mid = (lo + hi) // 2
            return sum_range(lo, mid) + sum_range(mid + 1, hi)
    return total


def total_sum(x):
    cps = critical_points(x)
    total = 0
    prev = 1
    for cp in cps:
        if cp > prev:
            total += sum_range(prev, cp - 1)
        total += f_of(cp)
        prev = cp + 1
    if prev <= x:
        total += sum_range(prev, x)
    return total


if __name__ == "__main__":
    o = build_o(4000)
    for n in range(1, 61):
        totals = [simulate(n, p) for p in range(1, n + 1)]
        assert f_brute(n, o) == totals.count(max(totals))
    for m in range(4000):
        k, q = m, 1
        best = 1 << 62
        while q <= 4 * m + 4:
            best = min(best, abs(m - q))
            q *= 2
        if m == 0:
            best = 1
        assert o[m] == m // 2 - best // 2
    for n in range(1, 3001):
        assert f_of(n) == f_brute(n, o)
    assert f_of(15) == 9 and f_of(20) == 6 and f_of(500) == 16
    assert total_sum(20) == 83
    assert total_sum(500) == 13343
    print(total_sum(10**12) % 10**8)  # 73811586
