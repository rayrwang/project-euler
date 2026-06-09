def solve(num: int = 1, den: int = 12345) -> int:
    # Writing x = 2^t, every integer x >= 2 gives a partition with k = x(x-1);
    # it is perfect iff x is a power of two. P at the threshold k(x) equals
    # (powers of two <= x) / (x - 1). Find the first x where that drops below
    # num/den; the answer is the corresponding k = x(x-1).
    x = 2
    perfect = 0
    while True:
        if x & (x - 1) == 0:
            perfect += 1
        total = x - 1
        if perfect * den < total * num:
            return x * (x - 1)
        x += 1


if __name__ == "__main__":
    print(solve())  # 44043947822
