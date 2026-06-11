"""Project Euler problem 566: Cake Icing Puzzle.

Adam repeatedly cuts pieces of sizes x = 360/a, y = 360/b, z = 360/sqrt(c)
degrees in cyclic order, flipping each piece (reversing it and turning its
icing over) and moving on around the cake.  F(a, b, c) is the number of
flips until all icing faces up again, and G(n) sums F over all
9 <= a < b < c <= n.  Find G(53).

Exact arithmetic: scaling the circle by a*b*c, every length is an integer
pair (p, q) representing p + q*sqrt(c) (q folds into p when c is square),
with sign tests via p^2 vs q^2 c, so the simulation is exact.  In the
cutter frame each step splits the leading arc of the current piece size,
reverses and toggles it, and rotates it to the back.

Key structural facts, verified during the run: segments only ever split
(never merge), so once three consecutive steps produce no split, every
step is a pure signed permutation of the segments; and the step map is
invertible, so from that moment the geometry sequence is purely periodic.
Empirically the period is one round (3 steps) for every triple, which the
code verifies explicitly and would handle as any multiple of 3.  The round
map is then a signed permutation pi with toggles tau, and "all icing up"
at time t0 + 3k + j reduces, per cycle of pi, to a cyclic-shift matching
problem between bit patterns; the admissible shifts are found in linear
time with a Z-algorithm string matcher (validated against brute force),
and combined across cycles by CRT, with unconstrained cycles skipped and
an ascending scan over any deferred coarse constraints.

The transient is the hard part: 14188 of the 14190 triples quiesce within
a few thousand steps, but (9,10,28) and especially (13,14,53) sit on
near-resonances (1/13 + 1/14 + 1/sqrt(53) differs from 2/7 by ~2e-6) and
refine into ~10^6 segments over ~3*10^6 steps.  A naive list costs O(m)
per step; instead the cake is an implicit treap with lazy reversal and
icing-toggle flags and subtree (length, count, icing-down) aggregates, so
each step is two splits and a merge in O(log m), all-up detection is O(1)
at the root, and stability checks are rare full traversals guarded by a
front-segment filter.  F(13,14,53) = 329422932751440 alone dominates G.

Verified: the given F(9,10,11) = 60, F(10,14,16) = 506,
F(15,16,17) = 785232 and G(11) = 60, G(14) = 58020, G(17) = 1269260, plus
direct step-by-step simulation cross-checks on sample triples.
"""

from math import gcd, isqrt

import numpy as np
from numba import njit


@njit(cache=True, inline="always")
def _pos(dp, dq, c):
    """Sign test: is dp + dq*sqrt(c) > 0 (assuming not both zero)."""
    if dp >= 0 and dq >= 0:
        return dp > 0 or dq > 0
    if dp <= 0 and dq <= 0:
        return False
    if dq > 0:
        return dq * dq * c > dp * dp
    return dp * dp > dq * dq * c


@njit(cache=True, inline="always")
def _update(x, lc, rc, p, q, sp, sq, cnt, down, bit):
    s1, s2, n, d = p[x], q[x], 1, bit[x]
    a = lc[x]
    if a >= 0:
        s1 += sp[a]
        s2 += sq[a]
        n += cnt[a]
        d += down[a]
    b = rc[x]
    if b >= 0:
        s1 += sp[b]
        s2 += sq[b]
        n += cnt[b]
        d += down[b]
    sp[x] = s1
    sq[x] = s2
    cnt[x] = n
    down[x] = d


@njit(cache=True, inline="always")
def _apply_rev(x, lc, rc, rev):
    if x >= 0:
        lc[x], rc[x] = rc[x], lc[x]
        rev[x] ^= 1


@njit(cache=True, inline="always")
def _apply_tog(x, cnt, down, bit, tog):
    if x >= 0:
        bit[x] ^= 1
        down[x] = cnt[x] - down[x]
        tog[x] ^= 1


@njit(cache=True, inline="always")
def _pushdown(x, lc, rc, cnt, down, bit, rev, tog):
    if rev[x]:
        _apply_rev(lc[x], lc, rc, rev)
        _apply_rev(rc[x], lc, rc, rev)
        rev[x] = 0
    if tog[x]:
        _apply_tog(lc[x], cnt, down, bit, tog)
        _apply_tog(rc[x], cnt, down, bit, tog)
        tog[x] = 0


