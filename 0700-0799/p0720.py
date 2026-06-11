import numba
import numpy as np

# A permutation is unpredictable iff no value (x + y) / 2 sits positionally
# between two same-parity values x and y.  Splitting odds from evens kills
# every cross-parity progression (their average is not an integer), and a
# progression inside the odds (or evens) maps, via v -> (v + 1) // 2 (or
# v -> v // 2), to a progression of the half-size problem.  A depth-first
# search for the lexicographically first unpredictable permutation (run
# below for N = 8 and 16) reveals the exact greedy-optimal interleaving of
# the two half-size solutions F on odds and evens:
#     F(2h) = [odd F-block except its last entry, first even entry,
#              last odd entry, remaining even entries],
# with F(4) = (1, 3, 2, 4).  Sliding the first even entry (the value 2)
# ahead of the last odd entry is lexicographically cheaper and creates no
# progression: 2 can only be the middle of (x, 2, y) with x + y = 4, and 1
# precedes 3 only in the final odd slot, after 2; the structure is confirmed
# by the given S(4) = 3, S(8) = 2295 and S(32) = 641839205 mod p.
#
# The rank is 1 + sum L_i * (N - 1 - i)! where L_i counts later values
# smaller than P(i) (the Lehmer code), accumulated mod p with a Fenwick
# tree in O(N log N).

MOD = 1_000_000_007


def first_unpredictable_dfs(n):
    """Reference: lex-first unpredictable permutation by backtracking."""
    pos = {}
    perm = []

    def extendable(v):
        # appending v creates P(i), P(j), v iff P(i) = 2 P(j) - v with i < j
        for j, mid in enumerate(perm):
            x = 2 * mid - v
            if x in pos and pos[x] < j:
                return False
        return True

    def dfs():
        if len(perm) == n:
            return True
        for v in range(1, n + 1):
            if v not in pos and extendable(v):
                pos[v] = len(perm)
                perm.append(v)
                if dfs():
                    return True
                perm.pop()
                del pos[v]
        return False

    dfs()
    return perm


def build(n):
    """Lex-first unpredictable permutation of [1..n] for n a power of two."""
    f = np.array([1, 3, 2, 4], dtype=np.int64)
    while len(f) < n:
        h = len(f)
        odds = 2 * f - 1
        evens = 2 * f
        f = np.concatenate([odds[: h - 1], evens[:1], odds[h - 1 :], evens[1:]])
    return f


@numba.njit(cache=True)
def rank_mod(p):
    """1-indexed lexicographic rank of permutation p, modulo MOD."""
    n = len(p)
    bit = np.zeros(n + 1, dtype=np.int64)
    fact = np.zeros(n, dtype=np.int64)
    fact[0] = 1
    for i in range(1, n):
        fact[i] = fact[i - 1] * i % MOD
    r = 1
    for i in range(n - 1, -1, -1):
        v = p[i]
        s = 0
        x = v - 1
        while x > 0:
            s += bit[x]
            x -= x & (-x)
        r = (r + (s % MOD) * fact[n - 1 - i]) % MOD
        while v <= n:
            bit[v] += 1
            v += v & (-v)
    return r


if __name__ == "__main__":
    assert first_unpredictable_dfs(8) == list(build(8))
    assert first_unpredictable_dfs(16) == list(build(16))
    assert rank_mod(build(4)) == 3
    assert rank_mod(build(8)) == 2295
    assert rank_mod(build(32)) == 641839205

    print(rank_mod(build(1 << 25)))  # 688081048
