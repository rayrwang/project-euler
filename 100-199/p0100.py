def solve():
    """Blue-disc count of the first arrangement with over 10^12 total discs for
    which P(two blue) = 1/2.

    2 b (b-1) = n (n-1) rearranges, with u = 2n-1 and v = 2b-1, to the negative
    Pell equation u^2 - 2 v^2 = -1, whose solutions follow (u, v) -> (3u+4v, 2u+3v).
    """
    limit = 10**12
    u, v = 1, 1
    while True:
        u, v = 3 * u + 4 * v, 2 * u + 3 * v
        total = (u + 1) // 2
        blue = (v + 1) // 2
        if total > limit:
            return blue

if __name__ == "__main__":
    print(solve())  # 756872327473
