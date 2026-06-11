from math import comb

import numba
import numpy as np


@numba.jit(cache=True)
def step(old: np.ndarray, new: np.ndarray) -> None:
    """One more distinct pip level: add (i, j, k) faces of it to (A, B, C).

    State: dp[a][b][c][w1][w2][w3] = number of partial patterns with a, b, c
    faces placed so far and win counts w1 = W(B>A), w2 = W(C>B), w3 = W(A>C).
    Faces at the new level beat exactly the faces already placed (ties at
    the same level count for nobody), so the win counts shift uniformly by
    (j a, k b, i c) for the whole (w1, w2, w3) block.
    """
    new[:] = 0
    for a in range(7):
        for b in range(7):
            for c in range(7):
                block = old[a, b, c]
                for i in range(7 - a):
                    for j in range(7 - b):
                        for k in range(7 - c):
                            if i == 0 and j == 0 and k == 0:
                                continue
                            tgt = new[a + i, b + j, c + k]
                            for w1 in range(a * b + 1):
                                for w2 in range(b * c + 1):
                                    for w3 in range(c * a + 1):
                                        v = block[w1, w2, w3]
                                        if v:
                                            tgt[w1 + j * a, w2 + k * b, w3 + i * c] += v


def pattern_counts() -> list[int]:
    """Accepted cyclic patterns per number of distinct pip levels m."""
    dp = np.zeros((7, 7, 7, 37, 37, 37), dtype=np.int64)
    nxt = np.empty_like(dp)
    dp[0, 0, 0, 0, 0, 0] = 1
    counts = []
    for _ in range(18):
        step(dp, nxt)
        dp, nxt = nxt, dp
        counts.append(int(dp[6, 6, 6, 19:, 19:, 19:].sum()))
    return counts


def count_sets(n: int, counts: list[int]) -> int:
    """Unordered nontransitive sets of three 6-sided dice with pips 1..n.

    A nontransitive set is exactly a directed 3-cycle in the (antisymmetric)
    beats relation, giving 3 ordered triples per set.  Win probabilities
    depend only on the interleaving pattern of the 18 faces across distinct
    pip levels, so count patterns by number of levels m and weight by
    binom(n, m) ways to choose the actual pip values.
    """
    ordered = sum(comb(n, m) * c for m, c in enumerate(counts, start=1))
    assert ordered % 3 == 0
    return ordered // 3


if __name__ == "__main__":
    counts = pattern_counts()
    assert count_sets(7, counts) == 9780
    print(count_sets(30, counts))  # 973059630185670
