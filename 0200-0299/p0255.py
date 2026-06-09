import numba
import numpy as np

# Heron's rounded square root: from x_0 = 7 * 10^6 (14 digits is even),
# iterate x' = floor((x + ceil(n / x)) / 2) until x' = x, counting the
# updates. The count is piecewise constant in n: for fixed x, ceil(n / x) = q
# on n in ((q-1) x, q x], and then x' = (x + q) / 2 is the same for the whole
# subinterval. Recursively splitting [10^13, 10^14) this way visits only
# about 10^7 first-level intervals (each of width x_0) and a handful of
# descendants per interval, summing iteration counts exactly. Verified
# against direct per-n simulation over all 4-digit numbers.


@numba.njit(cache=True)
def _total_iters(lo0: int, hi0: int, x0: int) -> int:
    total = 0
    stack_lo = np.empty(512, dtype=np.int64)
    stack_hi = np.empty(512, dtype=np.int64)
    stack_x = np.empty(512, dtype=np.int64)
    stack_k = np.empty(512, dtype=np.int64)
    q_first = (lo0 + x0 - 1) // x0
    q_last = (hi0 + x0 - 1) // x0
    for q in range(q_first, q_last + 1):
        lo = max(lo0, (q - 1) * x0 + 1)
        hi = min(hi0, q * x0)
        x1 = (x0 + q) // 2
        if x1 == x0:
            total += hi - lo + 1
            continue
        stack_lo[0] = lo
        stack_hi[0] = hi
        stack_x[0] = x1
        stack_k[0] = 1
        top = 1
        while top > 0:
            top -= 1
            slo = stack_lo[top]
            shi = stack_hi[top]
            x = stack_x[top]
            k = stack_k[top]
            qa = (slo + x - 1) // x
            qb = (shi + x - 1) // x
            for qq in range(qa, qb + 1):
                l2 = max(slo, (qq - 1) * x + 1)
                h2 = min(shi, qq * x)
                x2 = (x + qq) // 2
                if x2 == x:
                    total += (h2 - l2 + 1) * (k + 1)
                else:
                    stack_lo[top] = l2
                    stack_hi[top] = h2
                    stack_x[top] = x2
                    stack_k[top] = k + 1
                    top += 1
    return total


def solve() -> str:
    lo, hi = 10**13, 10**14 - 1
    total = _total_iters(lo, hi, 7 * 10**6)
    return f"{total / (hi - lo + 1):.10f}"


if __name__ == "__main__":
    print(solve())  # 4.4474011180
