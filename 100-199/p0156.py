def _count(n: int, d: int) -> int:
    # Number of times digit d appears writing out 1, 2, ..., n.
    cnt = 0
    p = 1
    while p <= n:
        high, cur, low = n // (p * 10), (n // p) % 10, n % p
        if cur > d:
            cnt += (high + 1) * p
        elif cur == d:
            cnt += high * p + low + 1
        else:
            cnt += high * p
        p *= 10
    return cnt


def _search(lo: int, hi: int, d: int, out: list[int]) -> None:
    # g(n) = f(n,d) - n changes by at most +(L-1) and at least -1 each step,
    # so g stays positive if g(lo) > hi-lo and negative if g(lo)+(L-1)(hi-lo) < 0.
    glo = _count(lo, d) - lo
    if glo > hi - lo:
        return
    if glo + (len(str(hi)) - 1) * (hi - lo) < 0:
        return
    if lo == hi:
        if glo == 0:
            out.append(lo)
        return
    mid = (lo + hi) // 2
    _search(lo, mid, d, out)
    _search(mid + 1, hi, d, out)


def solve(upper: int = 10**12) -> int:
    total = 0
    for d in range(1, 10):
        out: list[int] = []
        _search(1, upper, d, out)
        total += sum(out)
    return total


if __name__ == "__main__":
    print(solve())  # 21295121502550
