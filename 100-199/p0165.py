import numba
import numpy as np


def _segments(count: int = 5000) -> np.ndarray:
    nums = np.empty(4 * count, dtype=np.int64)
    s = 290797
    for i in range(4 * count):
        s = s * s % 50515093
        nums[i] = s % 500
    return nums.reshape(count, 4)


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _collect(seg: np.ndarray, xn: np.ndarray, yn: np.ndarray, dn: np.ndarray) -> int:
    n = seg.shape[0]
    idx = 0
    for i in range(n):
        x1, y1, x2, y2 = seg[i, 0], seg[i, 1], seg[i, 2], seg[i, 3]
        dx1, dy1 = x2 - x1, y2 - y1
        for j in range(i + 1, n):
            x3, y3, x4, y4 = seg[j, 0], seg[j, 1], seg[j, 2], seg[j, 3]
            dx2, dy2 = x4 - x3, y4 - y3
            den = dx1 * dy2 - dy1 * dx2
            if den == 0:
                continue
            nt = (x3 - x1) * dy2 - (y3 - y1) * dx2
            nu = (x3 - x1) * dy1 - (y3 - y1) * dx1
            if den < 0:
                den = -den
                nt = -nt
                nu = -nu
            # strict interior of both segments (excludes endpoints)
            if nt <= 0 or nt >= den or nu <= 0 or nu >= den:
                continue
            px = x1 * den + nt * dx1
            py = y1 * den + nt * dy1
            g = _gcd(_gcd(abs(px), abs(py)), den)
            xn[idx] = px // g
            yn[idx] = py // g
            dn[idx] = den // g
            idx += 1
    return idx


def solve(count: int = 5000) -> int:
    seg = _segments(count)
    cap = count * (count - 1) // 2
    xn = np.empty(cap, dtype=np.int64)
    yn = np.empty(cap, dtype=np.int64)
    dn = np.empty(cap, dtype=np.int64)
    k = _collect(seg, xn, yn, dn)
    points = set(zip(xn[:k].tolist(), yn[:k].tolist(), dn[:k].tolist()))
    return len(points)


if __name__ == "__main__":
    print(solve())  # 2868868
