# f(n, k) counts k-element subsets of {1..n} with odd sum. Brute force over
# all odd n <= 301 shows f(n, k) is odd exactly when n = 4m + 1, k = 4j + 1
# and j is a binary submask of m (a Lucas-style condition, giving
# 2^popcount(m) valid k per n). So the number of odd-triplets with n <= 10^12
# is sum over m <= (10^12 - 1) / 4 of 2^popcount(m), computed digit by digit:
# the m below a set bit of M contribute 2^(ones so far) * 3^(free bits).


def solve(limit: int = 10**12) -> int:
    m_max = (limit - 1) // 4
    total = 0
    ones = 0
    bits = bin(m_max)[2:]
    for i, b in enumerate(bits):
        if b == "1":
            total += 2**ones * 3 ** (len(bits) - i - 1)
            ones += 1
    return total + 2**ones  # m = m_max itself


if __name__ == "__main__":
    print(solve())  # 997104142249036713
