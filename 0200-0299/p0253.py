from decimal import Decimal, getcontext
from math import factorial

# Each placement either creates a segment (no placed neighbour), extends one
# (one neighbour) or merges two (both neighbours). The number of placement
# orders realising a given operation word factorises step by step: with s
# segments present, a create can happen in s + 1 ways, an extend in 2s ways
# and a merge in s - 1 ways. (Verified exactly: these products reproduce the
# per-word permutation counts for all words at n = 4..7 by exhaustive
# enumeration.) A DP over (segments, max so far) with those multipliers
# therefore counts all 40! orders by their maximum segment count, giving the
# expected maximum exactly.


def solve(n: int = 40) -> str:
    f: dict[tuple[int, int], int] = {(0, 0): 1}
    for _ in range(n):
        nf: dict[tuple[int, int], int] = {}
        for (s, m), c in f.items():
            key = (s + 1, max(m, s + 1))  # create
            nf[key] = nf.get(key, 0) + c * (s + 1)
            if s >= 1:  # extend
                key = (s, m)
                nf[key] = nf.get(key, 0) + c * 2 * s
            if s >= 2:  # merge
                key = (s - 1, m)
                nf[key] = nf.get(key, 0) + c * (s - 1)
        f = nf
    num = sum(m * c for (s, m), c in f.items() if s == 1)
    den = sum(c for (s, m), c in f.items() if s == 1)
    assert den == factorial(n)
    getcontext().prec = 30
    return str((Decimal(num) / Decimal(den)).quantize(Decimal("1.000000")))


if __name__ == "__main__":
    print(solve())  # 11.492847
