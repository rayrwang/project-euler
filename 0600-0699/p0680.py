"""Project Euler Problem 680: Yarra Gnisrever.

N = 10^18 is far too large to materialise, but K = 10^6 reversals can
only ever cut the initial run 0..N-1 into O(K) maximal arithmetic
segments of step +-1.  The array is kept as an implicit treap (keyed by
position) whose nodes hold whole segments.  A reversal is two splits by
element count, a lazy subtree reversal, and two merges.

Lazy reversal of a subtree swaps the children, flips the node's own
segment (new start = start + dir * (len - 1), dir = -dir), and updates
the aggregates in O(1): reversing any block of length L maps the
position-weighted sum P to (L - 1) * V - P where V is the value sum, and
the same formula applies to a single segment's internal sum.  Each node
therefore maintains, modulo 10^9: the segment's value sum and internal
sum of offset * value, plus subtree totals of both (combined with shift
terms offset * V).  Segment sums need L(L-1)/2 and (L-1)L(2L-1)/6 mod
10^9 for L up to 10^18, computed by dividing the even / divisible-by-3
factor out before reducing (10^9 is not prime to 2 and 3, so no modular
inverses).

When a split position falls inside a segment, the node is truncated in
place and a fresh node (random priority) takes the right part, merged
in front of the old right subtree.  Split and merge are iterative with
explicit stacks, which suits numba and bounds nothing on recursion; at
most two nodes are created per operation, so O(K) nodes suffice.  The
whole computation runs in a couple of seconds.

Verified: R(5, 4) = 27, R(10^2, 10^2) = 246597 and
R(10^4, 10^4) = 249275481640 from the statement (the latter two also
recomputed exactly by explicit array reversal), plus random small
(N, K) cases against brute force, both exactly and modulo 10^9.
"""

import numba
import numpy as np

N = 10**18
K = 10**6
MOD = 10**9


def fib_pairs(n: int, k: int) -> np.ndarray:
    """(s_j, t_j) = (F(2j-1) mod N, F(2j) mod N) for j = 1..k."""
    out = np.empty((k, 2), dtype=np.int64)
    a, b = 1, 1  # F1, F2
    for j in range(k):
        out[j, 0] = a
        out[j, 1] = b
        a = (a + b) % n
        b = (a + b) % n
    return out


@numba.jit(nogil=True)
def tri(length: int) -> int:
    """L * (L - 1) / 2 mod MOD without inverses."""
    a, b = length, length - 1
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    return (a % MOD) * (b % MOD) % MOD


@numba.jit(nogil=True)
def sqtri(length: int) -> int:
    """(L - 1) L (2L - 1) / 6 = sum of k^2 for k < L, mod MOD."""
    a, b, c = length - 1, length, 2 * length - 1
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    if a % 3 == 0:
        a //= 3
    elif b % 3 == 0:
        b //= 3
    else:
        c //= 3
    return (a % MOD) * (b % MOD) % MOD * (c % MOD) % MOD


@numba.jit(nogil=True)
def seg_sums(start: int, direction: int, length: int) -> tuple[int, int]:
    """Value sum and sum of offset * value of an AP segment, mod MOD."""
    t1 = tri(length)
    t2 = sqtri(length)
    s = ((start % MOD) * (length % MOD) + direction * t1) % MOD
    k = ((start % MOD) * t1 + direction * t2) % MOD
    return s, k


@numba.jit(nogil=True)
def pull(x, lch, rch, slen, ssum, skey, tot, sval, spos):
    lo, hi = lch[x], rch[x]
    tot[x] = tot[lo] + slen[x] + tot[hi]
    sval[x] = (sval[lo] + ssum[x] + sval[hi]) % MOD
    spos[x] = (
        spos[lo]
        + skey[x] + (tot[lo] % MOD) * ssum[x]
        + spos[hi] + ((tot[lo] + slen[x]) % MOD) * sval[hi]
    ) % MOD


