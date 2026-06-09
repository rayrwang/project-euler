from functools import lru_cache


def solve(days: int = 30) -> int:
    # Count length-`days` strings over {O, A, L} with at most one A and no three
    # consecutive L. DP over (position, A used, trailing run of L).
    @lru_cache(maxsize=None)
    def count(pos: int, late: int, run: int) -> int:
        if pos == days:
            return 1
        total = count(pos + 1, late, 0)            # on time
        if late == 0:
            total += count(pos + 1, 1, 0)          # absent (only once)
        if run < 2:
            total += count(pos + 1, late, run + 1)  # late
        return total

    return count(0, 0, 0)


if __name__ == "__main__":
    print(solve())  # 1918080160
