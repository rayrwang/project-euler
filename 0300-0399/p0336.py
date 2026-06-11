from itertools import permutations


def _simon_rotations(perm: tuple[int, ...], n: int) -> int:
    """Number of turntable rotations Simple Simon uses on `perm`.

    A rotation reverses a suffix of the train. Simon fixes carriage 0, then 1, and so on:
    to seat carriage i (with 0..i-1 already correct) found at index j, he reverses the
    suffix from j to send it to the end, then reverses the suffix from i to drop it into
    place -- two rotations, or one when it is already at the very end, or none when it is
    already seated. The worst case over all arrangements ("maximix") is 2n-3 rotations."""
    a = list(perm)
    moves = 0
    limit = 2 * n - 3
    for i in range(n - 1):
        if a[i] == i:
            continue
        j = a.index(i)
        if j == n - 1:
            a[i:] = a[i:][::-1]
            moves += 1
        else:
            a[j:] = a[j:][::-1]
            a[i:] = a[i:][::-1]
            moves += 2
        if moves > limit:
            return moves
    return moves


def solve(n: int = 11, rank: int = 2011) -> str:
    """The `rank`-th lexicographic maximix arrangement of n carriages.

    permutations() yields arrangements in lexicographic order, so counting those needing the
    maximal 2n-3 rotations until the target rank gives the answer directly. Verified by the
    given facts that six carriages have 24 maximix arrangements with DFAECB tenth."""
    target = 2 * n - 3
    seen = 0
    for perm in permutations(range(n)):
        if _simon_rotations(perm, n) == target:
            seen += 1
            if seen == rank:
                return "".join(chr(ord("A") + x) for x in perm)
    raise AssertionError("rank exceeds the number of maximix arrangements")


if __name__ == "__main__":
    # Six carriages: 24 maximix arrangements, the tenth lexicographically is DFAECB.
    assert solve(6, 10) == "DFAECB"
    print(solve())  # CAGBIHEFJDK
