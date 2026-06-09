def contains_origin(ax, ay, bx, by, cx, cy):
    # Signed side of the origin with respect to each edge (cross products).
    d1 = ax * by - bx * ay     # edge A->B
    d2 = bx * cy - cx * by     # edge B->C
    d3 = cx * ay - ax * cy     # edge C->A
    has_neg = d1 < 0 or d2 < 0 or d3 < 0
    has_pos = d1 > 0 or d2 > 0 or d3 > 0
    return not (has_neg and has_pos)   # inside iff all on the same side

if __name__ == "__main__":
    count = 0
    with open("assets/0102_triangles.txt") as f:
        for line in f:
            coords = [int(x) for x in line.split(",")]
            if contains_origin(*coords):
                count += 1
    print(count)  # 228
