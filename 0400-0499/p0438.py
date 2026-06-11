from fractions import Fraction

import numba
import numpy as np

def lagrange_weights(t, n):
    xs = np.arange(1, n + 2, dtype=np.float64)
    w = np.zeros(n + 1)
    for ki, x0 in enumerate(xs):
        p = 1.0
        for kj, x1 in enumerate(xs):
            if kj != ki:
                p *= (t - x1) / (x0 - x1)
        w[ki] = p
    return w

def build_constraints(n):
    """Rows (weights over f(1..n+1), lo, hi) that any valid value vector
    must satisfy. Midpoints give |f| caps; exterior integers give
    two-sided windows from the root boxes."""
    rows = []
    los = []
    his = []
    # midpoints
    for i in range(1, n + 1):
        t = i + 0.5
        b = 1.0
        for j in range(1, n + 1):
            b *= max(abs(t - j), abs(t - j - 1))
        rows.append(lagrange_weights(t, n))
        los.append(-b * (1 + 1e-9))
        his.append(b * (1 + 1e-9))
    # exterior points: t <= 0 and t >= n+2
    for t in [0, -1, n + 2, n + 3]:
        lo_m = 1.0
        hi_m = 1.0
        for i in range(1, n + 1):
            if t >= n + 2:
                lo_m *= (t - (i + 1))
                hi_m *= (t - i)
            else:
                lo_m *= (i - t)
                hi_m *= ((i + 1) - t)
        if t >= n + 2:
            lo, hi = lo_m + 1, hi_m  # strict lower (r_i < i+1), attained upper
        else:
            sgn = (-1) ** n
            if sgn > 0:
                lo, hi = lo_m, hi_m - 1
            else:
                lo, hi = -hi_m + 1, -lo_m
        rows.append(lagrange_weights(t, n))
        los.append(float(lo) - 1e-6)
        his.append(float(hi) + 1e-6)
    return np.array(rows), np.array(los), np.array(his)

def caps_and_products(n):
    pts = np.linspace(0, 1, 4001)
    B = np.zeros(n + 2)
    P = np.zeros((n + 2, n + 2))
    for k in range(1, n + 2):
        prod = 1.0
        for i in range(1, n + 1):
            prod *= max(abs(k - i), abs(k - i - 1))
        B[k] = prod * (1 + 1e-9)
    for k in range(1, n + 2):
        for kk in range(1, n + 2):
            if kk != k:
                prod = 1.0
                for i in range(1, n + 1):
                    r = i + pts
                    prod *= np.max(np.abs(k - r) * np.abs(kk - r))
                P[k, kk] = prod * 1.01
    return B, P


