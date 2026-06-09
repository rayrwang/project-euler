import math

from numba import njit


@njit(cache=True)
def _blancmange(x: float) -> float:
    # T(x) = sum_{n>=0} s(2^n x) / 2^n, with s(v) the distance to the nearest integer.
    total = 0.0
    weight = 1.0
    for _ in range(60):
        v = x - math.floor(x)
        d = v if v < 0.5 else 1.0 - v
        total += d * weight
        if weight < 1e-17:
            break
        x *= 2.0
        weight *= 0.5
    return total


@njit(cache=True)
def _integrate(n: int) -> float:
    # Area inside circle C (centre (1/4, 1/2), radius 1/4) and under the curve.
    # Per column the chord [ylow, yhigh] contributes min(T(x), yhigh) - ylow.
    r, cx, cy = 0.25, 0.25, 0.5
    h = 0.5 / n
    area = 0.0
    for i in range(n):
        x = (i + 0.5) * h
        disc = r * r - (x - cx) ** 2
        if disc <= 0:
            continue
        sq = math.sqrt(disc)
        ylow, yhigh = cy - sq, cy + sq
        t = _blancmange(x)
        top = t if t < yhigh else yhigh
        if top > ylow:
            area += top - ylow
    return area * h


def solve() -> float:
    return round(_integrate(1 << 22), 8)


if __name__ == "__main__":
    print(solve())  # 0.11316017
