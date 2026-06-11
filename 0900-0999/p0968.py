"""Project Euler 968: Quintuple Restricted Sums.

P(X...) is the sum of 2^a 3^b 5^c 7^d 11^e over non-negative quintuples
with all ten pairwise sums bounded: x_i + x_j <= X_ij. The bounds are of
order 10^9, so the lattice polytope is summed symbolically.

Engine (exact Fourier-Motzkin style summation): a term is a coefficient
times a single monomial times prod_i w_i^{x_i} over a region cut out by
constraints of the closed class
    lo_i <= x_i <= hi_i,   x_i + x_j <= shi_ij,
    x_i + x_j >= slo_ij,   x_i - x_j <= dif_ij.
To sum out x_t, collect its candidate lower bounds (constants, x_j - d,
s - x_j) and upper bounds (constants, x_j + d, s - x_j); split into cases
by which candidate binds (argmax of lowers, argmin of uppers, with strict
integer tie-breaks so each lattice point is counted exactly once). Every
comparison between two candidates is again a constraint of the class, and
numeric comparisons collapse immediately. Within a case,

    sum_{x=l}^{u} x^k w^x = w^{u+1} B_k(u+1) - w^l B_k(l),

where w B_k(n+1) - B_k(n) = n^k determines the degree-k polynomial B_k
(solvable since w != 1; weights are tracked exactly as exponent vectors
over the primes 2, 3, 5, 7, 11 so w = 1 is detected exactly, in which
case Faulhaber polynomials are used instead). Substituting the linear
bound form n = +-x_j + c transfers the exponential weight w^{+-1} onto
x_j and leaves a polynomial in x_j, so the term class is closed and the
recursion terminates after five eliminations.

The engine is validated against a direct five-fold brute force on thirty
random small bound sets and reproduces both given values
P(2,...,2) = 7120 and P(1,...,10) = 799809376 (mod 10^9 + 7). Each
evaluation with 10^9-scale bounds takes ~10 ms, and the final sum of
Q(n) for n < 100 follows in about a second.
"""

from itertools import product

P = 10**9 + 7
PRIMES = (2, 3, 5, 7, 11)
INV = {q: pow(q, P - 2, P) for q in PRIMES}


def wval(vec):
    """Value mod P of weight vector (exponents of 2,3,5,7,11)."""
    r = 1
    for q, e in zip(PRIMES, vec):
        r = r * (pow(q, e, P) if e >= 0 else pow(INV[q], -e, P)) % P
    return r


def wpow(vec, c):
    """vec^c mod P for possibly huge / negative integer c."""
    v = wval(vec)
    return pow(v, c % (P - 1), P)


def bk_polys(wv, kmax):
    """B_k polynomials (coeff lists, B_k[j] = coeff of n^j) satisfying
    w*B_k(n+1) - B_k(n) = n^k, for k = 0..kmax. Requires wv != 1 mod P."""
    from math import comb

    out = []
    for k in range(kmax + 1):
        b = [0] * (k + 1)
        # solve top down: coefficient of n^m in w*B(n+1) - B(n):
        # sum_{j>=m} b_j (w*C(j,m)) - b_m = [m == k]
        for m in range(k, -1, -1):
            s = 0
            for j in range(m + 1, k + 1):
                s = (s + b[j] * wv % P * comb(j, m)) % P
            rhs = (1 if m == k else 0) - s
            denom = (wv - 1) % P
            b[m] = rhs % P * pow(denom, P - 2, P) % P
        out.append(b)
    return out


def faulhaber(kmax):
    """F_k coeff lists with F_k(n) = sum_{x=0}^{n-1} x^k (degree k+1)."""
    from math import comb

    # Use recursion: F_k(n) = (n^{k+1} - sum_{j<k} C(k+1,j) F_j(n)) / (k+1)
    fs = []
    for k in range(kmax + 1):
        coeffs = [0] * (k + 2)
        coeffs[k + 1] = 1  # n^{k+1}
        for j in range(k):
            cj = comb(k + 1, j)
            for d, c in enumerate(fs[j]):
                coeffs[d] = (coeffs[d] - cj * c) % P
        inv = pow(k + 1, P - 2, P)
        fs.append([c * inv % P for c in coeffs])
    return fs


FAUL = faulhaber(8)


def poly_eval_shift(coeffs, s, c):
    """Given polynomial sum coeffs[j] * n^j, substitute n = s*x + c
    (s in {-1,0,1}, c integer): return dict power_of_x -> coeff mod P."""
    from math import comb

    cm = c % P
    out = {}
    for j, a in enumerate(coeffs):
        if a == 0:
            continue
        if s == 0:
            out[0] = (out.get(0, 0) + a * pow(cm, j, P)) % P
        else:
            for i in range(j + 1):
                term = a * comb(j, i) % P * pow(cm, j - i, P) % P
                if s == -1 and i % 2 == 1:
                    term = -term % P
                out[i] = (out.get(i, 0) + term) % P
    return {k: v for k, v in out.items() if v}


