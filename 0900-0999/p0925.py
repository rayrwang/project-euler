"""Project Euler 925: Larger Digit Permutation III.

B(n^2) = n^2 + Delta where Delta only rearranges the suffix of n^2 up to
its pivot (first place q with digit_q < digit_{q-1}), so

    T(N) = sum n^2 + sum Delta_n - corrections for B = 0.

The n^2 part is N(N+1)(2N+1)/6 mod p.  For the Delta part with N = 10^E,
the pivot of n^2 at place q is determined by n mod 10^(q+1), and since
10^(q+1) | N every residue class contributes exactly 10^(E-1-q) values
of n.  A DFS over n-residue classes mod 10^(j+1) whose square digits
d_0..d_{j-1} weakly increase upward enumerates all pivot configurations:
each pivot leaf at depth q <= E-2 adds Delta * 10^(E-1-q).  Children
digits follow d = (base + 2rc) mod 10, so classes with r = 0 mod 5
extend all ten children with one digit, and the suffix multiset, prefix
value mod p, and Delta (next smallest digit above the pivot, suffix
re-sorted ascending) are maintained incrementally along the path.

At depth E-1 the DFS switches to member enumeration: n = r + t*10^(E-1)
for t = 0..10 covers [1, 10^E]; the remaining digits of n^2 come from
D = n^2 div 10^(E-1) = (r^2 div 10^(E-1)) + 2rt + t^2 * 10^(E-1), which
fits in 64 bits, and each member resolves its pivot directly (or proves
its square's digits fully non-increasing: B = 0, so its n^2 term is
removed).  The only contamination in the class stage comes from numbers
whose square has fewer than E-1 digits and is fully non-increasing:
their class path acquires a fake pivot at place len(n^2) with an
artificial zero digit, which is impossible for any other member of the
same class, so subtracting the fake Delta and the n^2 term for each such
n (all below 10^((E-2)/2)) makes the count argument exact.

Validated against per-term brute force for N = 10^2..10^7 (including
the given T(10) = 270 and T(100) = 335316).  The full run takes a few
minutes single-core.
"""

import numpy as np
from numba import njit, prange

P = 10**9 + 7

PW = np.ones(80, dtype=np.int64)
for i in range(1, 80):
    PW[i] = PW[i - 1] * 10 % P
S = np.zeros(81, dtype=np.int64)
for i in range(1, 81):
    S[i] = (S[i - 1] + PW[i - 1]) % P
POW10 = np.ones(19, dtype=np.int64)
for i in range(1, 19):
    POW10[i] = POW10[i - 1] * 10


