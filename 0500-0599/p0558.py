"""
https://projecteuler.net/problem=558

r is the real root of x^3 = x^2 + 1. Every positive integer has a
unique finite representation n = sum b_k r^k with b_k in {0, 1} and
any two used exponents differing by at least 3; w(n) is the number
of terms. Find S(m) = sum_(j=1..m) w(j^2) for m = 5000000.

Greedy works and is forced: with gap-3 representations the maximal
value with top exponent m is the geometric sum r^m / (1 - r^(-3)) =
r^(m+1) exactly (since r^3 - 1 = r^2), approached but never attained
by finite sums - so the top exponent must be the largest k with
r^k <= x, and the remainder satisfies x - r^k < r^k (r - 1) =
r^(k-2) because r - 1 = r^(-2) exactly, forcing the next exponent
down by at least 3 automatically.

Exactness: x is tracked as an integer scaled by 2^400 against
precomputed rounded powers R[k] = round(r^k 2^400). Accumulated
rounding is tiny, but when a remainder is *exactly* a power, an
underestimate sends the greedy into an infinite r^t = r^(t-1) +
r^(t-4) + ... descent; comparing with a slack of 2^64 fixes this and
is sound because distinct elements of the lattice Z + Zr + Zr^2 with
the coefficient sizes occurring here differ by far more than
2^(-336). Termination is X < 2^70, with genuine remaining terms at
least r^(-130) 2^400 ~ 2^330.

Each representation is independently verified for j <= 1500 (and the
given examples for 3 and 10) by summing the exact coordinate triples
of r^k in Z[r] - multiplication by r maps (a, b, c) to (c, a, b+c) -
and checking the total equals (n, 0, 0), plus the gap >= 3
condition. The given S(10) = 61 and S(1000) = 19403 are asserted.
"""

from decimal import Decimal, getcontext


def _build_powers(klo: int, khi: int, scale_bits: int) -> dict[int, int]:
    getcontext().prec = 220
    r = Decimal("1.5")
    for _ in range(200):
        r = r - (r**3 - r**2 - 1) / (3 * r**2 - 2 * r)
    pw = Decimal(2) ** scale_bits
    out = {0: int(pw.to_integral_value())}
    v = pw
    for k in range(1, khi + 1):
        v = v * r
        out[k] = int(v.to_integral_value())
    v = pw
    for k in range(-1, klo - 1, -1):
        v = v / r
        out[k] = int(v.to_integral_value())
    return out


KLO, KHI = -420, 100
R = _build_powers(KLO, KHI, 400)
SLACK = 1 << 64
THRESH = 1 << 70


def rep_exponents(n: int) -> list[int]:
    x = n * R[0]
    k = KHI
    while R[k] > x + SLACK:
        k -= 1
    exps = []
    while x > THRESH:
        while R[k] > x + SLACK:
            k -= 1
            assert k >= KLO
        x -= R[k]
        exps.append(k)
        k -= 3
        if k < KLO:
            k = KLO
    return exps


def _r_pow_triple(k: int) -> tuple[int, int, int]:
    """coordinates of r^k in basis (1, r, r^2); r*(a,b,c) = (c,a,b+c)."""
    a, b, c = 1, 0, 0
    for _ in range(k if k >= 0 else -k):
        a, b, c = (c, a, b + c) if k >= 0 else (b, c - a, a)
    return a, b, c


def _verify(n: int, exps: list[int]) -> None:
    sa = sb = sc = 0
    for k in exps:
        a, b, c = _r_pow_triple(k)
        sa, sb, sc = sa + a, sb + b, sc + c
    assert (sa, sb, sc) == (n, 0, 0), n
    assert all(exps[i] - exps[i + 1] >= 3 for i in range(len(exps) - 1)), n


if __name__ == "__main__":
    assert rep_exponents(3) == [2, -1, -5, -10]  # given: w(3) = 4
    assert rep_exponents(10) == [6, -7, -10]  # given: w(10) = 3
    _verify(3, rep_exponents(3))
    _verify(10, rep_exponents(10))
    for j in range(1, 1501):
        _verify(j * j, rep_exponents(j * j))
    assert sum(len(rep_exponents(j * j)) for j in range(1, 11)) == 61  # given
    assert sum(len(rep_exponents(j * j)) for j in range(1, 1001)) == 19403  # given

    print(sum(len(rep_exponents(j * j)) for j in range(1, 5_000_001)))  # 226754889
