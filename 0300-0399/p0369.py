from collections import defaultdict
from math import comb


def f_values() -> list[int]:
    """f(n) for every hand size n = 0..52, where f(n) is the number of n-card
    hands (from a standard 52-card deck) that contain a 4-card Badugi -- four
    cards of distinct ranks and distinct suits.

    A hand contains a Badugi exactly when the bipartite graph between the four
    suits and the thirteen ranks (an edge for each card held) has a matching of
    size 4, i.e. the four suits can be assigned four distinct ranks. So f(n) =
    C(52, n) minus the hands whose maximum such matching is at most 3.

    Count the no-Badugi hands by processing the 13 ranks one at a time. For each
    rank we choose which of the 4 suits are present (a 4-bit mask, contributing
    that many cards), and a rank can be matched to at most one suit. The DP state
    is the set of suit-subsets reachable as a matching ("reach", a 16-bit mask
    over the 16 suit-subsets); a hand has a Badugi iff the full suit-set {all 4}
    becomes reachable. Tracking the card count alongside gives f(n) for every n.
    """
    dp: dict[int, list[int]] = defaultdict(lambda: [0] * 53)
    dp[1 << 0][0] = 1  # only the empty matching is reachable initially
    for _ in range(13):  # each of the 13 ranks
        ndp: dict[int, list[int]] = defaultdict(lambda: [0] * 53)
        for reach, arr in dp.items():
            for mask in range(16):  # which suits are present at this rank
                k = bin(mask).count("1")  # cards added by this rank
                add = 0
                for matched in range(16):
                    if (reach >> matched) & 1:
                        for s in range(4):
                            if (mask >> s) & 1 and not (matched >> s) & 1:
                                add |= 1 << (matched | (1 << s))
                new_reach = reach | add
                target = ndp[new_reach]
                for c in range(53 - k):
                    if arr[c]:
                        target[c + k] += arr[c]
        dp = ndp

    no_badugi = [0] * 53
    for reach, arr in dp.items():
        if not (reach >> 15) & 1:  # full suit-set never reachable -> no Badugi
            for c in range(53):
                no_badugi[c] += arr[c]

    return [comb(52, n) - no_badugi[n] for n in range(53)]


if __name__ == "__main__":
    f = f_values()
    # f(5) = 514800 (given): of the 2598960 five-card hands, that many hold a Badugi.
    assert f[5] == 514800
    print(sum(f[n] for n in range(4, 14)))  # 862400558448
