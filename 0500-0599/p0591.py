"""
https://projecteuler.net/problem=591

BQA_d(x, n) is the quadratic integer a + b sqrt(d) closest to x with
|a|, |b| <= n, and I_d takes its integral part a. Find the sum of
|I_d(BQA_d(pi, 10^13))| over all non-square positive d < 100.

For fixed d the task is inhomogeneous Diophantine approximation:
minimise the distance of b sqrt(d) - pi to the nearest integer over
|b| <= B, where B caps b so the rounded a stays within |a| <= n
(b sqrt(d) <= n + 1/2 + pi etc.; for b in that range the nearest
integer automatically satisfies |a| <= n). Each of the four
sign/side combinations reduces to

    minmod(t, c, N) = min over 0 <= b <= N of (c + b t) mod 1,

solved exactly by a Euclidean-style recursion: the candidates are c
itself (b = 0) and the value just after each wrap j = 1..floor(Nt+c),
which equals (c - j) mod t - an identical problem at scale t with
step (-1) mod t and offset (c-1) mod t, recursing in O(log N)
continued-fraction-like steps. The argmin b is rebuilt as
ceil((j - c)/t) on the way out. All arithmetic is 130-digit Decimal
(with a floored mod, since Decimal's % truncates), comfortably
resolving distances around 10^-27.

The recursion is verified against literal scans for 300 random
(t, c, N); the full solver against a literal scan over all
|b| <= 3000 for every d; and the four given facts
BQA_2(pi,10) = 6 - 2 sqrt(2), BQA_5(pi,100) = 26 sqrt(5) - 55,
BQA_7(pi,10^6) = 560323 - 211781 sqrt(7), and
I_2(BQA_2(pi,10^13)) = -6188084046055 are asserted.
"""

import random
from decimal import Decimal, getcontext

getcontext().prec = 130
ONE = Decimal(1)


def _dfloor(x: Decimal) -> int:
    return int(x.to_integral_value(rounding="ROUND_FLOOR"))


def _pmod(x: Decimal, m: Decimal) -> Decimal:
    return x - m * Decimal(_dfloor(x / m))


def minmod(t: Decimal, c: Decimal, n: int) -> tuple[Decimal, int]:
    """min over 0 <= b <= n of (c + b t) mod 1, with argmin."""
    if n <= 0:
        return c, 0
    jmax = _dfloor(n * t + c)
    if jmax == 0:
        return c, 0
    c1 = _pmod(c - 1, t)
    t1 = _pmod(-ONE, t)
    if t1 == 0:
        v, j = c1, 1
    else:
        sub_v, sub_j = minmod(t1 / t, c1 / t, jmax - 1)
        v = sub_v * t
        j = 1 + sub_j
    if v < c:
        return v, -_dfloor(-(Decimal(j) - c) / t)
    return c, 0


def _atan_inv(x: int) -> Decimal:
    xs = Decimal(x)
    term = ONE / xs
    total = term
    x2 = xs * xs
    n = 1
    while True:
        term = -term / x2
        add = term / (2 * n + 1)
        total += add
        if abs(add) < Decimal(10) ** (-125):
            return total
        n += 1


PI = 16 * _atan_inv(5) - 4 * _atan_inv(239)
HALF = Decimal("0.5")


def solve_d(d: int, n: int) -> tuple[Decimal, int, int]:
    """(distance, a, b) of the closest a + b sqrt(d) to pi, |a|,|b| <= n."""
    sq = Decimal(d).sqrt()
    b_pos = min(n, _dfloor((Decimal(n) + HALF + PI) / sq))
    b_neg = min(n, _dfloor((Decimal(n) + HALF - PI) / sq))
    cands = []
    for tt, cc, sgn_b, bound in (
        (_pmod(sq, ONE), _pmod(-PI, ONE), 1, b_pos),
        (_pmod(-sq, ONE), _pmod(PI, ONE), 1, b_pos),
        (_pmod(-sq, ONE), _pmod(-PI, ONE), -1, b_neg),
        (_pmod(sq, ONE), _pmod(PI, ONE), -1, b_neg),
    ):
        _, bb = minmod(tt, cc, bound)
        b = sgn_b * bb
        a = _dfloor(PI - b * sq + HALF)
        if abs(a) <= n and abs(b) <= n:
            cands.append((abs(Decimal(a) + b * sq - PI), a, b))
    return min(cands)


def _brute_d(d: int, n: int) -> tuple[Decimal, int, int]:
    sq = Decimal(d).sqrt()
    best = None
    for b in range(-n, n + 1):
        a = max(-n, min(n, _dfloor(PI - b * sq + HALF)))
        dist = abs(Decimal(a) + b * sq - PI)
        if best is None or dist < best[0]:
            best = (dist, a, b)
    assert best is not None
    return best


if __name__ == "__main__":
    rng = random.Random(591)
    for _ in range(300):
        t = Decimal(rng.random()).quantize(Decimal("1e-30"))
        c = Decimal(rng.random()).quantize(Decimal("1e-30"))
        if t == 0:
            continue
        n = rng.randrange(1, 3000)
        v1, b1 = minmod(t, c, n)
        best = min((_pmod(c + b * t, ONE), b) for b in range(n + 1))
        assert b1 == best[1] and abs(v1 - best[0]) < Decimal("1e-25")

    assert solve_d(2, 10)[1:] == (6, -2)  # given: 6 - 2 sqrt(2)
    assert solve_d(5, 100)[1:] == (-55, 26)  # given: 26 sqrt(5) - 55
    assert solve_d(7, 10**6)[1:] == (560323, -211781)  # given
    assert solve_d(2, 10**13)[1] == -6188084046055  # given

    nonsq = [d for d in range(2, 100) if _dfloor(Decimal(d).sqrt()) ** 2 != d]
    for d in nonsq:
        assert solve_d(d, 3000)[1:] == _brute_d(d, 3000)[1:], d

    print(sum(abs(solve_d(d, 10**13)[1]) for d in nonsq))  # 526007984625966
