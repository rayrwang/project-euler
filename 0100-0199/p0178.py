from collections import defaultdict


def solve(max_len: int = 40) -> int:
    # Step numbers (consecutive digits differ by 1) that are also pandigital
    # (use every digit 0-9). DP over (last digit, set of digits used).
    total = 0
    dp: dict[tuple[int, int], int] = defaultdict(int)
    for first in range(1, 10):
        dp[(first, 1 << first)] += 1
    for length in range(1, max_len + 1):
        for (last, mask), c in dp.items():
            if mask == 0x3FF:
                total += c
        if length == max_len:
            break
        nxt: dict[tuple[int, int], int] = defaultdict(int)
        for (last, mask), c in dp.items():
            for step in (last - 1, last + 1):
                if 0 <= step <= 9:
                    nxt[(step, mask | (1 << step))] += c
        dp = nxt
    return total


if __name__ == "__main__":
    print(solve())  # 126461847755
