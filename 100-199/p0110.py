def solve(target: int = 4_000_000) -> int:
    # #solutions of 1/x + 1/y = 1/n equals (d(n^2)+1)/2.
    # For n = prod p_i^a_i, d(n^2) = prod (2 a_i + 1). Need (d(n^2)+1)/2 > target.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    best = [1 << 70]

    def dfs(i: int, max_exp: int, n: int, divprod: int) -> None:
        if (divprod + 1) // 2 > target:
            if n < best[0]:
                best[0] = n
            return
        if i >= len(primes) or n >= best[0]:
            return
        p = primes[i]
        pe = 1
        for a in range(1, max_exp + 1):
            pe *= p
            if n * pe >= best[0]:
                break
            dfs(i + 1, a, n * pe, divprod * (2 * a + 1))

    dfs(0, 40, 1, 1)
    return best[0]


if __name__ == "__main__":
    print(solve())  # 9350130049860600
