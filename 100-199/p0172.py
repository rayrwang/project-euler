from math import comb


def _arrangements(length: int, limits: list[int]) -> int:
    # Number of ordered strings of the given length where digit i appears at
    # most limits[i] times, built by interleaving each digit's copies.
    dp = [0] * (length + 1)
    dp[0] = 1
    for mx in limits:
        nxt = [0] * (length + 1)
        for t in range(length + 1):
            if dp[t]:
                for k in range(min(mx, length - t) + 1):
                    nxt[t + k] += dp[t] * comb(t + k, k)
        dp = nxt
    return dp[length]


def solve(length: int = 18) -> int:
    # 18-digit numbers (no leading zero) with no digit used more than 3 times.
    total = _arrangements(length, [3] * 10)
    leading_zero = _arrangements(length - 1, [2] + [3] * 9)
    return total - leading_zero


if __name__ == "__main__":
    print(solve())  # 227485267000992000
