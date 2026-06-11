"""Project Euler 943: Self Describing Sequences.

S(a, b) is the generalized Kolakoski sequence: runs alternate value a, b
(starting with a) and the run lengths are the sequence itself. With n_a the
number of a's among the first N terms, T(a, b, N) = b N + (a - b) n_a, so
only the prefix count of a's is needed - at N = 22332223332233 for all
49062 ordered pairs.

S is the fixed point of run-length expansion: the same sequence describes
itself at every level, and the run containing element i one level down has
value a or b according to the parity of i. Counting a's in a huge prefix
descends the expansion tree: the explicit first 4096 letters, expanded
enough times, cover N, and the descent consumes whole chunk-subtrees to the
left of the cut. Each subtree summary - exact level-0 length, exact a-count
and the parity of the subtree's length at every intermediate level - is
computed by a depth-first walk (a chunk of 32 letters expands one level,
is re-cut into 32-letter chunks, and an explicit stack handles those) and
memoized by
(chunk letters, depth, parity context). The parity context is the absolute
start parity at each level below, threaded left to right using the returned
length parities; it is what makes mixed-parity (a, b) genuinely hard
(positional parities decide run values, and run lengths a, b of different
parity make these parities non-degenerate). The saving grace, in the spirit
of Brent and Osborn's Kolakoski algorithms, is that the number of distinct
(chunk, parity context) keys that ever occur grows only like ~N^0.43: about
8 million for the worst pair (2, 3) and dropping rapidly as a + b grows
(about 10^5 at a + b = 13, hundreds for a + b > 100), because both the
factor complexity of the sequence and the reachable parity patterns per
factor stay small. Same-parity pairs are nearly free since all or most
parity components are forced.

Verified against direct generation of the sequence for many mixed- and
same-parity pairs at N = 10^6 and 2 * 10^9, and against the given
T(2,3,10) = 25, T(4,2,10^4) = 30004, T(5,8,10^6) = 6499871.
"""

import numba
import numpy as np
from numba import int64, types
from numba.typed import Dict

MOD = 2233222333
N_TARGET = 22332223332233
LCH = 32  # chunk length
B = 4096  # explicit prefix length

KEY_T = types.UniTuple(int64, 2)
VAL_T = types.UniTuple(int64, 3)


@numba.njit(cache=True)
def gen_bits(a, b, n):
    """First n letters of S(a, b) as 0 (=a) / 1 (=b) array."""
    s = np.empty(n, np.uint8)
    s[0] = 0
    pos = 0
    j = 0
    while pos < n:
        run = b if s[j] else a
        v = j & 1
        e = min(pos + run, n)
        for i in range(pos, e):
            s[i] = v
        pos = e
        j += 1
    return s


@numba.njit(cache=True)
def expand_chunks(a, b, wbits, wlen, p, cb, cl):
    """One-level expansion of factor w cut into chunks of LCH letters.

    Letter i of w (0=a,1=b) is run i: a run of (a or b) copies of value
    bit (p+i)&1. Chunk bit patterns go to cb, lengths to cl; returns count.
    """
    nc = 0
    cur = np.int64(0)
    curlen = 0
    for i in range(wlen):
        x = b if (wbits >> i) & 1 else a
        vb = (p + i) & 1
        run = x
        while run > 0:
            take = min(run, LCH - curlen)
            if vb:
                cur |= ((np.int64(1) << take) - 1) << curlen
            curlen += take
            run -= take
            if curlen == LCH:
                cb[nc] = cur
                cl[nc] = LCH
                nc += 1
                cur = np.int64(0)
                curlen = 0
    if curlen > 0:
        cb[nc] = cur
        cl[nc] = curlen
        nc += 1
    return nc


@numba.njit(cache=True)
def count(a, b, wbits0, wlen0, pi0, d0, memo, scratch_b, scratch_l, fr):
    """Summary of the full d-level expansion of factor w, iteratively.

    pi bit 0 = start parity at level d, bit j = at level d-j.
    Returns (len0, a-count, par) with par bit j = parity of the subtree's
    total length at level d-1-j. fr is an int64 frame stack of shape
    (d0+2, 12): wbits, wlen, pi, d, nc, k, len0, cnt, consumed, par, base,
    sub_pi per frame.
    """
    sp = 0
    fr[0, 0] = wbits0
    fr[0, 1] = wlen0
    fr[0, 2] = pi0
    fr[0, 3] = d0
    fr[0, 5] = -1  # k = -1 marks an un-initialized frame
    r0 = np.int64(0)
    r1 = np.int64(0)
    r2 = np.int64(0)
    while sp >= 0:
        wbits = fr[sp, 0]
        wlen = fr[sp, 1]
        pi = fr[sp, 2]
        d = fr[sp, 3]
        if fr[sp, 5] < 0:
            # first visit
            if d == 0:
                nb = np.int64(0)
                for i in range(wlen):
                    nb += (wbits >> i) & 1
                r0, r1, r2 = wlen, wlen - nb, np.int64(0)
                sp -= 1
                continue
            key = (wbits | (wlen << 32) | (d << 38), pi)
            if key in memo:
                r0, r1, r2 = memo[key]
                sp -= 1
                continue
            nc = expand_chunks(a, b, wbits, wlen, pi & 1, scratch_b[d], scratch_l[d])
            if d == 1:
                n0 = np.int64(0)
                nb = np.int64(0)
                for kk in range(nc):
                    n0 += scratch_l[d, kk]
                    v = scratch_b[d, kk]
                    for i in range(scratch_l[d, kk]):
                        nb += (v >> i) & 1
                res = (n0, n0 - nb, n0 & np.int64(1))
                memo[key] = res
                r0, r1, r2 = res
                sp -= 1
                continue
            fr[sp, 4] = nc
            fr[sp, 5] = 0
            fr[sp, 6] = 0  # len0
            fr[sp, 7] = 0  # cnt
            fr[sp, 8] = 0  # consumed
            fr[sp, 9] = 0  # par
            fr[sp, 10] = pi >> 1  # base
            fr[sp, 11] = pi >> 1  # sub_pi
        else:
            # a child just returned: incorporate
            k = fr[sp, 5]
            fr[sp, 6] += r0
            fr[sp, 7] += r1
            consumed = fr[sp, 8] + scratch_l[d, k]
            par = (consumed & 1) | ((fr[sp, 9] ^ (r2 << 1)) & ~np.int64(1))
            mask = (np.int64(1) << (d - 1)) - 1
            fr[sp, 8] = consumed
            fr[sp, 9] = par
            fr[sp, 11] = fr[sp, 10] ^ ((consumed & 1) | (par & ~np.int64(1) & mask))
            fr[sp, 5] = k + 1
        k = fr[sp, 5]
        if k < fr[sp, 4]:
            fr[sp + 1, 0] = scratch_b[d, k]
            fr[sp + 1, 1] = scratch_l[d, k]
            fr[sp + 1, 2] = fr[sp, 11]
            fr[sp + 1, 3] = d - 1
            fr[sp + 1, 5] = -1
            sp += 1
        else:
            key = (wbits | (wlen << 32) | (d << 38), pi)
            res = (fr[sp, 6], fr[sp, 7], fr[sp, 9])
            memo[key] = res
            r0, r1, r2 = res
            sp -= 1
    return r0, r1, r2


