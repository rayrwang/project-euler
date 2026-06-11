MOD = 7**9


def _geometric_sum(ratio: int, n: int, mod: int) -> int:
    """sum_{k=0}^n ratio^k mod `mod`, valid when ratio-1 is invertible mod `mod`."""
    return (pow(ratio, n + 1, mod) - 1) * pow(ratio - 1, -1, mod) % mod


def solve(top: int = 10**18, mod: int = MOD) -> int:
    """sum_{k=0}^{top} M(2^k + 1) mod 7^9, where M(x) is the number of moves in Peter's bean game.

    With x bowls each holding one bean, a move empties a bowl and drops its beans one at a time
    clockwise, continuing from where the last bean landed, until the all-ones state recurs.
    Simulation gives M(5) = 15 and M(100) = 10920, and for x = 2^k + 1 the move count has the
    closed form

        M(2^k + 1) = 4^k - 3^k + 2^(k+1),

    found by separating the total bean travel 2^k(2^k + 2) from the moves and identifying the
    remainder's (2,3,4)-geometric structure. The requested sum is then three geometric series
    evaluated modulo 7^9 (each ratio minus one is a unit mod 7^9)."""
    s4 = _geometric_sum(4, top, mod)
    s3 = _geometric_sum(3, top, mod)
    s2 = 2 * (pow(2, top + 1, mod) - 1) % mod  # sum_{k=0}^{top} 2^(k+1)
    return (s4 - s3 + s2) % mod


if __name__ == "__main__":
    # M(2^k + 1) = 4^k - 3^k + 2^(k+1): k=2 gives M(5)=15, k=4 gives M(17)=207.
    assert 4**2 - 3**2 + 2**3 == 15
    print(solve())  # 5032316
