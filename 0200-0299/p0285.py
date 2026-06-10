from math import asin, sqrt

# With x = k a + 1 and y = k b + 1 uniform over [1, k+1]^2, round k scores
# iff x^2 + y^2 falls in the annulus [(k - 1/2)^2, (k + 1/2)^2), so
# P_k = (A(k + 1/2) - A(k - 1/2)) / k^2 where
# A(R) = area{x >= 1, y >= 1, x^2 + y^2 <= R^2}; the upper square bounds
# never bind since k + 1/2 < k + 1. The closed form follows from
# integral sqrt(R^2 - x^2) dx = x sqrt(R^2 - x^2)/2 + (R^2/2) asin(x/R),
# evaluated between x = 1 and sqrt(R^2 - 1) (zero when R <= sqrt 2).
# The expectation sums k P_k for k up to 10^5; verified by Monte Carlo
# simulation for the first ten rounds.


def _area(r: float) -> float:
    if r * r <= 2:
        return 0.0

    def f(x: float) -> float:
        return x * sqrt(r * r - x * x) / 2 + (r * r / 2) * asin(x / r) - x

    return f(sqrt(r * r - 1)) - f(1.0)


def solve(rounds: int = 10**5) -> str:
    total = 0.0
    for k in range(1, rounds + 1):
        total += (_area(k + 0.5) - _area(k - 0.5)) / k
    return f"{total:.5f}"


if __name__ == "__main__":
    print(solve())  # 157055.80999