@numba.jit(nogil=True)
def do_reverse(x, lch, rch, sstart, sdir, slen, skey, ssum, tot, sval,
               spos, rev):
    if x == 0:
        return
    lch[x], rch[x] = rch[x], lch[x]
    sstart[x] += sdir[x] * (slen[x] - 1)
    sdir[x] = -sdir[x]
    skey[x] = (((slen[x] - 1) % MOD) * ssum[x] - skey[x]) % MOD
    spos[x] = (((tot[x] - 1) % MOD) * sval[x] - spos[x]) % MOD
    rev[x] ^= 1


@numba.jit(nogil=True)
def push_down(x, lch, rch, sstart, sdir, slen, skey, ssum, tot, sval,
              spos, rev):
    if rev[x]:
        rev[x] = 0
        do_reverse(lch[x], lch, rch, sstart, sdir, slen, skey, ssum, tot,
                   sval, spos, rev)
        do_reverse(rch[x], lch, rch, sstart, sdir, slen, skey, ssum, tot,
                   sval, spos, rev)


@numba.jit(nogil=True)
def split(x, k, nxt, lch, rch, prio, sstart, sdir, slen, ssum, skey, tot,
          sval, spos, rev, stk):
    """First k elements of subtree x, and the rest (iterative)."""
    if x == 0:
        return 0, 0, nxt
    ltop = 0
    rtop = 0
    left = 0
    right = 0
    # stk[:512] holds the left stack, stk[512:] the right stack
    while x:
        push_down(x, lch, rch, sstart, sdir, slen, skey, ssum, tot, sval,
                  spos, rev)
        lsize = tot[lch[x]]
        if k < lsize:
            stk[512 + rtop] = x
            rtop += 1
            x = lch[x]
        elif k > lsize + slen[x]:
            k -= lsize + slen[x]
            stk[ltop] = x
            ltop += 1
            x = rch[x]
        else:
            if k == lsize:
                left = lch[x]
                lch[x] = 0
                pull(x, lch, rch, slen, ssum, skey, tot, sval, spos)
                right = x
            elif k == lsize + slen[x]:
                right = rch[x]
                rch[x] = 0
                pull(x, lch, rch, slen, ssum, skey, tot, sval, spos)
                left = x
            else:
                t = k - lsize
                old_right = rch[x]
                y = nxt
                nxt += 1
                lch[y] = 0
                rch[y] = 0
                rev[y] = 0
                sstart[y] = sstart[x] + sdir[x] * t
                sdir[y] = sdir[x]
                slen[y] = slen[x] - t
                ssum[y], skey[y] = seg_sums(sstart[y], sdir[y], slen[y])
                pull(y, lch, rch, slen, ssum, skey, tot, sval, spos)
                slen[x] = t
                ssum[x], skey[x] = seg_sums(sstart[x], sdir[x], slen[x])
                rch[x] = 0
                pull(x, lch, rch, slen, ssum, skey, tot, sval, spos)
                right = merge(y, old_right, lch, rch, prio, sstart, sdir,
                              slen, ssum, skey, tot, sval, spos, rev, stk)
                left = x
            break
    while ltop:
        ltop -= 1
        node = stk[ltop]
        rch[node] = left
        pull(node, lch, rch, slen, ssum, skey, tot, sval, spos)
        left = node
    while rtop:
        rtop -= 1
        node = stk[512 + rtop]
        lch[node] = right
        pull(node, lch, rch, slen, ssum, skey, tot, sval, spos)
        right = node
    return left, right, nxt


