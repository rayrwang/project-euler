def _blocks(m: int) -> tuple[list[int], list[int]]:
    # For m-digit strings (leading zeros allowed): count and numeric-value sum
    # grouped by digit sum.
    cnt = [1]
    val = [0]
    for length in range(1, m + 1):
        size = 9 * length
        nc = [0] * (size + 1)
        nv = [0] * (size + 1)
        place = 10 ** (length - 1)
        for s in range(len(cnt)):
            for d in range(10):
                nc[s + d] += cnt[s]
                nv[s + d] += d * place * cnt[s] + val[s]
        cnt, val = nc, nv
    return cnt, val


def _lead_blocks(m: int) -> tuple[list[int], list[int]]:
    # Same but the leading digit is 1..9.
    cnt, val = _blocks(m - 1)
    size = 9 * m
    nc = [0] * (size + 1)
    nv = [0] * (size + 1)
    place = 10 ** (m - 1)
    for s in range(len(cnt)):
        for d in range(1, 10):
            nc[s + d] += cnt[s]
            nv[s + d] += d * place * cnt[s] + val[s]
    return nc, nv


def solve(n: int = 47, modulus: int = 3**15) -> int:
    # A balanced number splits into first/last halves of floor(L/2) digits with
    # equal digit sums (an odd length has a free middle digit). Sum over the
    # shared digit-sum class s.
    total = 45 if n >= 1 else 0  # single-digit numbers
    for length in range(2, n + 1):
        h = length // 2
        cnt_any, sum_any = _blocks(h)
        cnt_lead, sum_lead = _lead_blocks(h)
        upto = min(len(cnt_any), len(cnt_lead))
        if length % 2 == 0:
            p = 10**h
            for s in range(upto):
                total += sum_lead[s] * p * cnt_any[s] + cnt_lead[s] * sum_any[s]
        else:
            p1, p0 = 10 ** (h + 1), 10**h
            for s in range(upto):
                total += (
                    sum_lead[s] * p1 * 10 * cnt_any[s]
                    + 45 * p0 * cnt_lead[s] * cnt_any[s]
                    + cnt_lead[s] * 10 * sum_any[s]
                )
    return total % modulus


if __name__ == "__main__":
    print(solve())  # 6273134
