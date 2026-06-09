import numba
import numpy as np

@numba.jit(cache=True)
def solve():
    """Least n with p(n) divisible by 10^6, via Euler's pentagonal recurrence mod 10^6."""
    mod = 1_000_000
    cap = 100_000
    p = np.zeros(cap, dtype=np.int64)
    p[0] = 1
    for n in range(1, cap):
        total = 0
        k = 1
        while True:
            g = k * (3 * k - 1) // 2          # generalized pentagonal numbers
            if g > n:
                break
            sign = 1 if k % 2 == 1 else -1
            total += sign * p[n - g]
            g2 = k * (3 * k + 1) // 2
            if g2 <= n:
                total += sign * p[n - g2]
            k += 1
        p[n] = total % mod
        if p[n] == 0:
            return n
    return -1

if __name__ == "__main__":
    print(solve())  # 55374
