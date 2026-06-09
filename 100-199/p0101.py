from fractions import Fraction

def u(n):
    # 1 - n + n^2 - n^3 + ... + n^10
    return sum((-1) ** i * n ** i for i in range(11))

def predict_next(xs, ys, target):
    """Value at `target` of the polynomial through points (xs, ys), by Lagrange."""
    total = Fraction(0)
    k = len(xs)
    for i in range(k):
        term = Fraction(ys[i])
        for j in range(k):
            if j != i:
                term *= Fraction(target - xs[j], xs[i] - xs[j])
        total += term
    return total

def solve():
    degree = 10
    xs = list(range(1, degree + 2))
    ys = [u(n) for n in xs]
    # Fitting only the first k terms gives a degree k-1 polynomial that matches
    # u at x = 1..k, so its first wrong prediction is at x = k+1. Sum those.
    return sum(int(predict_next(xs[:k], ys[:k], k + 1)) for k in range(1, degree + 1))

if __name__ == "__main__":
    print(solve())  # 37076114526
