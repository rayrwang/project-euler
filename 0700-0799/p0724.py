import numba

@numba.njit(cache=True)
def harmonic_sums(n):
    """Kahan-compensated H_n = sum 1/k and H2_n = sum 1/k^2, summed from the
    small terms up for accuracy."""
    h = 0.0
    ch = 0.0
    h2 = 0.0
    ch2 = 0.0
    for k in range(n, 0, -1):
        x = 1.0 / k
        y = x - ch
        t = h + y
        ch = (t - h) - y
        h = t
        x2 = x * x
        y2 = x2 - ch2
        t2 = h2 + y2
        ch2 = (t2 - h2) - y2
        h2 = t2
    return h, h2

def E(n):
    """Expected landing distance per package.

    Every second a uniformly random drone gets +1 speed; the flight ends one
    second after the last drone receives its first instruction, i.e. at time
    T + 1 where T is the coupon collector time for n coupons. An instruction
    issued at time t adds 1 cm/s for the remaining T + 1 - t seconds, so the
    total distance of all packages telescopes to sum_(t=1)^(T) (T + 1 - t) =
    T(T + 1)/2, and E(n) = E[T^2 + T] / (2n).

    With T a sum of independent geometrics of success (n-i)/n,
    E[T] = n H_n and Var T = n^2 H_n^(2) - n H_n, which collapses to
        E(n) = n (H_n^2 + H_n^(2)) / 2.
    This reproduces E(2) = 7/2 and E(5) = 12019/720 exactly (also confirmed
    by an exact Markov-chain computation and simulation for n = 4).
    """
    h, h2 = harmonic_sums(n)
    return n * (h * h + h2) / 2

if __name__ == "__main__":
    assert abs(E(2) - 3.5) < 1e-12
    assert abs(E(5) - 12019 / 720) < 1e-12
    assert abs(E(100) - 1427.193470) < 1e-6  # the given value is truncated
    print(round(E(10**8)))  # 18128250110