@numba.jit(cache=True)
def leaf_value(vals, n, binom, factj):
    """Exact validity + S(t) for the value vector vals[1..n+1].

    Returns S(t) = sum |a_i| if the polynomial has n real roots with
    sorted floors 1..n, else -1. All integer arithmetic:
    - Newton differences give the integer coefficients.
    - Roots at integers k (f(k) = 0) are synthetically divided out; the
      quotient must be nonzero at every integer 1..n+1 and its signs must
      flip exactly across intervals that still need a root and stay put
      across the others. Strict alternation then certifies one real root
      per remaining box, which exhausts the degree.
    """
    # Newton -> monomial coefficients (low -> high), exact
    d = np.empty(n + 1, dtype=np.int64)
    for i in range(n + 1):
        d[i] = vals[1 + i]
    coef = np.zeros(n + 2, dtype=np.int64)
    basis = np.zeros(n + 2, dtype=np.int64)
    nb = np.zeros(n + 2, dtype=np.int64)
    basis[0] = 1
    blen = 1
    for j in range(n + 1):
        c = d[0]
        if j > 0:
            c //= factj[j]
        for dd in range(blen):
            coef[dd] += c * basis[dd]
        # multiply basis by (x - (j+1))
        for dd in range(blen + 1):
            nb[dd] = 0
        for dd in range(blen):
            nb[dd + 1] += basis[dd]
            nb[dd] -= (j + 1) * basis[dd]
        for dd in range(blen + 1):
            basis[dd] = nb[dd]
        blen += 1
        # next difference layer
        for i in range(n - j):
            d[i] = d[i + 1] - d[i]
    # coef[0..n], coef[n] == 1
    # synthetic division by every integer root
    g = np.empty(n + 1, dtype=np.int64)
    for i in range(n + 1):
        g[i] = coef[i]
    deg = n
    in_s = np.ones(n + 1, dtype=np.bool_)  # boxes 1..n still needing a root
    for k in range(1, n + 1):
        if vals[k] == 0:
            # divide g by (x - k): high -> low Horner
            carry = 0
            for dd in range(deg, -1, -1):
                tmp = g[dd] + carry * k
                g[dd] = carry
                carry = tmp
            # carry is the remainder (= 0)
            deg -= 1
            in_s[k] = False
    # evaluate g at 1..n+1 and check the sign pattern
    prev_sign = 0
    for t in range(1, n + 2):
        v = 0
        for dd in range(deg, -1, -1):
            v = v * t + g[dd]
        if v == 0:
            return -1  # repeated integer root: no box for it
        s = 1 if v > 0 else -1
        if t > 1:
            need_flip = in_s[t - 1]
            if need_flip and s == prev_sign:
                return -1
            if not need_flip and s != prev_sign:
                return -1
        prev_sign = s
    total = 0
    for dd in range(n):
        total += coef[dd] if coef[dd] >= 0 else -coef[dd]
    return total

