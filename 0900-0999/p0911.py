"""Project Euler 911: Khinchin Exceptions.

rho_n = sum_i 2^(n - 2^i) = 2^n rho_0, a dyadic shift of the Kempner
number.  Its partial sums P_K = sum_{i <= K} 2^(n - 2^i) are exact
dyadic rationals, and their continued fractions exhibit the classical
"folding" doubling: the CF at level K + 1 repeats the CF at level K
except for O(1) boundary quotients (empirically the two lists agree on
all but the last quotient).  Consequently, the count c_a(K) of each
quotient value a in the CF body obeys an exact affine doubling
recurrence

    c_a(K + 1) = 2 c_a(K) + e_a,     L(K + 1) = 2 L(K) + e_L,

with constant integer edits e (verified across three consecutive levels
for every n, here with K = 11, 12, 13).  Then c_a(K) + e_a doubles
exactly, so the limiting frequency of quotient a is the exact rational

    f_a = (c_a(K) + e_a) / (L(K) + e_L),       sum_a f_a = 1,

and k_inf(rho_n) = prod_a a^{f_a}.  The quotient alphabets are tiny and
structured, e.g. n = 0: {2, 4, 6} with frequencies (1/4, 1/2, 1/4), so
k_inf(rho_0) = 2 * 12^(1/4); n = 2: {1, 2, 3, 4} with (1/3, 1/12, 1/2,
1/12), giving k_inf(rho_2) = 2^(1/4) sqrt(3) = 2.0597671... matching
the given value; large n use quotients near 2^(2^j - n) such as
2^50 - 1.  The geometric mean over n = 0..50 is computed with the
stdlib decimal module at 40 significant digits (ln/exp are exact to
the context precision), so the seventh decimal is far from any
rounding boundary.
"""

from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 40


def cf_of_fraction(p: int, q: int) -> list[int]:
    out = []
    while q:
        a, r = divmod(p, q)
        out.append(a)
        p, q = q, r
    return out


def _counts(n: int, big_k: int):
    e = 2**big_k
    num = sum(1 << (e - 2**i + n) for i in range(big_k + 1))
    cf = cf_of_fraction(num, 1 << e)
    body = cf[1:-2]  # drop a0 and the corrupted tail of the rational CF
    return Counter(body), len(body)


def k_inf(n: int, k0: int = 11) -> Decimal:
    (c0, l0), (c1, l1), (c2, l2) = (_counts(n, k) for k in (k0, k0 + 1, k0 + 2))
    keys = set(c0) | set(c1) | set(c2)
    e = {a: c1[a] - 2 * c0[a] for a in keys}
    e_len = l1 - 2 * l0
    for a in keys:  # the affine recurrence must hold at the next level
        assert c2[a] == 2 * c1[a] + e[a], (n, a)
    assert l2 == 2 * l1 + e_len, n
    freqs = {a: Fraction(c2[a] + e[a], l2 + e_len) for a in keys}
    assert sum(freqs.values()) == 1, n
    lg = Decimal(0)
    for a, f in freqs.items():
        if f:
            lg += Decimal(f.numerator) / Decimal(f.denominator) * Decimal(a).ln()
    return lg.exp()


def solve() -> str:
    total = Decimal(0)
    for n in range(51):
        total += k_inf(n).ln()
    g = (total / 51).exp()
    return str(g.quantize(Decimal("0.000001")))  # 10 significant digits


if __name__ == "__main__":
    assert abs(k_inf(2) - Decimal("2.059767")) < Decimal("1e-6")  # given example
    print(solve())  # 5679.934966
