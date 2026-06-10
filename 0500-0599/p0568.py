"""
https://projecteuler.net/problem=568

With the games of problem 567, D(n) = J_B(n) - J_A(n); give the 7
most significant digits of D(123456789) after stripping leading
zeros.

The two expectations agree to enormous depth: every coefficient of
the 1/n expansion cancels, and in fact D decays like 2^-n. The key
is an exact recurrence. Writing a_m = sum_k 1/C(m,k) and using
1/(k C(n,k)) = (1/k - 1/n) / C(n-1,k), one gets
J_B(n) = J_B(n-1) + 2/n - A_n with A_n = 2^-n sum_(j<=n) 2^j / j,
while the identity sum_k C(n,k)/k = sum_j (2^j - 1)/j gives
J_A(n) = A_n - 2^-n H_n. Combining with A_(n-1) = 2 A_n - 2/n
collapses everything:

    D(n) = D(n-1) + 2^-n (H_n - 2 H_(n-1)),

verified exactly with rationals for all n < 60. Since
sum 2^-m H_(m-1) = sum 2^-m / m = ln 2, the series telescopes to 0
at infinity, leaving the exact, rapidly convergent tail

    D(n) = sum_(m>n) 2^-m (H_(m-1) - 1/m) = 2^-n G(n),

(also verified directly against exact values), with
G(n) = sum_(i>=1) 2^-i (H_(n+i-1) - 1/(n+i)) ~ H_n. G is evaluated
with 60-digit Decimal arithmetic (Euler-Maclaurin H_n, 170 terms,
truncation below 1e-44), and the leading digits come from the
fractional part of log10 D = -n log10(2) + log10(G), with log10(2)
at 60 digits so the fractional part is good to ~1e-50.

The digit-extraction machinery reproduces the exact 7 digits of
D(6) = 0.03828125 -> 3828125 (the worked example) and of D(40).
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb

getcontext().prec = 60
GAMMA = Decimal("0.57721566490153286060651209008240243104215933593992359880577")
LOG10_2 = Decimal(2).ln() / Decimal(10).ln()


def _d_exact(n: int) -> Fraction:
    jb = sum(Fraction(1, k * comb(n, k)) for k in range(1, n + 1))
    ja = Fraction(sum(Fraction(comb(n, k), k) for k in range(1, n + 1)), 2**n)
    return jb - ja


def _digits7_exact(d: Fraction) -> str:
    return str(d.numerator * 10**80 // d.denominator).lstrip("0")[:7]


def _digits7(n: int, terms: int = 170) -> str:
    """First 7 significant digits of D(n) via the tail series."""
    nd = Decimal(n)
    h = nd.ln() + GAMMA + 1 / (2 * nd) - 1 / (12 * nd**2) + 1 / (120 * nd**4)
    g = Decimal(0)
    p = Decimal(1)
    half = Decimal(1) / 2
    for i in range(1, terms + 1):
        p *= half
        g += p * (h - 1 / (nd + i))
        h += 1 / (nd + i)  # H_(n+i-1) -> H_(n+i)
    ell = -n * LOG10_2 + g.log10()
    frac = ell - int(ell)
    if frac < 0:
        frac += 1  # mantissa exponent in [0, 1)
    return str(int(Decimal(10) ** (frac + 6)))


if __name__ == "__main__":
    harm = [Fraction(0)]
    for i in range(1, 80):
        harm.append(harm[-1] + Fraction(1, i))

    prev = Fraction(0)
    for n in range(1, 60):  # the telescoping recurrence, exactly
        d = _d_exact(n)
        assert d == prev + Fraction(1, 2**n) * (harm[n] - 2 * harm[n - 1])
        prev = d

    for n in (10, 25, 40):  # the tail-series representation
        tail = sum(
            Fraction(1, 2**m) * (harm[m - 1] - Fraction(1, m)) for m in range(n + 1, 79)
        )
        assert abs(_d_exact(n) - tail) < Fraction(1, 2**70)

    assert float(_d_exact(6)) == 0.03828125  # given
    assert _digits7_exact(_d_exact(6)) == "3828125"  # given example
    assert _digits7(40) == _digits7_exact(_d_exact(40))

    print(_digits7(123456789))  # 4228020
