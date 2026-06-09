from funcs import is_prime


def solve(target: int = 2000) -> int:
    # Only ring corners can reach PD = 3. For ring n the first tile
    # 3n^2-3n+2 has neighbour differences including 6n-1, 6n+1, 12n+5; the
    # last tile 3n^2+3n+1 (for n >= 2) has 6n-1, 6n+5, 12n-7. PD = 3 exactly
    # when those three are all prime. Tile 1 is the first PD = 3 tile, and
    # ring 1's last tile (7) is a special case that does not qualify.
    count = 1  # tile 1
    if count == target:
        return 1
    n = 1
    while True:
        if is_prime(6 * n - 1) and is_prime(6 * n + 1) and is_prime(12 * n + 5):
            count += 1
            if count == target:
                return 3 * n * n - 3 * n + 2
        if n >= 2 and is_prime(6 * n - 1) and is_prime(6 * n + 5) and is_prime(12 * n - 7):
            count += 1
            if count == target:
                return 3 * n * n + 3 * n + 1
        n += 1


if __name__ == "__main__":
    print(solve())  # 14516824220
