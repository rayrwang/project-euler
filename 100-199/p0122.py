def chain_len(n: int) -> int:
    # Shortest addition chain length for n = fewest multiplications for x^n.
    if n == 1:
        return 0

    def dfs(chain: list[int], maxd: int) -> bool:
        last = chain[-1]
        if last == n:
            return True
        depth = len(chain) - 1
        if depth == maxd:
            return False
        if last << (maxd - depth) < n:  # even repeated doubling can't reach n
            return False
        for i in range(len(chain) - 1, -1, -1):  # try largest sums first
            s = last + chain[i]
            if s > n:
                continue
            chain.append(s)
            if dfs(chain, maxd):
                return True
            chain.pop()
        return False

    d = 1
    while not dfs([1], d):
        d += 1
    return d


def solve(limit: int = 200) -> int:
    return sum(chain_len(k) for k in range(1, limit + 1))


if __name__ == "__main__":
    print(solve())  # 1582
