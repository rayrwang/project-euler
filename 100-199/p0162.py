from itertools import combinations


def solve(max_len: int = 16) -> str:
    # Count hexadecimal numbers of up to 16 digits (no leading zero) containing
    # at least one 0, one 1 and one A, by inclusion-exclusion over which of the
    # three required digits are forbidden. Result is reported in hexadecimal.
    required = (0, 1, 0xA)
    total = 0
    for length in range(1, max_len + 1):
        for r in range(4):
            for forbidden in combinations(required, r):
                alpha = 16 - len(forbidden)
                if 0 in forbidden:  # 0 absent: first digit is any allowed symbol
                    count = alpha**length
                else:
                    count = (alpha - 1) * alpha ** (length - 1)
                total += (-1) ** r * count
    return format(total, "X")


if __name__ == "__main__":
    print(solve())  # 3D58725572C62302
