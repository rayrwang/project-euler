import numpy as np
from numba import njit


@njit
def _compute(n: int) -> int:
    """M(n) = sum over all 1 <= i <= j <= n of A(i, j), where A(i, j) is the
    minimum of S_i..S_j and S is the given quadratic PRNG.

    This is the sum of minimums over every subarray. Sweeping left to right, keep
    a value-increasing stack of (value, span) blocks and a running quantity `cur`
    equal to the sum of minimums of all subarrays ending at the current position.
    Adding a new term S pops every block whose value is >= S (those subarrays now
    have minimum S), merges their spans, and contributes S * (merged span) to
    `cur`; adding `cur` to the total each step accumulates the full sum. The PRNG
    values are well spread, so the stack stays tiny, and the whole pass is O(n).
    """
    cap = 1 << 12
    stack_val = np.empty(cap, dtype=np.int64)
    stack_cnt = np.empty(cap, dtype=np.int64)
    top = 0
    cur = 0  # sum of minimums of subarrays ending at the current position
    total = 0
    s = 290797
    for _ in range(n):
        s = (s * s) % 50515093
        cnt = 1
        while top > 0 and stack_val[top - 1] >= s:
            top -= 1
            cur -= stack_val[top] * stack_cnt[top]
            cnt += stack_cnt[top]
        if top >= cap:
            new_cap = cap * 2
            nv = np.empty(new_cap, dtype=np.int64)
            nc = np.empty(new_cap, dtype=np.int64)
            for x in range(top):
                nv[x] = stack_val[x]
                nc[x] = stack_cnt[x]
            stack_val, stack_cnt, cap = nv, nc, new_cap
        stack_val[top] = s
        stack_cnt[top] = cnt
        top += 1
        cur += s * cnt
        total += cur
    return total


def solve(n: int = 2_000_000_000) -> int:
    return _compute(n)


if __name__ == "__main__":
    # M(10) = 432256955 and M(10000) = 3264567774119.
    assert _compute(10) == 432256955
    assert _compute(10000) == 3264567774119
    print(solve())  # 7435327983715286168
