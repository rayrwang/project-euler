from math import gcd

# Interval DP over the digit string 1..9: S[i][j] holds every exact rational
# reachable from digits i..j - the plain concatenated number, plus x op y
# over all split points and the four operations. Fractions are kept as
# normalised (numerator, denominator) pairs with exact integer arithmetic.
# The answer sums the distinct positive integers in S[0][8].


def solve(digits: str = "123456789") -> int:
    n = len(digits)
    table: list[list[set[tuple[int, int]]]] = [
        [set() for _ in range(n)] for _ in range(n)
    ]
    for i in range(n):
        table[i][i] = {(int(digits[i]), 1)}
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            vals = {(int(digits[i : j + 1]), 1)}
            for k in range(i, j):
                for an, ad in table[i][k]:
                    for bn, bd in table[k + 1][j]:
                        num, den = an * bd + bn * ad, ad * bd
                        g = gcd(num, den)
                        vals.add((num // g, den // g))
                        num = an * bd - bn * ad
                        g = gcd(num, den) or 1
                        vals.add((num // g, den // g))
                        num, den2 = an * bn, ad * bd
                        g = gcd(num, den2)
                        vals.add((num // g, den2 // g))
                        if bn != 0:
                            num, den2 = an * bd, ad * bn
                            if den2 < 0:
                                num, den2 = -num, -den2
                            g = gcd(abs(num), den2) or 1
                            vals.add((num // g, den2 // g))
            table[i][j] = vals
    return sum(num for num, den in table[0][n - 1] if den == 1 and num > 0)


if __name__ == "__main__":
    print(solve())  # 20101196798
