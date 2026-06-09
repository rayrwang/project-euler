from collections import defaultdict


def solve(n: int = 10**9, cost0: int = 1, cost1: int = 4) -> int:
    # Build the optimal prefix-free code greedily: repeatedly split the cheapest
    # current leaf of weight w into children of weight w+cost0 and w+cost1.
    # Splitting changes the total leaf-weight sum by w + cost0 + cost1. Leaves of
    # equal weight are batched so n up to 1e9 is handled in a short loop.
    counts: dict[int, int] = defaultdict(int)
    counts[0] = 1
    leaves = 1
    total = 0
    w = 0
    while leaves < n:
        c = counts[w]
        if c:
            e = min(c, n - leaves)
            total += e * (w + cost0 + cost1)
            leaves += e
            counts[w] -= e
            counts[w + cost0] += e
            counts[w + cost1] += e
        w += 1
    return total


if __name__ == "__main__":
    print(solve())  # 64564225042
