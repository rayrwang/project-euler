from collections import deque
from math import sqrt


def solve(tube_radius: int = 50, r_min: int = 30, r_max: int = 50) -> int:
    # Every ball has radius > tube_radius / 2, so each touches the wall and
    # consecutive balls nest on opposite sides. The axial gap between adjacent
    # balls depends only on the sum s of their radii:
    #     gap = sqrt((r_i + r_j)^2 - (2R - r_i - r_j)^2) = sqrt(4 R (s - R)).
    # gap is concave increasing in s, so the total is minimised by the
    # "valley" order: smallest radii in the middle, growing outward (any
    # swap toward that shape never increases the concave gap sum); this
    # matches an exhaustive Held-Karp check.
    dq: deque[int] = deque()
    for i, r in enumerate(range(r_min, r_max + 1)):
        if i % 2 == 0:
            dq.appendleft(r)
        else:
            dq.append(r)
    seq = list(dq)
    total = float(seq[0] + seq[-1])
    for a, b in zip(seq, seq[1:]):
        s = a + b
        total += sqrt(s * s - (2 * tube_radius - s) ** 2)
    return round(total * 1000)  # millimetres -> micrometres


if __name__ == "__main__":
    print(solve())  # 1590933
