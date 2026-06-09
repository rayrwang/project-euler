import numpy as np


def solve(n: int) -> int:
    """Number of simultaneous moves of n^2 ants on an n x n grid.

    Every ant steps to an adjacent square, destinations are distinct, and
    no edge is used by two ants. Distinct destinations make the move a
    permutation in which every square maps to a neighbour; the shared-edge
    rule forbids exactly the 2-cycles (two ants swapping across one edge).
    So f(n) counts directed cycle covers of the grid graph in which each
    undirected edge carries at most one ant.

    Count with a broken-profile DP over cells in row-major order. The
    frontier holds one ternary digit per column for the vertical edge
    hanging below the processed part (0 unused, 1 pointing down, 2 up)
    plus one digit for the horizontal edge left of the next cell. At each
    cell the incoming up/left states combine with chosen down/right states
    so that exactly one edge enters and one leaves the cell; boundary
    edges are forced unused. The DP array is indexed by the n + 1 ternary
    digits as an (n+1)-dimensional array of Python integers, so each
    transition is one slice addition and the counts are exact.
    """
    horizontal = n  # axis index of the horizontal carry edge
    dp = np.zeros((3,) * (n + 1), dtype=object)
    dp[(0,) * (n + 1)] = 1
    for r in range(n):
        for c in range(n):
            new = np.zeros_like(dp)
            for up in range(3) if r > 0 else (0,):
                for left in range(3) if c > 0 else (0,):
                    for down in range(3) if r < n - 1 else (0,):
                        for right in range(3) if c < n - 1 else (0,):
                            ins = (
                                (up == 1) + (left == 1)
                                + (down == 2) + (right == 2)
                            )
                            outs = (
                                (up == 2) + (left == 2)
                                + (down == 1) + (right == 1)
                            )
                            if ins != 1 or outs != 1:
                                continue
                            src: list[slice | int] = [slice(None)] * (n + 1)
                            dst: list[slice | int] = [slice(None)] * (n + 1)
                            src[c], src[horizontal] = up, left
                            dst[c], dst[horizontal] = down, right
                            new[tuple(dst)] += dp[tuple(src)]
            dp = new
    return int(dp[(0,) * (n + 1)])


if __name__ == "__main__":
    assert solve(2) == 2  # the single 4-cycle, two orientations
    assert solve(3) == 0  # odd bipartite classes admit no cycle cover
    assert solve(4) == 88
    print(solve(10))  # 112398351350823112
