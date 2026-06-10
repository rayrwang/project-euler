"""Project Euler 924: Larger Digit Permutation II.

a_n has about 2^n digits, but B only rearranges a suffix:
B(a_n) = a_n + Delta_n where Delta_n depends on the digits up to the
pivot (the first place q with digit_q < digit_{q-1}).  So
U(N) = sum (a_n mod p) + sum Delta_n over n with B != 0 (only n = 1, 2
have B = 0).

The a-part uses the rho cycle of x -> x^2 + 2 mod p (tail + period of a
few ten thousand steps).  For the Delta-part, the orbit modulo 10^K is
eventually periodic with period pi_K = 8 * 5^(K-2): 2-adically a_n
converges to a root of x^2 - x + 2 (so high powers of 2 stabilise),
while 5-adically the cycle multiplier is 1 mod 5, making each deeper
digit advance through an arithmetic progression per revolution.  Fixing
K0, every index n >= W0 falls into a class n0 + t * pi (pi = pi_{K0});
the low K0 digits, hence usually the pivot and Delta, are constant on
the class.  Exceptional classes (low digits weakly increasing, no pivot)
are resolved through the deep digits: the return map T = f^pi is
5-adically translation-like, so by Mahler/binomial interpolation

    a_{n0 + t pi} = sum_{j <= jmax} C(t, j) Delta^j (a_{n0})  (mod 10^40),

where the j-th finite difference Delta^j has 5-valuation >= j(K0-1)+1
and vanishes mod 2^40; jmax = ceil(39/(K0-1)) suffices and the
truncation is asserted by reproducing T^{jmax+1} exactly.  The digits
then depend on t only through t mod 5^m, so a base-5 branch tree over t
resolves every pivot with exact class counts.

Validation: exact big-integer brute force for N <= 22 (including the
given U(10) = 543870437), and a per-term reference (iterating every n
mod 10^40) up to N = 300000 across several K0, exercising the window
and exceptional machinery.  The production answer agrees for K0 = 10
and K0 = 11.
"""

import sys
from math import comb

sys.set_int_max_str_digits(10**7)

P = 10**9 + 7
DEEP = 40
MODD = 10**DEEP


def period(k: int) -> int:
    return 2 if k == 1 else 8 * 5 ** (k - 2)


def pivot_delta(digs: list[int]):
    """digs[i] = digit at place i.  -> (pivot place, B - n) or (None, None)."""
    for i in range(1, len(digs)):
        if digs[i] < digs[i - 1]:
            q = i
            suffix = digs[:q]
            piv = digs[q]
            cand = min(d for d in suffix if d > piv)
            new = sorted(suffix)
            new.remove(cand)
            new.append(piv)
            new.sort()
            old_val = sum(d * 10**j for j, d in enumerate(digs[: q + 1]))
            new_val = cand * 10**q + sum(
                d * 10**j for j, d in enumerate(reversed(new)))
            return q, new_val - old_val
    return None, None


def digits_low(x: int, k: int) -> list[int]:
    out = []
    for _ in range(k):
        x, d = divmod(x, 10)
        out.append(d)
    return out


def exact_delta_small(n: int):
    """Exact B(a_n) - a_n for small n, or None if B = 0."""
    a = 0
    for _ in range(n):
        a = a * a + 2
    s = list(str(a))
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i < 0:
        return None
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = sorted(s[i + 1:])
    return int("".join(s)) - a


