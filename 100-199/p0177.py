import math

import numba
import numpy as np


@numba.njit(cache=True)
def _labeled_solutions(tol: float) -> np.ndarray:
    # Diagonals meet at P, giving four triangles. With phi = angle APB, the eight
    # corner angles satisfy a1+a2 = c1+c2 = 180-phi and b1+b2 = d1+d2 = phi, plus
    # the law-of-sines closure (sin a2/sin a1)(sin b2/sin b1)(sin c2/sin c1)
    # (sin d2/sin d1) = 1. Iterate a1,a2,b1,c1 and solve the closure for d1.
    out = np.zeros((2_000_000, 8), dtype=np.int16)
    cnt = 0
    deg = math.pi / 180.0
    for a1 in range(1, 179):
        sa1 = math.sin(a1 * deg)
        for a2 in range(1, 180 - a1):
            phi = 180 - a1 - a2
            sa2 = math.sin(a2 * deg)
            cphi = math.cos(phi * deg)
            sphi = math.sin(phi * deg)
            ratio_a = sa2 / sa1
            for b1 in range(1, phi):
                b2 = phi - b1
                ratio_b = math.sin(b2 * deg) / math.sin(b1 * deg)
                for c1 in range(1, 180 - phi):
                    c2 = 180 - phi - c1
                    if c2 < 1:
                        continue
                    k = ratio_a * ratio_b * math.sin(c2 * deg) / math.sin(c1 * deg)
                    d1 = math.atan2(sphi, cphi + 1.0 / k) / deg
                    rd = round(d1)
                    if 1 <= rd <= phi - 1 and abs(d1 - rd) < tol:
                        out[cnt, 0] = a1
                        out[cnt, 1] = a2
                        out[cnt, 2] = b1
                        out[cnt, 3] = b2
                        out[cnt, 4] = c1
                        out[cnt, 5] = c2
                        out[cnt, 6] = rd
                        out[cnt, 7] = phi - rd
                        cnt += 1
    return out[:cnt]


def _canonical(row: tuple[int, ...]) -> tuple[int, ...]:
    a1, a2, b1, b2, c1, c2, d1, d2 = row
    seq = (d2, a1, a2, b1, b2, c1, c2, d1)  # angles in perimeter order
    candidates = [s[sh:] + s[:sh] for s in (seq, seq[::-1]) for sh in (0, 2, 4, 6)]
    return min(candidates)


def solve(tol: float = 1e-9) -> int:
    # Count non-similar integer-angled quadrilaterals: canonicalise each labeled
    # solution under the dihedral relabelling group and count distinct classes.
    sols = _labeled_solutions(tol)
    seen = {_canonical(tuple(int(x) for x in row)) for row in sols}
    return len(seen)


if __name__ == "__main__":
    print(solve())  # 129325
