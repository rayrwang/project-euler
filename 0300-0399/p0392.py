import numba
import numpy as np


@numba.jit(cache=True)
def red_area(free: np.ndarray, m: int) -> float:
    """4 * sum (t_{i+1} - t_i) t_{m+1-i} for the self-conjugate partition.

    t_1..t_q are the free variables (q = m // 2 (+1 if m odd, where the
    middle point is fixed at 1/sqrt(2))), and t_{m+1-i} = sqrt(1 - t_i^2).
    """
    t = np.empty(m + 2)
    t[0] = 0.0
    q = len(free)
    for i in range(q):
        t[1 + i] = free[i]
    if m % 2 == 1:
        t[q + 1] = np.sqrt(0.5)
    for i in range(1, q + 1):
        t[m + 1 - i] = np.sqrt(1.0 - t[i] * t[i])
    t[m + 1] = 1.0
    a = 0.0
    for i in range(m + 1):
        a += (t[i + 1] - t[i]) * t[m + 1 - i]
    return 4.0 * a


@numba.jit(cache=True)
def minimise(m: int) -> float:
    """Cyclic coordinate descent with golden-section line searches."""
    q = m // 2
    # Start from the arc-uniform partition t_i = sin(i pi / (2 m + 2)).
    free = np.sin(np.arange(1, q + 1) * np.pi / (2 * (m + 1)))
    gr = (np.sqrt(5.0) - 1.0) / 2.0
    best = red_area(free, m)
    while True:
        prev = best
        for i in range(q):
            lo = free[i - 1] if i > 0 else 0.0
            hi = free[i + 1] if i + 1 < q else (np.sqrt(0.5) if m % 2 else 1.0)
            a, b = lo + 1e-12, hi - 1e-12
            c = b - gr * (b - a)
            d = a + gr * (b - a)
            free[i] = c
            fc = red_area(free, m)
            free[i] = d
            fd = red_area(free, m)
            while b - a > 1e-13:
                if fc < fd:
                    b, d, fd = d, c, fc
                    c = b - gr * (b - a)
                    free[i] = c
                    fc = red_area(free, m)
                else:
                    a, c, fc = c, d, fd
                    d = a + gr * (b - a)
                    free[i] = d
                    fd = red_area(free, m)
            free[i] = (a + b) / 2
        best = red_area(free, m)
        if prev - best < 1e-15:
            return best


if __name__ == "__main__":
    assert f"{minimise(5):.10f}" == "3.3469640797"  # N = 10
    print(f"{minimise(200):.10f}")  # 3.1486734435
