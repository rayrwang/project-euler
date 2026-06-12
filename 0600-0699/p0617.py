"""Project Euler Problem 617: Mirror Power Sequence.

An (n,e)-MPS is an infinite sequence with a_{i+1} = min(a_i^e, n - a_i^e)
and all a_i > 1; it is determined by (n, e, a_0).  C(n) counts MPS over
all e, D(N) = sum_{n<=N} C(n); we need D(10^18).

A surviving orbit repeatedly powers up (x -> x^e, strictly increasing)
and reflects (x -> n - x^e once 2 x^e > n), so it must end in a cycle.
Cycles contain exactly one reflection: a two-reflection cycle would give
m^(e^a) - m = r^(e^b) - r with m != r and both exponents powers of the
same e, which the convexity gap x^E - (x-1)^E >= 2(x-1) rules out.  Thus
every cycle is b -> b^e -> ... -> b^(e^(k-1)) -> b with

    n = b + b^(e^k),

valid for all b, e >= 2, k >= 1 (the mode conditions hold automatically),
and contributing k distinct sequences (one per starting rotation).
Distinct (b, e, k) never produce colliding sequences: magnitude
comparisons force the parametrisation to be unique.

Transients: the backward tree of a cycle adds only e-th-root chains below
the base b -- starts a_0 = c with c^(e^t) = b, i.e.

    n = c^(e^t) + c^(e^(t+k)),   one sequence per (c >= 2, t >= 1).

Reflection-type predecessors never exist: for any surviving value v the
quantity n - v lands strictly between consecutive e-th powers
(window argument around B = b^(e^(k-1)) resp. the chain top), so it is
never a perfect e-th power.  Hence

  D(N) = sum_{e>=2, k>=1} [ k * #{b >= 2 : b + b^(e^k) <= N}
                            + #{(c, t) : c^(e^t) + c^(e^(t+k)) <= N} ].

Checks: a brute-force orbit-survival simulation computing C(n) directly
for all n <= 3000, and the given D(10) = 2, D(100) = 21, D(1000) = 69,
D(10^6) = 1303, D(10^12) = 1014800.
"""


import numba as nb


@nb.njit(cache=True)
def _cpow(base, exp, cap):
    """base**exp, saturating at cap+1 to stay inside int64."""
    r = 1
    for _ in range(exp):
        if r > cap // base:  # r * base would exceed cap (and may overflow int64)
            return cap + 1
        r *= base
    return r


@nb.njit(cache=True)
def count_b(E, N):
    """#{b >= 2 : b + b^E <= N} by integer root + adjust."""
    if 2 + _cpow(2, E, N) > N:
        return 0
    hi = int(round(N ** (1.0 / E))) + 2
    while hi + _cpow(hi, E, N) > N:
        hi -= 1
    return max(0, hi - 1)


@nb.njit(cache=True)
def D(N):
    total = 0
    # cycles: n = b + b^(e^k), k sequences each
    e = 2
    while 2 + _cpow(2, e, N) <= N:
        k = 1
        while 2 + _cpow(2, e**k, N) <= N:
            total += k * count_b(e**k, N)
            k += 1
        e += 1
    # transients: n = c^(e^t) + c^(e^(t+k)), one sequence each
    e = 2
    while _cpow(2, e, N) + _cpow(2, e**2, N) <= N:
        t = 1
        while _cpow(2, e**t, N) + _cpow(2, e ** (t + 1), N) <= N:
            k = 1
            while _cpow(2, e**t, N) + _cpow(2, e ** (t + k), N) <= N:
                c = 2
                while _cpow(c, e**t, N) + _cpow(c, e ** (t + k), N) <= N:
                    total += 1
                    c += 1
                k += 1
            t += 1
        e += 1
    return total


@nb.njit(cache=True)
def D_brute(N):
    """Direct semantics: count surviving (n, e, a_0) triples."""
    total = 0
    stamp = [0] * (N + 1)
    cur = 0
    for n in range(6, N + 1):
        e = 2
        while _cpow(2, e, n) <= n:  # a_0 = 2 must at least allow one step
            for a0 in range(2, n):
                cur += 1
                x = a0
                ok = True
                while stamp[x] != cur:
                    stamp[x] = cur
                    xe = _cpow(x, e, n)
                    nxt = min(xe, n - xe)
                    if nxt <= 1:
                        ok = False
                        break
                    x = nxt
                if ok:
                    total += 1
            e += 1
    return total


if __name__ == "__main__":
    assert D(10) == 2 and D_brute(10) == 2
    assert D(100) == 21 and D_brute(100) == 21
    assert D(1000) == 69
    assert D(3000) == D_brute(3000)
    assert D(10**6) == 1303
    assert D(10**12) == 1014800
    print(D(10**18))  # 1001133757
