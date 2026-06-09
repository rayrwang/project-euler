import numba

@numba.jit(cache=True)
def expected_white(n: int, m: int) -> float:
    """E(N, M): expected white disks after M random range flips.

    Disk i is flipped in a turn unless both endpoints land on the same
    side of it, so q_i = 1 - ((i-1)^2 + (N-i)^2) / N^2. Flip counts are
    independent across turns, giving P(white) = (1 + r_i^M) / 2 with
    r_i = 1 - 2 q_i, hence E = N/2 + (1/2) sum_i r_i^M.

    r_i falls monotonically from ~1 at the edges towards ~-0 in the middle
    (symmetrically in i <-> N+1-i), so r_i^M is negligible except for the
    first ~N ln(eps) / (4M) indices at each end: truncate when
    r^M < 1e-18, leaving at most N * 1e-18 < 1e-7 of error.
    """
    half = float(n) / 2.0
    tail = 0.0
    thresh = 10.0 ** (-18.0 / m)
    i = 1
    while i <= (n + 1) // 2:
        r = 1.0 - 4.0 * i / n + (2.0 * i * i + 2.0 * (i - 1.0) * (i - 1.0)) / (
            float(n) * float(n))
        if abs(r) < thresh:
            break
        tail += r**m
        i += 1
    # the two ends are mirror images; for odd n the centre disk is not
    # doubled, but its term is far below the truncation threshold anyway
    return half + tail

def exact_small(n: int, m: int) -> float:
    total = 0.0
    for i in range(1, n + 1):
        q = 1.0 - ((i - 1) ** 2 + (n - i) ** 2) / n**2
        total += (1.0 + (1.0 - 2.0 * q) ** m) / 2.0
    return total

if __name__ == "__main__":
    assert abs(exact_small(3, 1) - 10 / 9) < 1e-12
    assert abs(exact_small(3, 2) - 5 / 3) < 1e-12
    assert abs(exact_small(10, 4) - 5.157) < 5e-4
    assert abs(exact_small(100, 10) - 51.893) < 5e-4
    # truncated evaluator agrees with the full sum where both are feasible
    assert abs(expected_white(10**6, 4000) - exact_small(10**6, 4000)) < 1e-6
    print(f"{expected_white(10**10, 4000):.2f}")  # 5000624921.38