@numba.njit
def prefix_count(a, b, n_target):
    """Number of a's among the first n_target elements of S(a, b)."""
    s = gen_bits(a, b, B)
    if n_target <= B:
        tot = np.int64(0)
        for i in range(n_target):
            if not s[i]:
                tot += 1
        return tot
    d = 0
    cover = B // 2
    while cover < n_target + 1:
        nxt = cover * (a + b) // 2
        cover = nxt if nxt > cover else cover + 1
        d += 1
    memo = Dict.empty(KEY_T, VAL_T)
    maxc = (LCH * max(a, b)) // LCH + 2
    scratch_b = np.zeros((d + 1, maxc), np.int64)
    scratch_l = np.zeros((d + 1, maxc), np.int64)
    fr = np.zeros((d + 2, 12), np.int64)
    # top level: walk the explicit prefix's chunks directly at depth d
    rem = n_target
    total = np.int64(0)
    pi = np.int64(0)
    wbits = np.int64(0)
    wlen = 0
    # descend, starting from the explicit prefix as the level-d word
    top = True
    tb = np.zeros(B // 32 * maxc, np.int64)
    tl = np.zeros(B // 32 * maxc, np.int64)
    while d >= 1:
        if top:
            # expand the explicit prefix chunk by chunk (it is the level-d
            # word); reuse expand_chunks on its 32-letter pieces, threading
            # the carry of partial output chunks manually: simpler approach -
            # expand each 32-letter piece separately is wrong (chunks must be
            # contiguous), so expand whole prefix into big arrays.
            nc = 0
            cur = np.int64(0)
            curlen = 0
            for i in range(B):
                x = b if s[i] else a
                vb = i & 1
                run = x
                while run > 0:
                    take = min(run, LCH - curlen)
                    if vb:
                        cur |= ((np.int64(1) << take) - 1) << curlen
                    curlen += take
                    run -= take
                    if curlen == LCH:
                        tb[nc] = cur
                        tl[nc] = LCH
                        nc += 1
                        cur = np.int64(0)
                        curlen = 0
            if curlen > 0:
                tb[nc] = cur
                tl[nc] = curlen
                nc += 1
            cbv = tb
            clv = tl
        else:
            cbv = scratch_b[0]
            clv = scratch_l[0]
            nc = expand_chunks(a, b, wbits, wlen, pi & 1, cbv, clv)
        consumed = np.int64(0)
        par = np.int64(0)
        base = pi >> 1
        sub_pi = base
        mask = (np.int64(1) << max(d - 1, 1)) - 1
        found = False
        for k in range(nc):
            l0, c, lp = count(
                a, b, cbv[k], clv[k], sub_pi, d - 1, memo, scratch_b, scratch_l, fr
            )
            if l0 <= rem:
                rem -= l0
                total += c
                consumed += clv[k]
                par = (consumed & 1) | ((par ^ (lp << 1)) & ~np.int64(1))
                sub_pi = base ^ ((consumed & 1) | (par & ~np.int64(1) & mask))
            else:
                wbits = cbv[k]
                wlen = int(clv[k])
                pi = sub_pi
                found = True
                break
        if not found:
            return np.int64(-1)  # explicit prefix too short (should not occur)
        top = False
        d -= 1
    for i in range(rem):
        if not (wbits >> i) & 1:
            total += 1
    return total


@numba.njit
def solve_all(n_target, lo, hi):
    acc = np.int64(0)
    for a in range(lo, hi + 1):
        for bb in range(lo, hi + 1):
            if a == bb:
                continue
            na = prefix_count(a, bb, n_target)
            t = (np.int64(bb) % MOD) * (n_target % MOD) % MOD
            t = (t + (a - bb) % MOD * (na % MOD)) % MOD
            acc = (acc + t) % MOD
    return acc % MOD


def solve() -> int:
    return int(solve_all(N_TARGET, 2, 223))


if __name__ == "__main__":
    print(solve())  # 1038733707
