def solve(max_digits: int = 100, mod: int = 10**5) -> int:
    # n has k digits, n = 10a + d (d = last digit, a = leading k-1 digits).
    # Moving d to the front gives n' = d*10^(k-1) + a; requiring n' = m*n
    # yields a = d*(10^(k-1) - m) / (10m - 1).
    total = 0
    for k in range(2, max_digits + 1):
        pk = 10 ** (k - 1)
        for m in range(1, 10):
            denom = 10 * m - 1
            for d in range(1, 10):
                num = d * (pk - m)
                if num % denom:
                    continue
                a = num // denom
                lo = 1 if k == 2 else 10 ** (k - 2)
                if lo <= a < pk:
                    total += (10 * a + d) % mod
    return total % mod


if __name__ == "__main__":
    print(solve())  # 59206
