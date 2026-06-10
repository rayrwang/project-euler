"""Project Euler 912: Where are the Odds?

s_n is the n-th positive integer without '111' in binary, and s_n is odd
exactly when its last bit is 1.  Listing the valid numbers in increasing
order means lengths L = 1, 2, ... and, within a length, lexicographic
order of the bits after the leading 1.  A walk of that implicit trie
(automaton state = number of trailing ones, 0..2) visits the numbers in
rank order, so F(N) only needs, for every whole subtree passed over,
the aggregates over its completions of length r from state st (with
0-based lexicographic positions):

    T  = count,   O = #completions whose final bit is 1,
    S1 = sum of positions of those odd completions,   S2 = sum of pos^2.

A subtree entered when `base` numbers have already been consumed holds
items with global indices base + 1 + pos, contributing
(base+1)^2 O + 2(base+1) S1 + S2 to F.  The recurrences split on the
next bit (0 keeps the subtree first, 1 -- allowed while st < 2 --
offsets positions by the left count).  Counts T are kept exact for the
descent (N = 10^16 needs lengths up to ~63); all aggregates are mod
10^9 + 7.  Verified against brute force up to N = 50000 and the given
F(10) = 199.
"""

P = 10**9 + 7


def _build(rmax: int):
    cnt = [[0] * 3 for _ in range(rmax + 1)]
    odd = [[0] * 3 for _ in range(rmax + 1)]
    s1 = [[0] * 3 for _ in range(rmax + 1)]
    s2 = [[0] * 3 for _ in range(rmax + 1)]
    for st in range(3):
        cnt[1][st] = 1 + (st < 2)
        odd[1][st] = s1[1][st] = s2[1][st] = 1 if st < 2 else 0
    for r in range(2, rmax + 1):
        for st in range(3):
            t = cnt[r - 1][0]
            o = odd[r - 1][0]
            a = s1[r - 1][0]
            b = s2[r - 1][0]
            if st < 2:
                tl = t % P
                t += cnt[r - 1][st + 1]
                o = (o + odd[r - 1][st + 1]) % P
                a = (a + s1[r - 1][st + 1] + tl * odd[r - 1][st + 1]) % P
                b = (b + s2[r - 1][st + 1] + 2 * tl * s1[r - 1][st + 1]
                     + tl * tl % P * odd[r - 1][st + 1]) % P
            cnt[r][st] = t
            odd[r][st] = o % P
            s1[r][st] = a
            s2[r][st] = b
    return cnt, odd, s1, s2


def _block(base: int, o: int, a: int, b: int) -> int:
    b1 = (base + 1) % P
    return (b1 * b1 % P * o + 2 * b1 * a + b) % P


def solve(n: int) -> int:
    rmax = 130
    cnt, odd, s1, s2 = _build(rmax)
    total = 1 if n >= 1 else 0  # the number "1": rank 1, odd
    base = min(n, 1)
    length = 2
    while base + cnt[length - 1][1] <= n:
        r = length - 1
        total = (total + _block(base, odd[r][1], s1[r][1], s2[r][1])) % P
        base += cnt[r][1]
        length += 1
    m = n - base
    st, r = 1, length - 1
    while m > 0:
        if r == 1:
            base += 1  # the "0" leaf, even
            m -= 1
            if m > 0:  # the "1" leaf, odd (st < 2 guaranteed since it counts)
                base += 1
                total = (total + base * base) % P
                m -= 1
            break
        tl = cnt[r - 1][0]
        if m >= tl:
            total = (total + _block(base, odd[r - 1][0], s1[r - 1][0],
                                    s2[r - 1][0])) % P
            base += tl
            m -= tl
            st, r = st + 1, r - 1
        else:
            st, r = 0, r - 1
    return total % P


def brute(n: int) -> int:
    res = rank = v = 0
    while rank < n:
        v += 1
        if "111" not in bin(v):
            rank += 1
            if v % 2 == 1:
                res += rank * rank
    return res % P


if __name__ == "__main__":
    assert solve(10) == 199
    for n in (1, 2, 5, 7, 33, 100, 1234, 50000):
        assert solve(n) == brute(n), n
    print(solve(10**16))  # 674045136
