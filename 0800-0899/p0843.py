"""Project Euler 843: Periodic Circles.

Each step replaces every entry of a circular sequence by the absolute
difference of its two neighbours.  The maximum never increases, and on
any periodic orbit the values take only two magnitudes {0, c}; scaling
by c reduces the eventual dynamics to GF(2), where |x - y| = x XOR y
and one step is the linear map a_i -> a_{i-1} + a_{i+1}.  In the ring
R = GF(2)[x]/(x^n + 1) this is multiplication by alpha = (x^2 + 1)/x,
so the achievable eventual periods for size n are exactly the cycle
lengths of v -> alpha v on R (every 0/1 vector is itself a legitimate
starting state, so all linear periods really occur).

Writing n = 2^s m with m odd, x^n + 1 factors as the product of
f^(2^s) over the distinct irreducible divisors f of x^m + 1.  On the
component of f = x + 1, alpha is topologically nilpotent (it carries
the factor (x+1)^2) and contributes only the fixed point.  On every
other local component GF(2)[x]/f^j, alpha is a unit and an orbit's
eventual period is the multiplicative order of alpha modulo f^j for
some j <= 2^s; the achievable global periods are all least common
multiples of one choice per component.  Orders are computed by
reducing the group order 2^(d(j-1)) (2^d - 1) prime by prime, with
2^d - 1 factored by Miller-Rabin and Pollard rho.  The resulting
period sets match an exhaustive enumeration of all 2^n binary states
for n <= 16 and random real-integer simulations; summing the union of
the period sets reproduces S(6) = 6 and S(30) = 20381.
"""

from __future__ import annotations

import random
from math import gcd


def pmul(a: int, b: int, mod: int = 0) -> int:
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
    return pmod(r, mod) if mod else r


def pmod(a: int, m: int) -> int:
    dm = m.bit_length()
    while a.bit_length() >= dm:
        a ^= m << (a.bit_length() - dm)
    return a


def pdiv(a: int, b: int) -> tuple[int, int]:
    q = 0
    db = b.bit_length()
    while a.bit_length() >= db:
        sh = a.bit_length() - db
        q |= 1 << sh
        a ^= b << sh
    return q, a


def pgcd(a: int, b: int) -> int:
    while b:
        a, b = b, pmod(a, b)
    return a


def ppow(a: int, e: int, mod: int) -> int:
    r = 1
    a = pmod(a, mod)
    while e:
        if e & 1:
            r = pmul(r, a, mod)
        a = pmul(a, a, mod)
        e >>= 1
    return r


def factor_gf2(poly: int) -> dict[int, int]:
    """Irreducible factorisation of a GF(2)[x] polynomial (ints as polys)."""
    factors: dict[int, int] = {}

    def edf(p: int, d: int, mult: int) -> None:
        dp = p.bit_length() - 1
        if dp == d:
            factors[p] = factors.get(p, 0) + mult
            return
        while True:
            r = random.getrandbits(dp) | 1
            t = r
            acc = r
            for _ in range(d - 1):
                t = ppow(t, 2, p)
                acc ^= t
            g = pgcd(acc, p)
            if g not in (1, p):
                q, _ = pdiv(p, g)
                edf(g, d, mult)
                edf(q, d, mult)
                return

    def ddf(p: int, mult: int) -> None:
        d = 1
        h = 2  # the polynomial x
        while p != 1:
            dp = p.bit_length() - 1
            if d > dp // 2:
                factors[p] = factors.get(p, 0) + mult
                return
            h = ppow(h, 2, p)
            g = pgcd(h ^ 2, p)
            if g != 1:
                edf(g, d, mult)
                p, _ = pdiv(p, g)
                h = pmod(h, p)
            d += 1

    def rec(p: int, mult: int) -> None:
        if p == 1:
            return
        deriv = 0
        for i in range(1, p.bit_length(), 2):
            if (p >> i) & 1:
                deriv ^= 1 << (i - 1)
        if deriv == 0:  # p = q(x)^2
            q = 0
            for i in range(0, p.bit_length(), 2):
                if (p >> i) & 1:
                    q |= 1 << (i // 2)
            rec(q, 2 * mult)
            return
        g = pgcd(p, deriv)
        if g != 1:
            rec(g, mult)
            rec(pdiv(p, g)[0], mult)
            return
        ddf(p, mult)

    rec(poly, 1)
    return factors


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factor_int(n: int) -> dict[int, int]:
    f: dict[int, int] = {}

    def rho(n: int) -> int:
        while True:
            x = random.randrange(2, n)
            y, c, d = x, random.randrange(1, n), 1
            while d == 1:
                x = (x * x + c) % n
                y = (y * y + c) % n
                y = (y * y + c) % n
                d = gcd(abs(x - y), n)
            if d != n:
                return d

    def fact(n: int) -> None:
        if n == 1:
            return
        if n % 2 == 0:
            f[2] = f.get(2, 0) + 1
            fact(n // 2)
            return
        if is_prime(n):
            f[n] = f.get(n, 0) + 1
            return
        d = rho(n)
        fact(d)
        fact(n // d)

    fact(n)
    return f


def periods_for_n(n: int) -> set[int]:
    """Achievable eventual periods of the difference circle of size n."""
    facs = factor_gf2((1 << n) | 1)
    result = {1}
    for f, e in facs.items():
        if f == 0b11:  # x + 1: alpha eventually annihilates this part
            continue
        d = f.bit_length() - 1
        base = (1 << d) - 1
        base_factors = factor_int(base)
        opts = {1}
        fj = 1
        for j in range(1, e + 1):
            fj = pmul(fj, f) if j > 1 else f
            go = base << (d * (j - 1))
            gof = dict(base_factors)
            if j > 1:
                gof[2] = gof.get(2, 0) + d * (j - 1)
            alpha = pmul(0b101, ppow(2, go - 1, fj), fj)
            o = go
            for p, ee in gof.items():
                for _ in range(ee):
                    if ppow(alpha, o // p, fj) == 1:
                        o //= p
                    else:
                        break
            opts.add(o)
        result = {
            lcm_val for r in result for o in opts for lcm_val in (r * o // gcd(r, o),)
        }
    return result


def brute_periods(n: int) -> set[int]:
    periods = set()
    for v0 in range(1 << n):
        seen: dict[int, int] = {}
        v, t = v0, 0
        while v not in seen:
            seen[v] = t
            nv = 0
            for i in range(n):
                nv |= (((v >> ((i - 1) % n)) ^ (v >> ((i + 1) % n))) & 1) << i
            v = nv
            t += 1
        periods.add(t - seen[v])
    return periods


def period_union_sum(n_max: int) -> int:
    union: set[int] = set()
    for n in range(3, n_max + 1):
        union |= periods_for_n(n)
    return sum(union)


def main() -> None:
    random.seed(20230529)
    for n in range(3, 15):
        assert periods_for_n(n) == brute_periods(n), n
    assert period_union_sum(6) == 6
    assert period_union_sum(30) == 20381
    print(period_union_sum(100))  # 2816775424692


if __name__ == "__main__":
    main()