@njit(cache=False)
def _merge(a, b, lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog):
    if a < 0:
        return b
    if b < 0:
        return a
    if pri[a] >= pri[b]:
        _pushdown(a, lc, rc, cnt, down, bit, rev, tog)
        rc[a] = _merge(rc[a], b, lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog)
        _update(a, lc, rc, p, q, sp, sq, cnt, down, bit)
        return a
    _pushdown(b, lc, rc, cnt, down, bit, rev, tog)
    lc[b] = _merge(a, lc[b], lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog)
    _update(b, lc, rc, p, q, sp, sq, cnt, down, bit)
    return b


@njit(cache=False)
def _split(x, lp, lq, c, state, lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog):
    """Split subtree so the left part has exact length (lp, lq).

    May allocate one node (a segment is cut): state[0] = next free index,
    state[1] set to 1 on a cut.
    """
    if x < 0:
        return (-1, -1)
    _pushdown(x, lc, rc, cnt, down, bit, rev, tog)
    a = lc[x]
    llp = sp[a] if a >= 0 else 0
    llq = sq[a] if a >= 0 else 0
    d1p = lp - llp
    d1q = lq - llq
    if d1p == 0 and d1q == 0:
        lc[x] = -1
        _update(x, lc, rc, p, q, sp, sq, cnt, down, bit)
        return (a, x)
    if not _pos(d1p, d1q, c):
        aa, bb = _split(a, lp, lq, c, state, lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog)
        lc[x] = bb
        _update(x, lc, rc, p, q, sp, sq, cnt, down, bit)
        return (aa, x)
    d2p = d1p - p[x]
    d2q = d1q - q[x]
    if d2p == 0 and d2q == 0:
        b = rc[x]
        rc[x] = -1
        _update(x, lc, rc, p, q, sp, sq, cnt, down, bit)
        return (x, b)
    if _pos(d2p, d2q, c):
        aa, bb = _split(rc[x], d2p, d2q, c, state, lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog)
        rc[x] = aa
        _update(x, lc, rc, p, q, sp, sq, cnt, down, bit)
        return (x, bb)
    y = state[0]
    state[0] += 1
    state[1] = 1
    lc[y] = -1
    rc[y] = -1
    p[y] = p[x] - d1p
    q[y] = q[x] - d1q
    bit[y] = bit[x]
    rev[y] = 0
    tog[y] = 0
    _update(y, lc, rc, p, q, sp, sq, cnt, down, bit)
    right = _merge(y, rc[x], lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog)
    p[x] = d1p
    q[x] = d1q
    rc[x] = -1
    _update(x, lc, rc, p, q, sp, sq, cnt, down, bit)
    return (x, right)


