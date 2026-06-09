import numba
import numpy as np


def _lines(n: int) -> np.ndarray:
    # Affine image of the size-n cross-hatched triangle: 9n-3 lines a*x+b*y=c
    # in six direction families. Triangle counting is affine-invariant, so the
    # sheared right triangle {x>=0, y>=0, x+y<=n} gives the same counts.
    rows = []
    for k in range(n):
        rows.append((1, 0, k))           # x = k
        rows.append((0, 1, k))           # y = k
    for k in range(1, n + 1):
        rows.append((1, 1, k))           # x + y = k
    for c in range(-(n - 1), n):
        rows.append((1, -1, c))          # x - y = c
    for c in range(1, 2 * n):
        rows.append((2, 1, c))           # 2x + y = c
        rows.append((1, 2, c))           # x + 2y = c
    return np.array(rows, dtype=np.int64)


@numba.njit(cache=True)
def _count(line: np.ndarray, n: int) -> int:
    m = line.shape[0]
    total = 0
    for i in range(m):
        a1, b1, c1 = line[i, 0], line[i, 1], line[i, 2]
        for j in range(i + 1, m):
            a2, b2, c2 = line[j, 0], line[j, 1], line[j, 2]
            d12 = a1 * b2 - a2 * b1
            if d12 == 0:
                continue
            for k in range(j + 1, m):
                a3, b3, c3 = line[k, 0], line[k, 1], line[k, 2]
                d13 = a1 * b3 - a3 * b1
                if d13 == 0:
                    continue
                d23 = a2 * b3 - a3 * b2
                if d23 == 0:
                    continue
                # concurrent (or parallel, already excluded) iff this 3x3 det = 0
                det3 = (a1 * (b2 * c3 - b3 * c2) - b1 * (a2 * c3 - a3 * c2)
                        + c1 * (a2 * b3 - a3 * b2))
                if det3 == 0:
                    continue
                ok = True
                # each pairwise intersection must lie in {x>=0, y>=0, x+y<=n}
                for d, ax, bx, cx, ay, by, cy in (
                    (d12, a1, b1, c1, a2, b2, c2),
                    (d13, a1, b1, c1, a3, b3, c3),
                    (d23, a2, b2, c2, a3, b3, c3),
                ):
                    nx = cx * by - cy * bx          # x numerator
                    ny = ax * cy - ay * cx          # y numerator
                    if nx * d < 0 or ny * d < 0:
                        ok = False
                        break
                    if d > 0:
                        if nx + ny > n * d:
                            ok = False
                            break
                    elif nx + ny < n * d:
                        ok = False
                        break
                if ok:
                    total += 1
    return total


def solve(n: int = 36) -> int:
    return int(_count(_lines(n), n))


if __name__ == "__main__":
    print(solve())  # 343047
