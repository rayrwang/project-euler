def solve(pm: int = 524287, target: int = 990000, users: int = 10**6) -> int:
    # Lagged-Fibonacci call generator + union-find; return the count of
    # successful calls when the prime minister's component first reaches 99%.
    parent = list(range(users))
    size = [1] * users

    def find(x: int) -> int:
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    hist = [(100003 - 200003 * k + 300007 * k**3) % 1000000 for k in range(1, 56)]

    def value(k: int) -> int:  # 1-indexed
        if k <= 55:
            return hist[k - 1]
        v = (hist[k - 1 - 24] + hist[k - 1 - 55]) % 1000000
        hist.append(v)
        return v

    k = 1
    successful = 0
    while True:
        caller, called = value(k), value(k + 1)
        k += 2
        if caller == called:
            continue
        successful += 1
        ra, rb = find(caller), find(called)
        if ra != rb:
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        if size[find(pm)] >= target:
            return successful


if __name__ == "__main__":
    print(solve())  # 2325629
