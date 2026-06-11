import numba
import numpy as np

# A range [a, a+35] is divisible iff the bipartite graph "number m can take
# position d when d | m" has a perfect matching.  A number with no prime
# factor <= 31 has no divisor in [2, 36] at all ("rough"), so it can only
# occupy position 1; hence a valid window contains at most one rough number,
# which empirically holds for only ~3 in 10^4 starts.  The pipeline is:
#
#  1. Stream a rough-number bitmap: a wheel pattern over the primes <= 19
#     (period 9699690 * 32 numbers, word-aligned) AND-ed per 64-bit word
#     with precomputed bit masks for 23, 29, 31.  Every window with <= 1
#     rough number contains three consecutive 8-aligned bytes carrying <= 1
#     set bit, detected branchlessly with SWAR per-byte popcounts.
#  2. Triggered spans are refined with a sliding 36-bit popcount to the
#     exact candidate starts (<= 1 rough in window).
#  3. Candidates pass through the Hall-type filter "at most d numbers in
#     the window have largest divisor <= 36 at most d" for every d, with
#     the largest divisors maintained by incremental remainders.
#  4. Survivors get an exact maximum-matching test (Kuhn's algorithm with
#     position bitmasks), which is the definition, so no false positives.

L = 36
PERIOD = 9699690 * 32  # lcm of the wheel primes' product (x2) and 64 bits
NWORDS = PERIOD // 64
HEAD = 4  # buffer margin: last words of the previous block
TAIL = 68  # buffer margin: first words of the next block
WHEEL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)
MARK_PRIMES = (23, 29, 31)
ONES = np.uint64(0x0101010101010101)
HIGHS = np.uint64(0x8080808080808080)
M1 = np.uint64(0x5555555555555555)
M2 = np.uint64(0x3333333333333333)
M4 = np.uint64(0x0F0F0F0F0F0F0F0F)
EVENS = np.uint64(0xFEFEFEFEFEFEFEFE)


@numba.njit(cache=True)
def build_pattern() -> np.ndarray:
    """Bit j of word w is set iff 64 w + j is coprime to every prime <= 19."""
    pattern = np.full(NWORDS, ~np.uint64(0), dtype=np.uint64)
    for p in WHEEL_PRIMES:
        for m in range(0, PERIOD, p):
            pattern[m >> 6] &= ~(np.uint64(1) << np.uint64(m & 63))
    return pattern


@numba.njit(cache=True)
def build_masks(p: int) -> np.ndarray:
    """masks[r] clears the bits j of a word starting at r mod p with p | r+j."""
    masks = np.empty(p, dtype=np.uint64)
    for r in range(p):
        m = np.uint64(0)
        for j in range(64):
            if (r + j) % p == 0:
                m |= np.uint64(1) << np.uint64(j)
        masks[r] = ~m
    return masks


@numba.njit(cache=True)
def sieve_words(
    buf: np.ndarray,
    off: int,
    count: int,
    pattern: np.ndarray,
    poff: int,
    start: int,
    m23: np.ndarray,
    m29: np.ndarray,
    m31: np.ndarray,
) -> None:
    """buf[off + k] = rough bitmap of numbers [start + 64 k, start + 64 k + 64)."""
    r23, r29, r31 = start % 23, start % 29, start % 31
    for k in range(count):
        buf[off + k] = pattern[poff + k] & m23[r23] & m29[r29] & m31[r31]
        r23 += 18  # 64 mod 23
        if r23 >= 23:
            r23 -= 23
        r29 += 6  # 64 mod 29
        if r29 >= 29:
            r29 -= 29
        r31 += 2  # 64 mod 31
        if r31 >= 31:
            r31 -= 31


@numba.njit(cache=True, inline="always")
def get_bit(buf: np.ndarray, buf_start: int, number: int) -> int:
    i = number - buf_start
    return int((buf[i >> 6] >> np.uint64(i & 63)) & np.uint64(1))


