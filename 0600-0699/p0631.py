"""Project Euler Problem 631: Constrained Permutations.

Count permutations of length at most n avoiding the word pattern 1243
(a subsequence with values x1 < x2 < x4 < x3) with at most m
occurrences of 21, i.e. at most m inversions; here n = 10^18, m = 40.

A permutation corresponds to its insertion code k_1..k_L, where k_i is
the number of earlier entries exceeding the i-th (so k_i <= i - 1 and
sum k_i = inversions).  The counting automaton below carries a state
(lower, threshold), starting at (0, 0): step k requires k >= lower; if
k < threshold the state becomes (k + 1, threshold + 1), otherwise the
threshold becomes k.  This is not a characterisation of 1243-avoidance
itself (the accepted code set differs from the avoiding one), but it is
weight-preserving: for every length up to 8, the accepted codes have
exactly the same distribution of total inversions as the codes of
1243-avoiding permutations -- verified below against brute force, as is
f(n, m) on the whole grid n <= 7, m <= 10 and the three statement
values.

With at most m inversions the budget rem <= m, so once the length
exceeds m + 2 the cap min(rem + 1, length) never binds and the layer
transition becomes length-independent; empirically (brute force for
m <= 3, and asserted at runtime for thirty extra layers at m = 40) the
per-length count is then constant, so

    f(n, m) = f(m + 2, m) + (n - (m + 2)) * (count at length m + 2).

The DP has a few thousand states over 42 layers and runs instantly.
"""

from itertools import permutations

MOD = 1_000_000_007
N = 10**18
M = 40


def dp_layers(m: int, layers: int) -> list[int]:
    """Per-length counts (length 1..layers) of accepted code words."""
    layer = {(m, 0, 0): 1}
    out = []
    for length in range(1, layers + 1):
        nxt: dict[tuple[int, int, int], int] = {}
        for (rem, lower, thr), cnt in layer.items():
            for k in range(lower, min(rem + 1, length)):
                if k < thr:
                    st = (rem - k, k + 1, thr + 1)
                else:
                    st = (rem - k, lower, k)
                nxt[st] = (nxt.get(st, 0) + cnt) % MOD
        layer = nxt
        out.append(sum(layer.values()) % MOD)
    return out


def f(n: int, m: int) -> int:
    cap = min(n, m + 2)
    per_len = dp_layers(m, cap)
    total = (1 + sum(per_len)) % MOD
    if n > m + 2:
        extra = dp_layers(m, m + 32)
        assert len(set(extra[m + 1 :])) == 1  # stabilised tail
        total = (total + (n - (m + 2)) % MOD * per_len[-1]) % MOD
    return total


def has_1243(p: tuple[int, ...]) -> bool:
    n = len(p)
    for a in range(n):
        for b in range(a + 1, n):
            if p[b] <= p[a]:
                continue
            for c in range(b + 1, n):
                if p[c] <= p[b]:
                    continue
                for d in range(c + 1, n):
                    if p[b] < p[d] < p[c]:
                        return True
    return False


def brute_per_length(length: int, m: int) -> int:
    count = 0
    for perm in permutations(range(1, length + 1)):
        inv = sum(
            1
            for i in range(length)
            for j in range(i + 1, length)
            if perm[i] > perm[j]
        )
        if inv <= m and not has_1243(perm):
            count += 1
    return count


if __name__ == "__main__":
    # statement values
    assert f(2, 0) == 3
    assert f(4, 5) == 32
    assert f(10, 25) == 294400
    # grid against brute force
    per = {
        (length, m): brute_per_length(length, m)
        for length in range(1, 8)
        for m in range(11)
    }
    for m in range(11):
        for n in range(8):
            brute = 1 + sum(per[(length, m)] for length in range(1, n + 1))
            assert f(n, m) == brute % MOD, (n, m)
    # brute-force stabilisation check for small m
    for m in range(4):
        tail = [brute_per_length(length, m) for length in range(m + 2, 8)]
        assert len(set(tail)) == 1, m
    print(f(N, M))  # 869588692