class Term:
    __slots__ = ("c", "mono", "wt", "lo", "hi", "shi", "slo", "dif", "vars")

    def __init__(self, c, mono, wt, lo, hi, shi, slo, dif, vars_):
        self.c = c
        self.mono = mono
        self.wt = wt
        self.lo = lo
        self.hi = hi
        self.shi = shi
        self.slo = slo
        self.dif = dif
        self.vars = vars_

    def clone(self):
        return Term(
            self.c,
            dict(self.mono),
            {k: tuple(v) for k, v in self.wt.items()},
            dict(self.lo),
            dict(self.hi),
            dict(self.shi),
            dict(self.slo),
            dict(self.dif),
            set(self.vars),
        )


def add_le(t, v1, s1, c1, v2, s2, c2) -> bool:
    """Add constraint s1*x_{v1} + c1 <= s2*x_{v2} + c2 (v may be None).
    Returns False if region becomes empty (numerically)."""
    # normalize: move to  a*x_i + b*x_j <= c  with a,b in {-1,0,1}
    if v1 is None and v2 is None:
        return c1 <= c2
    if v1 == v2:
        s = s1 - s2
        c = c2 - c1
        if s == 0:
            return c >= 0
        if s > 0:  # s*x <= c, s in {1,2}
            return set_hi(t, v1, c // s)
        return set_lo(t, v1, -(c // (-s)))
    if v1 is None:
        # c1 <= s2 x + c2: -s2 x <= c2 - c1
        if s2 == 1:
            return set_lo(t, v2, c1 - c2)
        return set_hi(t, v2, c2 - c1)
    if v2 is None:
        if s1 == 1:
            return set_hi(t, v1, c2 - c1)
        return set_lo(t, v1, c1 - c2)
    # two distinct variables
    c = c2 - c1
    if s1 == 1 and s2 == 1:
        # x1 - x2 <= c
        key = (v1, v2)
        t.dif[key] = min(t.dif.get(key, c), c)
    elif s1 == 1 and s2 == -1:
        # x1 + x2 <= c
        key = frozenset((v1, v2))
        t.shi[key] = min(t.shi.get(key, c), c)
    elif s1 == -1 and s2 == 1:
        # -x1 - x2 <= c: x1 + x2 >= -c
        key = frozenset((v1, v2))
        t.slo[key] = max(t.slo.get(key, -c), -c)
    else:
        # -x1 + x2 >= -c: x2 - x1 <= ... wait: -x1 + c1 <= -x2 + c2
        # => x2 - x1 <= c
        key = (v2, v1)
        t.dif[key] = min(t.dif.get(key, c), c)
    # quick numeric checks
    for key in list(t.shi):
        if key in t.slo and t.slo[key] > t.shi[key]:
            return False
    return True


def set_hi(t, v, val) -> bool:
    cur = t.hi.get(v)
    t.hi[v] = val if cur is None else min(cur, val)
    return t.lo[v] <= t.hi[v]


def set_lo(t, v, val) -> bool:
    t.lo[v] = max(t.lo[v], val)
    return t.hi.get(v) is None or t.lo[v] <= t.hi[v]


def candidates(t, x):
    """(lowers, uppers) lists of (var_or_None, sign, const) for x's range."""
    lows = {(None, 0): t.lo[x]}
    ups = {}
    if t.hi.get(x) is not None:
        ups[(None, 0)] = t.hi[x]
    for (i, j), d in t.dif.items():
        if i == x and j in t.vars:
            ups[(j, 1)] = min(ups.get((j, 1), d), d)  # x <= x_j + d
        elif j == x and i in t.vars:
            lows[(i, 1)] = max(lows.get((i, 1), -d), -d)  # x >= x_i - d
    for key, sv in t.shi.items():
        if x in key:
            (j,) = key - {x}
            if j in t.vars:
                ups[(j, -1)] = min(ups.get((j, -1), sv), sv)
    for key, sv in t.slo.items():
        if x in key:
            (j,) = key - {x}
            if j in t.vars:
                lows[(j, -1)] = max(lows.get((j, -1), sv), sv)
    lo_list = [(v, s, c) for (v, s), c in lows.items()]
    up_list = [(v, s, c) for (v, s), c in ups.items()]
    return lo_list, up_list


def strip_var(t, x):
    """Remove all constraints mentioning x (they were consumed)."""
    t.vars.discard(x)
    t.lo.pop(x, None)
    t.hi.pop(x, None)
    for key in [k for k in t.dif if x in k]:
        del t.dif[key]
    for key in [k for k in t.shi if x in k]:
        del t.shi[key]
    for key in [k for k in t.slo if x in k]:
        del t.slo[key]
    t.wt.pop(x, None)
    t.mono.pop(x, None)


def eval_term(t) -> int:
    if not t.vars:
        return t.c
    # pick variable with fewest candidate pairs
    options = []
    for x in t.vars:
        lo_l, up_l = candidates(t, x)
        options.append((len(lo_l) * len(up_l), x, lo_l, up_l))
    _, x, lo_l, up_l = min(options, key=lambda o: o[0])
    total = 0
    for li, lcand in enumerate(lo_l):
        for ui, ucand in enumerate(up_l):
            t2 = t.clone()
            ok = True
            # lcand is the max of lowers: lcand >= others (strict for
            # earlier indices to break ties)
            for li2, other in enumerate(lo_l):
                if li2 == li:
                    continue
                # other <= lcand  (strict if li2 < li: other <= lcand - 1)
                adj = -1 if li2 < li else 0
                ok = add_le(
                    t2,
                    other[0],
                    other[1],
                    other[2],
                    lcand[0],
                    lcand[1],
                    lcand[2] + adj,
                )
                if not ok:
                    break
            if not ok:
                continue
            for ui2, other in enumerate(up_l):
                if ui2 == ui:
                    continue
                adj = 1 if ui2 < ui else 0
                ok = add_le(
                    t2,
                    ucand[0],
                    ucand[1],
                    ucand[2] + adj,
                    other[0],
                    other[1],
                    other[2],
                )
                if not ok:
                    break
            if not ok:
                continue
            # l <= u
            ok = add_le(t2, lcand[0], lcand[1], lcand[2], ucand[0], ucand[1], ucand[2])
            if not ok:
                continue
            total = (total + sum_var(t2, x, lcand, ucand)) % P
    return total


def sum_var(t, x, lcand, ucand) -> int:
    """Sum out x over [l, u] given binding candidates; returns value."""
    k = t.mono.get(x, 0)
    wvec = t.wt[x]
    lvar, lsign, lconst = lcand
    uvar, usign, uconst = ucand
    sub = []
    if any(wvec):
        wv = wval(wvec)
        if wv == 1:
            raise AssertionError("weight collided with 1 mod P")
        bks = bk_polys(wv, k)
        bk = bks[k]
        # + w^{u+1} B_k(u+1)
        sub.append((1, uvar, usign, uconst, 1, bk, wvec))
        # - w^{l} B_k(l)
        sub.append((-1, lvar, lsign, lconst, 0, bk, wvec))
    else:
        fk = FAUL[k]  # F_k(n) = sum_{x<n} x^k
        # sum_{l}^{u} = F_k(u+1) - F_k(l)
        sub.append((1, uvar, usign, uconst, 1, fk, None))
        sub.append((-1, lvar, lsign, lconst, 0, fk, None))
    total = 0
    for sign, bvar, bsign, bconst, shift, poly, wv in sub:
        t3 = t.clone()
        strip_var(t3, x)
        n_const = bconst + shift  # n = bsign*x_{bvar} + n_const
        coef_mult = sign % P
        if wv is not None:
            # w^{n} where n = bsign*x_bvar + n_const
            coef_mult = coef_mult * wpow(wv, n_const) % P
            if bvar is not None and bsign != 0:
                old = t3.wt[bvar]
                t3.wt[bvar] = tuple(o + bsign * w for o, w in zip(old, wv))
        pieces = poly_eval_shift(poly, bsign if bvar is not None else 0, n_const)
        for power, pc in pieces.items():
            t4 = t3.clone()
            t4.c = t4.c * coef_mult % P * pc % P
            if power:
                if bvar is None:
                    raise AssertionError
                t4.mono[bvar] = t4.mono.get(bvar, 0) + power
            total = (total + eval_term(t4)) % P
    return total


def p_of(xs: dict) -> int:
    """P with sum bounds xs[frozenset((i,j))]."""
    vs = "abcde"
    t = Term(
        1,
        {},
        {v: tuple(1 if i == k else 0 for i in range(5)) for k, v in enumerate(vs)},
        {v: 0 for v in vs},
        {},
        dict(xs),
        {},
        {},
        set(vs),
    )
    return eval_term(t)


def p_brute(xs: dict) -> int:
    vs = "abcde"
    lims = {}
    for v in vs:
        m = min(xs[key] for key in xs if v in key)
        lims[v] = m
    tot = 0
    for combo in product(*(range(lims[v] + 1) for v in vs)):
        pt = dict(zip(vs, combo))
        if all(
            pt[i] + pt[j] <= s for key, s in xs.items() for i, j in [tuple(sorted(key))]
        ):
            val = 1
            for q, v in zip(PRIMES, vs):
                val *= q ** pt[v]
            tot += val
    return tot % P


def make_xs(vals10):
    vs = "abcde"
    pairs = [frozenset((vs[i], vs[j])) for i in range(5) for j in range(i + 1, 5)]
    return dict(zip(pairs, vals10))


def solve() -> int:
    import random

    random.seed(7)
    for _ in range(30):
        xs = make_xs([random.randint(0, 6) for _ in range(10)])
        assert p_brute(xs) == p_of(xs)
    assert p_of(make_xs([2] * 10)) == 7120
    assert p_of(make_xs(list(range(1, 11)))) == 799809376
    seq = [1, 7]
    for _ in range(2, 1000):
        seq.append((7 * seq[-1] + seq[-2] ** 2) % P)
    total = 0
    for n in range(100):
        total = (total + p_of(make_xs(seq[10 * n : 10 * n + 10]))) % P
    return total


if __name__ == "__main__":
    print(solve())  # 885362394
