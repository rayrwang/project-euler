import numba
import numpy as np


def _bootstrap(v: int) -> tuple[int, list[int]]:
    # Generate U(2, v) naively until past the second even term e2 = 2(v+1),
    # after which every term is odd (Schmerl-Spiegel).
    e2 = 2 * v + 2
    seq = [2, v]
    members = {2, v}
    while seq[-1] <= e2:
        x = seq[-1] + 1
        while True:
            ways = 0
            for t in seq:
                if t < x and (x - t) in members and (x - t) > t:
                    ways += 1
            if ways == 1:
                break
            x += 1
        seq.append(x)
        members.add(x)
    return e2, seq


@numba.njit(cache=True)
def _extend(e2: int, member: np.ndarray, terms: np.ndarray, count: int, last: int) -> int:
    # An odd x joins U(2, v) iff exactly one of x-2, x-e2 is already present.
    x = last + 1 if (last + 1) % 2 == 1 else last + 2
    n = terms.shape[0]
    cap = member.shape[0]
    while count < n and x + 1 < cap:
        if member[x - 2] + member[x - e2] == 1:
            member[x] = 1
            terms[count] = x
            count += 1
        x += 2
    return count


@numba.njit(cache=True)
def _failure(s: np.ndarray) -> int:
    # KMP failure function; smallest period of s is len(s) - f[-1].
    n = s.shape[0]
    f = np.zeros(n, dtype=np.int64)
    k = 0
    for i in range(1, n):
        while k > 0 and s[i] != s[k]:
            k = f[k - 1]
        if s[i] == s[k]:
            k += 1
        f[i] = k
    return int(n - f[n - 1])


def _kth_term(v: int, target: int, n_terms: int) -> int:
    e2, seq = _bootstrap(v)
    member = np.zeros(4 * n_terms + 1000, dtype=np.uint8)
    for m in seq:
        member[m] = 1
    terms = np.zeros(n_terms, dtype=np.int64)
    for i, m in enumerate(seq[:n_terms]):
        terms[i] = m
    count = _extend(e2, member, terms, len(seq), seq[-1])
    terms = terms[:count]

    diff = np.diff(terms)
    start = diff.shape[0] // 2          # past the transient
    period = _failure(diff[start:])
    incr = int(terms[start + period] - terms[start])

    offset = (target - 1) - start
    q, r = divmod(offset, period)
    return int(terms[start] + q * incr + (terms[start + r] - terms[start]))


def solve(target: int = 10**11) -> int:
    # Sum the target-th term of U(2, 2n+1) for n = 2..10.
    return sum(_kth_term(2 * n + 1, target, 9_000_000) for n in range(2, 11))


if __name__ == "__main__":
    print(solve())  # 3916160068885