@numba.jit(cache=True)
def dfs(B, P, CW, CLO, CHI, order, n, fact, out):
    nc = len(CLO)
    weights = np.zeros(n + 2, dtype=np.int64)
    for k in range(1, n + 2):
        c = 1
        for t in range(1, k):
            c = c * (n - t + 1) // t
        weights[k] = c
    sign = np.zeros(n + 2, dtype=np.int64)
    for k in range(1, n + 2):
        sign[k] = 1 if (n + 1 - k) % 2 == 0 else -1
    binom = np.zeros((n + 1, n + 1), dtype=np.int64)
    for i in range(n + 1):
        binom[i, 0] = 1
        for j in range(1, i + 1):
            binom[i, j] = binom[i - 1, j - 1] + binom[i - 1, j]
    factj = np.ones(n + 1, dtype=np.int64)
    for j in range(1, n + 1):
        factj[j] = factj[j - 1] * j
    nlev = len(order)
    # suffix intervals: unchosen contributions (incl. points 1 and n+1)
    suf_lo = np.zeros((nlev + 1, nc))
    suf_hi = np.zeros((nlev + 1, nc))
    s1g = sign[1]
    for m in range(nc):
        w8 = CW[m, n]
        w1 = CW[m, 0] * s1g
        suf_lo[nlev, m] = min(0.0, w8 * B[n + 1]) + min(0.0, w1 * B[1])
        suf_hi[nlev, m] = max(0.0, w8 * B[n + 1]) + max(0.0, w1 * B[1])
    for lev in range(nlev - 1, -1, -1):
        k = order[lev]
        for m in range(nc):
            w = CW[m, k - 1] * sign[k]
            c = w * B[k]
            suf_lo[lev, m] = suf_lo[lev + 1, m] + min(0.0, c)
            suf_hi[lev, m] = suf_hi[lev + 1, m] + max(0.0, c)
    vals = np.zeros(n + 2, dtype=np.int64)
    bs = np.zeros(n + 2, dtype=np.int64)
    chosen_pt = np.zeros(n + 2, dtype=np.bool_)
    cur = np.zeros((nlev + 1, nc))
    idx = np.zeros(nlev, dtype=np.int64)
    stepv = np.ones(nlev, dtype=np.int64)
    budget = np.zeros(nlev + 1, dtype=np.int64)
    budget[0] = fact
    nout = 0
    total_s = 0
    lev = 0
    idx[0] = -(1 << 60)
    while lev >= 0:
        if idx[lev] < -1:
            k = order[lev]
            ll = 0
            while k - ll - 1 >= 1 and chosen_pt[k - ll - 1]:
                ll += 1
            rrr = 0
            while k + rrr + 1 <= n + 1 and chosen_pt[k + rrr + 1]:
                rrr += 1
            j = ll if ll >= rrr else rrr
            if j >= 2:
                mmod = factj[j]
                acc = 0
                if ll >= rrr:
                    for i2 in range(j):
                        t = binom[j, i2] * vals[k - j + i2]
                        if (j - i2) % 2 == 1:
                            acc -= t
                        else:
                            acc += t
                    target = (-acc) % mmod
                else:
                    for i2 in range(1, j + 1):
                        t = binom[j, i2] * vals[k + i2]
                        if (j - i2) % 2 == 1:
                            acc -= t
                        else:
                            acc += t
                    if j % 2 == 1:
                        target = acc % mmod
                    else:
                        target = (-acc) % mmod
                sb = (sign[k] * target) % mmod
                stepv[lev] = mmod
                idx[lev] = sb - mmod
            else:
                stepv[lev] = 1
                idx[lev] = -1
        idx[lev] += stepv[lev]
        k = order[lev]
        b = idx[lev]
        cap = budget[lev] // weights[k]
        if cap > int(B[k]):
            cap = int(B[k])
        if b > cap:
            chosen_pt[k] = False
            lev -= 1
            continue
        vk = sign[k] * b
        ok = True
        for d in range(lev):
            kk = order[d]
            if b * bs[kk] > P[k, kk]:
                ok = False
                break
            diff = vk - vals[kk]
            mm = k - kk if k > kk else kk - k
            if diff % mm != 0:
                ok = False
                break
        if ok:
            for m in range(nc):
                c = cur[lev, m] + CW[m, k - 1] * vk
                if c + suf_lo[lev + 1, m] > CHI[m] or c + suf_hi[lev + 1, m] < CLO[m]:
                    ok = False
                    break
        if ok:
            vals[k] = vk
            chosen_pt[k] = True
            lo = k
            while lo - 1 >= 1 and chosen_pt[lo - 1]:
                lo -= 1
            hi = k
            while hi + 1 <= n + 1 and chosen_pt[hi + 1]:
                hi += 1
            for st in range(lo, k + 1):
                for en in range(max(k, st + 2), hi + 1):
                    j = en - st
                    acc = 0
                    for i2 in range(j + 1):
                        t = binom[j, i2] * vals[st + i2]
                        if (j - i2) % 2 == 1:
                            acc -= t
                        else:
                            acc += t
                    if acc % factj[j] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                chosen_pt[k] = False
        if not ok:
            continue
        bs[k] = b
        for m in range(nc):
            cur[lev + 1, m] = cur[lev, m] + CW[m, k - 1] * vk
        if lev == nlev - 1:
            rr = budget[lev] - weights[k] * b
            if rr < 1:
                continue
            if s1g < 0 and rr % n != 0:
                continue
            lo1 = 0.0
            hi1 = min(B[1], float(rr - 1))
            for m in range(nc):
                c0 = cur[lev + 1, m] + CW[m, n] * rr
                c1 = CW[m, 0] * s1g - CW[m, n]
                if c1 > 1e-15:
                    lo = (CLO[m] - c0) / c1
                    hi = (CHI[m] - c0) / c1
                elif c1 < -1e-15:
                    lo = (CHI[m] - c0) / c1
                    hi = (CLO[m] - c0) / c1
                else:
                    if c0 > CHI[m] or c0 < CLO[m]:
                        lo1 = 1.0
                        hi1 = 0.0
                    continue
                if lo > lo1:
                    lo1 = lo
                if hi < hi1:
                    hi1 = hi
            jl = n - 1
            ml = factj[jl]
            accl = 0
            for i2 in range(1, jl + 1):
                t = binom[jl, i2] * vals[1 + i2]
                if (jl - i2) % 2 == 1:
                    accl -= t
                else:
                    accl += t
            tgt = accl % ml if jl % 2 == 1 else (-accl) % ml
            sbl = (sign[1] * tgt) % ml
            b1 = int(np.ceil(lo1 - 1e-9))
            if b1 < 0:
                b1 = 0
            b1 += (sbl - b1) % ml
            b1hi = int(np.floor(hi1 + 1e-9))
            while b1 <= b1hi:
                b8 = rr - b1
                okl = True
                if b8 < 1 or b8 > B[n + 1]:
                    okl = False
                v1 = s1g * b1
                if okl:
                    for d in range(nlev):
                        kk = order[d]
                        if b1 * bs[kk] > P[1, kk] or b8 * bs[kk] > P[n + 1, kk]:
                            okl = False
                            break
                        if kk > 1 and (v1 - vals[kk]) % (kk - 1) != 0:
                            okl = False
                            break
                        if (b8 - vals[kk]) % (n + 1 - kk) != 0:
                            okl = False
                            break
                if okl and b1 * b8 > P[1, n + 1]:
                    okl = False
                if okl and (b8 - v1) % n != 0:
                    okl = False
                if okl:
                    vals[1] = v1
                    vals[n + 1] = b8
                    for j in range(2, n + 1):
                        for st in range(1, n + 2 - j):
                            acc = 0
                            for i2 in range(j + 1):
                                t = binom[j, i2] * vals[st + i2]
                                if (j - i2) % 2 == 1:
                                    acc -= t
                                else:
                                    acc += t
                            if acc % factj[j] != 0:
                                okl = False
                                break
                        if not okl:
                            break
                if okl:
                    for m in range(nc):
                        c = cur[nlev, m] + CW[m, 0] * v1 + CW[m, n] * b8
                        if c > CHI[m] or c < CLO[m]:
                            okl = False
                            break
                if okl:
                    sv = leaf_value(vals, n, binom, factj)
                    if sv >= 0:
                        nout += 1
                        total_s += sv
                b1 += ml
            continue
        budget[lev + 1] = budget[lev] - weights[k] * b
        lev += 1
        idx[lev] = -(1 << 60)
    return nout, total_s

