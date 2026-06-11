"""Project Euler problem 524: First Sort II.

First Sort repeatedly moves the smaller element of the first out-of-order
adjacent pair to the front of the list; F(L) counts the moves.  Q(n, k) is
the smallest lexicographic index (1-based, within S_n) of a permutation P
of {1..n} with F(P) = k, and R(k) = min over n of Q(n, k).
Find R(12^12).

Peeling the minimum of the list gives the recursion F = 2 F(sigma_2) + d,
where sigma_2 is the pattern of elements >= 2 and d = 0 if 1 is first,
else 1 - F(B) with B the pattern before 1 (once 1 reaches the front,
every later move drops an element in front of it and triggers one more
move of 1).  Unrolling the recursion when one element is appended to a
prefix telescopes to a closed form:

    F(P) = sum over positions p where P[p] is NOT a left-to-right maximum
           of 2^(number of smaller elements before p).

Stripping the maximal identity prefix of any permutation leaves a pattern
tau with tau_1 != min whose index equals the whole permutation's index
while F is multiplied by a power of two.  Hence R(k) is the minimum over
j of the index of the lexicographically smallest tau in S_{s_j} with
F(tau) = k / 2^j, where s_j is the smallest size with 2^(s_j - 1) - 1 >=
k / 2^j; families whose minimal size exceeds the smallest one are
dominated, because an index in S_{s+1} of a permutation not starting
with 1 is at least s! + 1, larger than any index in S_s, and ones
starting with 1 reduce to another family.

The lexicographically smallest tau with F = V is built greedily by
position.  Placing value v contributes 0 if v exceeds everything before
it, else 2^(#smaller before).  A completion of remaining sorted values
r_1 < ... < r_t after a prefix with maximum M exists iff the residual can
be written as a sum in which each r_i contributes either 0 (it becomes a
left-to-right maximum: requires r_i > M, members of the zero set are
mutually increasing with all larger elements after them, and the largest
remaining value above M is forced into the zero set) or 2^e with
e in [r_i - i + z_i, r_i - 1], where z_i counts zero-set elements below
r_i (which are forced before r_i, while the rest of the exponent range is
freely realizable).  That representability test is a small memoized
recursion over values.

For k = 12^12 = 2^24 * 3^12 the only family at the minimal size 21 is
V = 3^12, so the answer is the index of the greedy solution in S_21.

Everything is verified: the closed form against direct simulation of the
sorting algorithm for all permutations with n <= 8 (including the given
F(4132) = 5), the greedy constructor against brute-force lexicographic
minima for all m <= 7 and every achievable V, and the family pipeline for
R(k) against a brute-force scan of all permutations of all n <= 8 for
every k <= 127.
"""

import sys
from functools import lru_cache
from itertools import permutations
from math import factorial

sys.setrecursionlimit(100000)


def f_simulate(perm: tuple[int, ...]) -> int:
    """F by running First Sort directly."""
    lst = list(perm)
    moves = 0
    while True:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst.insert(0, lst.pop(i + 1))
                moves += 1
                break
        else:
            return moves


def f_closed(perm: tuple[int, ...]) -> int:
    """F by the closed form over non left-to-right maxima."""
    total = 0
    mx = 0
    for p, v in enumerate(perm):
        if v > mx:
            mx = v
        else:
            total += 1 << sum(1 for u in perm[:p] if u < v)
    return total


def feasible(rem: tuple[int, ...], m_pref: int, target: int) -> bool:
    """Can sorted remaining values `rem` be arranged after a prefix with
    maximum m_pref so that their total F contribution equals target?"""
    t = len(rem)
    sufmax = [0] * (t + 1)
    for i in range(t - 1, -1, -1):
        sufmax[i] = sufmax[i + 1] + (1 << (rem[i] - 1))

    @lru_cache(maxsize=None)
    def go(i: int, zcnt: int, w: int) -> bool:
        if w < 0:
            return False
        if i == t:
            return w == 0
        if w > sufmax[i]:
            return False
        r = rem[i]
        if i == t - 1 and r > m_pref:
            # the largest remaining value above the prefix maximum has no
            # larger element available before it: forced left-to-right max
            return go(i + 1, zcnt + 1, w)
        lo = r - (i + 1) + zcnt
        e = lo
        while e <= r - 1 and (1 << e) <= w:
            if go(i + 1, zcnt, w - (1 << e)):
                return True
            e += 1
        return r > m_pref and go(i + 1, zcnt + 1, w)

    res = go(0, 0, target)
    go.cache_clear()
    return res


def lexmin(m: int, v_target: int) -> tuple[int, ...] | None:
    """Lexicographically smallest permutation of {1..m} with F = v_target."""
    rem = list(range(1, m + 1))
    prefix: list[int] = []
    mx = 0
    left = v_target
    for _ in range(m):
        for v in rem:
            contrib = 0 if v > mx else 1 << sum(1 for u in prefix if u < v)
            if contrib > left:
                continue
            r2 = tuple(x for x in rem if x != v)
            if feasible(r2, max(mx, v), left - contrib):
                prefix.append(v)
                rem.remove(v)
                left -= contrib
                mx = max(mx, v)
                break
        else:
            return None
    return tuple(prefix)


def lex_index(perm: tuple[int, ...]) -> int:
    n = len(perm)
    rem = sorted(perm)
    idx = 1
    for i, v in enumerate(perm):
        r = rem.index(v)
        idx += r * factorial(n - 1 - i)
        rem.pop(r)
    return idx


def min_size(v: int) -> int:
    s = 1
    while 2 ** (s - 1) - 1 < v:
        s += 1
    return s


def r_pipeline(k: int) -> int:
    """R(k) = min over halving families of the minimal-size lex minimum."""
    best = None
    w = k
    while True:
        tau = lexmin(min_size(w), w)
        assert tau is not None
        idx = lex_index(tau)
        if best is None or idx < best:
            best = idx
        if w % 2 or w == 0:
            break
        w //= 2
    return best


def main() -> None:
    assert f_simulate((4, 1, 3, 2)) == 5
    for n in range(1, 9):
        for p in permutations(range(1, n + 1)):
            assert f_simulate(p) == f_closed(p)
    for m in range(1, 8):
        for v in range(2 ** (m - 1)):
            bb = next(
                (
                    p
                    for p in permutations(range(1, m + 1))
                    if f_closed(p) == v
                ),
                None,
            )
            assert bb == lexmin(m, v), (m, v)
    # brute-force R(k) over all permutations of all n <= 8
    brute: dict[int, int] = {}
    for n in range(1, 9):
        for idx, p in enumerate(permutations(range(1, n + 1)), start=1):
            kk = f_closed(p)
            if kk not in brute or idx < brute[kk]:
                brute[kk] = idx
    for k in range(128):
        assert r_pipeline(k) == brute[k], k
    # k = 12^12 = 2^24 * 3^12: the only family at the minimal size 21 is
    # V = 3^12 (2 * 3^12 already exceeds 2^20 - 1), and the dominance
    # argument reduces R to that single family.
    tau = lexmin(21, 3**12)
    assert tau is not None and f_closed(tau) == 3**12
    print(lex_index(tau))  # 2432925835413407847


if __name__ == "__main__":
    main()
