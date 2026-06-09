def _is_nondivisor(n: int) -> bool:
    # The tribonacci sequence mod n is purely periodic (it returns to its start
    # 1, 1, 1); n divides some term iff a 0 appears before that recurrence.
    a, b, c = 1 % n, 1 % n, 1 % n
    start = (a, b, c)
    while True:
        a, b, c = b, c, (a + b + c) % n
        if c == 0:
            return False
        if (a, b, c) == start:
            return True


def solve(rank: int = 124) -> int:
    found = 0
    n = 1
    while True:
        n += 2
        if _is_nondivisor(n):
            found += 1
            if found == rank:
                return n


if __name__ == "__main__":
    print(solve())  # 2009
