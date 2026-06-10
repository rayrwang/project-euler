from decimal import Decimal, getcontext
from math import factorial

def smooth_permutations(n: int) -> int:
    """F(N): orderings of the 3-smooth numbers <= N where every element
    follows all its proper divisors — exactly the linear extensions of
    the divisibility poset on {2^i 3^j <= N}.

    Under (i, j) coordinates divisibility is the componentwise order, and
    the region is a Young diagram: row j (the power of 3) has length
    lambda_j = #{i : 2^i 3^j <= N}. Linear extensions of a Young diagram
    poset are standard Young tableaux, so the hook length formula gives
    F(N) = K! / prod(hooks) exactly, with K = |S(N)| around 1100 cells
    for N = 10^18 — comfortably exact in big integers.
    """
    rows = []
    p3 = 1
    while p3 <= n:
        rest = n // p3
        length = rest.bit_length()  # #{i >= 0 : 2^i <= rest}
        rows.append(length)
        p3 *= 3
    k = sum(rows)
    hooks = 1
    for j, row_len in enumerate(rows):
        for i in range(row_len):
            # column height at i: rows below j with length > i
            col = sum(1 for jj in range(j + 1, len(rows)) if rows[jj] > i)
            hooks *= (row_len - i) + col
    num = factorial(k)
    assert num % hooks == 0
    return num // hooks

def sci_format(v: int, places: int) -> str:
    getcontext().prec = places + 30
    d = Decimal(v)
    exp = len(str(v)) - 1
    mant = d / Decimal(10) ** exp
    q = mant.quantize(Decimal(1).scaleb(-places))
    if q >= 10:  # rounding overflowed the leading digit
        q = (q / 10).quantize(Decimal(1).scaleb(-places))
        exp += 1
    return f"{q}e{exp}"

def brute(n: int) -> int:
    smooth = []
    p2 = 1
    while p2 <= n:
        v = p2
        while v <= n:
            smooth.append(v)
            v *= 3
        p2 *= 2
    smooth.sort()
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def count(placed: int) -> int:
        if placed == (1 << len(smooth)) - 1:
            return 1
        total = 0
        for i, v in enumerate(smooth):
            if placed >> i & 1:
                continue
            ok = True
            for j, w in enumerate(smooth):
                if w != v and v % w == 0 and not placed >> j & 1:
                    ok = False
                    break
            if ok:
                total += count(placed | 1 << i)
        return total

    return count(0)

if __name__ == "__main__":
    assert smooth_permutations(6) == brute(6) == 5
    assert smooth_permutations(8) == brute(8) == 9
    assert smooth_permutations(20) == brute(20) == 450
    assert sci_format(smooth_permutations(1000), 10).startswith("8.8521816557e21"[:12])
    assert sci_format(112233445566778899, 10) == "1.1223344557e17"
    print(sci_format(smooth_permutations(10**18), 10))  # 5.5350769703e1512
