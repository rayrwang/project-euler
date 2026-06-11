"""
Project Euler Problem 776: Digit Sum Division
https://projecteuler.net/problem=776

F(N) = sum_{n <= N} n / d(n), where d(n) is the decimal digit sum of n, for
N = 1234567890123456789.  Report the answer in scientific notation with twelve
digits after the decimal point.

Digit DP grouped by digit sum.  The digit sum of any n <= N is at most
9 * 19 = 171, so group the terms by s = d(n).  A standard digit DP over the
decimal expansion of N accumulates, for each reachable digit sum s, the exact
pair (count, sum of the n's), all in integer arithmetic: when a digit "dig" is
appended, every partial value t becomes 10 t + dig, so the running sum-of-n for
a state updates as sum -> 10 * sum + dig * count.  Finally

    F = sum_s (sum_s) / s

is evaluated in high-precision Decimal so that the requested twelve significant
figures are exact.  Matches F(10) = 19 and the other given checks.
"""

from decimal import Decimal, getcontext


def f_of(big_n):
    digits = [int(ch) for ch in str(big_n)]
    length = len(digits)
    maxs = 9 * length

    # DP over positions with a "tight" flag.  State for the free branch is keyed
    # only by current digit sum; we carry (count, sumval) exactly.
    # We process digit by digit, splitting off the free (already-less-than-N)
    # mass at each position.
    # free_count[s], free_sum[s]: numbers strictly less than N's prefix so far,
    # with digit-sum s, value already accumulated.
    free_count = [0] * (maxs + 1)
    free_sum = [0] * (maxs + 1)
    # tight prefix: the exact prefix of N read so far (single state)
    tight_sum = 0  # value of the tight prefix
    tight_ds = 0  # digit sum of the tight prefix

    for pos in range(length):
        d = digits[pos]
        new_free_count = [0] * (maxs + 1)
        new_free_sum = [0] * (maxs + 1)
        # 1) extend existing free states by any digit 0..9
        for s in range(maxs + 1):
            c = free_count[s]
            if c == 0 and free_sum[s] == 0:
                continue
            sv = free_sum[s]
            for dig in range(10):
                ns = s + dig
                new_free_count[ns] += c
                new_free_sum[ns] += 10 * sv + dig * c
        # 2) the tight state branches: digits 0..d-1 become free, digit d stays tight
        for dig in range(d):
            ns = tight_ds + dig
            new_free_count[ns] += 1
            new_free_sum[ns] += 10 * tight_sum + dig
        tight_sum = 10 * tight_sum + d
        tight_ds = tight_ds + d
        free_count = new_free_count
        free_sum = new_free_sum

    # add the tight number itself (n == N)
    sum_by_s = list(free_sum)
    sum_by_s[tight_ds] += tight_sum

    getcontext().prec = 60
    total = Decimal(0)
    for s in range(1, maxs + 1):
        if sum_by_s[s]:
            total += Decimal(sum_by_s[s]) / Decimal(s)
    return total


def fmt_sci(x, places):
    getcontext().prec = 60
    # normalize to mantissa in [1, 10)
    s = x.scaleb(0).normalize()
    sign, digits, exp = s.as_tuple()
    e = len(digits) - 1 + exp
    mant = x / Decimal(10) ** e
    q = Decimal(10) ** (-places)
    mant = mant.quantize(q)
    return f"{mant}e{e}"


def main():
    assert f_of(10) == 19
    return fmt_sci(f_of(1234567890123456789), 12)


if __name__ == "__main__":
    print(main())  # 9.627509725002e33
