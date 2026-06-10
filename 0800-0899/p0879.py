from math import gcd

import numba
import numpy as np


def _between_masks(w: int, h: int) -> np.ndarray:
    """between[a][b] = bitmask of grid spots strictly between a and b."""
    n = w * h
    between = np.zeros((n, n), dtype=np.int64)
    for a in range(n):
        ax, ay = a % w, a // w
        for b in range(n):
            if a == b:
                continue
            dx, dy = b % w - ax, b // w - ay
            g = gcd(abs(dx), abs(dy))
            m = 0
            for k in range(1, g):
                m |= 1 << ((ay + k * dy // g) * w + (ax + k * dx // g))
            between[a][b] = m
    return between


@numba.jit(cache=True)
def _count(n: int, between: np.ndarray) -> int:
    """Number of achievable passwords (sequences of >= 2 distinct spots).

    Tracing toward any remaining spot selects the nearest remaining spot
    on the segment, so a sequence is achievable exactly when, for every
    consecutive pair, all grid spots strictly between them were already
    selected earlier.  f[mask][cur] counts achievable orderings of the
    spots in mask ending at cur; every state with at least two spots is a
    distinct password.
    """
    f = np.zeros((1 << n, n), dtype=np.int64)
    for s in range(n):
        f[1 << s][s] = 1
    total = 0
    for mask in range(1, 1 << n):
        for cur in range(n):
            if not (mask >> cur) & 1:
                continue
            prev_mask = mask ^ (1 << cur)
            if prev_mask == 0:
                continue
            acc = 0
            for prev in range(n):
                if (prev_mask >> prev) & 1 and f[prev_mask][prev]:
                    if between[prev][cur] & ~prev_mask == 0:
                        acc += f[prev_mask][prev]
            f[mask][cur] = acc
            total += acc
    return total


def passwords(w: int, h: int) -> int:
    return int(_count(w * h, _between_masks(w, h)))


if __name__ == "__main__":
    assert passwords(3, 3) == 389488  # given
    print(passwords(4, 4))  # 4350069824940
