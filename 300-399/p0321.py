def solve(num_terms: int) -> int:
    """Sum of the first `num_terms` values of n for which M(n) is triangular.

    Reversing the counters takes M(n) = n^2 + 2n moves: the 2n counters must
    advance n+1 cells each (2n(n+1) cell-steps); hops cover two cells and
    slides one, and the n^2 red/blue meetings are exactly the hops, leaving
    2n slides, so M(n) = 2n(n+1) - n^2 = n^2 + 2n.

    Requiring M(n) = k(k+1)/2 gives, after completing the square,
        m^2 - 8 u^2 = -7,    with u = n + 1 and m = 2k + 1.
    This Pell-like equation has two solution classes, generated from the
    fundamentals (m, u) = (1, 1) and (5, 2) by the unit 3 + sqrt(8):
        (m, u) -> (3m + 8u, m + 3u).
    Merging the u-values (dropping u = 1, i.e. n = 0) in increasing order
    gives the n = u - 1 of the sequence.
    """
    def y_values(m: int, u: int, count: int) -> list[int]:
        out = []
        for _ in range(count):
            out.append(u)
            m, u = 3 * m + 8 * u, m + 3 * u
        return out

    need = num_terms + 2
    us = sorted(set(y_values(1, 1, need) + y_values(5, 2, need)))
    ns = [u - 1 for u in us if u > 1][:num_terms]
    return sum(ns)


if __name__ == "__main__":
    # The first five terms are 1, 3, 10, 22, 63 (sum 99).
    assert solve(5) == 99
    print(solve(40))  # 2470433131948040
