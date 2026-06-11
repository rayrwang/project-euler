"""Project Euler problem 598: Split Divisibilities.

C(n) counts pairs a * b = n with a <= b such that a and b have the same
number of divisors; C(10!) = 3 is given.  Find C(100!).

Write 100! = prod p_i^{e_i} over its 25 primes.  A factor a corresponds
to an exponent vector x with 0 <= x_i <= e_i, and the condition
d(a) = d(b) reads prod (x_i + 1) = prod (e_i - x_i + 1), i.e. the ratio

    R(x) = prod (x_i + 1) / (e_i - x_i + 1)

must equal 1.  The full search space prod (e_i + 1) is about 4 * 10^16,
but R factors across primes, so meet-in-the-middle applies: split the
primes into two halves, build for each half the distribution
{ratio -> number of exponent choices} as exact reduced fractions (the
distinct-ratio counts stay modest because ratios collapse multiplica-
tively), and join with sum over r of count1(r) * count2(1/r).  Since the
exponent of 97 in 100! is odd, 100! is not a square, a = b is
impossible, and the ordered-solution count is exactly twice C.

Verified against a direct brute force over all factorisations of 6!, 8!
and 10!, the last reproducing the given C(10!) = 3.
"""

from fractions import Fraction
from math import factorial


def fact_exps(n: int) -> list[int]:
    exps = []
    for p in range(2, n + 1):
        if all(p % i for i in range(2, int(p**0.5) + 1)):
            e, q = 0, p
            while q <= n:
                e += n // q
                q *= p
            exps.append(e)
    return exps


def half_dist(es: list[int]) -> dict[Fraction, int]:
    dist = {Fraction(1): 1}
    for e in es:
        new: dict[Fraction, int] = {}
        for x in range(e + 1):
            r = Fraction(x + 1, e - x + 1)
            for k, c in dist.items():
                kk = k * r
                new[kk] = new.get(kk, 0) + c
        dist = new
    return dist


def count_c(n: int) -> int:
    es = sorted(fact_exps(n), reverse=True)
    d1 = half_dist(es[0::2])
    d2 = half_dist(es[1::2])
    total = 0
    for r, c in d1.items():
        inv = 1 / r
        if inv in d2:
            total += c * d2[inv]
    assert total % 2 == 0  # n! not a square, so a = b never occurs
    return total // 2


def brute_c(n: int) -> int:
    f = factorial(n)
    cnt = 0
    a = 1
    while a * a <= f:
        if f % a == 0:
            b = f // a
            da = sum(2 - (i * i == a) for i in range(1, int(a**0.5) + 1) if a % i == 0)
            db = sum(2 - (i * i == b) for i in range(1, int(b**0.5) + 1) if b % i == 0)
            cnt += da == db
        a += 1
    return cnt


def main() -> None:
    for n in (6, 8, 10):
        assert brute_c(n) == count_c(n), n
    assert count_c(10) == 3  # given

    print(count_c(100))  # 543194779059


if __name__ == "__main__":
    main()