@njit(cache=True, inline="always")
def sq_digit(r, j):
    """digit j of r^2 for r < 10^16, j up to 32."""
    a, b = divmod(r, 10**8)
    tw = 2 * a * b
    lo0 = (tw % 10**8) * 10**8 + b * b
    hi = a * a + tw // 10**8 + lo0 // 10**16
    lo = lo0 % 10**16
    if j < 16:
        return (lo // POW10[j]) % 10
    return (hi // POW10[j - 16]) % 10


@njit(cache=True, inline="always")
def leaf_delta(counts, q, v_pref, pd):
    """Delta mod P for pivot digit pd at place q; counts = suffix digit
    multiset (weakly increasing upward), v_pref = suffix value mod P."""
    cand = pd + 1
    while counts[cand] == 0:
        cand += 1
    ns = 0
    place_hi = q
    for g in range(10):
        c = counts[g]
        if g == cand:
            c -= 1
        if g == pd:
            c += 1
        if c:
            seg = (S[place_hi] - S[place_hi - c]) % P
            ns = (ns + g * seg) % P
            place_hi -= c
    return (cand * PW[q] % P + ns - v_pref - pd * PW[q] % P) % P


@njit(cache=True)
def dfs(r, j, last, counts, v_val, e):
    """Weighted Delta sum over the subtree of class r mod 10^j."""
    total = 0
    if j == e - 1:
        nmax = POW10[e]
        mod_j = POW10[e - 1]
        a, b = divmod(r, 10**8)
        tw = 2 * a * b
        lo0 = (tw % 10**8) * 10**8 + b * b
        hi0 = a * a + tw // 10**8 + lo0 // 10**16
        lo_r = lo0 % 10**16
        if e - 1 < 16:
            base = hi0 * (10**16 // POW10[e - 1]) + lo_r // POW10[e - 1]
        else:
            base = hi0 // POW10[e - 17]
        for t in range(11):
            n = r + t * mod_j
            if n < 1 or n > nmax:
                continue
            dd = base + 2 * r * t + t * t * mod_j  # n^2 // 10^(e-1)
            if dd == 0:
                nm = n % P
                total = (total - nm * nm) % P
                continue
            d0 = dd % 10
            if d0 < last:
                total = (total + leaf_delta(counts, j, v_val, d0)) % P
                continue
            cc = counts.copy()
            cc[d0] += 1
            la = d0
            vv = (v_val + d0 * PW[j]) % P
            q = j + 1
            dd //= 10
            found = False
            while dd:
                d = dd % 10
                if d < la:
                    total = (total + leaf_delta(cc, q, vv, d)) % P
                    found = True
                    break
                cc[d] += 1
                vv = (vv + d * PW[q]) % P
                la = d
                q += 1
                dd //= 10
            if not found:
                nm = n % P
                total = (total - nm * nm) % P
        return total
    mod = POW10[j]
    step = (2 * r) % 10
    base = sq_digit(r, j)
    if step == 0:
        d = base
        if j > 0 and d < last:
            return leaf_delta(counts, j, v_val, d) * 10 % P \
                * PW[e - 1 - j] % P
        counts[d] += 1
        nv = (v_val + d * PW[j]) % P
        for c in range(10):
            total = (total + dfs(r + c * mod, j + 1, d, counts, nv, e)) % P
        counts[d] -= 1
        return total
    for c in range(10):
        d = (base + step * c) % 10
        if j > 0 and d < last:
            total = (total + leaf_delta(counts, j, v_val, d)
                     * PW[e - 1 - j]) % P
        else:
            counts[d] += 1
            total = (total + dfs(r + c * mod, j + 1, d, counts,
                                 (v_val + d * PW[j]) % P, e)) % P
            counts[d] -= 1
    return total


@njit(cache=True, parallel=True)
def run_parallel(roots_r, roots_last, roots_counts, roots_v, d0, e):
    out = np.zeros(len(roots_r), dtype=np.int64)
    for i in prange(len(roots_r)):  # ty: ignore[not-iterable]
        counts = roots_counts[i].copy()
        out[i] = dfs(roots_r[i], d0, roots_last[i], counts, roots_v[i], e)
    return out


@njit(cache=True)
def small_b0_correction(e):
    """n with n^2 fully non-increasing and n^2 < 10^(e-2): undo the fake
    class-stage pivot (artificial 0 at place len) and the n^2 term."""
    total = 0
    lim = 10 ** (e - 2) if e >= 2 else 1
    n = 1
    while n * n < lim:
        sq = n * n
        x = sq
        last = x % 10
        x //= 10
        ok = True
        ln = 1
        counts = np.zeros(10, dtype=np.int64)
        counts[last] = 1
        v = last % P
        while x:
            d = x % 10
            if d < last:
                ok = False
                break
            counts[d] += 1
            v = (v + d * PW[ln]) % P
            last = d
            ln += 1
            x //= 10
        if ok:
            fake = leaf_delta(counts, ln, v, 0)
            total = (total - fake - sq % P) % P
        n += 1
    return total


def solve(e: int, d0: int = 4) -> int:
    n_max = 10**e
    total = (n_max % P) * ((n_max + 1) % P) % P * ((2 * n_max + 1) % P) % P \
        * pow(6, P - 2, P) % P
    d0 = min(d0, e - 1)
    roots = []
    shallow = [0]

    def go(r, j, last, counts, v_val):
        if j == d0:
            roots.append((r, last, counts.copy(), v_val))
            return
        mod = 10**j
        for c in range(10):
            n2 = r + c * mod
            d = (n2 * n2 // 10**j) % 10
            if j == 0 or d >= last:
                counts[d] += 1
                go(n2, j + 1, d, counts, (v_val + d * pow(10, j, P)) % P)
                counts[d] -= 1
            else:
                shallow[0] = (shallow[0]
                              + int(leaf_delta(counts, j, v_val, d))
                              * pow(10, e - 1 - j, P)) % P

    go(0, 0, -1, np.zeros(10, dtype=np.int64), 0)
    total = (total + shallow[0]) % P
    rr = np.array([x[0] for x in roots], dtype=np.int64)
    rl = np.array([x[1] for x in roots], dtype=np.int64)
    rc = np.stack([x[2] for x in roots]).astype(np.int64)
    rv = np.array([x[3] for x in roots], dtype=np.int64)
    out = run_parallel(rr, rl, rc, rv, d0, e)
    total = (total + int(out.sum() % P)) % P
    total = (total + int(small_b0_correction(e))) % P
    return total % P


@njit(cache=True)
def brute_t(n_max: int) -> int:
    """Per-term reference: pivot and Delta straight from the digits."""
    tot = 0
    digs = np.zeros(40, dtype=np.int64)
    for n in range(1, n_max + 1):
        a, b = divmod(n, 10**8)
        tw = 2 * a * b
        lo0 = (tw % 10**8) * 10**8 + b * b
        hi = a * a + tw // 10**8 + lo0 // 10**16
        lo = lo0 % 10**16
        ln = 0
        x = lo
        for _ in range(16):
            digs[ln] = x % 10
            x //= 10
            ln += 1
        x = hi
        for _ in range(20):
            digs[ln] = x % 10
            x //= 10
            ln += 1
        ln = 36
        while ln > 1 and digs[ln - 1] == 0:
            ln -= 1
        q = -1
        for i in range(1, ln):
            if digs[i] < digs[i - 1]:
                q = i
                break
        if q < 0:
            continue
        counts = np.zeros(10, dtype=np.int64)
        v = 0
        for i in range(q):
            counts[digs[i]] += 1
            v = (v + digs[i] * PW[i]) % P
        d = leaf_delta(counts, q, v, digs[q])
        sqm = (n % P) * (n % P) % P
        tot = (tot + sqm + d) % P
    return tot


if __name__ == "__main__":
    assert brute_t(10) == 270  # given
    assert brute_t(100) == 335316  # given
    for e_chk in (2, 3, 4, 5, 6):
        assert solve(e_chk) == brute_t(10**e_chk), e_chk
    print(solve(16, d0=5))  # 400034379
