import numba
import numpy as np

# Seven-segment matchstick counts for the digits 0-9; '+' and 'x' use 2 each.
DIGIT_COST = np.array([6, 2, 5, 5, 4, 5, 6, 3, 7, 6], dtype=np.int64)
THETA = 20  # addend P-cost cap (justified by the a posteriori check below)
EXACT_BELOW = 2001  # full-range addends are tried for n below this


@numba.njit(cache=True)
def compute_p(limit: int, dig: np.ndarray) -> np.ndarray:
    """P[n] = min matchsticks to write n as a product of digit-form numbers."""
    p = np.empty(limit + 1, dtype=np.int64)
    p[0] = 10**9
    for n in range(1, limit + 1):
        c = 0
        m = n
        while m:
            c += dig[m % 10]
            m //= 10
        p[n] = c
    for n in range(4, limit + 1):
        a = 2
        while a * a <= n:
            if n % a == 0:
                v = p[a] + p[n // a] + 2
                if v < p[n]:
                    p[n] = v
            a += 1
    return p


@numba.njit(cache=True)
def _len10(n: int) -> int:
    length = 0
    while n:
        length += 1
        n //= 10
    return length


@numba.njit(cache=True)
def compute_m(limit: int, p: np.ndarray, bs: np.ndarray, pb: np.ndarray) -> np.ndarray:
    """M[n] = min matchsticks overall (sums of products, each + costs 2).

    Peeling the smallest term b <= n/2 of an optimal sum costs P(b) + 2, so
    M[n] = min(P[n], min_b M[n - b] + P[b] + 2).  For n < EXACT_BELOW every
    b is tried; beyond that only the cheap addends bs (P <= THETA, sorted by
    cost pb) are.  Since every t satisfies M(t) >= 2 * len(t), once
    pb + 2 + 2 * len(ceil(n / 2)) >= best the remaining addends cannot help.
    """
    m = np.empty(limit + 1, dtype=np.int64)
    m[0] = 10**9
    for n in range(1, limit + 1):
        best = p[n]
        if n < EXACT_BELOW:
            for b in range(1, n // 2 + 1):
                v = m[n - b] + p[b] + 2
                if v < best:
                    best = v
        else:
            lb = 2 * _len10((n + 1) // 2)
            for i in range(len(bs)):
                if pb[i] + 2 + lb >= best:
                    break
                b = bs[i]
                if 2 * b > n:
                    continue
                v = m[n - b] + pb[i] + 2
                if v < best:
                    best = v
        m[n] = best
    return m


if __name__ == "__main__":
    limit = 10**6
    p = compute_p(limit, DIGIT_COST)
    bs = np.flatnonzero(p[: limit + 1] <= THETA).astype(np.int64)
    order = np.argsort(p[bs], kind="stable")
    bs, pb = bs[order], p[bs][order]
    m = compute_m(limit, p, bs, pb)

    assert m[28] == 9  # given: M(28) = 9 via 4 x 7
    assert m[1:101].sum() == 916  # given: T(100) = 916

    # Exactness proof.  Any factor f needs >= 2 * len(f) sticks, and a
    # product's factor lengths sum to at least the product's length, so
    # P(t) >= 2 * len(t) and hence M(t) >= 2 * len(t).  If an optimal sum
    # for n had smallest term b with P(b) > THETA, then since b <= n / 2,
    #     M(n) = M(n - b) + P(b) + 2 >= 2 * len(ceil(n / 2)) + THETA + 3,
    # so the bound below guarantees every useful addend was tried, and by
    # induction m[n] = M(n) (n < EXACT_BELOW tried everything anyway).
    for n in range(EXACT_BELOW, limit + 1):
        assert m[n] <= 2 * len(str((n + 1) // 2)) + THETA + 3

    print(int(m[1 : limit + 1].sum()))  # 26688208
