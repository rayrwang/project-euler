def a_exceeds(n: int, limit: int) -> bool:
    # True if the least repunit divisible by n has length A(n) > limit.
    # Track repunit mod n: x -> (10x + 1) mod n.
    x = 1 % n
    k = 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
        if k > limit:
            return True
    return False


def solve(limit: int = 1_000_000) -> int:
    # A(n) <= n, so the first n with A(n) > limit satisfies n > limit.
    n = limit + 1
    while True:
        if n % 2 and n % 5:  # n coprime to 10
            if a_exceeds(n, limit):
                return n
        n += 1


if __name__ == "__main__":
    print(solve())  # 1000023
