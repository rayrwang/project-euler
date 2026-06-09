from decimal import Decimal, getcontext


def solve(target: int = -600_000_000_000, n: int = 5000) -> str:
    # s(r) = sum_{k=1}^{n} (900 - 3k) r^(k-1) is strictly decreasing in r once
    # the negative tail dominates (already at r = 1 the sum is negative and
    # growing r weights the most negative terms hardest), so bisect for the
    # root of s(r) = target. Decimal arithmetic keeps 12 decimal places exact.
    getcontext().prec = 30
    t = Decimal(target)

    def s(r: Decimal) -> Decimal:
        total = Decimal(0)
        rp = Decimal(1)
        for k in range(1, n + 1):
            total += (900 - 3 * k) * rp
            rp *= r
        return total

    lo, hi = Decimal("1.0"), Decimal("1.1")
    for _ in range(60):
        mid = (lo + hi) / 2
        if s(mid) > t:
            lo = mid
        else:
            hi = mid
    return str(((lo + hi) / 2).quantize(Decimal("1.000000000000")))


if __name__ == "__main__":
    print(solve())  # 1.002322108633