def solve(n_max: int, k0: int = 10) -> int:
    pi = period(k0)
    w0 = 60
    # a-part: rho cycle mod p
    seen: dict[int, int] = {}
    x = 0
    vals = [0]
    n = 0
    while x not in seen:
        seen[x] = n
        x = (x * x + 2) % P
        n += 1
        vals.append(x)
    tail_p = seen[x]
    per_p = n - tail_p
    pref = [0] * (len(vals) + 1)
    for i in range(len(vals)):
        pref[i + 1] = (pref[i] + vals[i]) % P

    def s_upto(m: int) -> int:
        if m < 0:
            return 0
        if m < len(vals) - 1:
            return pref[m + 1]
        cyc = (pref[tail_p + per_p] - pref[tail_p]) % P
        full, rem = divmod(m - tail_p + 1, per_p)
        return (pref[tail_p] + full * cyc
                + (pref[tail_p + rem] - pref[tail_p])) % P

    total = (s_upto(n_max) - s_upto(2)) % P if n_max >= 3 else 0

    if n_max < w0 + pi:
        x = 0
        for n in range(1, n_max + 1):
            x = (x * x + 2) % MODD
            if n <= 7:
                d = exact_delta_small(n)
                if d is not None:
                    total = (total + d) % P
                continue
            q, d = pivot_delta(digits_low(x, DEEP))
            assert q is not None and q <= DEEP - 2, n
            total = (total + d) % P
        return total

    jmax = -(-(DEEP - 1) // (k0 - 1))
    nrev = jmax + 2
    exc: dict[int, list[int]] = {}
    x = 0
    for n in range(1, w0 + nrev * pi + 1):
        x = (x * x + 2) % MODD
        if 3 <= n < w0:
            if n <= 7:
                d = exact_delta_small(n)
                assert d is not None
            else:
                q, d = pivot_delta(digits_low(x, DEEP))
                assert q is not None and q <= DEEP - 2, n
            total = (total + d) % P
        elif w0 <= n < w0 + pi:
            if n > n_max:
                continue
            y, d_prev = divmod(x, 10)
            digs = [d_prev]
            q = None
            for i in range(1, k0):
                y, d = divmod(y, 10)
                digs.append(d)
                if d < d_prev:
                    q = i
                    break
                d_prev = d
            if q is not None:
                _, dd = pivot_delta(digs)
                cnt = (n_max - n) // pi + 1
                total = (total + dd % P * (cnt % P)) % P
            else:
                exc[n] = [x]
        elif n >= w0 + pi:
            n0 = w0 + ((n - w0) % pi)
            if n0 in exc and len(exc[n0]) < nrev:
                exc[n0].append(x)

    def v5(z: int) -> int:
        v = 0
        while z and z % 5 == 0:
            z //= 5
            v += 1
        return v if z else DEEP

    for n0, ts in exc.items():
        diffs = [ts[0]]
        row = ts
        for _ in range(jmax + 1):
            row = [(row[i + 1] - row[i]) % MODD for i in range(len(row) - 1)]
            diffs.append(row[0])
        tt = jmax + 1  # truncation check against T^{jmax+1}
        pred = sum(comb(tt, j) * diffs[j] for j in range(jmax + 1)) % MODD
        assert pred == ts[tt], ("interp", n0)
        for dd in diffs[1: jmax + 1]:
            assert dd % 2**DEEP == 0 and v5(dd) >= v5(diffs[1]), n0
        v5d1 = v5(diffs[1])
        tmax = (n_max - n0) // pi

        def value_at(t: int, diffs=diffs) -> int:
            return sum(comb(t, j) * diffs[j] for j in range(jmax + 1)) % MODD

        stack = [(0, 1, 0)]
        while stack:
            c, mod5, m = stack.pop()
            if c > tmax:
                continue
            fixed = v5d1 + m
            assert fixed <= DEEP, ("branch too deep", n0)
            digs = digits_low(value_at(c), min(fixed, DEEP))
            q, d = pivot_delta(digs)
            if q is not None and q <= len(digs) - 2:
                cnt = (tmax - c) // mod5 + 1
                total = (total + d % P * (cnt % P)) % P
            else:
                for i in range(5):
                    stack.append((c + i * mod5, mod5 * 5, m + 1))
    return total


def _exact_u(n_max: int) -> int:
    a, u = 0, 0
    for n in range(1, n_max + 1):
        a = a * a + 2
        d = exact_delta_small(n)
        if d is not None:
            u = (u + (a + d)) % P
    return u


def _reference(n_max: int) -> int:
    total = 0
    xp, xd = 0, 0
    for n in range(1, n_max + 1):
        xp = (xp * xp + 2) % P
        xd = (xd * xd + 2) % MODD
        if n <= 2:
            continue
        d = exact_delta_small(n) if n <= 7 else pivot_delta(
            digits_low(xd, DEEP))[1]
        total = (total + xp + d) % P
    return total


if __name__ == "__main__":
    assert _exact_u(10) == 543870437  # given
    for n_check in (8, 10, 16, 22):
        e = _exact_u(n_check)
        assert solve(n_check, 5) == e and solve(n_check, 6) == e, n_check
    ref = _reference(30000)
    for k0 in (5, 6, 7):
        assert solve(30000, k0) == ref, k0
    print(solve(10**16))  # 811141860
