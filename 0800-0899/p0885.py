from math import factorial

MOD = 1123455689
FACT = [factorial(i) for i in range(19)]


def s(n: int) -> int:
    """Sum of f(d) over all d with at most n digits.

    Pad every number with leading zeros to exactly n digits (zero itself
    contributes nothing).  f(d) depends only on the digit multiset, and a
    multiset with digit counts c_0, ..., c_9 arises from exactly
    n! / (c_0! ... c_9!) numbers, so S(n) is a sum over multisets.  The
    recursion fixes the counts of digits 1..9 one at a time, building the
    sorted number f and the denominator product incrementally; whatever
    remains is the count of zeros, which f ignores.
    """
    fact_n = FACT[n]

    def rec(digit: int, remaining: int, f: int, denom: int) -> int:
        if digit == 10:
            return (fact_n // (denom * FACT[remaining])) * f
        total = 0
        for c in range(remaining + 1):
            total += rec(digit + 1, remaining - c, f, denom * FACT[c])
            f = f * 10 + digit  # append one more copy of this digit
        return total

    return rec(1, n, 0, 1)


if __name__ == "__main__":
    assert s(1) == 45
    assert s(5) == 1543545675
    print(s(18) % MOD)  # 827850196
