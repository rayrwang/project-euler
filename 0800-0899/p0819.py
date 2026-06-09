import numba


@numba.njit(cache=True)
def _expected_steps(n: int) -> float:
    """Expected resampling steps to consensus, via the coalescent dual.

    One forward step replaces the tuple by n independent uniform picks from
    its entries. Run the process backwards: each new entry "descends" from the
    position it copied, so b currently-distinct lineages map to the number of
    distinct parents they chose -- exactly the count of occupied boxes when b
    balls land uniformly in n boxes. Consensus forward = coalescence to a
    single lineage backward, and the two have the same step distribution, so
    E(n) is the expected number of backward steps from n lineages to 1.

    Let q[b][j] be the probability that b balls occupy exactly j of n boxes;
    it satisfies q[b+1][j] = q[b][j] * j/n + q[b][j-1] * (n-j+1)/n. With
    T[1] = 0 and, removing the self-loop of "no coalescence",
        T[b] = (1 + sum_{j<b} q[b][j] T[j]) / (1 - q[b][b]).
    """
    inv_n = 1.0 / n
    q = [[0.0] * (n + 2) for _ in range(n + 1)]
    q[1][1] = 1.0
    for b in range(1, n):
        for j in range(1, b + 1):
            v = q[b][j]
            if v != 0.0:
                q[b + 1][j] += v * (j * inv_n)
                q[b + 1][j + 1] += v * ((n - j) * inv_n)
    t = [0.0] * (n + 1)
    for b in range(2, n + 1):
        acc = 0.0
        for j in range(1, b):
            acc += q[b][j] * t[j]
        t[b] = (1.0 + acc) / (1.0 - q[b][b])
    return t[n]


if __name__ == "__main__":
    assert f"{_expected_steps(3):.6f}" == "3.857143"  # 27/7
    assert f"{_expected_steps(5):.6f}" == "7.711982"
    print(f"{_expected_steps(10**3):.6f}")  # 1995.975556
