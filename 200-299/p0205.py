def _distribution(dice: int, sides: int) -> dict[int, int]:
    dist = {0: 1}
    for _ in range(dice):
        nxt: dict[int, int] = {}
        for total, ways in dist.items():
            for face in range(1, sides + 1):
                nxt[total + face] = nxt.get(total + face, 0) + ways
        dist = nxt
    return dist


def solve() -> float:
    # Peter rolls nine 4-sided dice, Colin six 6-sided dice; P(Peter > Colin).
    peter = _distribution(9, 4)
    colin = _distribution(6, 6)
    outcomes = 4**9 * 6**6
    wins = sum(pw * cw for ps, pw in peter.items()
               for cs, cw in colin.items() if ps > cs)
    return round(wins / outcomes, 7)


if __name__ == "__main__":
    print(solve())  # 0.5731441
