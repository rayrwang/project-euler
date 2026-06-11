import numpy as np
from numba import njit

BUFFER = 8  # only the last few totals are ever referenced; this is comfortably enough


@njit(cache=False)
def _expected(n: int) -> float:
    """E(n): the optimal expected number of black sheep.

    State (w, b) = (white, black). A uniformly random sheep bleats, then a sheep of the
    opposite colour crosses, so white->black grows black and vice versa; afterwards Peredur may
    remove white sheep. The classic Mabinogion result is that the optimal move is to cut the
    white flock down to one fewer than the black flock, keeping black a strict majority, so the
    value depends only on the canonical state with w <= b-1 (and w = 0, all black, is terminal
    with value b).

    Both bleats preserve the total w + b, except when a white bleat pushes the white flock to
    parity and triggers a removal, which drops the total by one or two. Hence, processing totals
    in increasing order, the same-total transitions form a tridiagonal system in w (solved by the
    Thomas algorithm) whose only outside references are to already-finished smaller totals -- so a
    short rolling buffer of recent totals suffices and the whole computation is O(n^2) time, O(n)
    memory. Crucially the very first move allows no removal: E(n) is one forced bleat from (n, n)
    into the optimal value function.
    """
    big_n = 2 * n
    width = n + 2
    buf = np.zeros((BUFFER, width))
    sub = np.zeros(width)
    sup = np.zeros(width)
    rhs = np.zeros(width)
    cp = np.zeros(width)
    dp = np.zeros(width)

    def value(w: int, b: int) -> float:
        if b == 0:
            return 0.0
        if w == 0:
            return float(b)
        if w <= b - 1:
            return buf[(w + b) % BUFFER][w]
        if b - 1 == 0:  # removing white leaves an all-black flock
            return float(b)
        return buf[(2 * b - 1) % BUFFER][b - 1]

    for total in range(1, big_n + 1):
        w_max = (total - 1) // 2  # canonical states need w < b = total - w
        slot = total % BUFFER
        for i in range(w_max + 2):
            buf[slot][i] = 0.0
        if w_max >= 1:
            for w in range(1, w_max + 1):
                b = total - w
                sub[w] = 0.0
                sup[w] = 0.0
                rhs[w] = 0.0
                # white bleat -> (w+1, b-1): same total unless it forces a removal
                if w + 1 <= b - 2:
                    sup[w] = -(w / total)
                else:
                    rhs[w] += (w / total) * value(w + 1, b - 1)
                # black bleat -> (w-1, b+1): same total, or terminal when w-1 = 0
                if w - 1 >= 1:
                    sub[w] = -(b / total)
                else:
                    rhs[w] += (b / total) * value(w - 1, b + 1)
            # Thomas algorithm (unit diagonal)
            cp[1] = sup[1]
            dp[1] = rhs[1]
            for w in range(2, w_max + 1):
                m = 1.0 - sub[w] * cp[w - 1]
                cp[w] = sup[w] / m
                dp[w] = (rhs[w] - sub[w] * dp[w - 1]) / m
            buf[slot][w_max] = dp[w_max]
            for w in range(w_max - 1, 0, -1):
                buf[slot][w] = dp[w] - cp[w] * buf[slot][w + 1]

    total = 2 * n
    return (n / total) * value(n + 1, n - 1) + (n / total) * value(n - 1, n + 1)


def solve(n: int = 10000) -> float:
    return _expected(n)


if __name__ == "__main__":
    assert abs(_expected(5) - 6.871346) < 5e-7
    print(f"{solve():.6f}")  # 19823.542204
