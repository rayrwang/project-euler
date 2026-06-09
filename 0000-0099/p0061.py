from collections import defaultdict

def figurate(p):
    """All 4-digit p-gonal numbers."""
    formulas = {
        3: lambda n: n * (n + 1) // 2,
        4: lambda n: n * n,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2),
    }
    f = formulas[p]
    nums, n = [], 1
    while True:
        v = f(n)
        if v > 9999:
            break
        if v >= 1000:
            nums.append(v)
        n += 1
    return nums

def solve():
    # Index each type's numbers by their leading two digits for instant matching.
    by_prefix = {p: defaultdict(list) for p in range(3, 9)}
    for p in range(3, 9):
        for v in figurate(p):
            by_prefix[p][str(v)[:2]].append(v)

    def extend(chain, used):
        if len(chain) == 6:
            return chain if str(chain[-1])[2:] == str(chain[0])[:2] else None
        suffix = str(chain[-1])[2:]
        for p in range(3, 9):
            if p in used:
                continue
            for v in by_prefix[p].get(suffix, []):
                found = extend(chain + [v], used | {p})
                if found:
                    return found
        return None

    # Anchor the octagonals (type 8) to break the cycle's rotational symmetry.
    for start in figurate(8):
        chain = extend([start], {8})
        if chain:
            return sum(chain)
    return None

if __name__ == "__main__":
    print(solve())  # 28684
