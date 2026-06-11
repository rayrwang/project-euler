import math


def maze_count(m: int, n: int) -> tuple[float, int]:
    """(mantissa, exponent) of C(m, n), the number of m x n mazes.

    A maze with a unique path between every pair of cells is exactly a
    spanning tree of the grid graph P_m box P_n.  By the matrix-tree
    theorem the spanning-tree count is the product of the nonzero
    Laplacian eigenvalues divided by the vertex count m*n, and the grid's
    Laplacian eigenvalues are the pairwise sums of the path-graph
    eigenvalues 4 sin^2(k pi / 2L).  The product overflows float range
    (about 10^25093 here), so it is accumulated in log10 space.
    """
    lam = [4.0 * math.sin(i * math.pi / (2 * m)) ** 2 for i in range(m)]
    mu = [4.0 * math.sin(j * math.pi / (2 * n)) ** 2 for j in range(n)]
    log_total = -math.log10(m * n)
    for li in lam:
        for mj in mu:
            if li == 0.0 and mj == 0.0:
                continue  # skip the single zero eigenvalue
            log_total += math.log10(li + mj)
    exponent = math.floor(log_total)
    mantissa = 10.0 ** (log_total - exponent)
    if mantissa >= 10.0:  # guard rounding at the decade boundary
        mantissa /= 10.0
        exponent += 1
    return mantissa, exponent


def sci(m: int, n: int) -> str:
    mantissa, exponent = maze_count(m, n)
    return f"{mantissa:.4f}e{exponent}"


if __name__ == "__main__":
    assert sci(2, 2) == "4.0000e0"
    assert sci(3, 4) == "2.4150e3"
    assert sci(9, 12) == "2.5720e46"
    print(sci(100, 500))  # 6.3202e25093
