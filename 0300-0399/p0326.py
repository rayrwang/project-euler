import numpy as np

MOD = 10**6


def _prefix_residues(period: int, m: int) -> np.ndarray:
    """Residues P_t mod m for t = 0 .. period-1, where P_t = sum_{i=1}^t a_i and a follows the
    closed form below (verified against the recurrence). With n = 6q + r,

        a_n = n/2            if r in {0, 2}
        a_n = 4q + 1         if r == 1
        a_n = q              if r in {3, 5}
        a_n = n - 1          if r == 4.
    """
    t = np.arange(period, dtype=np.int64)
    q, r = t // 6, t % 6
    a = np.empty(period, dtype=np.int64)
    a[r == 0] = t[r == 0] // 2
    a[r == 2] = t[r == 2] // 2
    a[r == 1] = 4 * q[r == 1] + 1
    a[r == 3] = q[r == 3]
    a[r == 5] = q[r == 5]
    a[r == 4] = t[r == 4] - 1
    a[0] = 0  # t = 0 contributes nothing; P_0 = 0
    return np.cumsum(a % m) % m


def solve(n: int = 10**12, m: int = MOD) -> int:
    """f(N, M): the number of pairs 1 <= p <= q <= N with (sum_{i=p}^q a_i) mod M = 0, where
    a_1 = 1 and a_n = (sum_{k=1}^{n-1} k*a_k) mod n.

    Writing P_t = sum_{i=1}^t a_i, a block sum (p..q) is divisible by M exactly when
    P_q == P_{q-1=p-1} mod M, so f(N, M) = sum_r C(c_r, 2) over the residue counts c_r among
    P_0, ..., P_N. The sequence a has a clean closed form periodic in n mod 6, which makes P_t
    mod M periodic with period 6M; counting residues over one period and scaling by the number
    of whole periods in [0, N] (plus the tail) gives the answer. The checks f(10, 10) = 4 and
    f(10^4, 10^3) = 97158 confirm the construction.
    """
    period = 6 * m
    residues = _prefix_residues(period, m)

    whole, tail = divmod(n + 1, period)  # n+1 indices t = 0 .. n
    counts = np.bincount(residues, minlength=m).astype(np.int64) * whole
    if tail:
        counts += np.bincount(residues[:tail], minlength=m).astype(np.int64)
    # C(c, 2) summed over residues; the total is ~10^18 and fits in int64.
    return int(np.sum(counts * (counts - 1) // 2))


if __name__ == "__main__":
    assert solve(10, 10) == 4
    assert solve(10**4, 10**3) == 97158
    print(solve())  # 1966666166408794329
