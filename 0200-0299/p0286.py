# The score is a Poisson binomial over 50 independent shots with success
# probabilities p_x = 1 - x/q; P(exactly 20) is computed by the standard
# 50 x 21 DP. As q increases past 50 the hit probabilities all rise and the
# 20-point probability falls monotonically through 0.02 (0.041 at q = 50+,
# 0.0022 at q = 60), so a bisection pins the unique root to ten decimals.


def _p20(q: float) -> float:
    dp = [0.0] * 21
    dp[0] = 1.0
    for x in range(1, 51):
        p = 1.0 - x / q
        for k in range(20, 0, -1):
            dp[k] = dp[k] * (1 - p) + dp[k - 1] * p
        dp[0] *= 1 - p
    return dp[20]


def solve(target: float = 0.02) -> str:
    lo, hi = 50.0001, 70.0
    f_lo = _p20(lo) - target
    for _ in range(100):
        mid = (lo + hi) / 2
        if (_p20(mid) - target) * f_lo > 0:
            lo = mid
            f_lo = _p20(lo) - target
        else:
            hi = mid
    return f"{(lo + hi) / 2:.10f}"


if __name__ == "__main__":
    print(solve())  # 52.6494571953
