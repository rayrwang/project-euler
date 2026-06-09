"""Project Euler 974: Very Odd Numbers.

Digits all odd; each of 1,3,5,7,9 occurs an odd number of times (so all five
occur and the length is odd, >= 5); divisible by 105 = 3*5*7.

Digit DP over state (parity mask of the five digits, value mod 105), building
from the most significant digit. g[m][mask][r] counts length-m suffixes that
bring state (mask, r) to (full mask, residue 0).
"""

DIGITS = (1, 3, 5, 7, 9)
BIT = {1: 1, 3: 2, 5: 4, 7: 8, 9: 16}


def build_tables(max_len: int) -> list[list[list[int]]]:
    g = [[[0] * 105 for _ in range(32)] for _ in range(max_len + 1)]
    g[0][31][0] = 1
    for m in range(1, max_len + 1):
        gm = g[m]
        gp = g[m - 1]
        for mask in range(32):
            row = gm[mask]
            for r in range(105):
                tot = 0
                base = (10 * r) % 105
                for d in DIGITS:
                    tot += gp[mask ^ BIT[d]][(base + d) % 105]
                row[r] = tot
    return g


def nth(n: int, max_len: int = 45) -> int:
    g = build_tables(max_len)
    # choose length
    length = None
    for ell in range(5, max_len + 1, 2):
        cnt = g[ell][0][0]
        if n <= cnt:
            length = ell
            break
        n -= cnt
    assert length is not None
    # construct digits most-significant first
    mask, r = 0, 0
    out = []
    for pos in range(length):
        rem = length - pos - 1
        for d in DIGITS:
            nmask = mask ^ BIT[d]
            nr = (10 * r + d) % 105
            c = g[rem][nmask][nr]
            if n <= c:
                out.append(d)
                mask, r = nmask, nr
                break
            n -= c
        else:
            raise AssertionError("construction failed")
    return int("".join(map(str, out)))


if __name__ == "__main__":
    print(nth(10 ** 16))  # 13313751171933973557517973175
