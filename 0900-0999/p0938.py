"""Project Euler 938: Exhausting a Colour.

Two cards are drawn without replacement from R red and B black: both red
are discarded (R -> R - 2), both black are returned (no change), mixed
returns the red and discards the black (B -> B - 1).  Conditioning away
the no-op draw, the embedded jump chain moves

    R -> R - 2  with probability (R - 1) / (R - 1 + 2B),
    B -> B - 1  with probability     2B / (R - 1 + 2B),

since both-red and mixed draws have unnormalised weights R(R-1) and 2RB.
With absorption P(0, B) = 1 and P(R, 0) = 0, the answer satisfies

    P(R, B) = (R-1)/(R-1+2B) * P(R-2, B) + 2B/(R-1+2B) * P(R, B-1).

(R only ever decreases by 2, so red's parity is invariant; with R even
the chain can genuinely reach R = 0.)  A two-line DP over B with a
rolling array over even R costs O(R B / 2) ~ 1.5e8 float operations --
convex combinations, so float64 easily holds 10 decimal digits.

Checks: P(2,2) = 7/15 = 0.4666666667, P(10,9) = 0.4118903397,
P(34,25) = 0.3665688069.  Runs in about a second.
"""

import numpy as np
from numba import njit


@njit(cache=True)
def p_black(r_total: int, b_total: int) -> float:
    nr = r_total // 2 + 1
    cur = np.zeros(nr)
    for b in range(1, b_total + 1):
        new = np.empty(nr)
        new[0] = 1.0
        for i in range(1, nr):
            r = 2 * i
            pr = (r - 1.0) / (r - 1.0 + 2.0 * b)
            new[i] = pr * new[i - 1] + (1.0 - pr) * cur[i]
        cur = new
    return cur[nr - 1]


def solve() -> str:
    assert "%0.10f" % p_black(2, 2) == "0.4666666667"
    assert "%0.10f" % p_black(10, 9) == "0.4118903397"
    assert "%0.10f" % p_black(34, 25) == "0.3665688069"
    return "%0.10f" % p_black(24690, 12345)


if __name__ == "__main__":
    print(solve())  # 0.2928967987