@njit(cache=False)
def find_period(a, b, c, sq_r, cap, max_steps, quiesce_gap, ref_p, ref_q, ref_b):
    """Simulate until the geometry repeats after split-quiescence.

    Returns (status, t, m, t_ref): status 1 = all-up at step t during the
    transient; 0 = geometry at t equals geometry at t_ref (reference
    written to ref arrays); -2 = node capacity exceeded; -4 = a split
    occurred after the reference was taken (retry with larger gap);
    -3 = max_steps exhausted.
    """
    lc = np.full(cap, -1, np.int64)
    rc = np.full(cap, -1, np.int64)
    pri = np.empty(cap, np.uint64)
    p = np.zeros(cap, np.int64)
    q = np.zeros(cap, np.int64)
    sp = np.zeros(cap, np.int64)
    sq = np.zeros(cap, np.int64)
    cnt = np.zeros(cap, np.int64)
    down = np.zeros(cap, np.int64)
    bit = np.zeros(cap, np.int8)
    rev = np.zeros(cap, np.int8)
    tog = np.zeros(cap, np.int8)
    seed = np.uint64(88172645463325252)
    for i in range(cap):
        seed ^= seed << np.uint64(13)
        seed ^= seed >> np.uint64(7)
        seed ^= seed << np.uint64(17)
        pri[i] = seed
    sp_arr = np.empty(3, np.int64)
    sq_arr = np.empty(3, np.int64)
    sp_arr[0], sq_arr[0] = b * c, 0
    sp_arr[1], sq_arr[1] = a * c, 0
    if sq_r > 0:
        sp_arr[2], sq_arr[2] = a * b * sq_r, 0
    else:
        sp_arr[2], sq_arr[2] = 0, a * b
    p[0] = a * b * c
    _update(0, lc, rc, p, q, sp, sq, cnt, down, bit)
    root = 0
    state = np.zeros(2, np.int64)
    state[0] = 1
    last_split = 0
    stack = np.empty(4096, np.int64)
    t = 0
    t_ref = -1
    ref_m = 0
    front_p = np.int64(-1)
    front_q = np.int64(-1)
    while t < max_steps:
        t += 1
        if state[0] + 2 >= cap:
            return (-2, t, cnt[root], -1)
        ph = (t - 1) % 3
        state[1] = 0
        pre_root, rest = _split(root, sp_arr[ph], sq_arr[ph], c, state,
                                lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog)
        _apply_rev(pre_root, lc, rc, rev)
        _apply_tog(pre_root, cnt, down, bit, tog)
        root = _merge(rest, pre_root, lc, rc, pri, p, q, sp, sq, cnt, down, bit, rev, tog)
        if state[1]:
            last_split = t
            if t_ref >= 0:
                return (-4, t, cnt[root], t_ref)
        if down[root] == 0:
            return (1, t, cnt[root], -1)
        if t_ref < 0:
            if t % 3 == 0 and t - last_split >= quiesce_gap:
                top = 0
                x = root
                idx = 0
                while top > 0 or x >= 0:
                    while x >= 0:
                        _pushdown(x, lc, rc, cnt, down, bit, rev, tog)
                        stack[top] = x
                        top += 1
                        x = lc[x]
                    top -= 1
                    x = stack[top]
                    ref_p[idx] = p[x]
                    ref_q[idx] = q[x]
                    ref_b[idx] = bit[x]
                    idx += 1
                    x = rc[x]
                t_ref = t
                ref_m = idx
                front_p = ref_p[0]
                front_q = ref_q[0]
        elif t % 3 == t_ref % 3:
            x = root
            _pushdown(x, lc, rc, cnt, down, bit, rev, tog)
            while lc[x] >= 0:
                x = lc[x]
                _pushdown(x, lc, rc, cnt, down, bit, rev, tog)
            if p[x] == front_p and q[x] == front_q:
                top = 0
                x = root
                idx = 0
                same = True
                while top > 0 or x >= 0:
                    while x >= 0:
                        _pushdown(x, lc, rc, cnt, down, bit, rev, tog)
                        stack[top] = x
                        top += 1
                        x = lc[x]
                    top -= 1
                    x = stack[top]
                    if same and (p[x] != ref_p[idx] or q[x] != ref_q[idx]):
                        same = False
                    idx += 1
                    x = rc[x]
                if same:
                    return (0, t, ref_m, t_ref)
    return (-3, t, cnt[root], t_ref)


@njit(cache=True)
def perm_over_period(a, b, c, sq_r, t0, m, nsteps, fp, fq):
    """Run nsteps labeled split-free steps from the flat state.

    Returns (pi, tau, targets, ok): pi[label] = final position,
    tau[label] = total toggle, targets[j][label] = toggle after j steps.
    """
    sp_arr = np.empty(3, np.int64)
    sq_arr = np.empty(3, np.int64)
    sp_arr[0], sq_arr[0] = b * c, 0
    sp_arr[1], sq_arr[1] = a * c, 0
    if sq_r > 0:
        sp_arr[2], sq_arr[2] = a * b * sq_r, 0
    else:
        sp_arr[2], sq_arr[2] = 0, a * b
    pp = fp.copy()
    qq = fq.copy()
    lbl = np.arange(m, dtype=np.int64)
    tog = np.zeros(m, np.int8)
    targets = np.zeros((nsteps, m), np.int8)
    pi = np.empty(m, np.int64)
    tau = np.empty(m, np.int8)
    buf_p = np.empty(m, np.int64)
    buf_q = np.empty(m, np.int64)
    buf_l = np.empty(m, np.int64)
    buf_t = np.empty(m, np.int8)
    for stepj in range(nsteps):
        ph = (t0 + stepj) % 3
        rem_p, rem_q = sp_arr[ph], sq_arr[ph]
        k = 0
        while True:
            dp = rem_p - pp[k]
            dq = rem_q - qq[k]
            if dp == 0 and dq == 0:
                k += 1
                break
            if _pos(dp, dq, c):
                rem_p, rem_q = dp, dq
                k += 1
            else:
                return (pi, tau, targets, 0)
        idx = 0
        for i in range(k, m):
            buf_p[idx] = pp[i]
            buf_q[idx] = qq[i]
            buf_l[idx] = lbl[i]
            buf_t[idx] = tog[i]
            idx += 1
        for i in range(k - 1, -1, -1):
            buf_p[idx] = pp[i]
            buf_q[idx] = qq[i]
            buf_l[idx] = lbl[i]
            buf_t[idx] = tog[i] ^ 1
            idx += 1
        pp, buf_p = buf_p, pp
        qq, buf_q = buf_q, qq
        lbl, buf_l = buf_l, lbl
        tog, buf_t = buf_t, tog
        if stepj + 1 < nsteps:
            for i in range(m):
                targets[stepj + 1][lbl[i]] = tog[i]
    for i in range(m):
        if pp[i] != fp[i] or qq[i] != fq[i]:
            return (pi, tau, targets, 0)
        pi[lbl[i]] = i
        tau[lbl[i]] = tog[i]
    return (pi, tau, targets, 1)


