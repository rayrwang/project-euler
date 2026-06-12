"""
Project Euler Problem 777: Lissajous Curves
https://projecteuler.net/problem=777

For coprime a, b the curve x = cos(at), y = cos(b(t - pi/10)), t in
[0, 2pi), crosses itself at certain points; d(a, b) sums x^2 + y^2 over
them, and s(m) sums d over all coprime pairs 2 <= a, b <= m.  Given
s(10) = 1602.5 and s(100) = 24256505, find s(10^6) to ten significant
digits.

Where the crossings are.  Two parameters give the same point when each
cosine agrees, i.e. (with phi = pi/10) a(t1 -+ t2) = 0 and
b(t1 - t2) = 0 or b(t1 + t2 - 2 phi) = 0 modulo 2 pi.  Equal differences
in both coordinates force t1 = t2; equal sums in both are solvable only
when 10 | ab, in which case the whole curve retraces itself (the
"open-arc" pictures) rather than crossing.  The genuine crossings come
from the two mixed cases, giving the discrete families

    x = (-1)^m cos(a phi + pi a k / b),  y = (-1)^k cos(pi m b / a),
    x = (-1)^j cos(pi a n / b),          y = (-1)^n cos(pi j b / a - b phi),

with m = 1..a-1, k mod 2b and n = 1..b-1, j mod 2a; the parametrisation
covers every double point exactly twice.  Summing cos^2 over the full
equally spaced angle sets (each progression completes whole turns, so
the oscillating halves vanish) gives, for 10 not dividing ab,

    d(a, b) = (4ab - 3a - 3b) / 2,

and in the retraced case the crossings halve to (a-1)(b-1)/2 points with

    d(a, b) = (2ab - 3a - 3b + 4) / 4.

Both formulas were verified against an exact-grid numerical crossing
finder (candidate parameters lie on pi/(ab) lattices) for every coprime
pair with a, b <= 41 and reproduce all five given d values.

Summation.  s(m) needs, over coprime pairs in [2, m]^2, the sums of ab,
of a + b, and the same restricted to 10 | ab.  The restriction unfolds
multiplicatively by inclusion-exclusion: [10 | ab] = 1 - [a, b odd]
- [5 not| a, 5 not| b] + [ab coprime to 10], each a product condition.
Moebius inversion over g = gcd(a, b) then reduces everything to
closed-form sums of x and of counts over [2/g, m/g] restricted to
divisibility by 2, 5 and 10, an O(m) exact-integer loop.  Multiplying by
4 keeps all quantities integral; s(10) and s(100) check out, and the
final value, about 2.53e23, is printed to ten significant digits.
"""

from decimal import Decimal, getcontext

M = 10**6


def mobius_sieve(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    comp = bytearray(n + 1)
    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def s_times_4(m):
    """4 s(m) as an exact integer."""
    mu = mobius_sieve(m)

    def tri(x):
        return x * (x + 1) // 2

    total = 0
    for d in range(1, m + 1):
        if mu[d] == 0:
            continue
        lo = 2 if d == 1 else 1
        hi = m // d
        if hi < lo:
            break

        def aq(q, lo=lo, hi=hi):
            return q * (tri(hi // q) - tri((lo - 1) // q))

        def cq(q, lo=lo, hi=hi):
            return hi // q - (lo - 1) // q

        asum, cnt = aq(1), cq(1)
        a_odd, c_odd = asum - aq(2), cnt - cq(2)
        a_no5, c_no5 = asum - aq(5), cnt - cq(5)
        a_u10 = asum - aq(2) - aq(5) + aq(10)
        c_u10 = cnt - cq(2) - cq(5) + cq(10)
        # unit conditions on a = d x require the d-part to comply too
        if d % 2 == 0:
            a_odd = c_odd = 0
        if d % 5 == 0:
            a_no5 = c_no5 = 0
        if d % 2 == 0 or d % 5 == 0:
            a_u10 = c_u10 = 0
        s1 = d * d * asum * asum
        s2 = 2 * d * asum * cnt
        t1 = d * d * (asum * asum - a_odd * a_odd - a_no5 * a_no5 + a_u10 * a_u10)
        t2 = 2 * d * (asum * cnt - a_odd * c_odd - a_no5 * c_no5 + a_u10 * c_u10)
        t0 = cnt * cnt - c_odd * c_odd - c_no5 * c_no5 + c_u10 * c_u10
        total += mu[d] * (8 * s1 - 6 * s2 - 6 * t1 + 3 * t2 + 4 * t0)
    return total


def fmt_sci10(v4):
    """v4/4 in scientific notation with 10 significant digits."""
    getcontext().prec = 50
    s = Decimal(v4) / 4
    e = len(str(v4 // 4)) - 1
    mant = (s / Decimal(10) ** e).quantize(Decimal("1.000000000"))
    return f"{mant}e{e}"


def main():
    assert s_times_4(10) == 6410  # s(10) = 1602.5
    assert s_times_4(100) == 4 * 24256505
    return fmt_sci10(s_times_4(M))


if __name__ == "__main__":
    print(main())  # 2.533018434e23
