def solve(lo: int = 3, hi: int = 1000) -> int:
    # (a-1)^n + (a+1)^n mod a^2 keeps only the k=0,1 binomial terms.
    # Even n -> remainder 2; odd n -> 2*a*n mod a^2 = a*((2n) mod a).
    # Max of (2n mod a): a-1 if a is odd (2 invertible), else a-2 (stays even).
    total = 0
    for a in range(lo, hi + 1):
        total += a * (a - 1) if a % 2 else a * (a - 2)
    return total


if __name__ == "__main__":
    print(solve())  # 333082500
