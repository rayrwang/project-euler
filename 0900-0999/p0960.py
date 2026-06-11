"""Project Euler 960: Stone Pile Game.

View each move as an edge between the two chosen piles. A successful play
makes n - 1 moves (n stones each, n(n-1) stones in total), and the edge
multiset must be a spanning tree: any connected component on k vertices
removes k(n-1) stones using n per edge, so n | k(n-1), forcing k = n.
Conversely, given a spanning tree the amounts are forced -- summing over
the subtree below an edge shows the lower endpoint v (with subtree size
k_v) removes n - k_v stones from its own pile while the parent pile loses
k_v -- and each pile's forced amounts add up to exactly its initial n - 1
stones, so the partial sums never overdraw a pile and every one of the
(n-1)! edge orders is feasible. The score of a play through tree T is
therefore order-independent:

    score(T) = sum over edges e of min(k_e, n - k_e),

with k_e the size of one side of the cut. Counting (tree, edge) pairs
whose cut has a side of size k gives C(n,k) k^(k-1) (n-k)^(n-k-1)
(choose the side, a tree on each part, and the connecting edge), each
(tree, edge) being counted for both sides, so

    F(n) = (n-1)!/2 * sum_{k=1}^{n-1} min(k, n-k) C(n,k) k^(k-1) (n-k)^(n-k-1).

A direct DFS over all sequences of turns confirms F(3) = 12 and
F(4) = 360, and the formula reproduces the given F(8) = 16785941760.
"""

from math import comb, factorial

MOD = 10**9 + 7


def f_formula(n: int) -> int:
    s = sum(
        min(k, n - k) * comb(n, k) * k ** (k - 1) * (n - k) ** (n - k - 1)
        for k in range(1, n)
    )
    return factorial(n - 1) * s // 2


def f_brute(n: int) -> int:
    """Sum of final scores over all successful sequences of turns."""
    total = 0

    def dfs(state: tuple, score: int) -> None:
        nonlocal total
        if not any(state):
            total += score
            return
        for i in range(n):
            for j in range(i + 1, n):
                lo = max(0, n - state[j])
                hi = min(n, state[i])
                for a in range(lo, hi + 1):
                    s2 = list(state)
                    s2[i] -= a
                    s2[j] -= n - a
                    dfs(tuple(s2), score + min(a, n - a))

    dfs(tuple([n - 1] * n), 0)
    return total


def solve() -> int:
    assert f_formula(3) == f_brute(3) == 12
    assert f_formula(4) == f_brute(4) == 360
    assert f_formula(8) == 16785941760
    return f_formula(100) % MOD


if __name__ == "__main__":
    print(solve())  # 243559751
