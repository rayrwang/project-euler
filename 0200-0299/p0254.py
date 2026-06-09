import numba
import numpy as np

# f(n) sums the factorials of n's digits, sf(n) is the digit sum of f(n),
# g(i) the smallest n with sf(n) = i, and sg(i) its digit sum.
#
# f(n) depends only on n's digit multiset, and the minimal n for a given
# value F = f(n) uses the canonical factorial-base form: digit d (1..8)
# appears a_d <= d times with sum a_d d! = F mod 9!, plus c = F div 9! nines,
# written in ascending order (replacing d+1 copies of d! by (d+1)! always
# shortens, and the canonical string is lexicographically minimal; verified
# against brute force for all i <= 40). So g(i) is determined by the best F
# with digit sum i: primarily minimise the total length c + len(prefix).
#
# The minimal number m_i with digit sum i pins the first useful window
# c0 >= m_i div 9!; since prefixes have at most 1+2+...+8 = 36 digits, only
# windows [c0, c0 + 36] can win. Within a window, scan the 9! prefix values
# in precomputed (length, lexicographic) order and take the first whose
# F = c 9! + p has digit sum i - the digit sum splits as ds(high part with
# carry) + table lookup on the low six digits. sg(i) = 9c + sum of prefix
# digits.

_F9 = 362880
_MILLION = 1_000_000


@numba.njit(cache=True)
def _digit_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


@numba.njit(cache=True)
def _first_valid_p(c: int, i: int, p_order: np.ndarray, ds_table: np.ndarray) -> int:
    base = c * _F9
    hi = base // _MILLION
    lo = base % _MILLION
    ds0 = _digit_sum(hi)
    ds1 = _digit_sum(hi + 1)
    for idx in range(len(p_order)):
        p = p_order[idx]
        lo2 = lo + p
        if base + p == 0:
            continue
        if lo2 >= _MILLION:
            if ds1 + ds_table[lo2 - _MILLION] == i:
                return p
        elif ds0 + ds_table[lo2] == i:
            return p
    return -1


def _prefix_digits(p: int) -> list[int]:
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
    digits = []
    for d in range(8, 0, -1):
        a, p = divmod(p, fact[d])
        digits += [d] * a
    return sorted(digits)


def solve(limit: int = 150) -> int:
    p_keys = sorted(
        range(_F9), key=lambda p: (len(_prefix_digits(p)), _prefix_digits(p))
    )
    p_order = np.array(p_keys, dtype=np.int64)
    ds_table = np.zeros(2 * _MILLION, dtype=np.uint8)
    for v in range(1, 2 * _MILLION):
        ds_table[v] = ds_table[v // 10] + v % 10

    total = 0
    for i in range(1, limit + 1):
        q, r = divmod(i, 9)
        m_i = int(("" if r == 0 else str(r)) + "9" * q)
        c = max(m_i // _F9, 0)
        while _first_valid_p(c, i, p_order, ds_table) < 0:
            c += 1
        candidates = []
        for cc in range(c, c + 37):
            p = _first_valid_p(cc, i, p_order, ds_table)
            if p >= 0:
                pref = _prefix_digits(int(p))
                candidates.append((cc + len(pref), pref, cc))
        best_len = min(t for t, _, _ in candidates)

        def full_key(item: tuple[int, list[int], int]) -> str:
            _, pref, cc = item
            return "".join(map(str, pref)) + "9" * min(cc, 40)  # 40 9s break ties

        best = min((it for it in candidates if it[0] == best_len), key=full_key)
        _, pref, cc = best
        total += 9 * cc + sum(pref)
    return total


if __name__ == "__main__":
    print(solve())  # 8184523820510
