def solve(limit: int = 10**6, lo: int = 1, hi: int = 10) -> int:
    # A square lamina of t tiles needs t = a^2 - c^2 with a > c >= 1 and a == c
    # (mod 2), i.e. t = 4 d s with 1 <= d < s. The number of laminae for t is the
    # count of such (d, s); tally how many t <= limit have between lo and hi.
    counts = [0] * (limit + 1)
    d = 1
    while 4 * d * (d + 1) <= limit:
        s = d + 1
        while 4 * d * s <= limit:
            counts[4 * d * s] += 1
            s += 1
        d += 1
    return sum(1 for t in range(1, limit + 1) if lo <= counts[t] <= hi)


if __name__ == "__main__":
    print(solve())  # 209566
