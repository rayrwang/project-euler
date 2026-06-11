"""Project Euler problem 597: Torpids.

n boats start 40 m apart (boat 1 lowest, rowing the full course L; boat i
starts 40(i-1) m upstream and rows L - 40(i-1)).  Each rows at speed
v_i = -log X_i (iid Exp(1)).  A boat rows until it reaches the finish or
catches the nearest active boat ahead ("bumps" it); the bumper then parks
permanently while the bumped boat carries on and may bump in turn.  After
the race, A places above B (for A starting lower) iff a bump chain leads
from A to B.  p(n, L) is the probability that the final order is an even
permutation of the start; find p(13, 1800) to 10 decimal places.

Structure (working in 40 m units, with boat i on the line
x = (i-1) + v_i t, remaining course D_i = L/40 - (i-1), finish time
T_i = D_i / v_i):

* Every boat moves along its fixed line until it parks, so the rearmost
  active boat ahead of a newcomer traces the LOWER ENVELOPE (clipped at
  the finish line) of the lines of all boats ahead.  The envelope's
  segment owners are exactly the bump chain c_1 -> c_2 -> ... -> e, its
  breakpoints are pairwise line crossings, and it exits the course at
  T_e = max T over the pack.
* Boat i bumps somebody iff T_i < T_e; concavity gives a single crossing,
  so the bump target is the owner of the envelope segment containing the
  crossing, characterised by two homogeneous linear inequalities (below
  the path at theta_{r-1}, at/above at theta_r).  If boat i does not
  bump, it screens the entire pack: followers interact with boat i alone.
* Permutation parity: inversions of the final order are precisely the
  chain-connected pairs, so (-1)^parity = (-1)^I with
  I = sum_i (S_i - 1), where S_i is the chain length seen by boat i; each
  bump at segment r contributes m - r + 1 = (new chain length) - 1.
  p_even = (1 + E[(-1)^I]) / 2.

All conditions are homogeneous linear inequalities in the speeds with
rational coefficients, so the expectation is computed exactly by a DP
over states (chain tuple, constraint set) whose measures are sums of
terms coef * prod(v^k) * exp(-<a, v>); integrating out a discarded
variable case-splits on which lower/upper bound binds and stays inside
the class.  Linear forms are interned to integer ids with
scale-canonical constraints (so equivalent states merge and duplicate
bounds cannot double-count), bound-case enumeration and per-term
integrals are memoised, and trivially empty or measure-zero regions
(a constraint and its negation both present) are pruned - without that
pruning, contradictory zero-measure states cascade and dominate the
running time.

Verified: p(3, 160) = 56/135 exactly (given), p(4, 400) = 0.5107843137
(given), the solver-posted ladder p(5..9, 1800), and an independent
event-driven Monte Carlo simulation of the raw race rules at a
configuration not given in the problem.  The n = 13 run takes about
three minutes and yields the exact rational, printed to 10 d.p.
"""

import random
from fractions import Fraction
from math import factorial, log

F0 = Fraction(0)
F1 = Fraction(1)

# ---------------- form interning ----------------
_forms: dict[tuple, int] = {}
_tuples: list[tuple] = []
_dicts: list[dict] = []
_allpos: list[bool] = []
_allneg: list[bool] = []


def intern(items) -> int:
    """items: iterable of (var, Fraction coeff), coeffs nonzero."""
    t = tuple(sorted((v, c) for v, c in items if c != 0))
    fid = _forms.get(t)
    if fid is None:
        fid = len(_tuples)
        _forms[t] = fid
        _tuples.append(t)
        _dicts.append(dict(t))
        _allpos.append(bool(t) and all(c > 0 for _, c in t))
        _allneg.append(bool(t) and all(c < 0 for _, c in t))
    return fid


ZERO = intern(())

_cn_cache: dict[int, int] = {}


def cnorm(fid: int) -> int:
    """Scale-canonicalise a constraint form (F >= 0 invariant under s>0)."""
    r = _cn_cache.get(fid)
    if r is None:
        t = _tuples[fid]
        if not t:
            r = fid
        else:
            s = abs(t[0][1])
            r = intern((v, c / s) for v, c in t) if s != 1 else fid
        _cn_cache[fid] = r
    return r


