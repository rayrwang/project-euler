def solve(limit: int = 10**8) -> int:
    # An ambiguous number is the midpoint of a Farey-neighbour pair, with
    # denominator 2bd for the two denominators b, d. Counting such pairs inside
    # (0, 1/100) is a walk over the Stern-Brocot subdivision of (0/1, 1/100):
    # node (b, d) has children (b, b+d) and (b+d, d); count those with 2bd <= L.
    # Each left spine (b fixed, d growing) is summed in closed form.
    half = limit // 2
    total = 0
    stack = [(1, 100)]
    while stack:
        b, d = stack.pop()
        if b * d > half:
            continue
        spine = (half - b * d) // (b * b) + 1   # nodes (b, d + k b), k = 0..spine-1
        total += spine
        for k in range(spine):
            dd = d + k * b
            bb = b + dd                          # right child denominator
            if bb * dd > half:
                break
            stack.append((bb, dd))
    # Straddling pairs (0/1, 1/d) for 51 <= d <= 99 give midpoints 1/(2d) in
    # (0, 1/100) that lie outside the subdivision; add those within the bound.
    total += sum(1 for d in range(51, 100) if 2 * d <= limit)
    return total


if __name__ == "__main__":
    print(solve())  # 52374425
