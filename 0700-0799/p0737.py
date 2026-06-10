import numba
import numpy as np

@numba.njit(cache=True)
def coins(loops, nmax):
    """Number of coins needed to loop `loops` times around the line.

    Every coin touches the line, so in projection all centres lie on the
    unit circle. The stack that advances fastest places each new coin at
    distance exactly 1 from the centroid M of all coins already placed:
    with cos(beta) = |M|/2 the new centre is the unit vector M-hat
    rotated by -beta (the advancing branch). This tight construction
    reproduces all three given values (31 coins for one loop, 154 for
    two, 6947 for ten), which pins down the intended balance model.

    Implementation notes: no trigonometry is needed for the placement
    itself (pure vector rotation); one arctan2 per step measures the
    angular advance. The centroid sum and the cumulative angle are both
    Kahan-compensated since the run takes ~7.6e8 steps and the final
    per-step advance (~1.7e-5 rad) must stay well above the accumulated
    rounding error.
    """
    goal = 2.0 * np.pi * loops
    sx, sy = 1.0, 0.0
    kx, ky = 0.0, 0.0      # Kahan compensation for the centroid sum
    px, py = 1.0, 0.0      # previous coin direction
    drop = 0.0
    dk = 0.0               # Kahan compensation for the cumulative angle
    k = 1
    while k < nmax:
        mx = sx / k
        my = sy / k
        mn = np.sqrt(mx * mx + my * my)
        cb = mn / 2.0
        sb = np.sqrt(1.0 - cb * cb)
        ux = mx / mn
        uy = my / mn
        cx = ux * cb + uy * sb
        cy = uy * cb - ux * sb
        dot = cx * px + cy * py
        crs = px * cy - py * cx
        d = np.arctan2(-crs, dot)
        if d < 0.0:
            d += 2.0 * np.pi
        y = d - dk
        t = drop + y
        dk = (t - drop) - y
        drop = t
        if drop > goal:
            return k + 1
        y = cx - kx
        t = sx + y
        kx = (t - sx) - y
        sx = t
        y = cy - ky
        t = sy + y
        ky = (t - sy) - y
        sy = t
        px, py = cx, cy
        k += 1
    return -1

if __name__ == "__main__":
    assert coins(1, 100) == 31
    assert coins(2, 1000) == 154
    assert coins(10, 10**5) == 6947
    print(coins(2020, 10**9))  # 757794899
