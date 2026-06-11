"""Project Euler Problem 685: Inverse Digit Sum II.

f(D, m) is the m-th positive integer with digit sum D; we need
S(10^4) = sum f(n^3, n^4) mod 10^9 + 7, where the numbers involved have up
to about 10^11 digits, so they are handled as sparse deficit patterns.

A length-L digit string with digit sum D corresponds to the deficit vector
e_i = 9 - d_i with entries in [0, 9] summing to E = 9L - D (leading digit
nonzero means e_1 <= 8).  The number of such vectors is

    V(L, E) = sum_j (-1)^j C(L, j) C(E - 10j + L - 1, L - 1),

a short inclusion-exclusion since j <= E / 10, with every binomial having
a small "choose" side (L - 1 when L is small, E - 10j when L is huge).
Counting per length locates the length of f(D, m) and its rank r within
it; unranking then walks the digits from the most significant, choosing
the smallest digit whose completion count covers r.  Almost all digits
are forced 9s, and a run of t nines reduces r by V(L, E) - V(L - t, E),
so the next non-nine position is found by binary search on the monotone
condition V(L - t - 1, E) <= V(L, E) - r; only the at most E non-nine
digits are ever materialised.  Each result is mostly-nines, so its value
modulo p is (10^L - 1) minus the few deficits times their place values.

Verified: f(10, 1) = 19, f(10, 10) = 109, f(10, 100) = 1423, S(3) = 7128,
S(10) = 32287064 mod 10^9 + 7, and f(D, m) against brute-force enumeration
for D <= 25 and m <= 300.
"""

MOD = 1_000_000_007
K = 10**4


def binom(a: int, k: int) -> int:
    if k < 0 or a < 0 or k > a:
        return 0
    k = min(k, a - k)
    out = 1
    for i in range(k):
        out = out * (a - i) // (i + 1)
    return out


def count_vectors(length: int, total: int) -> int:
    """Vectors of given length with entries in [0, 9] summing to total."""
    if total < 0 or total > 9 * length:
        return 0
    if length == 0:
        return 1  # the empty vector; the formula below hits C(-1, -1)
    out = 0
    sign = 1
    for j in range(total // 10 + 1):
        out += sign * binom(length, j) * binom(
            total - 10 * j + length - 1, length - 1
        )
        sign = -sign
    return out


def f_sparse(digit_sum: int, m: int) -> tuple[int, list[tuple[int, int]]]:
    """The m-th number with given digit sum, as (length, deficits).

    Deficits are (offset from the most significant position, e) pairs
    with e >= 1; all other digits are 9.
    """
    length = (digit_sum + 8) // 9
    while True:
        excess = 9 * length - digit_sum
        here = count_vectors(length, excess) - count_vectors(
            length - 1, excess - 9
        )
        if m <= here:
            break
        m -= here
        length += 1

    deficits = []
    pos, rem_len, rem_e, first = 0, length, excess, True
    while rem_e > 0:
        assert rem_len >= 1 and m >= 1
        # Try digits in increasing order at this position.
        placed = False
        for e in range(min(rem_e, 8 if first else 9), 0, -1):
            ways = count_vectors(rem_len - 1, rem_e - e)
            if m <= ways:
                deficits.append((pos, e))
                rem_e -= e
                placed = True
                break
            m -= ways
        first = False
        if placed:
            pos += 1
            rem_len -= 1
            continue
        # Digit 9 here; binary search the run of nines.  After t extra
        # nines the remaining rank is m - (V(rem_len-1, E) - V(L', E))
        # where L' = rem_len - 1 - t, and the next position is non-nine
        # once that rank fits within V(L', E) - V(L' - 1, E).
        base = count_vectors(rem_len - 1, rem_e)
        lo, hi = 0, rem_len - 1  # t in [lo, hi)
        while lo < hi:
            mid = (lo + hi) // 2
            if count_vectors(rem_len - 2 - mid, rem_e) <= base - m:
                hi = mid
            else:
                lo = mid + 1
        t = lo
        m -= base - count_vectors(rem_len - 1 - t, rem_e)
        pos += 1 + t
        rem_len -= 1 + t
    return length, deficits


def f_mod(digit_sum: int, m: int, mod: int) -> int:
    length, deficits = f_sparse(digit_sum, m)
    value = (pow(10, length, mod) - 1) % mod
    for pos, e in deficits:
        value = (value - e * pow(10, length - 1 - pos, mod)) % mod
    return value


def f_exact(digit_sum: int, m: int) -> int:
    length, deficits = f_sparse(digit_sum, m)
    digits = [9] * length
    for pos, e in deficits:
        digits[pos] -= e
    return int("".join(map(str, digits)))


def s(k: int, mod: int) -> int:
    return sum(f_mod(n**3, n**4, mod) for n in range(1, k + 1)) % mod


if __name__ == "__main__":
    assert f_exact(10, 1) == 19
    assert f_exact(10, 10) == 109
    assert f_exact(10, 100) == 1423
    for digit_sum in (1, 2, 7, 13, 25):
        want = [
            x for x in range(1, 10**5) if sum(map(int, str(x))) == digit_sum
        ][:300]
        assert all(
            f_exact(digit_sum, m) == want[m - 1]
            for m in range(1, len(want) + 1)
        )
    assert sum(f_exact(n**3, n**4) for n in (1, 2, 3)) == 7128
    assert s(10, MOD) == 32287064
    print(s(K, MOD))  # 662878999
