def solve(limit: int = 100) -> int:
    singles = list(range(1, 21)) + [25]
    doubles = [2 * i for i in range(1, 21)] + [50]
    trebles = [3 * i for i in range(1, 21)]
    darts = singles + doubles + trebles  # 62 distinct board segments
    n = len(darts)

    count = 0
    for f in doubles:  # finishing dart must be a double
        if f < limit:
            count += 1  # checkout in a single dart
        for x in darts:  # one preceding dart
            if x + f < limit:
                count += 1
        for i in range(n):  # two preceding darts, unordered multiset
            di = darts[i]
            if di + f >= limit:
                continue
            for j in range(i, n):
                if di + darts[j] + f < limit:
                    count += 1
    return count


if __name__ == "__main__":
    print(solve())  # 38182
