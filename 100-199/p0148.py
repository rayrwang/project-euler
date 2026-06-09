def solve(rows: int = 1_000_000_000) -> int:
    # Entries in row n not divisible by 7 = product of (base-7 digit + 1)
    # (Kummer/Lucas). Sum over rows 0..rows-1 by a base-7 digit DP: a full block
    # of 7^j rows contributes 28^j (since 1+2+...+7 = 28).
    digits = []
    x = rows
    while x:
        digits.append(x % 7)
        x //= 7
    digits.reverse()
    total = 0
    prefix = 1
    length = len(digits)
    for i, d in enumerate(digits):
        lower = length - 1 - i
        total += prefix * (d * (d + 1) // 2) * (28**lower)
        prefix *= d + 1
    return total


if __name__ == "__main__":
    print(solve())  # 2129970655314432
