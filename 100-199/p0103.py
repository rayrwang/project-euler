from itertools import combinations, product

def is_special(a):
    a = sorted(a)
    n = len(a)
    # Rule (ii): a set of k+1 smallest must outweigh the k largest.
    for q in range(1, (n - 1) // 2 + 1):
        if sum(a[: q + 1]) <= sum(a[n - q:]):
            return False
    # Rule (i): disjoint subsets have distinct sums  <=>  all subset sums distinct.
    sums = set()
    for r in range(n + 1):
        for combo in combinations(a, r):
            s = sum(combo)
            if s in sums:
                return False
            sums.add(s)
    return True

def solve():
    base = [11, 18, 19, 20, 22, 25]            # the optimum special set of size 6
    mid = base[len(base) // 2]
    candidate = sorted([mid] + [mid + x for x in base])   # construct size-7 candidate

    best = candidate
    best_sum = sum(candidate)
    radius = 2                                  # confirm by a small local search
    for deltas in product(range(-radius, radius + 1), repeat=len(candidate)):
        trial = [candidate[i] + deltas[i] for i in range(len(candidate))]
        if sum(trial) >= best_sum or len(set(trial)) != len(trial) or min(trial) <= 0:
            continue
        if is_special(trial):
            best, best_sum = sorted(trial), sum(trial)
    return "".join(str(x) for x in best)

if __name__ == "__main__":
    print(solve())  # 20313839404245