@numba.jit(nogil=True)
def merge(a, b, lch, rch, prio, sstart, sdir, slen, ssum, skey, tot,
          sval, spos, rev, stk):
    """Concatenate treaps a and b (iterative, stk[1024:] scratch)."""
    if a == 0:
        return b
    if b == 0:
        return a
    top = 0
    while a and b:
        if prio[a] >= prio[b]:
            push_down(a, lch, rch, sstart, sdir, slen, skey, ssum, tot,
                      sval, spos, rev)
            stk[1024 + top] = a
            stk[1536 + top] = 1
            top += 1
            a = rch[a]
        else:
            push_down(b, lch, rch, sstart, sdir, slen, skey, ssum, tot,
                      sval, spos, rev)
            stk[1024 + top] = b
            stk[1536 + top] = 0
            top += 1
            b = lch[b]
    root = a if a else b
    while top:
        top -= 1
        node = stk[1024 + top]
        if stk[1536 + top]:
            rch[node] = root
        else:
            lch[node] = root
        pull(node, lch, rch, slen, ssum, skey, tot, sval, spos)
        root = node
    return root


@numba.jit(nogil=True)
def run(n: int, ops: np.ndarray, prio: np.ndarray) -> int:
    cap = len(prio)
    lch = np.zeros(cap, dtype=np.int64)
    rch = np.zeros(cap, dtype=np.int64)
    sstart = np.zeros(cap, dtype=np.int64)
    sdir = np.zeros(cap, dtype=np.int64)
    slen = np.zeros(cap, dtype=np.int64)
    ssum = np.zeros(cap, dtype=np.int64)
    skey = np.zeros(cap, dtype=np.int64)
    tot = np.zeros(cap, dtype=np.int64)
    sval = np.zeros(cap, dtype=np.int64)
    spos = np.zeros(cap, dtype=np.int64)
    rev = np.zeros(cap, dtype=np.int64)
    stk = np.zeros(2048, dtype=np.int64)
    root = 1
    nxt = 2
    sstart[1] = 0
    sdir[1] = 1
    slen[1] = n
    ssum[1], skey[1] = seg_sums(0, 1, n)
    pull(1, lch, rch, slen, ssum, skey, tot, sval, spos)
    for idx in range(len(ops)):
        s, t = ops[idx, 0], ops[idx, 1]
        lo, hi = (s, t) if s <= t else (t, s)
        a, bc, nxt = split(root, lo, nxt, lch, rch, prio, sstart, sdir,
                           slen, ssum, skey, tot, sval, spos, rev, stk)
        b, c, nxt = split(bc, hi - lo + 1, nxt, lch, rch, prio, sstart,
                          sdir, slen, ssum, skey, tot, sval, spos, rev,
                          stk)
        do_reverse(b, lch, rch, sstart, sdir, slen, skey, ssum, tot,
                   sval, spos, rev)
        ab = merge(a, b, lch, rch, prio, sstart, sdir, slen, ssum, skey,
                   tot, sval, spos, rev, stk)
        root = merge(ab, c, lch, rch, prio, sstart, sdir, slen, ssum,
                     skey, tot, sval, spos, rev, stk)
    return spos[root] % MOD


def r_mod(n: int, k: int) -> int:
    rng = np.random.default_rng(12345)
    prio = rng.integers(0, 2**62, size=2 * k + 8).astype(np.int64)
    return int(run(n, fib_pairs(n, k), prio))


def r_brute(n: int, k: int) -> int:
    arr = list(range(n))
    for s, t in fib_pairs(n, k):
        lo, hi = (s, t) if s <= t else (t, s)
        arr[lo:hi + 1] = arr[lo:hi + 1][::-1]
    return sum(i * v for i, v in enumerate(arr))


if __name__ == "__main__":
    assert r_brute(5, 4) == 27
    assert r_brute(100, 100) == 246597
    assert r_brute(10**4, 10**4) == 249275481640
    for nn, kk in ((5, 4), (100, 100), (7, 30), (1000, 500),
                   (10**4, 10**4)):
        assert r_mod(nn, kk) == r_brute(nn, kk) % MOD, (nn, kk)
    print(r_mod(N, K))  # 563917241
