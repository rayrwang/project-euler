import numba
import numpy as np

from funcs import prime_sieve_bool

# Seven-segment patterns (as 7-bit masks) and their lit-segment counts.
_SEG = (
    (1, 1, 1, 0, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0), (1, 0, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 1), (0, 1, 1, 1, 0, 1, 0), (1, 1, 0, 1, 0, 1, 1),
    (1, 1, 0, 1, 1, 1, 1), (1, 1, 1, 0, 0, 1, 0), (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 1, 1),
)
SEG_COUNT = np.array([sum(t) for t in _SEG], dtype=np.int64)
SEG_BITS = np.array([sum(b << i for i, b in enumerate(t)) for t in _SEG], dtype=np.int64)

@numba.jit(cache=True)
def _popcount(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c

@numba.jit(cache=True)
def _sam(a, b, seg_count):
    # Clear every lit segment of a, then light every segment of b. 0 == blank.
    s = 0
    while a > 0:
        s += seg_count[a % 10]
        a //= 10
    while b > 0:
        s += seg_count[b % 10]
        b //= 10
    return s

@numba.jit(cache=True)
def _max(a, b, seg_bits):
    # Only toggle the segments that differ, digit by digit (right aligned).
    s = 0
    while a > 0 or b > 0:
        ba = seg_bits[a % 10] if a > 0 else 0
        bb = seg_bits[b % 10] if b > 0 else 0
        s += _popcount(ba ^ bb)
        a //= 10
        b //= 10
    return s

@numba.jit(cache=True)
def _digit_sum(n):
    t = 0
    while n > 0:
        t += n % 10
        n //= 10
    return t

@numba.jit(cache=True)
def saving(p, seg_count, seg_bits):
    # Display p, then its repeated digit sums down to one digit, starting and
    # ending from a blank screen. Return Sam's transitions minus Max's.
    sam = _sam(0, p, seg_count)
    mx = _max(0, p, seg_bits)
    cur = p
    while cur >= 10:
        nxt = _digit_sum(cur)
        sam += _sam(cur, nxt, seg_count)
        mx += _max(cur, nxt, seg_bits)
        cur = nxt
    sam += _sam(cur, 0, seg_count)
    mx += _max(cur, 0, seg_bits)
    return sam - mx

@numba.jit(cache=True)
def solve(lo, hi, is_pr, seg_count, seg_bits):
    diff = 0
    for p in range(lo, hi):
        if is_pr[p]:
            diff += saving(p, seg_count, seg_bits)
    return diff

if __name__ == "__main__":
    LO, HI = 10_000_000, 20_000_000
    is_pr = prime_sieve_bool(HI)
    print(solve(LO, HI, is_pr, SEG_COUNT, SEG_BITS))  # 13625242
