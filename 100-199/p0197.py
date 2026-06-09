from math import floor


def solve(iterations: int = 1000) -> float:
    # u_{n+1} = f(u_n) with f(x) = floor(2^(30.403243784 - x^2)) * 1e-9 settles
    # into a 2-cycle, so u_n + u_{n+1} stabilises; report it to 9 decimals.
    def f(x: float) -> float:
        return floor(2 ** (30.403243784 - x * x)) * 1e-9

    u = -1.0
    for _ in range(iterations):
        u = f(u)
    return round(u + f(u), 9)


if __name__ == "__main__":
    print(solve())  # 1.710637717
