from functools import lru_cache


@lru_cache(maxsize=None)
def _f(state: tuple[int, int, int, int, int]) -> float:
    # state = counts of (A1,A2,A3,A4,A5). A pick is uniform over all sheets.
    # Picking size k<5 removes it and adds one each of the smaller sizes
    # (repeated halving keeping one half); picking A5 just uses it.
    total = sum(state)
    if total == 0:
        return 0.0
    res = 1.0 if total == 1 else 0.0
    for k in range(5):
        if state[k] == 0:
            continue
        nxt = list(state)
        nxt[k] -= 1
        if k < 4:
            for m in range(k + 1, 5):
                nxt[m] += 1
        res += state[k] / total * _f(tuple(nxt))
    return res


def solve() -> float:
    # Expected single-sheet picks, excluding the first (the A1) and last (lone A5).
    return round(_f((1, 0, 0, 0, 0)) - 2, 6)


if __name__ == "__main__":
    print(f"{solve():.6f}")  # 0.464399
