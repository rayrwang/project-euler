import numpy as np


def solve(players: int = 100) -> float:
    # Track the gap between the two dice on the cycle. Each turn both dice move
    # -1/0/+1 with probability 1/6, 4/6, 1/6, so the gap changes by D in [-2, 2]
    # with the convolved distribution. Gap 0 is absorbing; solve for the expected
    # number of turns starting from the opposite players (gap = players/2).
    probs = {-2: 1 / 36, -1: 8 / 36, 0: 18 / 36, 1: 8 / 36, 2: 1 / 36}
    a = np.zeros((players, players))
    b = np.ones(players)
    a[0, 0] = 1
    b[0] = 0
    for d in range(1, players):
        a[d, d] += 1
        for delta, pr in probs.items():
            t = (d + delta) % players
            if t != 0:
                a[d, t] -= pr
    expected = np.linalg.solve(a, b)
    return round(float(expected[players // 2]), 6)


if __name__ == "__main__":
    print(solve())  # 3780.618622
