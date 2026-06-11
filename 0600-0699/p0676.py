"""Project Euler Problem 676: Matching Digit Sums.

For bases 2^k and 2^l both digit sums are computed from the binary
expansion by grouping bits, so process numbers in blocks of
L = lcm(k, l) bits: a block value v contributes
delta(v) = (sum of its k-bit groups) - (sum of its l-bit groups) to the
running difference, and i counts for M exactly when the total delta
is zero.

Pad N = 10^16 to a whole number of blocks (leading zeros change
nothing).  A suffix DP over block positions records, for every
achievable delta, the count of suffixes and the sum of their values.
Walking the blocks of N from the most significant, every smaller value
v at a tight position opens a free tail, contributing
count * prefix_value + suffix_sum at the complementary delta; finally N
itself is included when its total delta vanishes.  Per-block transitions
are aggregated by delta, so each of the ten (k, l) pairs costs only a
few thousand operations; everything is exact integer arithmetic, reduced
modulo 10^16 at the end.

Verified: M(10, 8, 2) = 18, M(100, 8, 2) = 292, and
M(10^6, 8, 2) = 19173952 from the statement, plus brute force for all
ten (k, l) pairs up to 10^4.
"""

from collections import defaultdict
from math import lcm

N = 10**16
MOD = 10**16


def block_deltas(big: int, small: int, width: int) -> list[int]:
    """delta(v) for all width-bit blocks: k-group sum minus l-group sum."""
    out = []
    big_mask = (1 << big) - 1
    small_mask = (1 << small) - 1
    for v in range(1 << width):
        d1 = d2 = 0
        x = v
        while x:
            d1 += x & big_mask
            x >>= big
        x = v
        while x:
            d2 += x & small_mask
            x >>= small
        out.append(d1 - d2)
    return out


def m_sum(n: int, k: int, ell: int) -> int:
    """Sum of i <= n with equal digit sums in bases 2^k and 2^l."""
    width = lcm(k, ell)
    deltas = block_deltas(k, ell, width)
    blocks = []
    x = n
    while x:
        blocks.append(x & ((1 << width) - 1))
        x >>= width
    blocks.reverse()

    # Aggregate per block: delta -> (count, sum of block values).
    agg: dict[int, tuple[int, int]] = defaultdict(lambda: (0, 0))
    for v, d in enumerate(deltas):
        c, s = agg[d]
        agg[d] = (c + 1, s + v)

    # suffix[j][d] = (count, sum of suffix values) over j free blocks.
    suffix: list[dict[int, tuple[int, int]]] = [{0: (1, 0)}]
    for j in range(1, len(blocks)):
        prev = suffix[-1]
        cur: dict[int, tuple[int, int]] = defaultdict(lambda: (0, 0))
        shift = 1 << (width * (j - 1))
        for d_block, (cb, sb) in agg.items():
            for d_prev, (cp, sp) in prev.items():
                c, s = cur[d_block + d_prev]
                cur[d_block + d_prev] = (
                    c + cb * cp, s + sb * shift * cp + cb * sp
                )
        suffix.append(dict(cur))

    total = 0
    prefix_delta = 0
    prefix_value = 0
    for j, w in enumerate(blocks):
        free = len(blocks) - 1 - j
        tail = 1 << (width * free)
        for v in range(w):
            need = -(prefix_delta + deltas[v])
            if need in suffix[free]:
                c, s = suffix[free][need]
                total += c * (prefix_value * (1 << width) + v) * tail + s
        prefix_delta += deltas[w]
        prefix_value = prefix_value * (1 << width) + w
    if prefix_delta == 0:
        total += n
    return total


def m_brute(n: int, k: int, ell: int) -> int:
    def dsum(i: int, bits: int) -> int:
        out = 0
        while i:
            out += i & ((1 << bits) - 1)
            i >>= bits
        return out

    return sum(i for i in range(1, n + 1) if dsum(i, k) == dsum(i, ell))


if __name__ == "__main__":
    assert m_sum(10, 3, 1) == 18
    assert m_sum(100, 3, 1) == 292
    assert m_sum(10**6, 3, 1) == 19173952
    pairs = [(k, ell) for k in range(3, 7) for ell in range(1, k - 1)]
    assert all(m_sum(10**4, k, ell) == m_brute(10**4, k, ell)
               for k, ell in pairs)
    answer = sum(m_sum(N, k, ell) for k, ell in pairs) % MOD
    print(answer)  # 3562668074339584
