import numpy as np
from numba import njit


@njit(cache=True)
def _count(limit: int, roots: np.ndarray) -> int:
    # The Barning matrices preserve a^2 + b^2 - c^2, so they map barely acute
    # triples to barely acute triples. Normalising every node to a <= b and
    # dropping the third (mirror) child at symmetric nodes (a == b) makes the
    # forest from the given roots hit each triangle exactly once (verified
    # against brute force up to perimeter 20000).
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


def solve(limit: int = 25_000_000) -> int:
    roots = np.array([[1, 1, 1], [1, 2, 2]], dtype=np.int64)
    return _count(limit, roots)


if __name__ == "__main__":
    print(solve())  # 61614848
