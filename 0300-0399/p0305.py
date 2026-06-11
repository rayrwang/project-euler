from functools import lru_cache


def _count_internal(off: int, pat: str, digits: int, lo: int, hi: int) -> int:
    """Count d-digit integers in [lo, hi] whose decimal string equals `pat` over
    positions [off, off+len(pat)) -- an occurrence of the pattern lying wholly inside
    one number."""
    length = len(pat)

    def below(bound: int) -> int:
        if bound < 10 ** (digits - 1):
            return 0
        s = str(min(bound, 10**digits - 1))

        @lru_cache(maxsize=None)
        def dp(pos: int, tight: bool) -> int:
            if pos == digits:
                return 1
            total = 0
            top = int(s[pos]) if tight else 9
            for d in range(top + 1):
                if pos == 0 and d == 0:
                    continue
                if off <= pos < off + length and d != int(pat[pos - off]):
                    continue
                total += dp(pos + 1, tight and d == top)
            return total

        result = dp(0, True)
        dp.cache_clear()
        return result

    return below(hi) - below(lo - 1)


def _count_fixed(prefix: str, suffix: str, digits: int, lo: int, hi: int) -> int:
    """Count d-digit integers in [lo, hi] whose string starts with `prefix` and ends with
    `suffix` (with prefix and suffix non-overlapping)."""
    plen, slen = len(prefix), len(suffix)

    def below(bound: int) -> int:
        if bound < 10 ** (digits - 1):
            return 0
        s = str(min(bound, 10**digits - 1))

        @lru_cache(maxsize=None)
        def dp(pos: int, tight: bool) -> int:
            if pos == digits:
                return 1
            total = 0
            top = int(s[pos]) if tight else 9
            for d in range(top + 1):
                if pos == 0 and d == 0:
                    continue
                if pos < plen and d != int(prefix[pos]):
                    continue
                if pos >= digits - slen and d != int(suffix[pos - (digits - slen)]):
                    continue
                total += dp(pos + 1, tight and d == top)
            return total

        result = dp(0, True)
        dp.cache_clear()
        return result

    return below(hi) - below(lo - 1)


def _count_boundary(digits: int, lo: int, hi: int, suf: str, rest: str) -> int:
    """Occurrences that start inside a d-digit number i (its last len(suf) digits equal
    `suf`) and continue into i+1, i+2, ... which must begin with `rest`.

    When the number has at least len(suf)+len(rest) digits and `suf` is not all nines,
    incrementing i leaves the upper digits untouched, so the condition collapses to: the
    string of i both starts with `rest` and ends with `suf`. The rare leftovers (very
    short numbers, or carries from a trailing run of nines) are counted directly."""
    r, lr = len(suf), len(rest)
    if digits >= r + lr and suf != "9" * r:
        return _count_fixed(rest, suf, digits, lo, hi)
    count = 0
    for i in range(lo, hi + 1):
        if not str(i).endswith(suf):
            continue
        buf = ""
        j = i + 1
        while len(buf) < lr:
            buf += str(j)
            j += 1
        if buf[:lr] == rest:
            count += 1
    return count


def _occurrences_upto(pat: str, m: int) -> int:
    """Number of occurrences of `pat` in 1·2·3···m that *start* within a number <= m."""
    length = len(pat)
    total = 0
    digits = 1
    while 10 ** (digits - 1) <= m:
        lo = 10 ** (digits - 1)
        hi = min(m, 10**digits - 1)
        if lo <= hi:
            for off in range(digits - length + 1):
                total += _count_internal(off, pat, digits, lo, hi)
            for off in range(max(0, digits - length + 1), digits):
                r = digits - off
                if 1 <= r <= length - 1:
                    total += _count_boundary(digits, lo, hi, pat[:r], pat[r:])
        digits += 1
    return total


def _length_upto(m: int) -> int:
    """Number of digits in the concatenation 1·2·3···m."""
    total = 0
    d = 1
    start = 1
    while start <= m:
        end = min(m, 10**d - 1)
        total += (end - start + 1) * d
        start = 10**d
        d += 1
    return total


def f(n: int) -> int:
    """Starting position (1-indexed) of the n-th occurrence of the digits of n in the
    string 1234567891011121314..."""
    pat = str(n)
    lo, hi = 1, 10**6
    while _occurrences_upto(pat, hi) < n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if _occurrences_upto(pat, mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    m = lo
    need = n - _occurrences_upto(pat, m - 1)  # which occurrence inside number m

    length = len(pat)
    text = str(m)
    j = m + 1
    while len(text) < len(str(m)) + length:
        text += str(j)
        j += 1
    seen = 0
    for off in range(len(str(m))):
        if text[off : off + length] == pat:
            seen += 1
            if seen == need:
                return _length_upto(m - 1) + off + 1
    raise AssertionError("occurrence not located")


def solve() -> int:
    return sum(f(3**k) for k in range(1, 14))


if __name__ == "__main__":
    assert f(1) == 1
    assert f(5) == 81
    assert f(12) == 271
    assert f(7780) == 111111365
    print(solve())  # 18174995535140
