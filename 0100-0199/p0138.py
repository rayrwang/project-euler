def solve(count: int = 12) -> int:
    # Base b, legs L, height h = b +/- 1. Then L^2 = (b/2)^2 + h^2 leads to
    # (5b +/- 4)^2 - 20 L^2 = -4, a Pell-type equation. The leg lengths satisfy
    # L_n = 18 L_{n-1} - L_{n-2} with L_0 = 1, L_1 = 17 (the b=16, L=17 triangle).
    prev, cur = 1, 17
    total = 0
    for _ in range(count):
        total += cur
        prev, cur = cur, 18 * cur - prev
    return total


if __name__ == "__main__":
    print(solve())  # 1118049290473932
