import numba
import numpy as np

MOD = 10**9 + 7

@numba.njit(cache=True)
def f(n):
    """Repeatedly discard the first term and take partial sums until a single
    value remains, starting from the Lucas sequence 1, 3, 4, 7, ...

    The final value is linear in the start: f(n) = sum_i a_i w_i(n), and
    propagating unit vectors shows the weights are the ballot numbers
        w_1 = 0,   w_i = (i - 1) / (2n - 1 - i) * C(2n - 1 - i, n - 1),
    verified directly for n <= 20 (for the all-ones start this sums to the
    Catalan number C_(n-1), e.g. f(8) = 429). Iterate i downward from
    w_n = 1 with the ratio
        w_i = w_(i+1) * (i - 1)(2n - 2 - i) / (i (n - i)),
    whose denominators stay <= n, so one modular-inverse table of size n
    suffices. The Lucas values run backwards via a_(i-1) = a_(i+1) - a_i
    after one forward pass for a_(n-1), a_n.
    """
    inv = np.empty(n + 1, dtype=np.int64)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD

    # Forward pass for the last two Lucas values mod MOD.
    prev, cur = 1, 3  # a_1, a_2
    for _ in range(n - 2):
        prev, cur = cur, (prev + cur) % MOD
    # Now prev = a_(n-1), cur = a_n.

    w = 1  # w_n
    total = cur * w % MOD  # i = n term
    for i in range(n - 1, 1, -1):
        # w_i from w_(i+1)
        w = w * (i - 1) % MOD * ((2 * n - 2 - i) % MOD) % MOD
        w = w * inv[i] % MOD * inv[n - i] % MOD
        prev, cur = (cur - prev) % MOD, prev  # step Lucas down to a_i
        total = (total + cur * w) % MOD
    return total

if __name__ == "__main__":
    assert f(8) == 2663
    assert f(20) == 742296999
    print(f(10**8))  # 711399016
