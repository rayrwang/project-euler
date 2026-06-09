from math import comb


def solve(dice: int = 20, sides: int = 12, top: int = 10, target: int = 70) -> int:
    # Classify each roll by m, the value of the top-th largest die. Let j be
    # the number of dice strictly above m (all of which are in the top set,
    # so j < top); the top set is completed by top - j dice equal to m, and i
    # >= top - j dice in total show m, with the rest strictly below m. Count:
    # choose which dice are high (C(dice, j)) with an ordered value DP, which
    # show m (C(dice - j, i)), and let the remaining dice take any of the
    # m - 1 smaller values. The high dice must sum to target - (top - j) m.
    def high_tuples(j: int, low: int, total: int) -> int:
        # Ordered j-tuples with entries in [low, sides] summing to total.
        dp = [0] * (total + 1)
        dp[0] = 1
        for _ in range(j):
            nd = [0] * (total + 1)
            for s in range(total + 1):
                if dp[s]:
                    for v in range(low, sides + 1):
                        if s + v <= total:
                            nd[s + v] += dp[s]
            dp = nd
        return dp[total]

    total = 0
    for m in range(1, sides + 1):
        for j in range(top):
            s = target - (top - j) * m
            if s < 0:
                continue
            nj = high_tuples(j, m + 1, s) if j else int(s == 0)
            if nj == 0:
                continue
            placements = sum(
                comb(dice - j, i) * (m - 1) ** (dice - j - i)
                for i in range(top - j, dice - j + 1)
            )
            total += comb(dice, j) * nj * placements
    return total


if __name__ == "__main__":
    print(solve())  # 7448717393364181966
