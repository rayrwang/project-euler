def matrix_sum(matrix: list[list[int]]) -> int:
    """Maximum sum choosing one entry per row, no two in the same column.

    Assignment problem solved by a bitmask DP over the set of used columns:
    after choosing entries for the first r rows, the chosen columns form a set
    with r bits, so dp[mask] is the best sum reaching that set and row
    r = popcount(mask) is processed next.
    """
    n = len(matrix)
    full = 1 << n
    dp = [-1] * full
    dp[0] = 0
    for mask in range(full):
        best = dp[mask]
        if best < 0:
            continue
        row = bin(mask).count("1")
        if row == n:
            continue
        row_vals = matrix[row]
        for col in range(n):
            bit = 1 << col
            if mask & bit:
                continue
            cand = best + row_vals[col]
            if cand > dp[mask | bit]:
                dp[mask | bit] = cand
    return dp[full - 1]


def solve(path: str) -> int:
    with open(path) as f:
        matrix = [[int(x) for x in line.split()] for line in f if line.strip()]
    return matrix_sum(matrix)


if __name__ == "__main__":
    example = [
        [7, 53, 183, 439, 863],
        [497, 383, 563, 79, 973],
        [287, 63, 343, 169, 583],
        [627, 343, 773, 959, 943],
        [767, 473, 103, 699, 303],
    ]
    assert matrix_sum(example) == 3315
    print(solve("assets/0345_matrix.txt"))  # 13938
