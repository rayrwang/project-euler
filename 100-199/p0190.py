from fractions import Fraction


def solve(max_m: int = 15) -> int:
    # Maximise x_1 x_2^2 ... x_m^m subject to sum x_i = m. Weighted AM-GM gives
    # x_i = 2i/(m+1); sum the floors of the resulting products for m = 2..15.
    total = 0
    for m in range(2, max_m + 1):
        product = Fraction(1)
        for i in range(1, m + 1):
            product *= Fraction(2 * i, m + 1) ** i
        total += int(product)
    return total


if __name__ == "__main__":
    print(solve())  # 371048281
