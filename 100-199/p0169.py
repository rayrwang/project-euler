from functools import lru_cache


@lru_cache(maxsize=None)
def _h(n: int) -> int:
    # Number of ways to write n as a sum of powers of 2, each used at most twice.
    # h(2m) = h(m) + h(m-1); h(2m+1) = h(m).
    if n < 0:
        return 0
    if n == 0:
        return 1
    return _h(n // 2) if n & 1 else _h(n // 2) + _h(n // 2 - 1)


def solve(n: int = 10**25) -> int:
    return _h(n)


if __name__ == "__main__":
    print(solve())  # 178653872807
