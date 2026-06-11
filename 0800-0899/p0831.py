"""Project Euler 831: Triple Product.

Swapping the summation order with C(m,j)C(j,i) = C(m,i)C(m-i,j-i) and
applying the alternating identity
sum_k (-1)^k C(n,k) C(a+k, r) = (-1)^n C(a, r-n) collapses the double
sum to g(m) = sum_i (-1)^(m-i) C(m,i) C(7i+5, m+5), and reading
C(7i+5, m+5) as a coefficient of (1+x)^(7i+5) turns this into the
binomial transform of a power:

    g(m) = [x^(m+5)] (1+x)^5 ((1+x)^7 - 1)^m
         = [x^5] (1+x)^5 Q(x)^m,   Q(x) = ((1+x)^7 - 1)/x.

So only Q(x)^m modulo x^6 matters: a binary power of a six-term
integer polynomial whose coefficients reach ~7^m.  The identity is
verified against the literal double sum for m <= 11, reproducing
g(10) = 127278262644918.

Since Q(0) = 7, g(142857) is approximately 7^142857 times a modest
polynomial factor, which is exactly why the problem asks for leading
digits in base 7: the exact 120-thousand-digit integer is computed
with big-integer arithmetic, its base-7 length determined by direct
comparison, and the top ten digits extracted by one division.
"""

from __future__ import annotations

import math
from math import comb


def g_definition(m: int) -> int:
    return sum(
        (-1) ** (j - i) * comb(m, j) * comb(j, i) * comb(j + 5 + 6 * i, j + 5)
        for j in range(m + 1)
        for i in range(j + 1)
    )


def g_value(m: int) -> int:
    base = [comb(7, k + 1) for k in range(6)]  # ((1+x)^7 - 1)/x mod x^6

    def mul(a: list[int], b: list[int]) -> list[int]:
        r = [0] * 6
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if i + j < 6:
                        r[i + j] += x * y
        return r

    result = [1, 0, 0, 0, 0, 0]
    acc = base[:]
    e = m
    while e:
        if e & 1:
            result = mul(result, acc)
        acc = mul(acc, acc)
        e >>= 1
    return sum(comb(5, 5 - k) * result[k] for k in range(6))


def leading_base7_digits(value: int, count: int) -> str:
    ndigits = max(1, int(value.bit_length() * math.log(2) / math.log(7)))
    p = 7**ndigits
    while p <= value:
        ndigits += 1
        p *= 7
    lead = value // 7 ** (ndigits - count)
    digits = []
    for _ in range(count):
        digits.append(lead % 7)
        lead //= 7
    return "".join(str(d) for d in reversed(digits))


def main() -> None:
    for m in range(12):
        assert g_definition(m) == g_value(m)
    assert g_value(10) == 127278262644918
    print(leading_base7_digits(g_value(142857), 10))  # 5226432553


if __name__ == "__main__":
    main()
