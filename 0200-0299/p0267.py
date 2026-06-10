from decimal import Decimal, getcontext
from math import comb, log

# With a fixed fraction f bet on each of 1000 tosses, h heads give capital
# (1 + 2f)^h (1 - f)^(1000 - h), which is increasing in h, so success is a
# tail event {h >= h_min(f)} and the best f minimises h_min. For a given h
# the capital-maximising fraction solves 2h/(1 + 2f) = (1000 - h)/(1 - f),
# i.e. f = (3h - 1000)/2000 (Kelly). Scanning h for the smallest value whose
# optimal fraction reaches 10^9 gives h* = 432 (f = 0.148); the answer is
# the exact binomial tail P(X >= h*) = sum_(k >= h*) C(1000, k) / 2^1000,
# evaluated with big integers and rounded to 12 decimals.


def solve(tosses: int = 1000, goal: int = 10**9) -> str:
    target = log(goal)
    h_star = None
    for h in range(tosses // 3 + 1, tosses + 1):
        f = (3 * h - tosses) / (2 * tosses)
        if f <= 0 or f >= 1:
            continue
        if h * log(1 + 2 * f) + (tosses - h) * log(1 - f) >= target:
            h_star = h
            break
    assert h_star is not None
    numerator = sum(comb(tosses, k) for k in range(h_star, tosses + 1))
    getcontext().prec = 60
    p = Decimal(numerator) / Decimal(2**tosses)
    return f"{p:.12f}"


if __name__ == "__main__":
    print(solve())  # 0.999992836187
