def solve() -> int:
    with open("assets/0107_network.txt") as f:
        rows = [line.strip().split(",") for line in f if line.strip()]
    n = len(rows)
    edges = []
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            c = rows[i][j]
            if c != "-":
                w = int(c)
                total += w
                edges.append((w, i, j))
    edges.sort()
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    mst = 0
    used = 0
    for w, a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            mst += w
            used += 1
            if used == n - 1:
                break
    return total - mst


if __name__ == "__main__":
    print(solve())  # 259679