def solve(n, order):
    B, P = caps_and_products(n)
    CW, CLO, CHI = build_constraints(n)
    fact = 1
    for t in range(2, n + 1):
        fact *= t
    out = np.zeros((1, n + 1), dtype=np.int64)
    cnt, total_s = dfs(B, P, CW, CLO, CHI, np.array(order, dtype=np.int64),
                       n, fact, out)
    return cnt, total_s


# --- exact root counting over Fraction, replacing sympy.real_roots in brute ---

def _trim(p: list) -> list:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def _is_zero(p: list) -> bool:
    return not p or (len(p) == 1 and p[0] == 0)


def _eval(p: list, x) -> Fraction:
    v = Fraction(0)
    for c in reversed(p):
        v = v * x + c
    return v


def _rem(a: list, b: list) -> list:
    """Remainder of a / b; polynomials as low->high Fraction lists."""
    a = a[:]
    db = len(b) - 1
    while len(a) - 1 >= db and not _is_zero(a):
        if a[-1] == 0:
            a.pop()
            continue
        f = a[-1] / b[-1]
        s = len(a) - 1 - db
        for i in range(db + 1):
            a[s + i] -= f * b[i]
        a.pop()
    return _trim(a)


def _sturm_chain(f: list) -> list:
    """Canonical Sturm chain f, f', -rem(...), ... (last nonzero ~ gcd(f, f'))."""
    chain = [f, _trim([i * f[i] for i in range(1, len(f))])]
    while True:
        r = _rem(chain[-2], chain[-1])
        if _is_zero(r):
            return chain
        chain.append([-c for c in r])


