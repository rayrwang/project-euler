import numpy as np
from numba import njit


@njit(cache=True)
def _count(limit: int, roots: np.ndarray) -> int:
    # Same Barning-matrix forest as problem 223 (the matrices preserve
    # a^2 + b^2 - c^2 = -1 too); root (2, 2, 3), normalise to a <= b, and skip
    # the mirror child at symmetric nodes so each triangle appears once.
    stack = np.empty((256, 3), dtype=np.int64)
    top = 0
    for i in range(len(roots)):
        stack[top] = roots[i]
        top += 1
    cnt = 0
    while top > 0:
        top -= 1
        a, b, c = stack[top]
        if a > b:
            a, b = b, a
        if a + b + c > limit:
            continue
        cnt += 1
        stack[top, 0] = a - 2 * b + 2 * c
        stack[top, 1] = 2 * a - b + 2 * c
        stack[top, 2] = 2 * a - 2 * b + 3 * c
        top += 1
        stack[top, 0] = a + 2 * b + 2 * c
        stack[top, 1] = 2 * a + b + 2 * c
        stack[top, 2] = 2 * a + 2 * b + 3 * c
        top += 1
        if a != b:
            stack[top, 0] = -a + 2 * b + 2 * c
            stack[top, 1] = -2 * a + b + 2 * c
            stack[top, 2] = -2 * a + 2 * b + 3 * c
            top += 1
    return cnt


def solve(limit: int = 75_000_000) -> int:
    roots = np.array([[2, 2, 3]], dtype=np.int64)
    return _count(limit, roots)


if __name__ == "__main__":
    print(solve())  # 4137330
