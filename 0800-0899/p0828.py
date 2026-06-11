"""Project Euler 828: Numbers Challenge.

Each challenge is a countdown puzzle: combine some of six given
numbers with +, -, *, / so that every intermediate value is a positive
integer and the result equals the target; the score is the sum of the
numbers used and s_n is the minimum score (0 if unsolvable).

A subset dynamic program solves each puzzle exactly: reach[mask] is
the set of values obtainable using ALL numbers indexed by mask, built
by splitting mask into the submask containing its lowest bit and the
complement (so each unordered split is combined once) and applying the
six directed operations u+v, u*v, u-v, v-u (when positive) and u/v,
v/u (when exact).  Duplicated input numbers are distinct items, so
multiset semantics come for free.  The minimum score is then the
smallest sum of nums over masks whose reachable set contains the
target -- including singletons, since using one number alone is a
legitimate solution.

The reachable sets stay small (a few thousand values), so all 200
puzzles finish in about two seconds; s_1 = 40 confirms the worked
example, and the weighted total sum 3^n s_n is reduced modulo
1005075251.
"""

from __future__ import annotations

from pathlib import Path

MOD = 1005075251
DATA = Path(__file__).resolve().parent.parent / "assets" / "0828_number_challenges.txt"


def min_score(target: int, nums: list[int]) -> int:
    n = len(nums)
    full = 1 << n
    reach: list[set[int] | None] = [None] * full
    for i in range(n):
        reach[1 << i] = {nums[i]}
    best = 0
    for mask in range(1, full):
        if reach[mask] is None:
            cur: set[int] = set()
            low = mask & -mask
            sub = (mask - 1) & mask
            while sub:
                if sub & low:
                    other = mask ^ sub
                    a_set, b_set = reach[sub], reach[other]
                    assert a_set is not None and b_set is not None
                    for u in a_set:
                        for v in b_set:
                            cur.add(u + v)
                            cur.add(u * v)
                            if u > v:
                                cur.add(u - v)
                            elif v > u:
                                cur.add(v - u)
                            if u % v == 0:
                                cur.add(u // v)
                            if v % u == 0:
                                cur.add(v // u)
                sub = (sub - 1) & mask
            reach[mask] = cur
        cur_set = reach[mask]
        assert cur_set is not None
        if target in cur_set:
            sc = sum(nums[i] for i in range(n) if mask >> i & 1)
            if best == 0 or sc < best:
                best = sc
    return best


def main() -> None:
    total = 0
    first = None
    with open(DATA) as f:
        for idx, line in enumerate(f.read().split(), 1):
            tgt, rest = line.split(":")
            score = min_score(int(tgt), [int(x) for x in rest.split(",")])
            if idx == 1:
                first = score
            total = (total + pow(3, idx, MOD) * score) % MOD
    assert first == 40
    print(total)  # 148693670


if __name__ == "__main__":
    main()
