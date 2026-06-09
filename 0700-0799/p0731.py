def A(n):
    """The 10 decimal digits of A = sum_{i>=1} 1 / (3^i 10^(3^i)) starting at
    the n-th digit after the decimal point.

    Those digits are floor(frac(10^(n-1) A) * 10^10). Shifting term i gives
    10^(n - 1 - 3^i) / 3^i. Terms with 3^i > n - 1 are smaller than
    10^(-(3^i - n)) and the first such exponent overshoots n by an enormous
    margin (powers of 3 are nowhere near n + 10 here), so they cannot touch
    the first dozens of digits. For 3^i <= n - 1 the integer part drops out
    of the fraction and the term contributes (10^(n - 1 - 3^i) mod 3^i) / 3^i.
    Put everything over the common denominator 3^m (m the largest valid i)
    and read off ten digits.
    """
    m = 1
    while 3 ** (m + 1) <= n - 1:
        m += 1
    numerator = 0
    for i in range(1, m + 1):
        r = pow(10, n - 1 - 3**i, 3**i)
        numerator += r * 3 ** (m - i)
    numerator %= 3**m
    return str(numerator * 10**10 // 3**m).rjust(10, "0")

if __name__ == "__main__":
    assert A(100) == "4938271604"
    assert A(10**8) == "2584642393"
    print(A(10**16))  # 6086371427
