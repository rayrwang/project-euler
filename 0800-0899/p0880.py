import numpy as np
from math import isqrt

import numba

# Squaring sqrt(cbrt(x) + cbrt(y)) = cbrt(a) + cbrt(b) + cbrt(c) gives six
# cube-root terms a^(2/3), ..., 2(ca)^(1/3) that must collapse to two.  In
# the group Q*/(Q*)^3 the six classes are -[a], -[b], -[c], [a]+[b], [b]+[c],
# [c]+[a]; with x/y not a cube no two of a, b, c may be cube-related (that
# route forces x/y to be a cube), and the only remaining collapse is
# -[a] = [b]+[c], i.e. abc = t^3 a perfect cube, which pairs the terms into
# three rays with values (a+2t)^3/a, (b+2t)^3/b, (c+2t)^3/c.  Getting two
# terms then requires one ray to vanish: b = -2t.  Writing t = 2s this is
#     b = -4s,   a c = -2 s^2,   x = (a+4s)^3/a,   y = (c+4s)^3/c,
# always integral because a | 2s^2 implies a | 64 s^3.  Enumerating s >= 1
# and divisors a = -d < 0 < c = 2s^2/d covers every unordered pair once
# (checked: collisions occur only at excluded cube-ratio pairs), with the
# exclusion "x/y is a rational cube" exactly when 2 s^2 d is a perfect cube,
# tested on exponents to avoid overflow.  AM-GM gives y >= 108 s^2, so
# s <= sqrt(N/108), and valid pairs force |a+4s| <= sqrt(2N) so the exact
# values fit in 64 bits via a gcd cascade x = prod (a+4s)/q_i.

MOD = 1031**3 + 2
N = 10**15


@numba.njit(cache=True)
def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(inline="always")
def exact_cube_div(p, d, n):
    """(ok, p^3 // d) for d | p^3; ok=False signals |value| > n."""
    ap = p if p >= 0 else -p
    q1 = ap if ap < d else d
    a, b = ap, d
    while b:
        a, b = b, a % b
    q1 = a
    d1 = d // q1
    a, b = ap, d1
    while b:
        a, b = b, a % b
    q2 = a
    d2 = d1 // q2
    a, b = ap, d2
    while b:
        a, b = b, a % b
    q3 = a  # d2 // q3 == 1 since d | p^3
    f1, f2, f3 = ap // q1, ap // q2, ap // q3
    m = f1 * f2
    if m > n or (f3 != 0 and m > n // f3):
        return False, 0
    v = m * f3
    if v > n:
        return False, 0
    return True, -v if p < 0 else v


@numba.njit(cache=True)
def h_sum(n, smax, spf, mod, collect):
    primes = np.empty(14, dtype=np.int64)
    exps = np.empty(14, dtype=np.int64)
    out = [np.int64(0) for _ in range(0)]
    total = 0
    count = 0
    fn = np.float64(n) * 1.0000001
    for s in range(1, smax + 1):
        v = s
        k = 0
        while v > 1:
            p = spf[v]
            e = 0
            while v % p == 0:
                v //= p
                e += 1
            primes[k] = p
            exps[k] = 2 * e
            k += 1
        has2 = False
        for i in range(k):
            if primes[i] == 2:
                exps[i] += 1
                has2 = True
        if not has2:
            primes[k] = 2
            exps[k] = 1
            k += 1
        ndiv = 1
        for i in range(k):
            ndiv *= exps[i] + 1
        big_t = 2 * s * s
        divs = np.empty(ndiv, dtype=np.int64)
        divs[0] = 1
        cnt = 1
        for i in range(k):
            p = primes[i]
            base = cnt
            pe = np.int64(1)
            for _ in range(exps[i]):
                pe *= p
                for j in range(base):
                    divs[cnt] = divs[j] * pe
                    cnt += 1
        for di in range(cnt):
            d = divs[di]
            pa = 4 * s - d  # a = -d, x = -pa^3/d
            apa = pa if pa >= 0 else -pa
            if apa == 0:
                continue
            if np.float64(apa) ** 3 > fn * np.float64(d):
                continue
            cp = big_t // d
            pc = cp + 4 * s  # c = cp, y = pc^3/cp > 0
            if np.float64(pc) ** 3 > fn * np.float64(cp):
                continue
            ok1, x = exact_cube_div(-pa, d, n)
            if not ok1 or x == 0:
                continue
            ok2, y = exact_cube_div(pc, cp, n)
            if not ok2 or y == 0:
                continue
            # x/y rational cube <=> 2 s^2 d is a perfect cube
            iscube = True
            for i in range(k):
                e = exps[i]
                p = primes[i]
                w = d
                while w % p == 0:
                    w //= p
                    e += 1
                if e % 3:
                    iscube = False
                    break
            if iscube:
                continue
            count += 1
            ax = x if x > 0 else -x
            total = (total + ax + y) % mod
            if collect:
                out.append(x)
                out.append(y)
                out.append(np.int64(s))
                out.append(-d)
    return count, total, out


def verify_identities(rows: np.ndarray) -> None:
    """Each collected pair must satisfy the nested radical equation."""

    def cbrt(v: float) -> float:
        return np.sign(v) * np.abs(np.float64(v)) ** (1.0 / 3.0)

    for x, y, s, a in rows:
        c = 2 * s * s // (-a)
        lhs_sq = cbrt(x) + cbrt(y)
        rhs = cbrt(a) + cbrt(-4 * s) + cbrt(c)
        assert lhs_sq >= 0
        assert abs(np.sqrt(lhs_sq) - abs(rhs)) < 1e-6 * max(1.0, abs(rhs))


if __name__ == "__main__":
    spf = spf_sieve(isqrt(N // 108) + 2)

    c, t, dat = h_sum(1000, isqrt(1000 // 108) + 1, spf, MOD, True)
    assert t == 2535 and c == 5  # given H(10^3)
    rows = np.array(dat, dtype=np.int64).reshape(-1, 4)
    assert (-4, 125) in {(int(r[0]), int(r[1])) for r in rows}  # given example
    verify_identities(rows)

    c, t, dat = h_sum(6000, 8, spf, MOD, True)
    rows = np.array(dat, dtype=np.int64).reshape(-1, 4)
    assert (5, 5324) in {(int(r[0]), int(r[1])) for r in rows}  # given example
    verify_identities(rows)

    # enumeration hits each pair exactly once at scale
    c, t, dat = h_sum(10**9, isqrt(10**9 // 108) + 1, spf, MOD, True)
    rows = np.array(dat, dtype=np.int64).reshape(-1, 4)
    assert len(np.unique(rows[:, :2], axis=0)) == c
    verify_identities(rows[:: max(1, len(rows) // 500)])

    _, answer, _ = h_sum(N, isqrt(N // 108) + 1, spf, MOD, False)
    print(answer)  # 522095328
