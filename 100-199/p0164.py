from collections import defaultdict


def solve(length: int = 20) -> int:
    # Count length-digit numbers (no leading zero) where no three consecutive
    # digits sum to more than 9. DP over the last two digits.
    dp: dict[tuple[int, int], int] = defaultdict(int)
    for d1 in range(1, 10):
        for d2 in range(10):
            dp[(d1, d2)] += 1
    for _ in range(length - 2):
        nxt: dict[tuple[int, int], int] = defaultdict(int)
        for (a, b), cnt in dp.items():
            for x in range(max(0, 10 - a - b)):
                nxt[(b, x)] += cnt
        dp = nxt
    return sum(dp.values())


if __name__ == "__main__":
    print(solve())  # 378158756814587
