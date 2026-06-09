def _rows(width: int) -> list[frozenset[int]]:
    # Every way to fill one row of given width with bricks of length 2 and 3,
    # recorded by the set of internal crack positions.
    result: list[frozenset[int]] = []

    def build(pos: int, cracks: list[int]) -> None:
        if pos == width:
            result.append(frozenset(cracks))
            return
        for brick in (2, 3):
            if pos + brick <= width:
                build(pos + brick, cracks if pos + brick == width else cracks + [pos + brick])

    build(0, [])
    return result


def solve(width: int = 32, height: int = 10) -> int:
    rows = _rows(width)
    n = len(rows)
    compatible = [[j for j in range(n) if rows[i].isdisjoint(rows[j])] for i in range(n)]
    counts = [1] * n
    for _ in range(height - 1):
        counts = [sum(counts[j] for j in compatible[i]) for i in range(n)]
    return sum(counts)


if __name__ == "__main__":
    print(solve())  # 806844323190414
