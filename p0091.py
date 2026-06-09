import numba
import numpy as np

@numba.jit(cache=True)
def count_right(xs, ys):
    m = len(xs)
    count = 0
    for i in range(m):
        px, py = xs[i], ys[i]
        for j in range(i + 1, m):
            qx, qy = xs[j], ys[j]
            if px * qy - py * qx == 0:        # O, P, Q collinear -> degenerate
                continue
            # A right angle at a vertex means its two edge vectors dot to zero.
            if px * qx + py * qy == 0:                                  # at O
                count += 1
            elif (-px) * (qx - px) + (-py) * (qy - py) == 0:            # at P
                count += 1
            elif (-qx) * (px - qx) + (-qy) * (py - qy) == 0:            # at Q
                count += 1
    return count

if __name__ == "__main__":
    n = 50
    xs, ys = [], []
    for x in range(n + 1):
        for y in range(n + 1):
            if x or y:                        # exclude the origin
                xs.append(x)
                ys.append(y)
    print(count_right(np.array(xs), np.array(ys)))  # 14234
