def solve() -> int:
    # tau permutes the 64 inputs; the constraint f(x) AND f(tau(x)) = 0 means each
    # cycle is an independent-set problem on a ring, whose count is a Lucas number.
    def tau(x: int) -> int:
        a1, a2, a3, a4, a5, a6 = ((x >> i) & 1 for i in range(6))
        bits = (a2, a3, a4, a5, a6, a1 ^ (a2 & a3))
        return sum(bit << i for i, bit in enumerate(bits))

    def lucas(n: int) -> int:
        a, b = 2, 1  # L0, L1
        for _ in range(n):
            a, b = b, a + b
        return a

    seen = [False] * 64
    result = 1
    for start in range(64):
        if not seen[start]:
            length, x = 0, start
            while not seen[x]:
                seen[x] = True
                x = tau(x)
                length += 1
            result *= lucas(length)
    return result


if __name__ == "__main__":
    print(solve())  # 15964587728784
