from math import factorial


def solve(turns: int = 15) -> int:
    # Turn i has 1 blue and i red discs: P(blue)=1/(i+1). Scaling each turn by
    # (i+1), blue carries weight 1 and red weight i. Coefficient of x^k in
    # prod_{i=1..turns} (i + x) is the weighted count of exactly k blue draws.
    coeff = [1]
    for i in range(1, turns + 1):
        nxt = [0] * (len(coeff) + 1)
        for j, c in enumerate(coeff):
            nxt[j] += c * i      # red drawn
            nxt[j + 1] += c      # blue drawn
        coeff = nxt
    need = turns // 2 + 1        # strictly more blue than red
    wins = sum(coeff[need:])
    total = factorial(turns + 1)  # product of (i+1)
    return total // wins          # fair prize, rounded down


if __name__ == "__main__":
    print(solve())  # 2269
