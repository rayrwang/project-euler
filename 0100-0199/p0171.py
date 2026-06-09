from math import isqrt


def solve(digits: int = 20, mod: int = 10**9) -> int:
    # Sum every 0 < n < 10^20 whose digit-square-sum is a perfect square; report
    # the last 9 digits. Digit DP over positions tracking the square-sum, the
    # count of numbers, and their running total mod 10^9.
    squares = {i * i for i in range(isqrt(digits * 81) + 1)}
    dp: dict[int, tuple[int, int]] = {0: (1, 0)}
    for _ in range(digits):
        nxt: dict[int, tuple[int, int]] = {}
        for ss, (cnt, total) in dp.items():
            for d in range(10):
                key = ss + d * d
                c, t = nxt.get(key, (0, 0))
                nxt[key] = (c + cnt, (t + total * 10 + d * cnt) % mod)
        dp = nxt
    return sum(t for ss, (c, t) in dp.items() if ss in squares and ss > 0) % mod


if __name__ == "__main__":
    print(solve())  # 142989277
