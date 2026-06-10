from functools import cache

import numpy as np

MOD = 989898989


def f_count(n: int) -> int:
    """Number of fair arrangements of n two-coin stacks, mod MOD.

    Gary removes gold coins (with anything above), Sally silver, so each
    stack is a partisan game.  All four stack types are surreal numbers:
    a lone gold coin is {0 | } = 1, hence (bottom, top) values
        GG = {1, 0 | } = 2,   GS = {0 | 1} = 1/2,
    and their mirror images SS = -2, SG = -1/2.  A sum of numbers is zero
    -- i.e. a loss for whichever player starts -- exactly when the values
    add to zero, so an arrangement is fair iff 4 #GG + #GS = 4 #SS + #SG.
    Giving a stack of value v the weight x^(4 + 2v),
        F(n) = [x^(4n)] (x^8 + x^5 + x^3 + 1)^n,
    extracted by multiplying the sparse quartic in n vectorised passes.
    """
    coef = np.zeros(8 * n + 1, dtype=np.int64)
    coef[0] = 1
    for _ in range(n):
        nxt = coef.copy()
        nxt[3:] += coef[:-3]
        nxt[5:] += coef[:-5]
        nxt[8:] += coef[:-8]
        coef = nxt % MOD
    return int(coef[4 * n])


@cache
def _wins(stacks: tuple[str, ...], gold_to_move: bool) -> bool:
    """Brute-force the actual game: does the player to move win?"""
    target = "G" if gold_to_move else "S"
    for i, st in enumerate(stacks):
        for j, coin in enumerate(st):
            if coin == target:
                rest = stacks[:i] + (st[:j],) + stacks[i + 1 :]
                rest = tuple(s for s in rest if s)
                if not _wins(tuple(sorted(rest)), not gold_to_move):
                    return True
    return False


def _f_brute(n: int) -> int:
    from itertools import product

    count = 0
    for arr in product(("GG", "GS", "SG", "SS"), repeat=n):
        key = tuple(sorted(arr))
        if not _wins(key, True) and not _wins(key, False):
            count += 1
    return count


if __name__ == "__main__":
    for n in range(1, 6):
        assert f_count(n) == _f_brute(n), n
    assert f_count(2) == 4  # given
    assert f_count(10) == 63594  # given
    print(f_count(9898))  # 958666903