@njit(cache=True)
def allowed_shifts(u, e, w, mm):
    """All s in [0, mm) with u[i]^pre[i+s]^pre[i] == w[(i+s)%L] for all i."""
    ll = len(u)
    pre = np.zeros(3 * ll + 1, np.int8)
    for i in range(3 * ll):
        pre[i + 1] = pre[i] ^ e[i % ll]
    blen = mm + ll - 1
    s = np.empty(ll + 1 + blen, np.int8)
    for i in range(ll):
        s[i] = u[i] ^ pre[i]
    s[ll] = 2
    for i in range(blen):
        s[ll + 1 + i] = w[i % ll] ^ pre[i]
    ns = len(s)
    z = np.zeros(ns, np.int64)
    lo, r = 0, 0
    for i in range(1, ns):
        if i < r:
            zi = z[i - lo]
            if zi < r - i:
                z[i] = zi
                continue
            z[i] = r - i
        while i + z[i] < ns and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            lo, r = i, i + z[i]
    out = np.empty(mm, np.int64)
    cnt = 0
    for shift in range(mm):
        if z[ll + 1 + shift] >= ll:
            out[cnt] = shift
            cnt += 1
    return out[:cnt]


def ext_gcd(aa, bb):
    if bb == 0:
        return aa, 1, 0
    d, x, y = ext_gcd(bb, aa % bb)
    return d, y, x - (aa // bb) * y


def solve_from_perm(t0, m, b0, pi, tau, targets, ctx):
    """Minimal t = t0 + nsteps*k + j with all icing up."""
    nsteps = len(targets)
    seen = np.zeros(m, dtype=bool)
    cycles = []
    for start in range(m):
        if seen[start]:
            continue
        cyc = []
        x = start
        while not seen[x]:
            seen[x] = True
            cyc.append(x)
            x = pi[x]
        cycles.append(np.array(cyc, dtype=np.int64))

    best = None
    for j in range(nsteps):
        tgt = targets[j]
        cons = set()
        ok = True
        for cyc in cycles:
            ll = len(cyc)
            u = b0[cyc]
            e = tau[cyc]
            w = tgt[cyc]
            par = int(e.sum()) & 1
            mm = ll if par == 0 else 2 * ll
            allowed = allowed_shifts(u, e, w, mm)
            if len(allowed) == 0:
                ok = False
                break
            if len(allowed) == mm:
                continue
            cons.add((mm, tuple(int(x) for x in allowed)))
        if not ok:
            continue
        if not cons:
            k = 0
        else:
            ordered = sorted(cons, key=lambda t: (len(t[1]) / t[0], -t[0]))
            mod, residues = 1, [0]
            rest = []
            failed = False
            for mm, allowed in ordered:
                g = gcd(mod, mm)
                lcm_ = mod // g * mm
                if mod > 1 and lcm_ // mod * len(residues) > 2_000_000:
                    rest.append((mm, set(allowed)))
                    continue
                newres = []
                for r1 in residues:
                    for r2 in allowed:
                        if (r1 - r2) % g == 0:
                            d, p_, q_ = ext_gcd(mod // g, mm // g)
                            step = (r2 - r1) // g % (mm // g)
                            newres.append((r1 + step * p_ % (mm // g) * mod) % lcm_)
                residues = sorted(set(newres))
                mod = lcm_
                if not residues:
                    failed = True
                    break
            if failed:
                continue
            k = None
            t_ = 0
            while k is None:
                for rr in residues:
                    cand_k = t_ * mod + rr
                    if all(cand_k % mm in aset for mm, aset in rest):
                        k = cand_k
                        break
                t_ += 1
                assert t_ <= 10**7, ctx
        cand = t0 + nsteps * k + j
        if cand >= 1 and (best is None or cand < best):
            best = cand
    assert best is not None, ctx
    return best


def flips(a, b, c):
    """F(a, b, c)."""
    r = isqrt(c)
    sq_r = r if r * r == c else 0
    cap_log2 = 14
    quiesce = 30
    while True:
        cap = 1 << cap_log2
        ref_p = np.empty(cap, np.int64)
        ref_q = np.empty(cap, np.int64)
        ref_b = np.empty(cap, np.int8)
        st, t, m, tr = find_period(a, b, c, sq_r, cap, 500_000_000, quiesce, ref_p, ref_q, ref_b)
        if st == -2:
            cap_log2 += 2
            assert cap_log2 <= 26, (a, b, c)
            continue
        if st == -4:
            quiesce *= 4
            assert quiesce <= 10**7, (a, b, c)
            continue
        break
    if st == 1:
        return t
    assert st == 0, (a, b, c, st)
    nsteps = t - tr
    assert nsteps % 3 == 0 and nsteps <= 96, (a, b, c, nsteps)
    fp = ref_p[:m].copy()
    fq = ref_q[:m].copy()
    b0 = ref_b[:m].copy()
    pi, tau, targets, ok = perm_over_period(a, b, c, sq_r, tr, m, nsteps, fp, fq)
    assert ok == 1, (a, b, c)
    return solve_from_perm(tr, m, b0, pi, tau, targets, (a, b, c))


def flips_direct(a, b, c, max_steps):
    """Pure-python exact step-by-step simulation (validation)."""
    r = isqrt(c)
    square = r * r == c

    def norm(p, q):
        return (p + q * r, 0) if square else (p, q)

    def pos(p, q):
        if square:
            return p + q * r > 0
        if p >= 0 and q >= 0:
            return p > 0 or q > 0
        if p <= 0 and q <= 0:
            return False
        if q > 0:
            return q * q * c > p * p
        return p * p > q * q * c

    sizes = [norm(b * c, 0), norm(a * c, 0), norm(0, a * b)]
    segs = [(a * b * c, 0, 0)]
    for t in range(1, max_steps + 1):
        rem_p, rem_q = sizes[(t - 1) % 3]
        prefix = []
        i = 0
        while True:
            p, q, bt = segs[i]
            dp, dq = rem_p - p, rem_q - q
            if dp == 0 and dq == 0:
                prefix.append((p, q, bt))
                i += 1
                break
            if pos(dp, dq):
                prefix.append((p, q, bt))
                rem_p, rem_q = dp, dq
                i += 1
            else:
                prefix.append((rem_p, rem_q, bt))
                segs[i] = (p - rem_p, q - rem_q, bt)
                break
        segs = segs[i:] + [(p, q, bt ^ 1) for (p, q, bt) in reversed(prefix)]
        if all(bt == 0 for (_, _, bt) in segs):
            return t
    return None


def main() -> None:
    for trip, want in [((9, 10, 11), 60), ((10, 14, 16), 506), ((15, 16, 17), 785232)]:
        assert flips(*trip) == want, trip
    for trip in [(18, 29, 34), (15, 32, 43), (11, 14, 22), (13, 35, 36)]:
        assert flips(*trip) == flips_direct(*trip, max_steps=600000), trip

    def big_g(n):
        return sum(
            flips(a, b, c)
            for a in range(9, n - 1)
            for b in range(a + 1, n)
            for c in range(b + 1, n + 1)
        )

    assert big_g(11) == 60 and big_g(14) == 58020 and big_g(17) == 1269260  # given
    print(big_g(53))  # 329569369413585


if __name__ == "__main__":
    main()
