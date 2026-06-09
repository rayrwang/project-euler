from collections import defaultdict
from math import isqrt


def _is_sq(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def solve() -> int:
    # Both x+y,x-y and x+z,x-z being squares means y and z are each values v
    # with x +/- v square, i.e. 2x = c^2 + d^2 and v = (c^2 - d^2)/2. Collect
    # those candidate v per x, then seek a pair (y>z) with y+z, y-z also square.
    limit_c = 1500
    cand: dict[int, list[int]] = defaultdict(list)
    for c in range(2, limit_c + 1):
        c2 = c * c
        for d in range(1, c):
            s = c2 + d * d
            if s % 2:
                continue
            cand[s // 2].append((c2 - d * d) // 2)

    best = None
    for x in sorted(cand):
        if best is not None and x >= best:
            break
        vs = sorted(set(cand[x]))
        for i in range(len(vs)):
            y = vs[i]
            for j in range(i):
                z = vs[j]  # z < y
                if _is_sq(y + z) and _is_sq(y - z):
                    total = x + y + z
                    if best is None or total < best:
                        best = total
    assert best is not None
    return best


if __name__ == "__main__":
    print(solve())  # 1006193
