def num_hexagons(n: int) -> int:
    """Count integer-sided equiangular convex hexagons with perimeter <= n.

    Inscribe the hexagon in an equilateral triangle of side x by extending
    three alternate sides; the three cut-off corners are equilateral triangles
    of sides a <= b <= c. The hexagon sides are a, b, c and x-a-b, x-b-c, x-a-c,
    giving perimeter 3x - (a+b+c). Using the smaller of the two circumscribing
    triangles forces x >= a+b+c, so each hexagon is counted once.
    """
    total = 0
    for s in range(3, n // 2 + 1):  # s = a + b + c
        # partitions of s into exactly 3 positive parts
        p3 = round(s * s / 12)
        # x ranges over s <= x <= (n + s) // 3
        total += p3 * ((n + s) // 3 - s + 1)
    return total

if __name__ == "__main__":
    print(num_hexagons(55106))  # 2668608479740672
