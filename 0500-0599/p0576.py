"""Project Euler problem 576: Irrational Jumps.

A point hops counterclockwise around a circle of circumference 1 in steps
of fixed irrational length l, starting at 0, until it first lands in a
gap of length g whose near edge sits at distance d from the start.
S(l, g, d) = l * m where m is the first index with frac(m l) in
[d, d + g].  M(n, g) maximises sum over primes p <= n of
S(sqrt(1/p), g, d) over a single common d.  Find M(100, 0.00002).

For each prime, m_p(d) is a piecewise-constant function of d: the window
[d, d + g] slides over the circle and m_p(d) is the minimum label among
the points frac(m / sqrt(p)) it contains.  Sorting the first M_p multiples
by position (M_p chosen adaptively so the largest circular gap is at most
g, which guarantees every window is nonempty), a two-pointer sweep with a
monotonic deque produces all pieces in O(M_p) - the classic sliding-window
minimum, with enter events at q - g and exit events just after q.  The
global objective F(d) = sum l_p m_p(d) is then maximised by merging all
piece boundaries into one event sweep, updating one prime's contribution
per event.

Precision: positions are computed in 80-bit longdouble and quantised to
int64 on a 10^18 grid, so all window comparisons are integer-exact; the
quantisation error (~1e-18 per point, with m up to a few million) is far
below the spacing of distinct event boundaries, and numba handles the
int64 sweeps.  F itself sums 25 terms of size l_p * m_p in float64,
accurate to ~1e-11 - ample for 4 decimal places.

Verified: the three given S(sqrt(1/2), 0.06, *) values by direct
simulation, and the given M(3, 0.06) = 29.5425 and M(10, 0.01) =
266.9010 through the full pipeline.
"""

from math import isqrt, sqrt

import numpy as np
from numba import njit

SCALE = 10**18


def positions_int(p: int, m_max: int) -> np.ndarray:
    """frac(m / sqrt(p)) for m = 1..m_max, scaled to int64 by 1e18."""
    ld = np.longdouble
    lp = ld(1) / np.sqrt(ld(p))
    m = np.arange(1, m_max + 1, dtype=np.int64).astype(ld)
    pos = (m * lp) % ld(1)
    return (pos * ld(SCALE)).astype(np.int64)


@njit(cache=True)
def max_circular_gap(sq):
    n = len(sq)
    best = sq[0] + (10**18 - sq[n - 1])
    for i in range(1, n):
        d = sq[i] - sq[i - 1]
        if d > best:
            best = d
    return best


@njit(cache=True)
def pieces_for_prime(q, lab, g):
    """Sliding-window minimum over sorted points q with labels lab.

    Returns (starts, values): m_p(d) = values[t] for d in
    [starts[t], starts[t + 1]); domain [0, SCALE - g]; window closed.
    """
    n = len(q)
    starts = np.empty(2 * n + 2, np.int64)
    vals = np.empty(2 * n + 2, np.int64)
    np_ = 0
    dq = np.empty(n, np.int64)
    head, tail = 0, 0
    i = 0  # next point to exit (first with q[i] >= d)
    j = 0  # next point to enter (enters when d >= q[j] - g)
    d = np.int64(0)
    dmax = SCALE - g
    while j < n and q[j] <= g:
        m = lab[j]
        while tail > head and lab[dq[tail - 1]] >= m:
            tail -= 1
        dq[tail] = j
        tail += 1
        j += 1
    while True:
        starts[np_] = d
        vals[np_] = lab[dq[head]]
        np_ += 1
        e_exit = q[i] + 1 if i < n else SCALE + 1
        e_enter = q[j] - g if j < n else SCALE + 1
        e = min(e_exit, e_enter)
        if e > dmax:
            break
        if e_enter == e:
            m = lab[j]
            while tail > head and lab[dq[tail - 1]] >= m:
                tail -= 1
            dq[tail] = j
            tail += 1
            j += 1
        if e_exit == e:
            if dq[head] == i:
                head += 1
            i += 1
        d = e
    return starts[:np_], vals[:np_]


@njit(cache=True)
def sweep_max(ev_d, ev_p, ev_m, init_m, lvals):
    cur = init_m.copy()
    f = 0.0
    for p in range(len(cur)):
        f += lvals[p] * cur[p]
    best = f
    for t in range(len(ev_d)):
        p = ev_p[t]
        f += lvals[p] * (ev_m[t] - cur[p])
        cur[p] = ev_m[t]
        if f > best:
            best = f
    return best


def m_func(p: int, g_int: int):
    m_max = max(4 * SCALE // g_int, 1000)
    while True:
        pos = positions_int(p, m_max)
        order = np.argsort(pos, kind="stable")
        q = pos[order]
        lab = (order + 1).astype(np.int64)
        if max_circular_gap(q) <= g_int:
            break
        m_max *= 2
    return pieces_for_prime(q, lab, np.int64(g_int))


def big_m(n: int, g: float) -> float:
    g_int = round(g * SCALE)
    primes = [p for p in range(2, n + 1) if all(p % i for i in range(2, isqrt(p) + 1))]
    lvals = np.array([1.0 / sqrt(p) for p in primes])
    all_d, all_p, all_m, init = [], [], [], []
    for idx, p in enumerate(primes):
        starts, vals = m_func(p, g_int)
        init.append(vals[0])
        all_d.append(starts[1:])
        all_p.append(np.full(len(starts) - 1, idx, np.int64))
        all_m.append(vals[1:])
    ev_d = np.concatenate(all_d)
    ev_p = np.concatenate(all_p)
    ev_m = np.concatenate(all_m)
    order = np.argsort(ev_d, kind="stable")
    return sweep_max(
        ev_d[order], ev_p[order], ev_m[order], np.array(init, np.int64), lvals
    )


def s_direct(p: int, g: float, d: float) -> float:
    """Brute-force S(sqrt(1/p), g, d) by stepping in longdouble."""
    ld = np.longdouble
    lp = ld(1) / np.sqrt(ld(p))
    pos = ld(0)
    m = 0
    while True:
        m += 1
        pos = (pos + lp) % ld(1)
        if ld(d) <= pos <= ld(d) + ld(g):
            return float(lp * m)


def main() -> None:
    assert abs(s_direct(2, 0.06, 0.7) - 0.7071) < 1e-4  # given
    assert abs(s_direct(2, 0.06, 0.3543) - 1.4142) < 1e-4  # given
    assert abs(s_direct(2, 0.06, 0.2427) - 16.2634) < 1e-4  # given
    assert abs(big_m(3, 0.06) - 29.5425) < 1e-4  # given
    assert abs(big_m(10, 0.01) - 266.9010) < 1e-4  # given

    print(f"{big_m(100, 0.00002):.4f}")  # 344457.5871


if __name__ == "__main__":
    main()
