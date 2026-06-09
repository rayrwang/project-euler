from math import isqrt


def solve(k: int = 15) -> int:
    # A_F(x) = sum F_i x^i = x/(1-x-x^2). Setting it equal to n gives
    # n x^2 + (n+1) x - n = 0, rational iff 5n^2+2n+1 is a perfect square.
    # The nth golden nugget is F_{2k} * F_{2k+1}.
    f = [0, 1, 1]
    while len(f) <= 2 * k + 1:
        f.append(f[-1] + f[-2])
    n = f[2 * k] * f[2 * k + 1]
    assert isqrt(5 * n * n + 2 * n + 1) ** 2 == 5 * n * n + 2 * n + 1
    return n


if __name__ == "__main__":
    print(solve())  # 1120149658760