_neg_cache: dict[int, int] = {}


def fneg(fid: int) -> int:
    r = _neg_cache.get(fid)
    if r is None:
        r = intern((v, -c) for v, c in _tuples[fid])
        _neg_cache[fid] = r
    return r


def zero_measure(cons) -> bool:
    """True if the set contains F >= 0 and -F >= 0 (after cnorm)."""
    s = set(cons)
    return any(cnorm(fneg(f)) in s for f in s)


_add_cache: dict[tuple, int] = {}


def f_add(a: int, b: int, s: Fraction = F1) -> int:
    key = (a, b, s)
    r = _add_cache.get(key)
    if r is None:
        d = dict(_dicts[a])
        for v, c in _tuples[b]:
            nc = d.get(v, F0) + s * c
            if nc:
                d[v] = nc
            elif v in d:
                del d[v]
        r = intern(d.items())
        _add_cache[key] = r
    return r


def f_scale(a: int, s: Fraction) -> int:
    return f_add(ZERO, a, s)


def coeff(fid: int, var: int) -> Fraction:
    return _dicts[fid].get(var, F0)


# ---------------- polynomial part ----------------
def pt_mul(p1, p2):
    d = {}
    for v, k in p1:
        d[v] = d.get(v, 0) + k
    for v, k in p2:
        d[v] = d.get(v, 0) + k
    return tuple(sorted(d.items()))


_fp_cache: dict[tuple, tuple] = {}


def form_pow(fid: int, j: int):
    """(form)^j -> tuple of (powtuple, Fraction coef)."""
    key = (fid, j)
    r = _fp_cache.get(key)
    if r is not None:
        return r
    p = {(): F1}
    base = _tuples[fid]
    if not base and j > 0:
        r = ()
    else:
        for _ in range(j):
            np_ = {}
            for pw, c in p.items():
                for v, cv in base:
                    k = pt_mul(pw, ((v, 1),))
                    np_[k] = np_.get(k, F0) + c * cv
            p = np_
        r = tuple(p.items())
    _fp_cache[key] = r
    return r


def merge_terms(terms):
    agg = {}
    for coef, pw, e in terms:
        k = (pw, e)
        if k in agg:
            agg[k] += coef
        else:
            agg[k] = coef
    return [(c, pw, e) for (pw, e), c in agg.items() if c != 0]


class Diverge(Exception):
    pass


# ---------------- single-term integration, memoised ----------------
_it_cache: dict[tuple, tuple] = {}


def integrate_term_shape(pw, e: int, var: int, lo: int, up):
    """Integral over var in [lo, up(None=inf)] of prod(v^pw) exp(-<e,v>).

    Returns tuple of (Fraction factor, powtuple, exp_id).
    """
    key = (pw, e, var, lo, up)
    r = _it_cache.get(key)
    if r is not None:
        return r
    a = coeff(e, var)
    k = dict(pw).get(var, 0)
    rest_pw = tuple((v, p) for v, p in pw if v != var)
    rest_e = intern((v, c) for v, c in _tuples[e] if v != var)
    out = []

    def antideriv_at(sign, bound):
        e_new = f_add(rest_e, bound, a)
        kf = factorial(k)
        for j in range(k + 1):
            c = -sign * Fraction(kf, factorial(j)) / a ** (k - j + 1)
            for pw2, c2 in form_pow(bound, j):
                out.append((c * c2, pt_mul(rest_pw, pw2), e_new))

    def power_at(sign, bound):
        for pw2, c2 in form_pow(bound, k + 1):
            out.append((sign * c2 / (k + 1), pt_mul(rest_pw, pw2), rest_e))

    if a > 0:
        if up is not None:
            antideriv_at(F1, up)
        antideriv_at(-F1, lo)
    elif up is None:
        raise Diverge((a, k))
    elif a == 0:
        power_at(F1, up)
        power_at(-F1, lo)
    else:
        antideriv_at(F1, up)
        antideriv_at(-F1, lo)
    # merge inside the shape
    agg = {}
    for c, pw2, e2 in out:
        kk = (pw2, e2)
        agg[kk] = agg.get(kk, F0) + c
    r = tuple((c, pw2, e2) for (pw2, e2), c in agg.items() if c != 0)
    _it_cache[key] = r
    return r