@numba.njit(cache=True)
def can_match(a: int, length: int) -> bool:
    """Exact test: numbers a..a+length-1 onto positions 1..length (Kuhn)."""
    masks = np.empty(length, dtype=np.uint64)
    for o in range(length):
        m = a + o
        mk = np.uint64(0)
        for d in range(1, length + 1):
            if m % d == 0:
                mk |= np.uint64(1) << np.uint64(d - 1)
        masks[o] = mk
    match_of = np.full(length, -1, dtype=np.int64)  # position -> number
    stack_num = np.empty(length + 1, dtype=np.int64)
    stack_rem = np.empty(length + 1, dtype=np.uint64)
    path_pos = np.empty(length + 1, dtype=np.int64)
    for i0 in range(length):
        visited = np.uint64(0)
        top = 0
        stack_num[0] = i0
        stack_rem[0] = masks[i0]
        augmented = False
        while top >= 0:
            rem = stack_rem[top] & ~visited
            if rem == np.uint64(0):
                top -= 1
                continue
            bit = rem & (~rem + np.uint64(1))
            stack_rem[top] ^= bit
            visited |= bit
            p = 0
            b = bit
            while b > np.uint64(1):
                b >>= np.uint64(1)
                p += 1
            if match_of[p] == -1:
                match_of[p] = stack_num[top]
                for d in range(top - 1, -1, -1):
                    match_of[path_pos[d]] = stack_num[d]
                augmented = True
                break
            path_pos[top] = p
            stack_num[top + 1] = match_of[p]
            stack_rem[top + 1] = masks[match_of[p]]
            top += 1
        if not augmented:
            return False
    return True


@numba.njit(cache=True)
def check_run(c0: int, c1: int, valids: np.ndarray, nv: int) -> int:
    """Hall prefix filter + exact matching for candidate starts c0..c1."""
    n = c1 - c0 + L
    maxd = np.empty(n, dtype=np.int64)
    rem = np.empty(L + 1, dtype=np.int64)
    for d in range(2, L + 1):
        rem[d] = c0 % d
    for i in range(n):
        md = 1
        for d in range(L, 1, -1):
            if rem[d] == 0:
                md = d
                break
        maxd[i] = md
        for d in range(2, L + 1):
            rem[d] += 1
            if rem[d] == d:
                rem[d] = 0
    cnt = np.empty(L + 1, dtype=np.int64)
    for a in range(c0, c1 + 1):
        cnt[:] = 0
        for o in range(L):
            cnt[maxd[a - c0 + o]] += 1
        s = 0
        ok = True
        for d in range(1, L):
            s += cnt[d]
            if s > d:
                ok = False
                break
        if ok and can_match(a, L):
            valids[nv] = a
            nv += 1
    return nv


@numba.njit(cache=True)
def refine_interval(
    plo: int,
    phi: int,
    buf: np.ndarray,
    buf_start: int,
    valids: np.ndarray,
    nv: int,
    collect_candidates: bool,
) -> int:
    """Keep starts whose window holds <= 1 rough number; forward runs on."""
    cnt = 0
    for o in range(L):
        cnt += get_bit(buf, buf_start, plo + o)
    a = plo
    run_start = -1
    while True:
        if cnt <= 1:
            if run_start < 0:
                run_start = a
        elif run_start >= 0:
            if collect_candidates:
                for c in range(run_start, a):
                    valids[nv] = c
                    nv += 1
            else:
                nv = check_run(run_start, a - 1, valids, nv)
            run_start = -1
        if a == phi:
            break
        cnt += get_bit(buf, buf_start, a + L) - get_bit(buf, buf_start, a)
        a += 1
    if run_start >= 0:
        if collect_candidates:
            for c in range(run_start, phi + 1):
                valids[nv] = c
                nv += 1
        else:
            nv = check_run(run_start, phi, valids, nv)
    return nv


