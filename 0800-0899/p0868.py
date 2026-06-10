def sjt_rank_rec(perm: list[int]) -> int:
    """Rank of a permutation of 1..k in Steinhaus-Johnson-Trotter order.

    The bell-ringers' procedure (always swap the largest letter that can
    move into a fresh permutation, preferring the largest of all) is
    exactly the SJT enumeration: consecutive blocks of k permutations
    share the relative order of 1..k-1 while the letter k sweeps across
    all k positions, leftwards when the sub-permutation's rank r is even
    and rightwards when it is odd.  Hence with p the position of k,
        rank = r * k + (k - 1 - p  if r even else  p).
    """
    k = len(perm)
    if k == 1:
        return 0
    p = perm.index(k)
    sub = [x for x in perm if x != k]
    r = sjt_rank_rec(sub)
    d = (k - 1 - p) if r % 2 == 0 else p
    return r * k + d


def _simulate(n: int) -> list[tuple[int, ...]]:
    """Brute-force the verbal procedure to validate the SJT claim."""
    cur = list(range(1, n + 1))
    seen = {tuple(cur)}
    order = [tuple(cur)]
    while True:
        moved = False
        for big in range(n, 0, -1):
            i = cur.index(big)
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    cur[i], cur[j] = cur[j], cur[i]
                    t = tuple(cur)
                    if t not in seen:
                        seen.add(t)
                        order.append(t)
                        moved = True
                        break
                    cur[i], cur[j] = cur[j], cur[i]
            if moved:
                break
        if not moved:
            return order


def word_rank(word: str) -> int:
    alpha = sorted(word)
    return sjt_rank_rec([alpha.index(c) + 1 for c in word])


if __name__ == "__main__":
    for n in range(2, 7):
        order = _simulate(n)
        assert len(order) == len(set(order))
        for idx, t in enumerate(order):
            assert sjt_rank_rec(list(t)) == idx, (n, t)
    assert word_rank("CBA") == 3
    assert word_rank("BELFRY") == 59
    print(word_rank("NOWPICKBELFRYMATHS"))  # 3832914911887589