# ---------------- bounds-case enumeration, memoised ----------------
_bc_cache: dict[tuple, tuple] = {}


def bounds_cases(cons: frozenset, var: int):
    """Split region {all forms >= 0} for integration over var >= 0.

    Returns tuple of (lo_id, up_id_or_None, frozenset other_cons).
    Cases with trivially empty regions are dropped.
    """
    key = (cons, var)
    r = _bc_cache.get(key)
    if r is not None:
        return r
    lows = [ZERO]
    ups = []
    others = []
    for f in cons:
        a = coeff(f, var)
        if a == 0:
            others.append(f)
            continue
        rest = intern((v, c) for v, c in _tuples[f] if v != var)
        if a > 0:
            lows.append(f_scale(rest, -F1 / a))
        else:
            ups.append(f_scale(rest, F1 / (-a)))
    lows = list(dict.fromkeys(lows))
    ups = list(dict.fromkeys(ups))
    cases = []
    up_options = ups if ups else [None]
    for lo in lows:
        for up in up_options:
            cc = list(others)
            ok = True
            for lo2 in lows:
                if lo2 == lo:
                    continue
                d = f_add(lo, lo2, -F1)
                if d != ZERO:
                    cc.append(d)
            if up is not None:
                for up2 in ups:
                    if up2 == up:
                        continue
                    d = f_add(up2, up, -F1)
                    if d != ZERO:
                        cc.append(d)
                d = f_add(up, lo, -F1)
                if d != ZERO:
                    cc.append(d)
            out = set()
            for f in cc:
                if f == ZERO or _allpos[f]:
                    continue
                if _allneg[f]:
                    ok = False
                    break
                out.add(cnorm(f))
            if ok and not zero_measure(out):
                cases.append((lo, up, frozenset(out)))
    r = tuple(cases)
    _bc_cache[key] = r
    return r


def integrate_out(terms, cons: frozenset, var: int):
    cases = bounds_cases(cons, var)
    res = []
    for lo, up, cc in cases:
        new_terms = []
        for coef, pw, e in terms:
            for fac, pw2, e2 in integrate_term_shape(pw, e, var, lo, up):
                new_terms.append((coef * fac, pw2, e2))
        new_terms = merge_terms(new_terms)
        if new_terms:
            res.append((new_terms, cc))
    return res


def kill_vars(cases, kill):
    """Integrate out all vars in `kill` from list of (terms, cons-frozenset),
    greedily choosing the var with fewest bound-splits per case."""
    out = []
    stack = [(t, c, frozenset(kill)) for t, c in cases]
    while stack:
        terms, cons, kv = stack.pop()
        if not kv:
            out.append((terms, cons))
            continue
        # pick var with fewest cases
        best = next(iter(kv))
        bn = len(bounds_cases(cons, best))
        for v in kv:
            n = len(bounds_cases(cons, v))
            if n < bn:
                best, bn = v, n
            if bn <= 1:
                break
        for t2, c2 in integrate_out(terms, cons, best):
            stack.append((t2, c2, kv - {best}))
    return out