@numba.njit(cache=True)
def solve(target: int, out: np.ndarray, collect_candidates: bool) -> int:
    """Scan increasing a, appending hits to out until target are found."""
    pattern = build_pattern()
    m23, m29, m31 = build_masks(23), build_masks(29), build_masks(31)
    buf = np.zeros(HEAD + NWORDS + TAIL, dtype=np.uint64)
    nv = 0
    cprev = np.uint64(0)  # packed per-byte popcounts of the previous word
    pend_lo, pend_hi = 0, -1  # pending merged raw interval of starts
    watermark = 0  # highest start already examined
    block = 0
    while nv < target:
        if block >= 4000:
            break
        start = block * PERIOD
        if block > 0:
            buf[:HEAD] = buf[HEAD + NWORDS - HEAD : HEAD + NWORDS]
        sieve_words(buf, HEAD, NWORDS, pattern, 0, start, m23, m29, m31)
        sieve_words(buf, HEAD + NWORDS, TAIL, pattern, 0, start + PERIOD, m23, m29, m31)
        buf_start = start - HEAD * 64
        for k in range(NWORDS):
            w = buf[HEAD + k]
            # SWAR per-byte popcounts, then per-byte sums of three
            # consecutive byte counts (carrying in the previous word's).
            c = w - ((w >> np.uint64(1)) & M1)
            c = (c & M2) + ((c >> np.uint64(2)) & M2)
            c = (c + (c >> np.uint64(4))) & M4
            t = (
                c
                + ((c << np.uint64(8)) | (cprev >> np.uint64(56)))
                + ((c << np.uint64(16)) | (cprev >> np.uint64(48)))
            )
            cprev = c
            z = t & EVENS
            trig = (z - ONES) & ~z & HIGHS  # flags bytes of t that are <= 1
            if trig == np.uint64(0):
                continue
            word_byte = (start + 64 * k) >> 3
            while trig != np.uint64(0):
                low = trig & (~trig + np.uint64(1))
                trig ^= low
                j = 0
                b = low
                while b > np.uint64(128):
                    b >>= np.uint64(8)
                    j += 1
                gb = word_byte + j  # last byte of a sparse byte-triple
                a_lo, a_hi = 8 * gb - 28, 8 * gb - 16
                if a_lo <= pend_hi + 1:
                    if a_hi > pend_hi:
                        pend_hi = a_hi
                else:
                    lo = max(pend_lo, watermark + 1, 1)
                    if lo <= pend_hi:
                        watermark = pend_hi
                        nv = refine_interval(
                            lo, pend_hi, buf, buf_start, out, nv, collect_candidates
                        )
                        if nv >= target:
                            return nv
                    pend_lo, pend_hi = a_lo, a_hi
        block += 1
    lo = max(pend_lo, watermark + 1, 1)
    if lo <= pend_hi and nv < target:
        nv = refine_interval(lo, pend_hi, buf, buf_start, out, nv, collect_candidates)
    return nv


if __name__ == "__main__":
    # Given: the first four divisible ranges of length 4 start at 1, 2, 3, 6.
    firsts4 = [a for a in range(1, 100) if can_match(a, 4)][:4]
    assert firsts4 == [1, 2, 3, 6]

    # Stage 1+2 (candidate generation) cross-checked against a plain sieve.
    limit = 2 * 10**7
    rough = np.ones(limit + 64, dtype=np.uint8)
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        rough[p::p] = 0
    rough[0] = 0
    sums = np.cumsum(rough, dtype=np.int64)
    starts = np.arange(1, limit - L)
    reference = starts[(sums[starts + L - 1] - sums[starts - 1]) <= 1]
    cand = np.empty(len(reference) + 100, dtype=np.int64)
    nc = solve(len(reference), cand, True)
    assert np.array_equal(cand[:nc], reference)

    # The pipeline agrees with the exact matching run on every small start.
    direct = [a for a in range(1, 3 * 10**5) if can_match(a, L)]
    found = np.empty(64, dtype=np.int64)
    nf = solve(len(direct), found, False)
    assert list(found[:nf]) == direct

    n_found = solve(36, found, False)
    assert n_found >= 36
    print(found[35])  # 274229635640
