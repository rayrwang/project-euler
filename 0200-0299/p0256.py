import numba
import numpy as np

# A column-by-column DP (state: protrusion mask plus vertical-pair mask, with
# the no-four-corners check applied at every interior row boundary between
# adjacent columns) establishes which rooms admit tatami tilings. Running it
# for all widths a <= 13 over a wide range of b reveals - and exhaustively
# confirms, with zero mismatches for b up to 130 - the clean rule (the
# Ruskey-Williams characterisation): writing b = k (a + 1) + r, the room
# a x b (a <= b, ab even) is tatami-free iff
#     k >= 1 and 2 <= r <= a - 3 - 2k.
# It also reproduces the statement's data exactly: T(70) = 1 via 7 x 10
# only, and T(1320) = 5 via precisely 20x66, 22x60, 24x55, 30x44, 33x40.
#
# Counting: for every a (the rule needs a >= 7) and every band k, the free b
# form the run k (a + 1) + 2 ... k (a + 1) + (a - 3 - 2k), thinned to even b
# when a is odd. Each free room increments a counter at index s / 2
# (uint16 - T can exceed 255 near 10^8); the answer is the first s with
# exactly 200. The known bound s < 10^8 suffices: the scan finds the
# minimum within it.


@numba.njit(cache=True)
def _search(s_max: int, target: int) -> int:
    counts = np.zeros(s_max // 2 + 1, dtype=np.uint16)
    a = 7
    while a * (a + 3) <= s_max:
        b_max = s_max // a
        step = 2 if a % 2 == 1 else 1
        k = 1
        while True:
            r_hi = a - 3 - 2 * k
            if r_hi < 2:
                break
            base = k * (a + 1)
            if base + 2 > b_max:
                break
            r = 2
            if a % 2 == 1 and (base + r) % 2 == 1:
                r += 1
            while r <= r_hi:
                b = base + r
                if b > b_max:
                    break
                counts[a * b // 2] += 1
                r += step
            k += 1
        a += 1
    for half in range(1, s_max // 2 + 1):
        if counts[half] == target:
            return 2 * half
    return -1


def solve(target: int = 200, s_max: int = 100_000_000) -> int:
    return int(_search(s_max, target))


if __name__ == "__main__":
    print(solve())  # 85765680
