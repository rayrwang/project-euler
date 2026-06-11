"""Problem 416: A Frog's Trip.

Reversing each homeward trip turns m round trips into 2m independent
left-to-right paths jumping 1-3, all starting on square 1 and landing
exactly on square n; F(m, n) counts 2m-tuples of such paths whose
landings cover every square except at most one. Paths are processed
square by square: the state is the multiset (n0, n1, n2) of paths
that are on the current square / overflying one / overflying two more,
plus a flag for the one allowed missed square (n0 = 0). Each step the
n0 grounded paths redistribute by a trinomial into the three skip
classes. With 2m = 20 paths that is C(22, 2) * 2 = 462 states, and
F(m, n) is a single entry of the step matrix to the power n - 1.
"""

import numba
import numpy as np

MOD = 10**9

def build_states(paths: int):
    states = []
    index = {}
    for n0 in range(paths + 1):
        for n1 in range(paths + 1 - n0):
            n2 = paths - n0 - n1
            for miss in range(2):
                index[(n0, n1, n2, miss)] = len(states)
                states.append((n0, n1, n2, miss))
    return states, index

def build_matrix(paths: int) -> np.ndarray:
    """One step: visit current square (n0 = 0 consumes the miss budget),
    then ground paths choose jumps 1/2/3 and everyone advances."""
    from math import comb
    states, index = build_states(paths)
    k = len(states)
    mat = np.zeros((k, k), dtype=np.int64)
    for si, (n0, n1, n2, miss) in enumerate(states):
        if n0 == 0:
            if miss == 1:
                continue  # second miss: dead
            new_miss = 1
        else:
            new_miss = miss
        for a in range(n0 + 1):
            for b in range(n0 + 1 - a):
                c = n0 - a - b
                w = comb(n0, a) * comb(n0 - a, b) % MOD
                tj = index[(a + n1, b + n2, c, new_miss)]
                mat[si, tj] = (mat[si, tj] + w) % MOD
    return mat

@numba.jit(cache=True)
def mat_mul(a: np.ndarray, b: np.ndarray, mod: int) -> np.ndarray:
    k = a.shape[0]
    out = np.zeros((k, k), dtype=np.int64)
    for i in range(k):
        for kk in range(k):
            v = a[i, kk]
            if v == 0:
                continue
            for j in range(k):
                out[i, j] = (out[i, j] + v * b[kk, j]) % mod
    return out

def frog_ways(m: int, n: int) -> int:
    paths = 2 * m
    _, index = build_states(paths)
    mat = build_matrix(paths)
    start = index[(paths, 0, 0, 0)]
    # after n - 1 steps every path must be grounded on square n
    targets = [index[(paths, 0, 0, 0)], index[(paths, 0, 0, 1)]]
    k = mat.shape[0]
    vec = np.zeros(k, dtype=np.int64)
    vec[start] = 1
    e = n - 1
    while e:
        if e & 1:
            nv = np.zeros(k, dtype=np.int64)
            for i in range(k):
                if vec[i]:
                    nv = (nv + vec[i] * mat[i]) % MOD
            vec = nv
        mat = mat_mul(mat, mat, MOD)
        e >>= 1
    return int(sum(vec[t] for t in targets) % MOD)

def brute(m: int, n: int) -> int:
    """Direct enumeration over tuples of paths (tiny cases)."""
    from itertools import product
    paths = []
    def gen(pos, hist):
        if pos == n - 1:
            paths.append(frozenset(hist))
            return
        for j in (1, 2, 3):
            if pos + j <= n - 1:
                gen(pos + j, hist + [pos + j])
    gen(0, [0])
    count = 0
    for combo in product(paths, repeat=2 * m):
        visited = frozenset().union(*combo)
        if len(visited) >= n - 1:
            count += 1
    return count

if __name__ == "__main__":
    assert frog_ways(1, 3) == brute(1, 3) == 4  # given
    assert frog_ways(1, 4) == brute(1, 4) == 15  # given
    assert frog_ways(1, 5) == brute(1, 5) == 46  # given
    assert frog_ways(2, 3) == brute(2, 3) == 16  # given
    assert frog_ways(2, 6) == brute(2, 6)
    assert frog_ways(2, 100) == 429619151  # given
    print(frog_ways(10, 10**12))  # 898082747