def _variations_at(chain: list, x) -> int:
    signs = [1 if v > 0 else -1 for v in (_eval(p, x) for p in chain) if v != 0]
    return sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])


def _variations_at_inf(chain: list, positive: bool) -> int:
    signs = []
    for p in chain:
        s = 1 if p[-1] > 0 else -1
        if not positive and (len(p) - 1) % 2 == 1:
            s = -s
        signs.append(s)
    return sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])


def _has_n_real_roots_with_floors(coefs: list[int], n: int) -> bool:
    """Whether the monic integer polynomial (coefs high -> low, degree n) has
    n real roots whose sorted floors are exactly 1..n. Fully exact:

    - Squarefree test: the last element of the Sturm chain is ~gcd(f, f'); a
      repeated root would duplicate a floor, so non-squarefree f is invalid.
    - Integer roots in 1..n+1 are divided out exactly (a root at integer k
      has floor k, so it lands in box k; a root at n+1 fits no box). The
      quotient h is then nonzero at every integer 1..n+1, so Sturm's theorem
      counts its distinct roots in each open box (i, i+1) cleanly.
    - Validity <=> every box [i, i+1) holds exactly one root and the divided
      integer roots plus the real roots of h account for all n roots (which
      also rules out roots outside [1, n+1), real or at stray integers).
    """
    f = [Fraction(c) for c in reversed(coefs)]
    chain = _sturm_chain(f)
    if len(chain[-1]) > 1:
        return False  # gcd(f, f') nonconstant: repeated root
    h = f
    boxes = [0] * (n + 1)
    ndiv = 0
    for k in range(1, n + 2):
        if _eval(h, k) == 0:
            deg = len(h) - 1
            q = [Fraction(0)] * deg
            q[deg - 1] = h[deg]
            for d in range(deg - 2, -1, -1):
                q[d] = h[d + 1] + k * q[d + 1]
            h = q
            ndiv += 1
            if k <= n:
                boxes[k] += 1
    if len(h) > 1:
        ch = _sturm_chain(h)
        var = [_variations_at(ch, k) for k in range(1, n + 2)]
        total_h = _variations_at_inf(ch, False) - _variations_at_inf(ch, True)
        for i in range(1, n + 1):
            boxes[i] += var[i - 1] - var[i]
    else:
        total_h = 0
    if ndiv + total_h != n:
        return False
    return all(boxes[i] == 1 for i in range(1, n + 1))


def brute(n: int):
    """Independent check for tiny n: enumerate coefficients in Vieta boxes
    and validate roots exactly with Sturm chains over Fraction."""
    from itertools import combinations
    from itertools import product as iproduct
    # elementary symmetric ranges from roots in [i, i+1)
    lo_e = [0] * (n + 1)
    hi_e = [0] * (n + 1)
    for k in range(1, n + 1):
        lo_e[k] = sum(int(np.prod(c)) for c in combinations(range(1, n + 1), k))
        hi_e[k] = sum(int(np.prod(c)) for c in combinations(range(2, n + 2), k))
    cnt = 0
    total = 0
    ranges = [range(lo_e[k], hi_e[k] + 1) for k in range(1, n + 1)]
    for es_tuple in iproduct(*ranges):
        coefs = [1]
        for k, e in enumerate(es_tuple, start=1):
            coefs.append((-1) ** k * e)
        if _has_n_real_roots_with_floors(coefs, n):
            cnt += 1
            total += sum(abs(c) for c in coefs[1:])
    return cnt, total

if __name__ == "__main__":
    assert solve(3, [2, 3]) == brute(3)  # full independent pipeline check
    cnt4, s4 = solve(4, [3, 4, 2])
    assert (cnt4, s4) == (12, 2087)  # both given for n = 4
    cnt7, s7 = solve(7, [4, 5, 3, 6, 2, 7])
    assert cnt7 == 24883200  # the Vandermonde volume prod_{i<j} (j - i)
    print(s7)  # 2046409616809
