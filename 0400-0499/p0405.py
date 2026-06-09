from collections import Counter

MOD = 17**7

Tile = tuple[int, int, int, int]

def subdivide(tiles: list[Tile]) -> list[Tile]:
    """One substitution step; coordinates are scaled by 4 to stay integral.

    A horizontal 2:1 tile becomes two vertical side strips and a middle
    square cut into two stacked horizontal tiles (and the same rotated for
    vertical tiles), per the figure in the problem.
    """
    out = []
    for (x, y, w, h) in tiles:
        x, y, w, h = 4 * x, 4 * y, 4 * w, 4 * h
        if w == 2 * h:
            q = w // 4
            out += [(x, y, q, h), (x + 3 * q, y, q, h),
                    (x + q, y, 2 * q, h // 2), (x + q, y + h // 2, 2 * q, h // 2)]
        else:
            q = h // 4
            out += [(x, y, w, q), (x, y + 3 * q, w, q),
                    (x, y + q, w // 2, 2 * q), (x + w // 2, y + q, w // 2, 2 * q)]
    return out

def four_meet_points(tiles: list[Tile]) -> int:
    """Four tiles meet at a point exactly when it is a corner of four tiles."""
    c: Counter[tuple[int, int]] = Counter()
    for (x, y, w, h) in tiles:
        c[(x, y)] += 1
        c[(x + w, y)] += 1
        c[(x, y + h)] += 1
        c[(x + w, y + h)] += 1
    return sum(1 for v in c.values() if v == 4)

def f_mod(n_base: int, n_exp: int) -> int:
    """f(n) mod 17^7 for n = n_base^n_exp via the closed form
    f(n) = (6*4^n - 20*2^n + 15 - (-1)^n) / 15."""
    phi = 16 * 17**6  # Euler phi of 17^7; 2 and 4 are coprime to 17^7
    e = pow(n_base, n_exp, phi)
    parity = pow(n_base % 2, n_exp)  # n is even iff n_base is even (n_exp > 0)
    sign = -1 if parity else 1
    inv15 = pow(15, -1, MOD)
    return (6 * pow(4, e, MOD) - 20 * pow(2, e, MOD) + 15 - sign) * inv15 % MOD

if __name__ == "__main__":
    # Closed form against direct simulation for n = 1..8.
    tiles: list[Tile] = [(0, 0, 2, 1)]
    for n in range(1, 9):
        tiles = subdivide(tiles)
        assert four_meet_points(tiles) == (6 * 4**n - 20 * 2**n + 15 - (-1)**n) // 15
    assert f_mod(10, 9) == 126897180  # given: f(10^9) mod 17^7
    print(f_mod(10, 10**18))  # 237696125