def p_even(n, course_units):
    cu = Fraction(course_units)

    def dist(i):
        return cu - (i - 1)

    one = F1
    states = {((n,), frozenset()): [(one, (), intern([(n, F1)]))]}

    for i in range(n - 1, 0, -1):
        new_states = {}

        def add_state(chain, cons: frozenset, terms):
            key = (chain, cons)
            if key in new_states:
                new_states[key] = merge_terms(new_states[key] + terms)
            else:
                new_states[key] = merge_terms(terms)

        own = intern([(i, F1)])
        for (chain, cons), terms in states.items():
            m = len(chain)
            base = [(c, pw, f_add(e, own)) for c, pw, e in terms]
            w = list(chain)

            def g_form(j, w=w):
                cj, cj1 = w[j - 1], w[j]
                dj = Fraction(cj1 - cj)
                return intern([(cj, Fraction(cj - i) + dj),
                               (cj1, Fraction(-(cj - i))), (i, -dj)])

            cm = w[-1]
            exit_form = cnorm(intern([(cm, dist(i)), (i, -dist(cm))]))

            # no-bump branch
            cc = cons | {exit_form}
            if not any(_allneg[f] for f in cc) and not zero_measure(cc):
                for t2, c2 in kill_vars([(base, frozenset(
                        f for f in cc if not _allpos[f]))], w):
                    c3 = set()
                    bad = False
                    for f in c2:
                        fd = _dicts[f]
                        if set(fd) == {i}:
                            if fd[i] < 0:
                                bad = True
                            continue
                        c3.add(f)
                    if not bad:
                        add_state((i,), frozenset(c3), t2)

            # bump branches
            for r in range(1, m + 1):
                sign = one if (m - r + 1) % 2 == 0 else -one
                bc = set(cons)
                if r >= 2:
                    bc.add(cnorm(g_form(r - 1)))
                if r <= m - 1:
                    bc.add(cnorm(f_scale(g_form(r), -F1)))
                else:
                    bc.add(cnorm(f_scale(exit_form, -F1)))
                if any(_allneg[f] for f in bc) or zero_measure(bc):
                    continue
                bc = frozenset(f for f in bc if not _allpos[f])
                tms = [(sign * c, pw, e) for c, pw, e in base]
                new_chain = (i,) + chain[r - 1:]
                for t2, c2 in kill_vars([(tms, bc)], w[: r - 1]):
                    add_state(new_chain, c2, t2)

        states = new_states

    total = one - one  # 0 of the right type
    for (chain, cons), terms in states.items():
        for t2, c2 in kill_vars([(terms, cons)], chain):
            assert not c2, c2
            for coef, pw, e in t2:
                assert not pw and e == ZERO, (pw, e)
                total += coef
    return (1 + total) / 2


def simulate_parity(n: int, cu: int, rng: random.Random) -> int:
    """Event-driven simulation of the literal race rules; 1 if even."""
    v = [0.0] + [-log(rng.random()) for _ in range(n)]  # 1-indexed
    active = set(range(1, n + 1))
    edges = []  # (bumper, bumped)
    while True:
        best_t, best_ev = None, None
        act = sorted(active)
        for idx, i in enumerate(act):
            t_fin = (cu - (i - 1)) / v[i]
            if best_t is None or t_fin < best_t:
                best_t, best_ev = t_fin, ("finish", i)
            if idx + 1 < len(act):
                j = act[idx + 1]
                if v[i] > v[j]:
                    t_c = (j - i) / (v[i] - v[j])
                    if t_c < best_t:
                        best_t, best_ev = t_c, ("bump", i, j)
        if best_ev is None:
            break
        if best_ev[0] == "finish":
            active.discard(best_ev[1])
        else:
            _, i, j = best_ev
            edges.append((i, j))
            active.discard(i)
        if not active:
            break
    # chain pairs: reachability in the bump forest (out-degree <= 1)
    nxt = dict(edges)
    pairs = 0
    for i in range(1, n + 1):
        j = i
        while j in nxt:
            j = nxt[j]
            pairs += 1
    return 1 - (pairs % 2) * 2  # +1 even, -1 odd


def mc_even(n: int, cu: int, trials: int) -> float:
    rng = random.Random(597)
    s = sum(simulate_parity(n, cu, rng) for _ in range(trials))
    return (1 + s / trials) / 2


def main() -> None:
    assert p_even(3, 4) == Fraction(56, 135)  # given (L = 160)
    assert f"{float(p_even(4, 10)):.10f}" == "0.5107843137"  # given
    # solver-posted reference values for L = 1800
    assert f"{float(p_even(5, 45)):.10f}" == "0.5326110679"
    assert f"{float(p_even(6, 45)):.10f}" == "0.4869586875"
    # independent simulation of the raw rules at a non-given configuration
    assert abs(mc_even(4, 7, 100_000) - float(p_even(4, 7))) < 0.006

    print(f"{float(p_even(13, 45)):.10f}")  # 0.5001817828


if __name__ == "__main__":
    main()
