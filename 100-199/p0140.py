def solve(count: int = 30) -> int:
    # A_G(x) = sum G_k x^k = (x + 3x^2)/(1 - x - x^2) for the modified Fibonacci
    # sequence 1,4,5,9,...; A_G(x) = n is rational iff 5n^2 + 14n + 1 is a
    # perfect square. The golden nuggets satisfy n_k = 7 n_{k-2} - n_{k-4} + 7.
    n = [2, 5, 21, 42]
    while len(n) < count:
        k = len(n)
        n.append(7 * n[k - 2] - n[k - 4] + 7)
    return sum(n[:count])


if __name__ == "__main__":
    print(solve())  # 5673835352990
