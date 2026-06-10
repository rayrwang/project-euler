from collections import defaultdict

# Digit DP from the least significant digit: appending digit d to n appends
# digit (137 d + c) mod 10 to 137 n with the new carry (137 d + c) div 10
# (carries stay below 137), so the state is (carry, running digit-sum
# difference). After 18 digits the remaining carry flushes its own decimal
# digits into 137 n; states whose final difference is zero are counted.
# Verified against brute force below 10^4 and 10^5.


def solve(num_digits: int = 18, k: int = 137) -> int:
    dp: dict[tuple[int, int], int] = defaultdict(int)
    dp[(0, 0)] = 1
    for _ in range(num_digits):
        ndp: dict[tuple[int, int], int] = defaultdict(int)
        for (c, diff), w in dp.items():
            for d in range(10):
                t = k * d + c
                ndp[(t // 10, diff + d - t % 10)] += w
        dp = ndp
    total = 0
    for (c, diff), w in dp.items():
        if diff == sum(int(ch) for ch in str(c)):
            total += w
    return total


if __name__ == "__main__":
    print(solve())  # 20444710234716473
