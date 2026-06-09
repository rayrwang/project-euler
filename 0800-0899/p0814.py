import itertools

import numpy as np

MOD = 998244353


def scream_count(n: int) -> int:
    """S(n): ways exactly 2n of 4n circled people scream, mod MOD.

    Pair person i with the diametrically opposite person i + 2n, giving 2n
    "sites" of two people (top, bottom) arranged in a cycle; consecutive
    sites are joined top-top and bottom-bottom, and the wrap-around joins
    top to bottom (the two semicircles swap). Person i screams iff their
    gaze is reciprocated: an R-L match with a neighbour, or both members of
    a site choosing O.

    A 9-state transfer matrix over (top, bottom) choices, with x marking
    screamers (weight x^2 per R-L match on either rail and x^2 per O-O
    site), gives S(n) as the x^(2n) coefficient of the swap-twisted trace
    of M(x)^(2n). The trace is a polynomial of degree 4n, recovered by
    evaluating at the 2^k-th roots of unity of the NTT-friendly modulus and
    inverting the transform at the single needed coefficient.
    """
    states = list(itertools.product(range(3), repeat=2))  # 0=L, 1=R, 2=O
    k_states = 9
    size = 1
    while size < 4 * n + 1:
        size *= 2
    root = pow(3, (MOD - 1) // size, MOD)
    xs = np.empty(size, dtype=np.int64)
    xs[0] = 1
    for k in range(1, size):
        xs[k] = xs[k - 1] * root % MOD

    m = np.empty((size, k_states, k_states), dtype=np.int64)
    for i, (a, b) in enumerate(states):
        for j, (a2, b2) in enumerate(states):
            e = 2 * ((a == 1 and a2 == 0) + (b == 1 and b2 == 0)
                     + (a2 == 2 and b2 == 2))
            v = np.ones(size, dtype=np.int64)
            for _ in range(e):
                v = v * xs % MOD
            m[:, i, j] = v

    def batched_matmul(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        # 9 products of values < MOD stay within int64.
        return np.einsum("kij,kjl->kil", x, y) % MOD

    power = np.broadcast_to(np.eye(k_states, dtype=np.int64),
                            (size, k_states, k_states)).copy()
    base, e = m, 2 * n
    while e:
        if e & 1:
            power = batched_matmul(power, base)
        base = batched_matmul(base, base)
        e >>= 1

    swap = [states.index((b, a)) for (a, b) in states]
    trace = np.zeros(size, dtype=np.int64)
    for i in range(k_states):
        trace = (trace + power[:, i, swap[i]]) % MOD

    w = pow(pow(int(root), MOD - 2, MOD), 2 * n, MOD)
    acc, wk = 0, 1
    for k in range(size):
        acc = (acc + int(trace[k]) * wk) % MOD
        wk = wk * w % MOD
    return acc * pow(size, MOD - 2, MOD) % MOD


if __name__ == "__main__":
    assert scream_count(1) == 48
    assert scream_count(10) == 420121075
    print(scream_count(10**3))  # 307159326
