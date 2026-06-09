from functools import reduce
from itertools import permutations
from math import gcd

_FULL = set("0123456789")


def _divisors(g: int) -> list[int]:
    ds = []
    i = 1
    while i * i <= g:
        if g % i == 0:
            ds.append(i)
            if i != g // i:
                ds.append(g // i)
        i += 1
    return ds


def _valid(p: str) -> bool:
    # Some split of P into >=2 product-parts admits a common factor m whose
    # quotients, concatenated after m, form a 0-9 pandigital input string.
    n = len(p)
    for mask in range(1, 1 << (n - 1)):
        parts = []
        prev = 0
        ok = True
        for i in range(n - 1):
            if mask >> i & 1:
                seg = p[prev : i + 1]
                if len(seg) > 1 and seg[0] == "0":
                    ok = False
                    break
                parts.append(int(seg))
                prev = i + 1
        if not ok:
            continue
        seg = p[prev:]
        if len(seg) > 1 and seg[0] == "0":
            continue
        parts.append(int(seg))
        if len(parts) < 2:
            continue
        for m in _divisors(reduce(gcd, parts)):
            inp = str(m) + "".join(str(part // m) for part in parts)
            if len(inp) == 10 and set(inp) == _FULL:
                return True
    return False


def solve() -> int:
    # Largest 0-9 pandigital concatenated product whose inputs are also pandigital.
    for perm in permutations("9876543210"):
        if perm[0] == "0":
            continue
        p = "".join(perm)
        if _valid(p):
            return int(p)
    raise RuntimeError("no solution found")


if __name__ == "__main__":
    print(solve())  # 9857164023
