import numba

@numba.jit(cache=True)
def count_square_laminae(n):
    """Count square laminae using up to n tiles.

    For an outer width a, the hole width b shares a's parity and uses
    a^2 - b^2 tiles. Starting from the widest hole (b = a - 2, the thinnest
    border) and shrinking b increases the tile count monotonically, so we can
    stop as soon as it exceeds n.
    """
    count = 0
    a = 3
    while 4 * a - 4 <= n:        # thinnest lamina (b = a - 2) uses 4a - 4 tiles
        b = a - 2
        while b >= 1 and a * a - b * b <= n:
            count += 1
            b -= 2
        a += 1
    return count

if __name__ == "__main__":
    print(count_square_laminae(1_000_000))  # 1572729
