from collections import deque


def f(n: int) -> int:
    """Least positive multiple of n whose decimal digits are all <= 2."""
    # BFS over remainders mod n. Build the number digit by digit, trying
    # digits in increasing order and lengths in increasing order, so the
    # first time a remainder is reached it is via the smallest such number.
    # The first time remainder 0 is reached gives f(n).
    seen = [False] * n
    queue: deque[tuple[int, int]] = deque()
    for d in (1, 2):  # leading digit, no leading zero
        r = d % n
        if not seen[r]:
            seen[r] = True
            queue.append((r, d))
    while queue:
        r, num = queue.popleft()
        if r == 0:
            return num
        for d in (0, 1, 2):
            r2 = (r * 10 + d) % n
            if not seen[r2]:
                seen[r2] = True
                queue.append((r2, num * 10 + d))
    raise AssertionError("unreachable: every n has such a multiple")


def solve(limit: int) -> int:
    return sum(f(n) // n for n in range(1, limit + 1))


if __name__ == "__main__":
    assert solve(100) == 11363107
    print(solve(10000))  # 1111981904675169
